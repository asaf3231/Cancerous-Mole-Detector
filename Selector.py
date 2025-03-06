import os
import shutil
import pandas as pd

# 🔹 נתיב לתיקיית התמונות שעברו Augmentation
output_dir = "dataset/processed_images/output"

# 🔹 נתיב לקובץ ה-CSV עם התוויות
csv_file = "dataset/diagnoses.csv"  # עדכני לנתיב הנכון של ה-CSV שלך

# 🔹 קריאת קובץ ה-CSV
df = pd.read_csv(csv_file)

# 🔹 יצירת תיקיות `malignant` ו-`benign` בתוך `output`
malignant_dir = os.path.join(output_dir, "malignant")
benign_dir = os.path.join(output_dir, "benign")
os.makedirs(malignant_dir, exist_ok=True)
os.makedirs(benign_dir, exist_ok=True)

# 🔹 מעבר על כל שורת תמונה בקובץ ה-CSV
for index, row in df.iterrows():
    image_name = row["image"] + ".jpg"  # הוספת סיומת לתמונה
    
    # בדיקה אם הקובץ קיים ב-`output/`
    image_path = os.path.join(output_dir, image_name)
    if not os.path.exists(image_path):
        continue  # אם הקובץ לא נמצא, דולג עליו

    # 🔹 מיון התמונה לפי הקטגוריה שלה
    if row["MEL"] == 1:  # אם מלנומה, מעבירים ל-malignant
        shutil.move(image_path, os.path.join(malignant_dir, image_name))
    elif row["NV"] == 1:  # אם שומה שפירה, מעבירים ל-benign
        shutil.move(image_path, os.path.join(benign_dir, image_name))

print("✔ כל התמונות מוינו בהצלחה לתיקיות `malignant/` ו-`benign/`.")