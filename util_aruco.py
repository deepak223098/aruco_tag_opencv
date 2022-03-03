import argparse
import imutils
import cv2
import sys
import numpy as np


class ArucoTag:
    path_to_save = r'output/DICT_4X4_50_1.png'
    path_to_read = r"input/image1.pnd"
    ARUCO_DICT = {
        "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
        "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
        "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
        "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
        "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
        "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
        "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
        "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
        "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
        "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
        "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
        "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
        "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
        "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
        "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
        "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
        "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
        "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
        "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
        "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
        "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
    }

    def __init__(self, arucoType="DICT_4X4_50", size=300, id=1):
        self.arucoType = self.ARUCO_DICT[arucoType]
        # will generate 300x300x1 channel image
        self.size = size
        self.id = id  # what id need to attached in the arucoImage

        # load the ArUCo dictionary
        self.arucoDict = cv2.aruco.Dictionary_get(self.arucoType)

    def generateArucoTag(self):
        tag = np.zeros((self.size, self.size, 1), dtype="uint8")
        # here 1 is padding in the image
        cv2.aruco.drawMarker(self.arucoDict, self.id, 300, tag, 1)
        cv2.imwrite(self.path_to_save, tag)
        cv2.imshow("ArUCo Tag", tag)
        print(f"Successfully saved {self.path_to_save}, ID {self.id} ")
        cv2.waitKey(0)

    def detectArucoTag(self):
        pass

