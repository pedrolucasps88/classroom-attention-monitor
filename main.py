import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions
import numpy as np

model_path = 'models/face_landmarker.task'
options = vision.FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=vision.RunningMode.VIDEO,
    num_faces=10,
    output_face_blendshapes=False,
    output_facial_transformation_matrixes=False
)
landmarker = vision.FaceLandmarker.create_from_options(options)
cap = cv2.VideoCapture(0)
frame_id = 0

while cap.isOpened():
    on, frame = cap.read()
    if not on:
        continue
    frame_id +=1
    frame.flags.writeable = False
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=frame
    )
    frame.flags.writeable = True
    result = landmarker.detect_for_video(mp_image, frame_id)
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    try:
        if result.face_landmarks:
            for i, face in enumerate(result.face_landmarks):
                print(f"face {i} detected with {len(face)} points")
    except:
        pass
    cv2.imshow('analise', cv2.flip(frame, 1))
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()