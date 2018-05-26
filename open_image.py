from PIL import Image
import numpy as np
import cv2

pilImg = Image.open('rasp.jpeg')
opencvImage = cv2.cvtColor(np.array(pilImg), cv2.COLOR_RGB2BGR)
cv2.imshow('Demo image', opencvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()