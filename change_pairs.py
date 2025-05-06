import os
import csv

# Eingabedateien
input_files = [
    "fashion/fasion-resize-pairs-train.csv",
    "fashion/fasion-resize-pairs-test.csv"
]

# Zielordner
output_dir = "fashion/filtered"
os.makedirs(output_dir, exist_ok=True)

# Filterkriterium
filter_prefix = "fashionMENTees_Tanks"

for input_file in input_files:
    output_file = os.path.join(output_dir, os.path.basename(input_file))

    with open(input_file, "r", encoding="utf-8") as f_in:
        reader = csv.DictReader(f_in)
        rows = [row for row in reader if row["from"].startswith(filter_prefix)]

    # Schreibvorgang mit Kopfzeile
    with open(output_file, "w", newline="", encoding="utf-8") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=["from", "to"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Gefilterte Datei geschrieben: {output_file}")