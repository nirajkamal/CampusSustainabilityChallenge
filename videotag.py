import cv2
import matplotlib.pyplot as plt
cap = cv2.VideoCapture('vid.mov')
cap.set(cv2.CAP_PROP_POS_MSEC,1000)      # Go to the 1 sec. position
ret,frame = cap.read()                   # Retrieves the frame at the specified second
frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
width = 640                              #width of the frame
height = 516                             #height of the frame
dim = (width, height)
frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA) #resizes the frame
cv2.imwrite("image.jpg", frame)          # Saves the frame as an image
img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
plt.imshow(frame)
plt.show()
