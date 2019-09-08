import cv2, time

#1 Create object
video = cv2.VideoCapture(0)
#3 Create frame object
check, frame = video.read()

print(check)
print(frame) #representing image
#4 Show frame
cv2.imshow("CApturing", frame)
#5 Press key to out
cv2.waitKey(0)
# Shutdown camera
video.release()
