# 📌 Deskripsi

Proyek ini merupakan **sistem penjadwalan otomatis** yang dirancang untuk membantu manajemen waktu mahasiswa. Sistem ini mengatur jadwal harian berdasarkan:

- Jadwal tetap (kuliah/kegiatan rutin)
- Tugas/aktivitas lainnya

---

## ⚡ Algoritma yang Digunakan

### 1. Eisenhower Matrix
Mengelompokkan tugas berdasarkan kategori:

- **Urgent & Important**: Harus segera dikerjakan
- **Not Urgent & Important**: Dijadwalkan
- **Urgent & Not Important**: Delegasikan jika bisa
- **Not Urgent & Not Important**: Bisa diabaikan

### 2. Weighted Priority Scheduling
Memberikan skor prioritas pada setiap tugas dengan rumus:

Skor = (Urgent × 2) + (Important × 2) + (1 / days_left)


- `Urgent` = 1 jika mendesak, 0 jika tidak  
- `Important` = 1 jika penting, 0 jika tidak  
- `days_left` = sisa hari menuju deadline  

Jika sebuah tugas **tidak memiliki deadline**, maka `days_left` dianggap sangat besar → nilainya mendekati nol, sehingga **skornya rendah**.

---

## ⚙️ Input

1. Jadwal tetap  
   Contoh: jam kuliah, makan, olahraga, kegiatan rutin  
2. Daftar tugas  
   Nama tugas, durasi pengerjaan, deadline (opsional), nilai urgent, nilai important  
3. Kegiatan bebas (opsional)  
   Misalnya: main game, menonton film, tanpa deadline  
4. Pilihan user  
   Apakah hasil jadwal ingin disimpan ke file Excel atau hanya ditampilkan

---

## 🔄 Proses

1. Hitung skor prioritas berdasarkan urgent, important, dan kedekatan deadline  
2. Urutkan tugas dari skor tertinggi ke terendah  
3. Tandai slot waktu tetap (fixed schedule) sebagai `occupied`  
4. Masukkan tugas ke slot kosong sesuai urutan prioritas dan durasi  
5. Simpan hasil (opsional) ke file Excel jika user memilih

---

## 📤 Output

- Daftar tugas berdasarkan skor prioritas  
- Jadwal harian otomatis (07.00 – 22.00) berisi fixed schedule dan tugas prioritas  
- File Excel (`to_do_list.xlsx`) jika user memilih menyimpan
