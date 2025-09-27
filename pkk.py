import pandas as pd
from datetime import datetime, timedelta

#inputan jadwal fix 

fixed_schedule = []
n_fixed = int(input("Berapa banyak jadwal fixed kamu? (kuliah/organisasi/kegiatan rutin)? "))
for i in range(n_fixed):
    print(f"\n Masukkan deskripsi jadwal fixed ke-{i+1}:")
    start = input("  Jam mulai (HH:MM) : ")
    end = input("  Jam selesai (HH:MM): ")
    activity = input("  Nama aktivitas     : ")
    fixed_schedule.append({"start": start, "end": end, "activity": activity})

#inputan jadwal tugas/keseharian

tasks = []
n_tasks = int(input("\n Berapa banyak tugas/keseharian kamu? "))
for i in range(n_tasks):
    print(f"\n Masukkan deskripsi task ke-{i+1}:")
    task = input("  Nama task           : ")
    deadline = input("  Deadline (YYYY-MM-DD) [kosong/tekan enter jika tidak ada]: ")
    urgent = int(input("  Urgent (1=ya, 0=tidak): "))
    important = int(input("  Important (1=ya, 0=tidak): "))
    duration = int(input("  Durasi (jam)        : "))

    # jika tidak ada deadline
    if deadline.strip() == "":
        deadline = "9999-12-31"  

    tasks.append({
        "task": task,
        "deadline": deadline,
        "urgent": urgent,
        "important": important,
        "duration": duration
    })

# Menghitung Skor Prioritas
today = datetime.today().date()
for t in tasks:
    deadline = datetime.strptime(t["deadline"], "%Y-%m-%d").date()
    days_left = (deadline - today).days + 1
    if deadline.year == 9999: 
        deadline_score = 0
    else:
        deadline_score = 1 / days_left

    t["score"] = (t["urgent"] * 2) + (t["important"] * 2) + deadline_score

# Urutkan task berdasarkan skor
sorted_tasks = sorted(tasks, key=lambda x: x["score"], reverse=True)

#Print task berdasarkan skor 

print("\n=== Daftar Task Berdasarkan Prioritas ===")
df_tasks = pd.DataFrame(sorted_tasks)
print(df_tasks[["task", "deadline", "urgent", "important", "score"]])

# Masukkan Slot waktu kosong ke jadwal
def time_range(start, end, delta=60):
    """Buat list slot per jam"""
    start_dt = datetime.strptime(start, "%H:%M")
    end_dt = datetime.strptime(end, "%H:%M")
    while start_dt < end_dt:
        yield start_dt
        start_dt += timedelta(minutes=delta)

slots = list(time_range("07:00", "22:00", 60))

# Menandai semua slot sebagai kosong
schedule = {slot.strftime("%H:%M"): None for slot in slots}

# menandai slot fixed
for f in fixed_schedule:
    start = datetime.strptime(f["start"], "%H:%M")
    end = datetime.strptime(f["end"], "%H:%M")
    for slot in slots:
        if start <= slot < end:
            schedule[slot.strftime("%H:%M")] = f["activity"]

# Mengisi slot kosong dengan task prioritas

for task in sorted_tasks:
    dur = task["duration"]
    count = 0
    for slot in slots:
        time_str = slot.strftime("%H:%M")
        if schedule[time_str] is None:  
            schedule[time_str] = task["task"]
            count += 1
            if count == dur:
                break

# Output Hasil 

df = pd.DataFrame(list(schedule.items()), columns=["Time", "Activity"])
print("\n===== Jadwal Harian Anda =====")
print(df)

save_choice = input("\nApakah Anda ingin menyimpan jadwal ke Excel? (yes/no): ").strip().lower()
if save_choice == "yes":
    df.to_excel("jadwal_harian.xlsx", index=False)
    print("✅ Jadwal berhasil disimpan ke 'jadwal_harian.xlsx'")
elif save_choice == "no":
    print("❌ Jadwal tidak disimpan. Semoga membantu mengatur waktu Anda!")
else:
    print("Masukkan input dengan benar")

    
