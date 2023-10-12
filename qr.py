#code for encoder
import qrcode as qr
img = qr.make("https://www.youtube.com/")
img.save("my_qr.png")

#code for decoder
import cv2

img= cv2.imread("my_qr.png")
data= cv2.QRCodeDetector()
v1,v2,v3=data.detectAndDecode(img)

print(v1)