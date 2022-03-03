import cv2
from util_aruco import ArucoTag

arco = ArucoTag(arucoType="DICT_4X4_50", id=20, size=300)


arco.path_to_save = r"output/dgupta_DICT_4X4_50_20.png"
arco.generateArucoTag()
