import os

def generate_layout_xml(layout_name, primary_color, background_color, components):
    xml_lines = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<androidx.constraintlayout.widget.ConstraintLayout',
        '    xmlns:android="http://schemas.android.com/apk/res/android"',
        '    xmlns:app="http://schemas.android.com/apk/res-auto"',
        '    android:layout_width="match_parent"',
        '    android:layout_height="match_parent"',
        f'    android:background="{background_color}">',
        ''
    ]

    id_counter = 1
    for component in components:
        if component == "TextView":
            xml_lines += [
                f'    <TextView',
                f'        android:id="@+id/textView{id_counter}"',
                f'        android:layout_width="wrap_content"',
                f'        android:layout_height="wrap_content"',
                f'        android:text="Hello, Material3!"',
                f'        android:textColor="{primary_color}"',
                f'        app:layout_constraintTop_toTopOf="parent"',
                f'        app:layout_constraintStart_toStartOf="parent"',
                f'        android:layout_marginTop="32dp"',
                f'        android:layout_marginStart="16dp" />',
                ''
            ]
        elif component == "Button":
            xml_lines += [
                f'    <Button',
                f'        android:id="@+id/button{id_counter}"',
                f'        android:layout_width="wrap_content"',
                f'        android:layout_height="wrap_content"',
                f'        android:text="Klik Saya"',
                f'        android:backgroundTint="{primary_color}"',
                f'        android:textColor="#FFFFFF"',
                f'        app:layout_constraintTop_toBottomOf="@+id/textView{id_counter}"',
                f'        app:layout_constraintStart_toStartOf="parent"',
                f'        android:layout_marginTop="24dp"',
                f'        android:layout_marginStart="16dp" />',
                ''
            ]
        elif component == "EditText":
            xml_lines += [
                f'    <EditText',
                f'        android:id="@+id/editText{id_counter}"',
                f'        android:layout_width="match_parent"',
                f'        android:layout_height="wrap_content"',
                f'        android:hint="Masukkan teks..."',
                f'        android:textColor="{primary_color}"',
                f'        app:layout_constraintTop_toBottomOf="@+id/button{id_counter}"',
                f'        app:layout_constraintStart_toStartOf="parent"',
                f'        app:layout_constraintEnd_toEndOf="parent"',
                f'        android:layout_marginTop="24dp"',
                f'        android:layout_marginHorizontal="16dp" />',
                ''
            ]
        id_counter += 1

    xml_lines.append('</androidx.constraintlayout.widget.ConstraintLayout>')

    filename = f"{layout_name}.xml"
    with open(filename, "w") as f:
        f.write("\n".join(xml_lines))
    return filename


# CLI
print("╔══════════════════════════════╗")
print("║ Android Layout Generator 🧩 ║")
print("╚══════════════════════════════╝")

layout_name = input("Nama layout (tanpa .xml): ").strip()
primary_color = input("Warna utama (contoh #6200EE): ").strip()
background_color = input("Warna latar belakang (contoh #FFFFFF): ").strip()

print("\nPilih komponen yang ingin ditambahkan:")
print("[1] TextView\n[2] Button\n[3] EditText")
selected = input("Masukkan pilihan (pisahkan dengan koma): ").strip()

map_components = {
    "1": "TextView",
    "2": "Button",
    "3": "EditText"
}

selected_components = [map_components.get(i.strip()) for i in selected.split(",") if map_components.get(i.strip())]

if not selected_components:
    print("❌ Tidak ada komponen dipilih.")
else:
    output_file = generate_layout_xml(layout_name, primary_color, background_color, selected_components)
    print(f"\n✅ File '{output_file}' berhasil dibuat! Letakkan di folder `res/layout/` Android Studio.")
