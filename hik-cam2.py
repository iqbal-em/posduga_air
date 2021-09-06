import cv2
import requests
import numpy as np
from hikvisionapi import Client

cam = Client('http://192.168.1.64', 'admin', 't4ng3r4ng')
while True:
    print("starting picture capture")
    vid = cam.Streaming.channels[102].picture(method ='get', type = 'opaque_data')
    bytes = b''    
    with open('img.png', 'wb') as f:
        for chunk in vid.iter_content(chunk_size=1024):
            bytes += chunk
            a = bytes.find(b'\xff\xd8')
            b = bytes.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = bytes[a:b+2]
                bytes = bytes[b+2:]
                i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                cv2.imwrite('img.png', i)
                cv2.imshow('i', i)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()
        break
