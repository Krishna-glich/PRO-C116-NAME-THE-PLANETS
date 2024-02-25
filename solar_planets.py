import cv2
img=cv2.imread('solar-system.jpg')

cv2.putText( img,
    "sun",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (225,225,225)

)  

cv2.putText( img,
    "mercury",
    (100,170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (225,225,225)

)  
cv2.putText( img,
    "venus",
    (190,160),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (225,225,225)

)  
cv2.putText( img,
    "earth",
    (300,160),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (225,225,225)

)  
cv2.putText( img,
    "mars",
    (400,170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (225,225,225)

)  
cv2.putText( img,
    "jupiter",
    (500,50),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (225,225,225)

)  
cv2.putText( img,
    "saturn",
    (800,100),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (225,225,225)

)  
cv2.putText( img,
    "uranus",
    (950,100),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (225,225,225)

)  

cv2.putText( img,
    "neptune",
    (1100,100),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (225,225,225)

)  



cv2.imshow("output",img)
cv2.waitKey(0)  