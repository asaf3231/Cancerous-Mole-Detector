import cv2
import os

# נתיב לתיקיית התמונות
input_folder = "./dataset/images"
output_folder = "./dataset/processed_images"

# יצירת תיקייה חדשה לתמונות המעובדות
os.makedirs(output_folder, exist_ok=True)
# מעבר על כל התמונות בתיקייה
for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)

            # שינוי גודל התמונה ל-224x224
            img_resized = cv2.resize(img, (224, 224))

            # שמירה של התמונה המעובדת
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, img_resized)

print(img_resized)