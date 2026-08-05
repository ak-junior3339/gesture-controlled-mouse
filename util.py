import numpy as np 

# Function: get_angle()
# Purpose : Calculates the angle formed by three points
#           (A, B, C), where B is the vertex.
#
#           A
#            \
#             \
#              B ------ C
#
#           The function finds the angle ∠ABC.
# ---------------------------------------------------------
def get_angle(a,b,c):
    # Find the direction (in radians) of vector BC
    # and subtract the direction of vector BA.
    # This gives the angle between the two vectors.
    # which means calculate the anglw between (bc and x axis) - (ab and x axis)
    # this will give the angle between the two lines
    radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
    # Convert radians to degrees and ignore the sign.
    angle = np.abs(np.degrees(radians))
    return angle


# ---------------------------------------------------------
# Function: get_distance()
# Purpose : Calculates the Euclidean distance between
#           two landmarks and scales it from
#           [0, 1]  --->  [0, 1000]
#
#           Landmark 1 ●------------● Landmark 2
#
#           The scaled value is easier to use for
#           applications like cursor movement,
#           volume control, or gesture detection.
# ---------------------------------------------------------
def get_distance(landmarks_list):
    # Need at least two landmarks to measure distance.
    if len(landmarks_list) < 2 :
        return 

    # Extract the coordinates of the two landmarks.
    (x1,y1),(x2,y2) = landmarks_list[0],landmarks_list[1]

    # Calculate the Euclidean distance using:
    # √((x2-x1)² + (y2-y1)²)
    L = np.hypot(x2 - x1, y2 - y1)

    # MediaPipe landmarks are normalized (0 to 1).
    # Scale the distance to a more convenient range (0 to 1000).
    return np.interp(L, [0, 1], [0, 1000])

