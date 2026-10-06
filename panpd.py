# import pandas as pd

# df = pd.read_csv(r"C:\Users\rober\Downloads\Housing.csv")

# from pathlib import Path

# print(Path(__file__).with_name("housing_data").read_text())

# print(df.head())
# print(df.info())
# print(df.describe())

# import csv
# from pathlib import Path

# file_path = Path(__file__).with_name("housing_data")

# with file_path.open(newline="", encoding="utf-8") as file:
#     for row in csv.reader(file):
#         print(row)