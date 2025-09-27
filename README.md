# time_management
📌 Deskripsi

Proyek ini merupakan sistem penjadwalan otomatis yang dirancang untuk membantu manajemen waktu mahasiswa. Sistem ini mengatur jadwal harian berdasarkan jadwal tetap (kuliah/kegiatan rutin), tugas dengan deadline, serta kegiatan tanpa deadline (misalnya hiburan).

Algoritma utama yang digunakan adalah:

Eisenhower Matrix → untuk mengelompokkan tugas berdasarkan kategori urgent/not urgent dan important/not important.

Weighted Priority Scheduling → untuk memberikan skor prioritas pada setiap tugas dengan rumus:

Skor = (Urgent × 2) + (Important × 2) + (1 / days_left)


Jika sebuah tugas tidak memiliki deadline, maka days_left dianggap sangat besar sehingga skornya rendah.

⚙️ Input

Jadwal tetap (misalnya jam kuliah atau kegiatan rutin).

Daftar tugas (nama tugas, durasi, deadline, nilai urgent, nilai important).

Kegiatan bebas (opsional, tanpa deadline).

Pilihan user apakah ingin menyimpan hasil ke file Excel.

🔄 Proses

Hitung skor prioritas untuk setiap tugas.

Urutkan tugas berdasarkan skor.

Tandai slot waktu yang sudah diisi oleh jadwal tetap.

Masukkan tugas ke slot kosong sesuai urutan prioritas.

Jika user ingin menyimpan, hasil akan diekspor ke Excel (.xlsx).

📤 Output

Daftar tugas berdasarkan prioritas.

Jadwal harian yang sudah disusun dari pukul 07.00–22.00.

File to_do_list.xlsx (jika user memilih menyimpan).

🚀 Tujuan

Proyek ini dibuat sebagai latihan pemrograman Python untuk mengimplementasikan konsep algoritma penjadwalan sekaligus membantu meningkatkan keterampilan manajemen waktu.
