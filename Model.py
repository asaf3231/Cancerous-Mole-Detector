from keras.src.applications.mobilenet_v2 import MobileNetV2
from keras.src.layers import Dense, Flatten, Dropout
from keras.src.models import Model
import os

# טעינת MobileNetV2 ללא השכבות העליונות
base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights="imagenet")

# הוספת שכבות מותאמות ל-3 קטגוריות
x = Flatten()(base_model.output)
x = Dense(128, activation="relu")(x)
x = Dropout(0.3)(x)  # Dropout למניעת Overfitting
x = Dense(3, activation="softmax")(x)  # שלוש קטגוריות: malignant, benign, unknown

# בניית המודל הסופי
model = Model(inputs=base_model.input, outputs=x)

# הקפאת השכבות של MobileNetV2 למניעת אימון מחדש
for layer in base_model.layers:
    layer.trainable = False

# קומפילציה של המודל
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

if not os.path.exists("models"):
    os.makedirs("models")

model.save("models/skin_lesion_classifier.h5")