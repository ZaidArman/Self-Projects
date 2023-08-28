import cv2

face_data_path = "C:/Users/zaid arman/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"

face_cap = cv2.CascadeClassifier(face_data_path)
video_cap = cv2.VideoCapture(0)

while True:
    ret, video_data = video_cap.read()
    color = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)  # Corrected this line
    
    faces = face_cap.detectMultiScale(color, scaleFactor=1.1, minNeighbors=10, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)  # Corrected "flag" to "flags"
    
    for (x,y, width,  height) in faces:
        cv2.rectangle(video_data, (x,y), (x+width, y+height), (0, 255, 0), 2)  # Corrected the rectangle coordinates
    cv2.imshow("Face Detection", video_data)
    
    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()
cv2.destroyAllWindows()
