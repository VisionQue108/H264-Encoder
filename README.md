This script captures video from a webcam, saves it as an AVI file, and then converts the AVI file to a more compressed H.264 format.

Requirements:

OpenCV (cv2)
Python threading library
GStreamer library (version 1.0 or later)
Instructions:

Make sure you have the required libraries installed.
Run the script: python your_script_name.py
Script Functionality:

The script first opens the default webcam using OpenCV's VideoCapture function.
The frame_capture function performs the following:
Captures frames from the webcam in a loop.
Gets the frame width and height.
Creates a video writer object to save the frames as an AVI file named output.avi.
Continuously writes captured frames to the AVI file.
When the script is interrupted (usually by pressing Ctrl+C), it performs the conversion:
GStreamer is initialized.
A GStreamer pipeline is created to convert the output.avi file to output.h264 using H.264 encoding.
The conversion progress is monitored until the output.h264 file is created.
GStreamer is shut down.
