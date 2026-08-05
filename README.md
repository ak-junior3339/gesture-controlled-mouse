#  Virtual Mouse using Hand Gestures

Control your computer mouse using just your hand! This project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to detect hand gestures in real-time and perform mouse actions such as cursor movement, clicking, double-clicking, and taking screenshots.

---

## Features

- Move the mouse cursor using your index finger
- Left Click
- Right Click
- Double Click
- Take Screenshot using a hand gesture
- Real-time gesture recognition
- Webcam-based interaction (No additional hardware required)
- More can be added as well 

---

## Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI
- pynput

---

## Project Structure

```
Virtual-Mouse/
│
├── main.py          # Main application
├── util.py          # Helper functions (angle & distance calculations)
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 📌 How It Works

1. The webcam captures live video.
2. MediaPipe detects **21 hand landmarks**.
3. The project calculates:
   - Finger joint angles
   - Distance between thumb and index finger
4. Different gesture combinations are mapped to mouse operations.
5. PyAutoGUI and pynput execute the corresponding mouse events.

---

## ✋ Supported Gestures

| Gesture | Action |
|----------|--------|
| Index finger extended + Middle finger extended + Thumb close | Move Cursor |
| Index finger bent | Left Click |
| Middle finger bent | Right Click |
| Index + Middle finger bent | Double Click |
| Open Palm Widely | Take Screenshot |

> **Note:** Gesture detection is based on finger joint angles and thumb-index finger distance.

---

## 🧠 Gesture Detection Logic

The project detects gestures by computing:

- **Finger joint angles**
- **Euclidean distance** between thumb and index finger

### Helper Functions

- `get_angle()`
  - Calculates the angle between three hand landmarks.

- `get_distance()`
  - Computes the Euclidean distance between two landmarks.

These values are used to determine which gesture is currently being performed.

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/ak-junior3339/gesture-controlled-mouse.git

cd Virtual-Mouse
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

Press **Q** to quit.

---

## 📚 Required Libraries

```text
opencv-python
mediapipe
numpy
pyautogui
pynput
```

Install manually if needed:

```bash
pip install opencv-python mediapipe numpy pyautogui pynput
```

---

## 🎯 Future Improvements

- Smooth cursor movement using interpolation
- Drag and Drop gesture
- Scroll gesture
- Volume control
- Brightness control
- Multi-hand support
- Custom gesture training
- Gesture calibration for different users

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub. It helps others discover the project and motivates further development!

---

## 👨‍💻 Author

**Aishwarya Kumar Singh**

Passionate about Machine Learning, Deep Learning, Computer Vision, and AI-powered applications.

LinkedIn: https://www.linkedin.com/in/aishwarya-kumar-singh-244a93269/