import os

from PIL import Image
from niimprint import SerialTransport, PrinterClient

model = os.getenv("NIIMPRINT_PRINTER_NAME") or "b21"
port = os.getenv("NIIMPRINT_PRINTER_PORT")
density = int(os.getenv("NIIMPRINT_PRINTER_DENSITY"))


def print_image(image: Image.Image) -> None:
    transport = SerialTransport(port=port)
    printer = PrinterClient(transport)
    printer.print_image(image, density=density)