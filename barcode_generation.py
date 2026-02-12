import os

import treepoem
from PIL import ImageOps, ImageDraw, ImageFont, Image

from dto import PrintBarcodeDto


FONT_SIZE = int(os.getenv('NIIMPRINT_FONT_SIZE'))
PADDING = int(os.getenv('NIIMPRINT_PADDING'))
FONT_NAME = os.getenv('NIIMPRINT_FONT_NAME')
STICKER_WIDTH = int(os.getenv('NIIMPRINT_STICKER_WIDTH'))
STICKER_HEIGHT = int(os.getenv('NIIMPRINT_STICKER_HEIGHT'))


def generate_barcode(data: PrintBarcodeDto) -> Image.Image:
    image = treepoem.generate_barcode(
        barcode_type='code128', 
        data=data.code,
        options={
            # Just for the correct aspect ratio for ImageDraw.contain
            'width': str((STICKER_WIDTH) / 10 * 2.54),
            'height': (STICKER_HEIGHT) * 2 / 3 / 10 * 2.54
        }
    )
    
    image = ImageOps.contain(
        image, 
    (STICKER_WIDTH - (PADDING * 2),
         STICKER_HEIGHT - (PADDING * 2)),
         Image.Resampling.NEAREST,
    )
    image = ImageOps.expand(image, border=PADDING, fill="white")
    image = ImageOps.expand(image, border=(0, FONT_SIZE * 2, 0, 0), fill="white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_NAME, FONT_SIZE)
    draw.text((PADDING, PADDING), data.code, font=font, fill="black")
    draw.text((PADDING, PADDING + FONT_SIZE), data.title, font=font, fill="black")
    image = image.crop((0, 0, STICKER_WIDTH, STICKER_HEIGHT))
    image.convert("1")
    return image