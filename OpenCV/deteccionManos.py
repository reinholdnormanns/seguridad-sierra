import cv2

#Se guarda la captura obtenida del smartphone
cap = cv2.VideoCapture('http://localhost:8080/video')

while True:

    ret, frame = cap.read()
    cv2.imshow('Video', frame)

    #Cierra el frame al presionar Esc
    if cv2.waitKey(1) == 27:
        exit(0)
