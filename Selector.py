import os
import shutil
import pandas as pd

melignent = ["MEL","SCC","BCC"]
benign = ["NV","BKL","DF","VASC","AK"]

# 🔹 נתיב לתיקיית התמונות אחרי Augmentation
output_dir = "dataset/processed_images/output"

# 🔹 נתיב לקובץ ה-CSV עם התוויות
csv_file = "dataset/diagnoses.csv"  # עדכני לנתיב הנכון של ה-CSV שלך

# 🔹 קריאת קובץ ה-CSV
df = pd.read_csv(csv_file)

# 🔹 יצירת תיקיות לקטגוריות אם הן לא קיימות
malignant_dir = os.path.join(output_dir, "malignant")
benign_dir = os.path.join(output_dir, "benign")
unk_dir = os.path.join(output_dir, "unknown")

# 🔹 קבלת רשימת כל התמונות בתיקיית output
all_images = os.listdir(output_dir)

# 🔹 מעבר על כל שורת תמונה בקובץ ה-CSV
for index, row in df.iterrows():
    isic_id = row["image"]

    # 🔹 חיפוש הקובץ המתאים בתיקיית `output`
    matching_files = [f for f in all_images if isic_id in f]  # מחפש כל קובץ שמכיל את ה-ISIC ID

    # 🔹 אם נמצאו קבצים מתאימים, ממיינים אותם לתיקייה המתאימה
    for image_name in matching_files:
        image_path = os.path.join(output_dir, image_name)
        if os.path.exists(image_path):
            if row["image"] in melignent :  # מלנומה = malignant
                shutil.move(image_path, os.path.join(malignant_dir, image_name))
            elif row["image"] in benign:
                shutil.move(image_path, os.path.join(benign_dir, image_name))
            else:
                shutil.move(image_path, os.path.join(unk_dir, image_name))
