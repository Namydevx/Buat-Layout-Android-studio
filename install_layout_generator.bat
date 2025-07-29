@echo off
cls
echo ============================================
echo   🔧 Menginstall Layout Generator...
echo ============================================

:: Cek apakah Python sudah ada
where python >nul 2>&1
if errorlevel 1 (
    echo ❌ Python belum terinstal. Silakan install Python dulu dari https://www.python.org
    pause
    exit /b
)

:: Unduh file dari GitHub
echo ⏳ Mengunduh skrip...
curl -o layout_generator.py https://raw.githubusercontent.com/Namydevx/Buat-Layout-Android-studio/main/layout_generator.py

:: Jalankan skrip
echo ✅ Selesai. Menjalankan tool...
python layout_generator.py

pause
