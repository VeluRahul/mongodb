import cv2
import keyboard  # Import keyboard module

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('doorbell_footage.avi', fourcc, 20.0, (640, 480))

print("Recording... Press 'q' to stop.")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow('Doorbell Camera', frame)

        if keyboard.is_pressed('q'):  # Detect 'q' key
            print("Stopping recording...")
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("Video saved as 'doorbell_footage.avi'")
