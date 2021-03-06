import cv2

# load some pre trained data on face frontals from opencv (haar cascade algorithm)

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# capture from a webcam (0 = default cam)
webcam = cv2.VideoCapture(0)


# loop through all frames
while True:

    # read current frame
    good_frame_read, frame = webcam.read()
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # rgb is backwards in opencv

    # detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)

    # draw rects around faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("NibbaNaeNae's face detector", frame)
    key = cv2.waitKey(1)
    if face_coordinates == ():
        print("Not picked up face")
    else:
        print(face_coordinates)

    # break out of program using ascii for X/x 
    if key==88 or key==120:
        break

print("Code completed")
print("UwU")
