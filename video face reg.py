    import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') #face properties cascade file
cap = cv2.VideoCapture(0)    #to access cam
if cap.isOpened():
    while cap.isOpened():
        bool, img1 = cap.read()   #read the img   #bool is value that image is read or not
        gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #gray img  conversion
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)#face detection
        for (x, y, w, h) in faces:
            cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 0), 1) #drawing rectangels
        cv2.imshow('img', img1)#showing images
        k = cv2.waitKey(10)
        if k==27: #esc key foe interruption
            break
            cv2.destroyAllWindows()
else:
    print("camera not found\ ")
cap.release()
