import cv2

def main():
    # Setting up the camera to capture video
    cap = cv2.VideoCapture(0)
    try:
        while cap.isOpened():
            # 'ret' will contain true or false depending upon the cap.read()
            # if ret is True then frame will contain a frame
            ret,frame = cap.read()
            if not ret :
                break
            # Flipping the image for mirror image so that right <-> left dosent get interchanged
            frame = cv2.flip(frame,1)
            # Showing the frame on screen 
            cv2.imshow('Frame',frame)
            # Code for waiting 1 ms and if q is pressed then quit
            if cv2.waitKey(1)  &  0xFF == ord('q'):
                break
    # Finally Block
    finally : 
        cap.release()
        cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
            