import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

counter = 0
stage = None

# Function to calculate angle
def calculate_angle(a, b, c):

    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle > 180:
        angle = 360-angle

    return angle


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

with mp_pose.Pose(min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:

            landmarks = results.pose_landmarks.landmark

            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            angle = calculate_angle(shoulder, elbow, wrist)

            cv2.putText(image, str(int(angle)),
                        tuple(np.multiply(elbow, [640,480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (255,255,255), 2)

            shoulder_y = shoulder[1]
            wrist_y = wrist[1]

            # Arm down
            if wrist_y > shoulder_y:
                stage = "DOWN"

            # Correct hand raise
            if wrist_y < shoulder_y and stage == "DOWN" and angle > 150:
                stage = "UP"
                counter += 1

            # Wrong posture 1: arm bent
            if wrist_y < shoulder_y and angle < 150:
                cv2.putText(image, "Straighten Arm!", (200,80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0,0,255), 2)

            # Wrong posture 2: hand not high enough
            if wrist_y > shoulder_y and angle > 150:
                cv2.putText(image, "Raise Hand Higher!", (200,120),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0,0,255), 2)

        except:
            pass

        cv2.rectangle(image, (0,0), (260,90), (245,117,16), -1)

        cv2.putText(image, 'Hand Raises', (10,20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0,0,0), 2)

        cv2.putText(image, str(counter), (10,70),
                    cv2.FONT_HERSHEY_SIMPLEX, 2,
                    (255,255,255), 2)

        if counter >= 5:
            cv2.putText(image, "Target Reached!", (200,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0,255,0), 2)

        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

        cv2.imshow('Hand Raise Detection', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    print("Total Hand Raises Detected:", counter)

    cap.release()
    cv2.destroyAllWindows()