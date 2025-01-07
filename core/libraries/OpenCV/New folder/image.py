import cv2

# imread 
img1 = cv2.imread('nitesh_photo.jpg')

# # gray image
img1 = cv2.imread('nitesh_photo.jpg', -1)

# # hight securation (-1)
img1 = cv2.imread('nitesh_photo.jpg', 0)

# resize
img1 = cv2.resize(img1, (500,500))

# print(img1)

# imshow
cv2.imshow('Original', img1)

#waitkey
cv2.waitKey(3000)
# cv2.destoryWindows()


'''program'''

path = input('Enter path:')

img1 = cv2.imread(path,0)
cv2.imwrite('gray.png', img1)