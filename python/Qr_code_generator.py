import qrcode

data=input("Enter your URL:").strip()

filename=input("Enter the filename:")

qr=qrcode.QRCode(box_size=10,border=4)

qr.add_data(data)

image=qr.make_image(fill_color='black',background_color='white')
image.save(filename)

print(f"qrcode savef succesfully{filename}")