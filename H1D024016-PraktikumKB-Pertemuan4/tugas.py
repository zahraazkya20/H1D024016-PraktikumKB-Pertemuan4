import tkinter as tk
from tkinter import messagebox

# SISTEM PAKAR KERUSAKAN KOMPUTER/LAPTOP

# KNOWLEDGE BASE
knowledge_base = {
    "RAM Rusak / Longgar": {
        "gejala": ["blue_screen", "sering_restart", "gagal_booting", "bunyi_beep"],
        "solusi": "Coba bersihkan pin RAM dengan penghapus karet lalu pasang kembali. Jika tetap bermasalah, ganti RAM baru."
    },
    "Overheat (Prosesor/CPU Panas)": {
        "gejala": ["mati_tiba_tiba", "kipas_berisik", "lambat_saat_berat", "panas_berlebih"],
        "solusi": "Bersihkan debu pada heatsink dan kipas. Ganti thermal paste prosesor. Pastikan ventilasi laptop/PC tidak tertutup."
    },
    "Hardisk Corrupt / Rusak": {
        "gejala": ["gagal_booting", "file_hilang", "loading_lama", "bunyi_klik"],
        "solusi": "Jalankan perintah 'chkdsk /f' di CMD. Backup data segera. Jika ada bunyi klik, segera ganti hardisk baru."
    },
    "VGA / GPU Bermasalah": {
        "gejala": ["layar_artefak", "layar_hitam", "driver_crash", "blue_screen"],
        "solusi": "Update atau reinstall driver VGA. Jika VGA eksternal, coba cabut-pasang kembali. Cek kondisi slot PCIe."
    },
    "Power Supply (PSU) Lemah": {
        "gejala": ["mati_tiba_tiba", "gagal_menyala", "tidak_stabil", "bau_terbakar"],
        "solusi": "Ukur tegangan output PSU dengan multimeter. Jika tidak stabil atau ada bau terbakar, segera ganti PSU baru."
    },
    "Infeksi Virus / Malware": {
        "gejala": ["lambat_saat_berat", "program_terbuka_sendiri", "file_hilang", "iklan_muncul"],
        "solusi": "Jalankan scan antivirus secara full scan. Gunakan Malwarebytes untuk malware. Pertimbangkan install ulang OS jika parah."
    }
}

# DAFTAR SEMUA GEJALA UNTUK PERTANYAAN
semua_gejala = [
    ("blue_screen", "Apakah komputer/laptop sering mengalami Blue Screen (BSOD)?"),
    ("sering_restart", "Apakah komputer/laptop sering restart sendiri secara tiba-tiba?"),
    ("gagal_booting", "Apakah komputer/laptop sering gagal atau lama saat booting?"),
    ("bunyi_beep", "Apakah terdengar bunyi BEEP panjang/berulang saat dinyalakan?"),
    ("mati_tiba_tiba", "Apakah komputer/laptop mati mendadak tanpa peringatan?"),
    ("kipas_berisik", "Apakah kipas/fan terdengar sangat berisik saat beroperasi?"),
    ("lambat_saat_berat", "Apakah sistem sangat lambat saat menjalankan program berat?"),
    ("panas_berlebih", "Apakah bodi laptop/PC terasa sangat panas saat digunakan?"),
    ("file_hilang", "Apakah ada file yang hilang atau tidak bisa dibuka tiba-tiba?"),
    ("loading_lama", "Apakah loading program/file membutuhkan waktu sangat lama?"),
    ("bunyi_klik", "Apakah terdengar bunyi klik-klik dari dalam casing saat bekerja?"),
    ("layar_artefak", "Apakah muncul artefak/glitch aneh atau garis-garis di layar?"),
    ("layar_hitam", "Apakah layar tiba-tiba menjadi hitam meski komputer masih menyala?"),
    ("driver_crash", "Apakah sering muncul notifikasi driver crash atau not responding?"),
    ("gagal_menyala", "Apakah komputer/laptop kadang sama sekali tidak mau menyala?"),
    ("tidak_stabil", "Apakah tegangan listrik/daya terasa tidak stabil saat digunakan?"),
    ("bau_terbakar", "Apakah tercium bau seperti terbakar atau hangus dari dalam casing?"),
    ("program_terbuka_sendiri", "Apakah ada program atau jendela yang terbuka sendiri tanpa perintah?"),
    ("iklan_muncul", "Apakah sering muncul iklan pop-up secara tiba-tiba di layar?")
]

# KELAS APLIKASI GUI
class AplikasiPakarKomputer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Kerusakan Komputer/Laptop")
        self.root.geometry("520x320")
        self.root.resizable(False, False)

        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        # HEADER
        self.label_judul = tk.Label(
            root,
            text="Sistem Pakar Diagnosa Kerusakan Komputer/Laptop",
            font=("Arial", 11, "bold"),
            wraplength=500,
            justify="center"
        )
        self.label_judul.pack(pady=(15, 5))

        self.label_sub = tk.Label(
            root,
            text="Jawab setiap pertanyaan dengan jujur sesuai kondisi perangkat Anda.",
            font=("Arial", 9),
            fg="gray"
        )
        self.label_sub.pack()

        # AREA PERTANYAAN
        self.frame_pertanyaan = tk.Frame(root, relief="groove", bd=2, padx=10, pady=10)
        self.frame_pertanyaan.pack(fill="x", padx=20, pady=10)

        self.label_nomor = tk.Label(
            self.frame_pertanyaan,
            text="",
            font=("Arial", 9),
            fg="#888888"
        )
        self.label_nomor.pack(anchor="w")

        self.label_tanya = tk.Label(
            self.frame_pertanyaan,
            text="Klik 'Mulai Diagnosa' untuk memulai pemeriksaan.",
            font=("Arial", 11),
            wraplength=460,
            justify="left"
        )
        self.label_tanya.pack(anchor="w", pady=(2, 0))

        # PROGRESS BAR SEDERHANA
        self.label_progress = tk.Label(root, text="", font=("Arial", 9), fg="#555555")
        self.label_progress.pack()

        # FRAME TOMBOL JAWABAN (disembunyikan di awal)
        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(
            self.frame_jawaban, text="✔  YA", width=12,
            bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
            command=lambda: self.jawab('y')
        )
        self.btn_tidak = tk.Button(
            self.frame_jawaban, text="✘  TIDAK", width=12,
            bg="#f44336", fg="white", font=("Arial", 10, "bold"),
            command=lambda: self.jawab('t')
        )
        self.btn_ya.pack(side=tk.LEFT, padx=15)
        self.btn_tidak.pack(side=tk.LEFT, padx=15)

        # TOMBOL MULAI
        self.btn_mulai = tk.Button(
            root, text="Mulai Diagnosa",
            bg="#2196F3", fg="white", font=("Arial", 10, "bold"),
            width=18, command=self.mulai_tanya
        )
        self.btn_mulai.pack(pady=10)

    # ------------------------------------------------------------------
    def mulai_tanya(self):
        # Reset working memory (seperti clear_db di Prolog)
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        self.btn_mulai.pack_forget()       # Sembunyikan tombol mulai
        self.frame_jawaban.pack(pady=10)   # Tampilkan tombol YA/TIDAK
        self.tampilkan_pertanyaan()

    # ------------------------------------------------------------------
    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            total = len(semua_gejala)
            no   = self.index_pertanyaan + 1

            # Update label nomor dan teks pertanyaan
            self.label_nomor.config(text=f"Pertanyaan {no} dari {total}")
            self.label_tanya.config(text=teks)
            self.label_progress.config(
                text=f"Progress: {'█' * no}{'░' * (total - no)}  ({no}/{total})"
            )
        else:
            # Semua pertanyaan sudah dijawab, proses hasil
            self.proses_hasil()

    # ------------------------------------------------------------------
    def jawab(self, respon):
        # Jika jawaban 'y', masukkan gejala ke working memory (seperti assertz di Prolog)
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)

        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    # ------------------------------------------------------------------
    def proses_hasil(self):
        # MESIN INFERENSI: cocokkan gejala_terpilih dengan knowledge_base
        hasil = []
        for kerusakan, data in knowledge_base.items():
            syarat = data["gejala"]
            # Penyakit terdeteksi jika SEMUA gejala syarat ada di gejala_terpilih
            if all(s in self.gejala_terpilih for s in syarat):
                hasil.append((kerusakan, data["solusi"]))

        # Susun pesan output
        if hasil:
            pesan = "Terdeteksi kemungkinan kerusakan:\n\n"
            for i, (kerusakan, solusi) in enumerate(hasil, 1):
                pesan += f"{i}. {kerusakan}\n"
                pesan += f"   Solusi: {solusi}\n\n"
        else:
            pesan = (
                "Tidak terdeteksi kerusakan spesifik.\n\n"
                "Kemungkinan masalah bersifat sementara atau\n"
                "kombinasi gejala tidak cocok dengan database.\n\n"
                "Disarankan membawa ke teknisi untuk pengecekan lebih lanjut."
            )

        messagebox.showinfo("Hasil Diagnosa", pesan)

        # Reset tampilan ke awal
        self.frame_jawaban.pack_forget()
        self.label_nomor.config(text="")
        self.label_progress.config(text="")
        self.label_tanya.config(text="Diagnosa selesai. Klik 'Mulai Diagnosa' untuk mengulang.")
        self.btn_mulai.pack(pady=10)

# MENJALANKAN APLIKASI
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPakarKomputer(root)
    root.mainloop()