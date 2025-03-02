import gridfs
import cv2
import numpy as np
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["doorbell_storage"]
fs = gridfs.GridFS(db)

# Retrieve the video file
video_file = fs.find_one({"filename": "doorbell_footage.avi"})

# Save retrieved video to a temporary file
with open("retrieved_video.avi", "wb") as output:
    output.write(video_file.read())

# Play the retrieved video
cap = cv2.VideoCapture("retrieved_video.avi")

print("Playing video... Press 'q' to stop.")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Retrieved Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

print("Video playback finished.")
