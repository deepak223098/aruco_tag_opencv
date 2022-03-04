import argparse
import imutils
import cv2
import sys
import numpy as np


class ArucoTag:
    # set class variable
    path_to_save = r'output/DICT_4X4_50_1.png'
    path_to_read = r"input/image1.png"
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

    def detectArucoTag(self, image):
        image = imutils.resize(image, width=600)
        arucoParams = cv2.aruco.DetectorParameters_create()
        (corners, ids, rejected) = cv2.aruco.detectMarkers(image, self.arucoDict,
                                                           parameters=arucoParams)

        # verify *at least* one ArUco marker was detected
        imls = []
        if len(corners) > 0:
            # flatten the ArUco IDs list
            ids = ids.flatten()

            # loop over the detected ArUCo corners
            for (markerCorner, markerID) in zip(corners, ids):
                # extract the marker corners (which are always returned in
                # top-left, top-right, bottom-right, and bottom-left order)
                corners = markerCorner.reshape((4, 2))
                (topLeft, topRight, bottomRight, bottomLeft) = corners

                # convert each of the (x, y)-coordinate pairs to integers
                topRight = (int(topRight[0]), int(topRight[1]))
                bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
                bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
                topLeft = (int(topLeft[0]), int(topLeft[1]))

                # draw the bounding box of the ArUCo detection
                cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
                cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
                cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
                cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)

                # compute and draw the center (x, y)-coordinates of the ArUco
                # marker
                cX = int((topLeft[0] + bottomRight[0]) / 2.0)
                cY = int((topLeft[1] + bottomRight[1]) / 2.0)
                cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)

                # draw a line from center point to the right, Horizontal Line
                cv2.line(image, (cX, cY), (cX + 40, cY), (255, 0, 0), 2)
                # draw a line from center point to the upwards, Vertical Line
                cv2.line(image, (cX, cY), (cX, cY - 40), (0, 0, 255), 2)
                # draw a line from center point to the downwards, Vertical Line
                cv2.line(image, (cX, cY), (cX, cY + 40), (0, 255, 0), 2)

                # draw the ArUco marker ID on the image
                cv2.putText(image, str(markerID),
                            (topLeft[0], topLeft[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, (255, 0, 0), 3)
                print("[INFO] ArUco marker ID: {}".format(markerID))
                imls.append(image.copy())
            return image, imls

