from util_aruco import ArucoTag

# call a ArucoTab module from the utility
arco = ArucoTag(arucoType="DICT_4X4_50", id=20, size=300)
# change the output path to save the image
arco.path_to_save = r"output/dgupta_DICT_4X4_50_20.png"
# call the function to generate your own aruco tag
arco.generateArucoTag()
