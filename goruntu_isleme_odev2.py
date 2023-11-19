#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import numpy as np


camera = cv2.VideoCapture(0)

while True:
    # Video akışından kare alma
    ret, frame = camera.read()

    #  HSV renk uzayına çevirme
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığı
    red_lower = np.array([0, 100, 100])
    red_upper = np.array([10, 255, 255])

    # Yeşil renk aralığı
    green_lower = np.array([30, 40, 40])
    green_upper = np.array([80, 255, 255])

    # Mavi renk aralığı
    blue_lower = np.array([90, 50, 50])
    blue_upper = np.array([120, 255, 255])

    #  maskeleme
    red_mask = cv2.inRange(hsv_frame, red_lower, red_upper)
    green_mask = cv2.inRange(hsv_frame, green_lower, green_upper)
    blue_mask = cv2.inRange(hsv_frame, blue_lower, blue_upper)

    # Yeşil ve mavi renkleri siyahlaştırma
    result_frame = cv2.bitwise_and(frame, frame, mask=~(green_mask | blue_mask))

    # görüntüyü gösterme
    cv2.imshow("normal hali",frame)
    cv2.imshow('sadece kırmızı nesne ', result_frame)

    #  döngüden çıkmak için 'q' ya bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırakın ve pencereleri kapatın
camera.release()
cv2.destroyAllWindows()


# In[ ]:




