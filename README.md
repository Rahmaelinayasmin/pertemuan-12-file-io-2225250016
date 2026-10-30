# Pertemuan 12 - File I/O dan Error Handling

Nama: Rahma Elina Yasmin
NIM: 2225250016
Kelas: 3F

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input
NIM,nilai

## Cara Menjalankan
python tugas/rekap_nilai_file.py

## Error yang Ditangani
- FileNotFoundError
- ValueError

## Test Case

| Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| File tersedia dan data valid | Rekap berhasil dibuat | Rekap ditulis ke data/hasil_rekap.txt | Berhasil |
| File tidak ditemukan | Menampilkan pesan error | File tidak ditemukan | Berhasil |
| Nilai tidak valid | Baris dilewati | Baris tidak valid dilewati | Berhasil |

## Refleksi
Error yang ditemukan adalah FileNotFoundError karena program dijalankan dari folder yang tidak sesuai. Error tersebut ditangani dengan memastikan program dijalankan dari folder utama proyek dan menggunakan try-except.