# IP Camera Filter Viewer

This Python application allows real-time viewing and filtering of video feed from an IP camera. It supports various image processing filters such as **Blur**, **Canny Edge Detection**, and **Feature (Corner) Detection** using OpenCV.

## Features

* Live video stream from an IP camera (`.jpg` snapshot URL)
* Toggle between different filters using keyboard:

  * **P**: Preview (normal frame)
  * **B**: Blur filter
  * **C**: Canny edge detection
  * **F**: Feature detection (corners)
  * **Q / Esc**: Quit the application
* Overlay instructions directly on the video feed
* Corner detection using `cv2.goodFeaturesToTrack`

## Requirements
* Python 3.6+
* OpenCV
* NumPy
* requests library

Install dependencies using pip:

```bash
pip install opencv-python numpy requests
```

## How It Works

1. The script fetches frames from an IP camera by downloading `.jpg` snapshots from a given URL.
2. Each frame is processed based on the selected filter.
3. Instructions are drawn on the frame, and the processed image is displayed using OpenCV's GUI.

## Setup

Update the `url` variable in the script with the snapshot URL of your IP camera:

```python
url = "http://192.168.1.228:8080/shot.jpg"
```

Make sure your IP camera supports `.jpg` snapshot URLs and is accessible from your local network.


![Alt text](Assets/Features.png?raw=true "Feature")

![Alt text](Assets/Canny.png?raw=true "Feature")
