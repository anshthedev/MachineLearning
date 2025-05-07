import numpy as np
import cv2

vid_file_path = "/Users/ansh/PycharmProjects/LearningPython/MachineLearning/Datasets/sample_rotating.mov"

def resize(img):
    return cv2.resize(img, (512, 512))

# Normalizes the Video
def saturate_frame(frame, saturation_factor=1.5):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Saturation is first index of HSV
    # np.clip() is keep values within a range
    hsv[..., 1] = np.clip(hsv[..., 1] * saturation_factor, 0, 255)

    # Convert back to BGR
    saturated_frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return saturated_frame


cap = cv2.VideoCapture(vid_file_path)
ret, frame = cap.read()

l_b = np.array([100, 150, 0])  # lower hsv bound for blue
u_b = np.array([140, 255, 255])  # upper hsv bound for blue

while ret:
    ret, frame = cap.read()

    # Saturate the frame before processing it further
    frame = saturate_frame(frame, saturation_factor=1.5)

    pts2 = np.float32([[0,0],[400,0],[0,600],[400,600]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    result = cv2.wrapPerspective(frame, matrix, (400,600))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Binary Operation:
    # Anything within the bounds gets a 1
    # Anything outside the bounds gets a 0
    # 0 = Black; 1 = White
    mask = cv2.inRange(hsv, l_b, u_b)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # Looking for the object with the largest area of mask
        max_contour = contours[0]
        for contour in contours:
            if cv2.contourArea(contour) > cv2.contourArea(max_contour):
                max_contour = contour

        contour = max_contour

        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        x, y, w, h = cv2.boundingRect(approx)
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)  # Creates Straight Box
        # cv2.drawContours(frame, [approx], 0, (255, 255, 0), 2)  # Draws Contours for Rotated Box

        (x1,y1), (w1, h1), angle  = cv2.minAreaRect(approx)
        rect = (x1,y1), (w1, h1), angle
        box = cv2.boxPoints(rect) # Takes in Rect Values and Makes Box Vertices
        box = np.intp(box) # Converts All Values to Integer

        cv2.drawContours(frame, [box], 0, (0, 255, 255), 2)

        print( angle)

    cv2.imshow("frame", frame)
    cv2.imshow("result) result)
    cv2.imshow("mask", mask)

    # # Debugging Lower and Upper Bounds
    # lower_bound_hsv = np.uint8([[l_b]])
    # upper_bound_hsv = np.uint8([[u_b]])
    # lower_bound_bgr = cv2.cvtColor(lower_bound_hsv, cv2.COLOR_HSV2BGR)
    # upper_bound_bgr = cv2.cvtColor(upper_bound_hsv, cv2.COLOR_HSV2BGR)
    # cv2.imshow("Lower Bound Color", lower_bound_bgr)
    # cv2.imshow("Upper Bound Color", upper_bound_bgr)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
