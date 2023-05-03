import cv2
import numpy as np

# lê uma imagem usando a biblioteca OpenCV
img = cv2.imread('lena.png')

# converte a imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# aplica um filtro de suavização na imagem
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# detecta as bordas na imagem usando o operador Canny
edges = cv2.Canny(blur, 100, 200)

