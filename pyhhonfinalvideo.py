import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import array
import csv

option = {
    'model': 'cfg/yolo.cfg',
    'load': 'bin/yolo.weights',
    'threshold': 0.2,
    'gpu': 1.0
}

tfnet = TFNet(option)

capture = cv2.VideoCapture(0 )
colors = [tuple(255 * np.random.rand(3)) for i in range(100)]

with open('tag1.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

l = len(data)
for x in range(l):
    data[x] = list(map(int, data[x]))


while (capture.isOpened()):
    stime = time.time()
    ret, frame = capture.read()
    width = 640  # width of the frame
    height = 516  # height of the frame
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if ret:
        result = tfnet.return_predict(frame)
        frame.shape
        a = np.array(result)
        size = len(a)
        personi = array.array('i', [])
        for q in range(size):
            object = result[q]['label']
            if (object == 'person'): personi.append(q)

        #tablei = array.array('i', [])
        #for q in range(size):
        #    object = result[q]['label']
        #    if (object == 'diningtable'): tablei.append(q)

        pn = len(personi)
        #tn = len(tablei)
        status = [[0 for x in range(2)] for y in range(l)]
        for w in range(l):
            txav = (data[w][1] + data[w][3])/2
            tyav = (data[w][2] + data[w][4])/2
            status[w][0] = w
            for q in range(pn):
                v = personi[q]
                pxav = (result[v]['topleft']['x'] + result[v]['bottomright']['x'])/2
                pyav = (result[v]['topleft']['y'] + result[v]['bottomright']['y'])/2
                xdi = abs(pxav - txav)
                ydi = abs(pyav - tyav)
                if (xdi <= (
                        abs(result[v]['bottomright']['x'] - result[v]['topleft']['x']) + abs(data[w][1] -
                        data[w][3]))/2):
                    if (ydi <= (
                            abs(result[v]['topleft']['y'] - result[v]['bottomright']['y']) + abs(data[w][2] -
                            data[w][4]))/2): status[w][1] = status[w][1] + 1

        print(status)
        with open('status1.csv', 'w', newline='') as f:
            tw = csv.writer(f)
            tw.writerows(status)

        for color, resul in zip(colors, result):
            if (resul['label'] == 'person'):
              tl = (resul['topleft']['x'], resul['topleft']['y'])
              br = (resul['bottomright']['x'], resul['bottomright']['y'])
              label = resul['label']
              frame = cv2.rectangle(frame, tl, br, color, 2)
              frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 0.2, (0, 0, 0), 1)

        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break

