import os
import shutil

# train/test list files
splits = {
    "train": "fashion/train.lst",
    "test": "fashion/test.lst"
}

# Basisverzeichnis der Bilder
base_image_dir = "fashion/MEN/Tees_Tanks"
output_base = "fashion/filtered"

# Zielordner erstellen
for split in splits:
    os.makedirs(os.path.join(output_base, f"{split}_highres"), exist_ok=True)

for split, list_path in splits.items():
    with open(list_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.startswith("fashionMENTees_Tanks")]

    ids = set()
    for line in lines:
        try:
            full_id = line.split("id")[1].split("_")[0]  # z. B. 0000122204
            short_id = full_id[:8]                      # z. B. 00001222
            folder_name = f"id_{short_id}"
            ids.add(folder_name)
        except IndexError:
            print(f"❌ Fehlerhafte Zeile: {line}")

    for folder_name in ids:
        source_folder = os.path.join(base_image_dir, folder_name)
        target_folder = os.path.join(output_base, f"{split}_highres")

        if os.path.isdir(source_folder):
            for fname in os.listdir(source_folder):
                src = os.path.join(source_folder, fname)
                dst = os.path.join(target_folder, f"{folder_name}_{fname}")
                shutil.copy2(src, dst)
        else:
            print(f"⚠️ Ordner nicht gefunden: {source_folder}")

    print(f"✅ Alle Bilder für {split} wurden kopiert.")
