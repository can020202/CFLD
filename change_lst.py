import os

# Pfade
input_files = ["fashion/train.lst", "fashion/test.lst"]
output_dir = "fashion/filtered"

# Stelle sicher, dass der Zielordner existiert
os.makedirs(output_dir, exist_ok=True)

# Filter-Kriterium
filter_prefix = "fashionMENTees_Tanks"

for input_file in input_files:
    output_file = os.path.join(output_dir, os.path.basename(input_file))

    with open(input_file, "r", encoding="utf-8") as f_in:
        lines = f_in.readlines()

    # Nur Zeilen behalten, die mit dem gewünschten Präfix anfangen
    filtered_lines = [line for line in lines if line.startswith(filter_prefix)]

    # Gefilterte Zeilen in die neue Datei schreiben
    with open(output_file, "w", encoding="utf-8") as f_out:
        f_out.writelines(filtered_lines)

    print(f"Gefilterte Datei geschrieben: {output_file}")
