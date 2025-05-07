
import os
import shutil
from pathlib import Path

def is_probably_binary(data: bytes) -> bool:
    # Check for non-ASCII characters as a rough heuristic
    text_characters = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)))
    return bool(data.translate(None, text_characters))

def hex_to_binary(hex_str: str) -> bytes:
    cleaned_hex = hex_str.replace('\n', ' ').replace('\r', ' ').strip()
    return bytes.fromhex(cleaned_hex)

def main():
    base_dir = Path.cwd()
    content_dir = base_dir
    output_dir = base_dir / "converted"
    output_dir.mkdir(exist_ok=True)

    for file in content_dir.glob("content*"):
        if file.is_file():
            try:
                with open(file, "rb") as f:
                    raw = f.read()

                try:
                    # Try interpreting as hex dump
                    text = raw.decode("utf-8")
                    binary_data = hex_to_binary(text)
                    output_file = output_dir / f"{file.name}_converted.bin"
                    with open(output_file, "wb") as out:
                        out.write(binary_data)
                    print(f"[✓] Converted hex: {file.name} → {output_file.name}")
                except (ValueError, UnicodeDecodeError):
                    # If decode fails, treat as already-binary
                    output_file = output_dir / f"{file.name}_copy.bin"
                    shutil.copy(file, output_file)
                    print(f"[✓] Copied binary: {file.name} → {output_file.name}")
            except Exception as e:
                print(f"[!] Error processing {file.name}: {e}")

if __name__ == "__main__":
    main()
