import cv2
import mediapipe as mp

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize Webcam
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)
        # Convert the frame to RGB as Mediapipe expects RGB input
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame for hand landmarks
        result = hands.process(rgb_frame)
        
        # Draw hand landmarks if any are detected
        if result.multi_hand_landmarks:
            for hand_landmarks, hand_label in zip(result.multi_hand_landmarks, result.multi_handedness):
                # Draw the hand landmarks
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Get label of the hand (Left or Right)
                label = hand_label.classification[0].label
                # Draw the label on the frame
                cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
        # Show the output frame
        cv2.imshow('Hand Detection', frame)
        
        # Exit loop on 'q' press
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
