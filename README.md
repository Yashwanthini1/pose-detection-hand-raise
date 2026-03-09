# pose-detection-hand-raise
This is a Computer vision project using OpenCV and MediaPipe for Human pose detection system that detects body landmarks, counts hand raises in real time, and provides feedback for incorrect posture.
Features
- Real-time pose detection using MediaPipe
- Detects human body landmarks
- Counts the number of hand raises
- Detects incorrect posture
- Displays feedback messages on the screen
- Stops when the target number of repetitions is reached

Technologies Used
- Python
- OpenCV
- MediaPipe
- NumPy

Installation

Clone the repository:

git clone https://github.com/Yashwanthini1/pose-detection-hand-raise.git

Navigate to the project folder:

cd pose-detection-hand-raise

Install the required libraries:

pip install -r requirements.txt

How to Run the Program

Run the following command:

python hand_raise_detection.py

The webcam will open and begin detecting body landmarks.

How It Works

The system uses MediaPipe Pose to detect body landmarks such as the shoulder, elbow, and wrist.

The program calculates the angle between the shoulder, elbow, and wrist joints to determine whether the arm is raised correctly.

If the hand moves from a down position to above the shoulder, the program counts it as a valid hand raise.

The system also detects incorrect posture and displays feedback such as:
- Straighten Arm! when the arm is bent
- Raise Hand Higher! when the hand is not lifted enough

The counter increases until the target number of repetitions is reached.

Output

The program displays:
- Body pose landmarks
- Hand raise counter
- Real-time feedback messages
- Target completion message when the required repetitions are reached

Applications
- Fitness monitoring
- Exercise repetition counting
- Human activity recognition
- Computer vision learning projects

Requirements
Make sure your system has:
- Python 3.8+
- Webcam enabled

Install dependencies using:

pip install opencv-python mediapipe numpy

Author
This project was developed as a computer vision application using OpenCV and MediaPipe for pose detection and exercise tracking.
