import cv2

img_name = input("Set image name: ")
img_counter = int(input("Set image counter: "))

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        file_name = "{}_{}.png".format(img_name, img_counter)
        cv2.imwrite(file_name, frame)
        print("{} written!".format(file_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()