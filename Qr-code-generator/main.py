import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

data = input("Enter the data to encode in the QR code: ")
color = input("Enter the color for the QR code (e.g., 'black', 'blue', '#FF5733'): ")
back_color = input("Enter the background color for the QR code (e.g., 'white', 'yellow', '#C0C0C0'): ")
name = input("Enter the name for the QR code image file (without extension): ")

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color=color, back_color=back_color).convert('RGB')

img.save(name + '.png')

img.show()

