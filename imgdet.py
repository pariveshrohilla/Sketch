import cv2
import numpy
import requests

# URL of the IP camera snapshot image
url = "http://192.168.1.228:8080/shot.jpg"

PREVIEW  = 0
BLUR     = 1 
FEATURES = 2
CANNY    = 3

# Parameters for corner detection
feature_params = dict(maxCorners=500, qualityLevel=0.2, minDistance=15, blockSize=9)

image_filter = PREVIEW
alive = True

win_name = "Camera Filters"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while alive:
    img_resp = requests.get(url)
    img_arr = numpy.asarray(bytearray(img_resp.content), dtype=numpy.uint8)
    frame = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    if frame is None:
        print("Failed to grab frame")
        break

    # Apply selected filter
    if image_filter == PREVIEW:
        result = frame
    elif image_filter == CANNY:
        result = cv2.Canny(frame, 80, 150)
    elif image_filter == BLUR:
        result = cv2.blur(frame, (13, 13))
    elif image_filter == FEATURES:
        result = frame.copy()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
        if corners is not None:
            for x, y in numpy.float32(corners).reshape(-1, 2):
                cv2.circle(result, (int(x), int(y)), 10, (0, 255, 0), 1)

    # Overlay instructions text on the frame
    instructions = [
        "Press keys to change filters:",
        "P: Preview (normal)",
        "B: Blur",
        "C: Canny edges",
        "F: Feature detection (corners)",
        "Q, Esc: Quit program"
    ]

    font = cv2.FONT_HERSHEY_SIMPLEX
    start_x, start_y = 10, 30
    line_height = 25
    font_scale = 0.7
    color = (0, 255, 255)  # Yellow color
    thickness = 2

    for i, line in enumerate(instructions):
        y = start_y + i * line_height
        cv2.putText(result, line, (start_x, y), font, font_scale, color, thickness, cv2.LINE_AA)

    # Show the final frame with overlay
    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)

 
    if key == ord("Q") or key == ord("q") or key == 27:
        alive = False
    elif key == ord("C") or key == ord("c"):
        image_filter = CANNY
    elif key == ord("B") or key == ord("b"):
        image_filter = BLUR
    elif key == ord("F") or key == ord("f"):
        image_filter = FEATURES
    elif key == ord("P") or key == ord("p"):
        image_filter = PREVIEW

cv2.destroyAllWindows()
