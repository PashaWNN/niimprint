# Niimbot printers print server

This app allows to print stickers with barcodes via simple HTTP interface.

Just POST a request to `/print_barcode` with the following body:
```json
{
    "code": "1234567890",
    "title": "Sticker title"
}
```

There is not much configuration options as it is intended for the personal use.


To run the app via Docker, you'll need to set some environment variables, example is 
in `.env.example` file. You'll also need to give Docker container access to the printer via
serial USB port. You can do that by running container using the following commands (replace
`/dev/tty.usbmodem1` with your printer's port):
```
docker build . -t niimprint
docker run -v /dev/tty.usbmodem1:/dev/tty.usbmodem1 -it --rm --name niimprint-server -p 80:8080 niimprint
```