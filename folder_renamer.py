import os
import csv
import argparse

def load_mappings(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        print(f"Detected columns: {reader.fieldnames}")

        expected_cols = {'original', 'new'}
        if not expected_cols.issubset(reader.fieldnames):
            raise ValueError(f"CSV is missing expected columns: {expected_cols}")
        
        rows = list(reader)

        for row in rows:
            print(row)
        
        return [(row['original'], row['new']) for row in rows]

def rename_folders(base_path, mappings, reverse=False):
    for original, new in mappings:
        src = os.path.join(base_path, new if reverse else original)
        dst = os.path.join(base_path, original if reverse else new)

        print(f"Attempting: {src} -> {dst}")  # Debug print

        if not os.path.exists(src):
            print(f"[SKIP] Source folder does not exist: {src}")
            continue
        if os.path.exists(dst):
            print(f"[WARN] Destination already exists, skipping: {dst}")
            continue

        os.rename(src, dst)
        print(f"[OK] Renamed: {src} -> {dst}")

def main():
    parser = argparse.ArgumentParser(description="Rename folders based on a CSV mapping file.")
    parser.add_argument("directory", help="Path to the folder containing folders to rename")
    parser.add_argument("csv", help="CSV file with 'original' and 'new' folder name mappings.")
    parser.add_argument("--reverse", action="store_true", help="Use this to rename back to original names.")

    args = parser.parse_args()

    mappings = load_mappings(args.csv)
    rename_folders(args.directory, mappings, reverse=args.reverse)

if __name__ == "__main__":
    main()