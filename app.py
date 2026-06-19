import streamlit as st
import cv2
from music_player import play_music

st.title("🎭 Emotion AI Music Player")

run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # dummy emotion (replace with model prediction)
    emotion = "happy"

    play_music(emotion)

    FRAME_WINDOW.image(frame)

cap.release()