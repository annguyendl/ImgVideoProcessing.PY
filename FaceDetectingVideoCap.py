import cv2

face_cascade = cv2.CascadeClassifier("./resources/haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()

    print(check)
    print(frame)

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img,
    scaleFactor=1.05,
    minNeighbors=5)

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h),
        (0, 255, 0), 2)

    cv2.imshow("Detecting faces", frame)
    key = cv2.waitKey(200)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()