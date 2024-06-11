import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

# Load the pre-trained model
# json_file = open("emotiondetector.json", "r")
# model_json = json_file.read()
# json_file.close()
# model = model_from_json(model_json)
model = load_model("best_model.h5")

# Define the list of emotion labels
labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Open a connection to the webcam (0 indicates the default webcam)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (48, 48), interpolation=cv2.INTER_LINEAR)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    # Resize the frame to match the input size of the trained model
    roi = cv2.resize(gray, (48, 48))
    
    # Normalize the frame
    roi = roi / 255.0

    # Reshape the frame to match the input shape expected by the model
    roi = np.reshape(roi, (1, 48, 48, 1))

    # Make a prediction
    prediction = model.predict(roi)
    
    # Get the predicted emotion label
    emotion_label = labels[np.argmax(prediction)]

    # Display the emotion label on the frame
    cv2.putText(frame, f"Emotion: {emotion_label}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Emotion Detection', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
