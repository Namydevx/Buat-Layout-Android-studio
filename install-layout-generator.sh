#!/bin/bash

clear
echo -e "\033[96m╔════════════════════════════════════════╗"
echo -e "║  🔧 Menginstall Layout Generator...     ║"
echo -e "╚════════════════════════════════════════╝\033[0m"

# Instal Python jika belum ada
if ! command -v python3 &> /dev/null; then
    echo "⏳ Python belum terinstal, menginstal sekarang..."
    apt update && apt install -y python3
fi

# Unduh skrip dari GitHub
curl -sSLo layout_generator.py https://raw.githubusercontent.com/Namydevx/Buat-Layout-Android-studio/main/layout_generator.py

# Tambahkan permission
chmod +x layout_generator.py

# Jalankan
echo -e "\n\033[92m✅ Skrip berhasil diunduh. Menjalankan tool...\033[0m"
python3 layout_generator.py
