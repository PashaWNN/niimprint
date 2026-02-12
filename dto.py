from pydantic import BaseModel


class PrintBarcodeDto(BaseModel):
    code: str
    title: str