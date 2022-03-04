from util_aruco import ArucoTag
import cv2


# call a ArucoTab module from the utility
arco = ArucoTag(arucoType="DICT_4X4_50")
arco.path_to_read = r"input/shinchan_1.png"
print("arco.path_to_read", arco.path_to_read)
image = cv2.imread(arco.path_to_read)
# process the image to detect the Aruco Tag in a Given Image
image, _ = arco.detectArucoTag(image)
# show the detected ArucoTag
cv2.imshow("DetectedArucoTag", image)
cv2.waitKey(0)

