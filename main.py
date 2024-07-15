import cv2

# Define the GStreamer pipeline string
gst_pipeline = "filesrc location=object_counting_output1.mp4 ! decodebin ! videoscale ! video/x-raw,width=1080,height=720 ! videoconvert ! videocrop top=50 left=400 right=400 bottom=500 ! appsink"


# Open the video capture with the GStreamer pipeline
cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

# Check if the video capture is opened
if not cap.isOpened():
    print("Error: Unable to open video capture")
else:
    # Read and display frames
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('IP Camera Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()

# import cv2
# print(cv2.getBuildInformation())
