from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pyipp import IPP, Printer

app = FastAPI()

@app.get('/probe', response_class=PlainTextResponse)
async def metrics(target):
  black_level = 0
  color_level = 0
  busy = 0
  success = 0

  async with IPP(target) as ipp:
    try:
      printer: Printer = await ipp.printer()

      black_level = get_cartrige_level(printer, 'Black')
      color_level = get_cartrige_level(printer, 'Color')
      busy = 1 if is_busy(printer) else 0
      success = 1
    except Exception as e:
      print('Something went wrong', e)
    finally:
      return ('# HELP busy If printer is currently busy\n'
              '# TYPE busy gauge\n'
              f'''busy {busy}\n'''
              '# HELP cartridge_level_percent Cartridge fill level by color\n'
              '# TYPE cartridge_level_percent gauge\n'
              f'''cartridge_level_percent{"black"} {black_level}\n'''
              f'''cartridge_level_percent{"color"} {color_level}\n'''
              '# HELP success Displays whether or not the probe was a success\n'
              '# TYPE success gauge\n'
              f'''success {success}\n'''
      )

def is_busy(printer):
  return printer.state.printer_state != 'idle'

def get_cartrige_level(printer, name):
  for marker in printer.markers:
    if marker.name == name:
      return marker.level
