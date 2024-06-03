import cv2

# Initialize the camera
camera = cv2.VideoCapture(0)  # 0 is the default camera
fourcc = cv2.VideoWriter_fourcc(*'XVID')

recording = False
out = None

while True:
    ret, frame = camera.read()
    if not ret:
        break
    
    # Display a green rectangle when recording
    if recording:
        cv2.putText(frame, 'Recording...', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        out.write(frame)
    
    cv2.imshow('Logitech Camera', frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):  # Press Space to start/stop recording
        if not recording:
            out = cv2.VideoWriter('recording.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            recording = True
        else:
            recording = False
            out.release()
    elif key == ord('q'):  # Press 'q' to quit
        break

# Release resources
camera.release()
if recording:
    out.release()
cv2.destroyAllWindows()
