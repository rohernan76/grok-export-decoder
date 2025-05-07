# Grok Export Decoder

This tool helps you decode and convert raw export files from Grok (xAI's chatbot) into usable file formats like `.png`, `.json`, `.csv`, or `.txt`.

## 🧠 Why This Exists

Grok exports chat data into folders with UUID names and ambiguous `content` files. These files might be:
- Hexadecimal dumps (encoded PNGs, JSON, etc.)
- Raw binary files
- UTF-8 text blobs

This script batch-processes all such files in a folder and:
- Detects if the file is already binary or hex-encoded
- Converts or copies appropriately
- Outputs clean, labeled files in a `/converted` directory

## 🛠️ Usage

### 1. Clone this repo

```bash
git clone https://github.com/rohernan76/grok-export-decoder.git
cd grok-export-decoder
```

### 2. Set up a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Move your Grok folders into this project directory (or adjust the script path)

```bash
python3 hex_to_binary_smart_batch.py
```

### 4. Check the `/converted` folder for output!

## 📁 Output Examples

| Original File        | Converted Output       | Type        |
|----------------------|------------------------|-------------|
| content 2_copy.bin   | content_2.txt          | UTF-8 text  |
| content 3_copy.bin   | content_3.csv          | CSV         |
| content 4_copy.bin   | content_4.png          | PNG image   |
| content 5_copy.bin   | content_5.json         | JSON        |

## ✅ Requirements

See `requirements.txt` for Python dependencies.
