import cv2

'''read video and display'''
# cap = cv2.VideoCapture('video1.mkv')
# while True:
#     ret, frame = cap.read()
#     frame = cv2.resize(frame, (1080,720))
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     # cv2.imshow('Frame', frame)
#     cv2.imshow('gray', gray)
#     k = cv2.waitKey(25)
#     if k == ord('q') & 0xFF:
#         break
# cap.release()

'''read camera and save'''
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("output.avi",fourcc,10.0,(640,480),0) # remove last 0

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        output.write(gray)

        cv2.imshow('gray', gray)
        k = cv2.waitKey(1)
        if k == ord('q') & 0xFF:
            break
    else:
        break
cap.release()
output.release()