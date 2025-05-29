# Folder Renamer Script

This Python script renames folders inside a specified directory based on a CSV mapping file. It helps you temporarily rename folders with user-friendly names for easier editing and then revert them back to their original names for program compatibility.

---

## Features

- Rename folders from "original" names to "new" names based on CSV mappings.
- Rename folders back to original names using a `--reverse` flag.
- Skips missing folders and warns if the destination name already exists.

---

## Usage

Run the script from the command line with the following arguments:

```bash
python folder_renamer.py <directory_path> <csv_file> [--reverse]