import qrcode
import cv2
import uuid

contador = int(input("¿Cuantos codigos deseas generar?: "))
while contador > 0:
    # Se genera un ID único
    id = str(uuid.uuid4())  # Convertir UUID a una cadena de texto

    # Se crea el código QR
    img = qrcode.make("http://127.0.0.1:5000/signup/"+id)
    img.save(id + ".png")  # Guardar la imagen como un archivo PNG con el nombre del ID
    contador -= 1

# Lee el QR y saca el contenido
#detector = cv2.QRCodeDetector()
#val, points, straight_qrcode = detector.detectAndDecode(cv2.imread(id + ".png"))
#print(val)
