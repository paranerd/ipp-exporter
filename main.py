from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pyipp import IPP, Printer

app = FastAPI()

@app.get('/metrics', response_class=PlainTextResponse)
async def metrics(host):
  async with IPP(host) as ipp:
    printer: Printer = await ipp.printer()

    black_level = get_cartrige_level(printer, 'Black')
    color_level = get_cartrige_level(printer, 'Color')
    state = get_state(printer)

    return ('# HELP is_printing Printer state\n'
            '# TYPE is_printing gauge\n'
            f'''is_printing {state != 'idle'}\n'''
            '\n'
            '# HELP black_level Level of black color\n'
            '# TYPE black_level gauge\n'
            f'''black_level {black_level}\n'''
            '\n'
            '# HELP color_level Level of black color\n'
            '# TYPE color_level gauge\n'
            f'''color_level {color_level}'''
    )

def get_state(printer):
  return printer.state.printer_state

def get_cartrige_level(printer, name):
  for marker in printer.markers:
    if marker.name == name:
      return marker.level
