import numpy as np
import cv2
from tensorflow.keras.utils import to_categorical
from emotion_model import create_model
import os

# Example label map
emotion_labels = ['angry','disgust','fear','happy','neutral','sad','surprise']

def load_data(path):
    data = []
    labels = []

    for label, emotion in enumerate(emotion_labels):
        folder = os.path.join(path, emotion)

        for img_name in os.listdir(folder):
            img = cv2.imread(os.path.join(folder, img_name), cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (48,48))

            data.append(img)
            labels.append(label)

    data = np.array(data).reshape(-1,48,48,1) / 255.0
    labels = to_categorical(labels, num_classes=7)

    return data, labels


train_data, train_labels = load_data("dataset/train")

model = create_model()

model.fit(train_data, train_labels, epochs=15, batch_size=64, validation_split=0.2)

model.save("model/emotion_model.h5")

print("Model Trained Successfully!")