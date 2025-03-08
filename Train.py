from keras.src.legacy.preprocessing.image import ImageDataGenerator
from keras.src.saving import load_model
import tensorflow as tf

tf.config.run_functions_eagerly(True)
# טעינת המודל השמור (אם בנית אותו בקובץ אחר)
model = load_model("models/skin_lesion_classifier.h5")

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
# **📌 טוענים מחדש את הנתונים עבור האימון**
train_datagen = ImageDataGenerator(validation_split=0.2)

train_generator = train_datagen.flow_from_directory(
    "dataset/processed_images/output/",
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical",
    subset="training"
)

val_generator = train_datagen.flow_from_directory(
    "dataset/processed_images/output/",
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical",
    subset="validation"
)

# **📌 ביצוע האימון**
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=50,
    verbose=1
)

print("✔ האימון הסתיים!")

# **📌 שמירת המודל מחדש לאחר האימון**
model.save("models/skin_lesion_classifier_trained.h5")
