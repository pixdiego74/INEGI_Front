import qrcode

input = 'http://127.0.0.1:5000/4059'

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(input)
qr.make(fit = True)

img = qr.make_image(fill = 'black', back_color = '#003057')
img.save('qrdiego.png')