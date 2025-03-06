import pandas as pd 

csv_path = "./dataset/diagnoses.csv"
df = pd.read_csv(csv_path)
df = df[['image', 'MEL', 'NV', 'BCC', 'AK', 'BKL', 'DF', 'VASC', 'SCC', 'UNK']]