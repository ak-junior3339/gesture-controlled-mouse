import cv2
import mediapipe as mp
import util 
import pyautogui
from pynput.mouse import Button, Controller
import random

mouse = Controller()
screen_width,screen_height = pyautogui.size()
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    # we are capturing video so no static 
    static_image_mode = False,
    model_complexity = 1,
    # min. confidence score required for detection
    min_detection_confidence = 0.7,
    # the next line says that only if you are 70% confident that a hand is hand only then track it 
    min_tracking_confidence = 0.7,
    #Max number of hands
    max_num_hands = 1
)

def find_finger_tip(processed):
    if processed.multi_hand_landmarks:
        hand_landmarks = processed.multi_hand_landmarks[0]
        # WE WILL RETURN THE ATTRIBUTE OF INDEX FINGER TIP WHIC CAN BE ACESSED DIRECTLY USING 
        # 'mpHands.HandLandmark.INDEX_FINGER_TIP'
        return hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]

def move_mouse(index_finger_tip):
    if index_finger_tip is not None :
        x = int(index_finger_tip.x * screen_width)
        y = int(index_finger_tip.y * screen_height)
        pyautogui.moveTo(x,y)

def is_left_click(landmarks_list,thumb_index_dist):
    return (
        util.get_angle(landmarks_list[5],landmarks_list[6],landmarks_list[8]) < 50 and 
        util.get_angle(landmarks_list[9],landmarks_list[10],landmarks_list[12]) > 90 and 
        thumb_index_dist > 50 
    )

def is_right_click(landmarks_list,thumb_index_dist):
    return (
        util.get_angle(landmarks_list[5],landmarks_list[6],landmarks_list[8]) > 90 and 
        util.get_angle(landmarks_list[9],landmarks_list[10],landmarks_list[12]) < 50 and 
        thumb_index_dist > 50 
    )

def is_double_click(landmarks_list,thumb_index_dist):
    return (
            util.get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 50 and
            util.get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) < 50 and
            thumb_index_dist > 50
    )
def is_screenshot(landmarks_list,thumb_index_dist):
    return (
            util.get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) > 90 and
            util.get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) > 90 and
            util.get_angle(landmarks_list[13], landmarks_list[14], landmarks_list[16]) > 90  and 
            util.get_angle(landmarks_list[17], landmarks_list[18], landmarks_list[20]) > 90 and 
            thumb_index_dist > 150
    )

def detect_gesture(frame, landmarks_list, processed):
    # mediapipe hands detect 21 gestures
    if len(landmarks_list) >=21:
        index_finger_tip = find_finger_tip(processed)
        thumb_index_dist = util.get_distance([landmarks_list[4],landmarks_list[5]])
        # Cursor Movement
        if thumb_index_dist < 50 and util.get_angle(landmarks_list[5],landmarks_list[6],landmarks_list[8]) > 90:
            move_mouse(index_finger_tip)
        # Left Click
        elif is_left_click(landmarks_list , thumb_index_dist): 
            mouse.press(Button.left)
            mouse.release(Button.left)
            cv2.putText(frame, "Left Click", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        elif is_right_click(landmarks_list , thumb_index_dist): 
            mouse.press(Button.right)
            mouse.release(Button.right)
            cv2.putText(frame, "Right Click", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
        elif is_double_click(landmarks_list , thumb_index_dist):
            pyautogui.doubleClick()
            cv2.putText(frame, "Double Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0),3)
        elif is_screenshot(landmarks_list,thumb_index_dist ):
            im1 = pyautogui.screenshot()
            label = random.randint(1, 1000)
            im1.save(f'my_screenshot_{label}.png')
            cv2.putText(frame, "Screenshot Taken", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)

def main():
    # Setting up the camera to capture video
    cap = cv2.VideoCapture(0)
    draw = mp.solutions.drawing_utils
    try:
        while cap.isOpened():
            # 'ret' will contain true or false depending upon the cap.read()
            # if ret is True then frame will contain a frame
            ret,frame = cap.read()
            if not ret :
                break
            # Flipping the image for mirror image so that right <-> left dosent get interchanged
            frame = cv2.flip(frame,1)
            # Open cv captures the frame by default in BGR format but to process 
            # it by mediapipe we need to convert it to RGB format 
            frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            # Now processing the RGB frame to detect all the 21 landmarks from frame
            processed = hands.process(frameRGB)
            landmarks_list = []
            if processed.multi_hand_landmarks:
                # If the processed frame captures 2 hands make it 1 and the respective landmarks
                hand_landmarks = processed.multi_hand_landmarks[0]
                # Drawing the Hand Landmarks with connections in thr open CV's BGR frame
                draw.draw_landmarks(frame,hand_landmarks,mpHands.HAND_CONNECTIONS)
                for lm in hand_landmarks.landmark:
                    landmarks_list.append((lm.x,lm.y))
            detect_gesture(frame, landmarks_list, processed)
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
            