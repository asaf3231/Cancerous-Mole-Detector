import sys
import os
import Augmentor

# קבלת הנתיב של התיקייה הראשית (בה נמצאת isic-2019)
BASE_DIR = os.path.dirname(os.path.abspath("/Users/asaframati/Documents/Reichman/IOT/isicChallenge"))
# הוספת הנתיב של isic-2019 לנתיב החיפוש של פייתון
sys.path.append(os.path.join(BASE_DIR, "isic-2019"))

# יצירת Pipeline של Augmentation לתמונות שלך
pipeline = Augmentor.Pipeline("dataset/processed_images")  # הנתיב לתמונות שלך


num_images = len([f for f in os.listdir("dataset/processed_images") if f.endswith((".jpg"))])

# 📌 הוספת טרנספורמציות ל-Augmentor
pipeline.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)  # סיבוב קל
pipeline.flip_left_right(probability=0.5)  # שיקוף אופקי
pipeline.zoom(probability=0.5, min_factor=1.1, max_factor=1.3)  # זום אקראי
pipeline.random_brightness(probability=0.5, min_factor=0.7, max_factor=1.3)  # שינוי תאורה

# 📌 הפעלת ה-Augmentation ליצירת 1000 תמונות חדשות
pipeline.sample(num_images * 2)
print("done")