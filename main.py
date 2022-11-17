from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pyipp import IPP, Printer

app = FastAPI()

def get_printer_info(printer):
  """Get printer info."""
  black_level = 0
  color_level = 0
  busy = 0

  black_level = get_cartridge_level(printer, 'Black')
  color_level = get_cartridge_level(printer, 'Color')
  busy = 1 if is_busy(printer) else 0

  return ('# HELP ipp_busy If printer is currently busy\n'
          '# TYPE ipp_busy gauge\n'
          f'''ipp_busy {busy}\n'''
          '# HELP ipp_cartridge_level_percent Cartridge fill level by color\n'
          '# TYPE ipp_cartridge_level_percent gauge\n'
          f'''ipp_cartridge_level_percent{{type="black"}} {black_level}\n'''
          f'''ipp_cartridge_level_percent{{type="color"}} {color_level}\n'''
  )

def get_success_info(success):
  """Get metrics string to determine success or failure."""
  return ('# HELP ipp_success Displays whether or not the probe was a success\n'
          '# TYPE ipp_success gauge\n'
          f'''ipp_success {1 if success else 0}\n'''
  )

def is_busy(printer):
  """Determine if printer is busy."""
  return printer.state.printer_state != 'idle'

def get_cartridge_level(printer, name):
  """Get cartridge for type."""
  for marker in printer.markers:
    if marker.name == name:
      return marker.level

@app.get('/probe', response_class=PlainTextResponse)
async def probe(target):
  metrics = ''

  async with IPP(target) as ipp:
    try:
      printer: Printer = await ipp.printer()

      metrics += get_printer_info(printer)
      metrics += get_success_info(True)
    except Exception as e:
      print('Something went wrong', e)
      metrics += get_success_info(False)
    finally:
      return metrics
