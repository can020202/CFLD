import os

# Eingabedateien
input_files = [
    "fashion/fasion-resize-annotation-train.csv",
    "fashion/fasion-resize-annotation-test.csv"
]


# Zielverzeichnis
output_dir = "fashion/filtered"
os.makedirs(output_dir, exist_ok=True)

# Filterkriterium
filter_prefix = "fashionMENTees_Tanks"

for input_file in input_files:
    output_file = os.path.join(output_dir, os.path.basename(input_file))

    with open(input_file, "r", encoding="utf-8") as f_in:
        lines = f_in.readlines()

    # Kopfzeile behalten
    header = lines[0]
    filtered_lines = [line for line in lines[1:] if line.startswith(filter_prefix)]

    # Neue Datei mit Kopfzeile + gefilterten Daten schreiben
    with open(output_file, "w", encoding="utf-8") as f_out:
        f_out.write(header)
        f_out.writelines(filtered_lines)

    print(f"Gefilterte Datei geschrieben: {output_file}")
