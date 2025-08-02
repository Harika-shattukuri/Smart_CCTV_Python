import cv2
import time
import datetime
import pyaudio
import numpy as np
import wave

# Initialize video capture
cap = cv2.VideoCapture(0)

# Load the face and body cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

# Initialize detection variables
detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

# Set frame size and codec for video writer
frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Initialize PyAudio
p = pyaudio.PyAudio()
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
THRESHOLD = 500  # Adjust this threshold according to your environment

# Open audio stream
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

def detect_noise():
    data = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False), dtype=np.int16)
    return np.max(data) > THRESHOLD

# Function to save audio
def save_audio(frames, filename):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# List to hold audio frames
audio_frames = []

while True:
    # Read a frame from the webcam
    _, frame = cap.read()

    # Convert the frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)
    noise_detected = detect_noise()

    # Detection logic
    if len(faces) + len(bodies) > 0 or noise_detected:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
            audio_frames = []  # Clear previous audio frames
            print("Started Recording!")
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                save_audio(audio_frames, f"{current_time}.wav")
                print('Stopped Recording!')
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)
        audio_frames.append(stream.read(CHUNK, exception_on_overflow=False))

    # Display the frame
    cv2.imshow("Camera", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
if detection:
    out.release()
    save_audio(audio_frames, f"{current_time}.wav")
cap.release()
stream.stop_stream()
stream.close()
p.terminate()
cv2.destroyAllWindows()