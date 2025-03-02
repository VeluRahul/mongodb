import gridfs
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["doorbell_storage"]  # Database name

# Initialize GridFS
fs = gridfs.GridFS(db)

# Open and store the video file
with open("doorbell_footage.avi", "rb") as video_file:
    file_id = fs.put(video_file, filename="doorbell_footage.avi")
    print(f"Video stored in MongoDB with file ID: {file_id}")
