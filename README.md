# Sistem Pakar Diagnosa Kerusakan Komputer/Laptop

Program sistem pakar berbasis Python GUI yang mampu mendiagnosa kerusakan pada komputer/laptop berdasarkan gejala yang dimasukkan oleh pengguna, dilengkapi dengan solusi singkat untuk setiap kerusakan yang terdeteksi.

---

## Fitur Program

- Mendeteksi **6 jenis kerusakan** komputer/laptop
- **19 pertanyaan gejala** interaktif dengan jawaban YA/TIDAK
- **Progress bar** yang menunjukkan posisi pertanyaan saat ini
- Output menampilkan **nama kerusakan** dan **solusi singkat**
- Antarmuka grafis (GUI) menggunakan Tkinter
- Opsi untuk mengulang diagnosa setelah selesai

---

## Knowledge Base

| No | Kerusakan | Gejala Utama |
|----|-----------|--------------|
| 1 | RAM Rusak / Longgar | Blue screen, sering restart, gagal booting, bunyi beep |
| 2 | Overheat (Prosesor/CPU Panas) | Mati tiba-tiba, kipas berisik, panas berlebih, lambat saat berat |
| 3 | Hardisk Corrupt / Rusak | Gagal booting, file hilang, loading lama, bunyi klik |
| 4 | VGA / GPU Bermasalah | Layar artefak/glitch, layar hitam, driver crash, blue screen |
| 5 | Power Supply (PSU) Lemah | Mati tiba-tiba, gagal menyala, tidak stabil, bau terbakar |
| 6 | Infeksi Virus / Malware | Lambat, program terbuka sendiri, file hilang, iklan pop-up |

---

## Cara Menjalankan

**Requirement:**
- Python 3.x
- Tkinter (sudah built-in pada Python, tidak perlu instalasi tambahan)

**Jalankan program:**
```bash
python tugas.py
```

---

## Cara Penggunaan

1. Jalankan program, jendela aplikasi akan terbuka
2. Klik tombol **Mulai Diagnosa** untuk memulai sesi pemeriksaan
3. Jawab setiap pertanyaan gejala dengan menekan tombol **YA** atau **TIDAK**
4. Setelah semua pertanyaan selesai, hasil diagnosa beserta solusi akan muncul dalam popup
5. Klik **Mulai Diagnosa** kembali jika ingin mengulang pemeriksaan

---

## Struktur File

```
NIM-PraktikumKB-Pertemuan4/
│
├── percobaan1.py   # Silsilah keluarga — simulasi logika predikat Prolog
├── percobaan2.py   # Diagnosa malaria sederhana dengan set operations
├── percobaan3.py   # Sistem pakar malaria interaktif berbasis console
├── percobaan4.py   # Sistem pakar malaria berbasis GUI Tkinter
└── tugas.py        # Sistem pakar diagnosa kerusakan komputer/laptop (GUI)
```
