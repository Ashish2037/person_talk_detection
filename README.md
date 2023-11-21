# person_talk_detection
This Python script utilizes the Mediapipe library to detect facial landmarks and determine mouth openness in real-time using a webcam.

# Prerequisites
Before running the script, make sure you have the following dependencies installed:

OpenCV (pip install opencv-python)
Mediapipe (pip install mediapipe)

# Description
The script performs the following steps:

Captures video from the webcam.
Detects facial landmarks using the Mediapipe Face Mesh model.
Calculates the distance between upper and lower lip landmarks to determine mouth openness.
Displays the real-time video feed with the mouth openness status.

# Interpretation
If the mouth is open, the text "Mouth Open" is displayed.
If the mouth is closed, the text "Mouth Closed" is displayed.

# Keyboard Shortcut
Press 'q' to quit the application.

# Credits
Mediapipe for the Face Mesh model.
OpenCV for computer vision functionalities.
