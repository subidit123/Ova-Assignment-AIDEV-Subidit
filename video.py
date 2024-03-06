import cv2

# Open the video file
cap = cv2.VideoCapture(r"C:\Users\Subidit Chakraborty\Downloads\pexels_videos_2711134 (2160p) (1).mp4")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # Display the frame
        cv2.imshow('Uploaded Video', frame)
        
        # Press 'q' to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything when done
cap.release()
cv2.destroyAllWindows()
