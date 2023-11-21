import cv2
import mediapipe as mp


# All the Landmarks for Lips

# LIPS = [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95,
#         185, 40, 39, 37, 0, 267, 269, 270, 409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78]

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    while True:

        ret, frame = cap.read()

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_mesh.process(frame_rgb)

        if results.multi_face_landmarks:
            for landmarks in results.multi_face_landmarks:
                # to Extract landmarks for the upper and lower lips
                upper_lip_landmarks = landmarks.landmark[0]
                lower_lip_landmarks = landmarks.landmark[87]

                # to Calculate the distance between the upper and lower lip landmarks
                lip_distance = abs(upper_lip_landmarks.y - lower_lip_landmarks.y)*100
                print(int(lip_distance))

                mouth_open = lip_distance > 1

                # Display the mouth openness status
                status_text = "Mouth Open" if mouth_open else "Mouth Closed"
                cv2.putText(frame, status_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Mouth Openness Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

