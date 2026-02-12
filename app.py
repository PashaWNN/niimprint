from litestar import Litestar, post
from litestar.exceptions import HTTPException
from litestar.logging import LoggingConfig

from barcode_generation import generate_barcode
from dto import PrintBarcodeDto
from niimbot import print_image


@post('/print_barcode')
def print_barcode(data: PrintBarcodeDto) -> None:
    barcode = generate_barcode(data)
    try:
        print_image(barcode)
    except AttributeError as e:
        raise HTTPException(
            status_code=500,
            detail=(
                'AttributeError caught during printing. '
                'Perhaps printer is offline?'
            ),
        )

app = Litestar([print_barcode], logging_config=LoggingConfig(log_exceptions='always'))