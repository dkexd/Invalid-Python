import cv2, time

# 1. Create object, 0 for external camera
video = cv2.VideoCapture(0)

# a var
a = 0
while True:
    a = a + 1
    # 3. Create frame object
    check, frame = video.read()
    print(check)
    print(frame)  # representing image

    # 4. Show frame
    cv2.imshow("Capturing", frame)

    # 5. Press key to out
    #cv2.waitKey(0)

    # 7. For playing
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
print(a)
# Shutdown camera
video.release()

cv2.destroyAllWindows()
