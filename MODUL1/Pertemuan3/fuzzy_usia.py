import mysql.connector

# ==========================================================
# 1. KONEKSI DATABASE
# ==========================================================
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="fuzzy_modul1"
    )
    print("Koneksi database berhasil!\n")
except mysql.connector.Error as err:
    print(f"Gagal koneksi ke database: {err}")
    exit()

# ==========================================================
# 2. FUNGSI KEANGGOTAAN
# ==========================================================
# --- Anak ---
def fungsi_anak_turun(x):
    return (11 - x) / 2

# --- Remaja ---
def fungsi_remaja_naik(x):
    return (x - 10) / 2

def fungsi_remaja_turun(x):
    return (19 - x) / 2

# --- Dewasa ---
def fungsi_dewasa_naik(x):
    return (x - 18) / 7  # Mengikuti interval 18 - 25 pada gambar (25 - 18 = 7)

def fungsi_dewasa_turun(x):
    return (65 - x) / 5

# --- Bayi ---
def trapesium_down_bayi(x):
    return (5 - x) / 2

# --- Pemuda ---
def trapesium_up_pemuda(x):
    return (x - 15) / 2

def trapesium_down_pemuda(x):
    return (24 - x) / 2

# --- Lansia ---
def trapesium_up_lansia(x):
    return (x - 60) / 5

# ==========================================================
# 3. DICTIONARY FUNGSI
# ==========================================================
fungsi = {
    "fungsi_anak_turun": fungsi_anak_turun,
    "fungsi_remaja_naik": fungsi_remaja_naik,
    "fungsi_remaja_turun": fungsi_remaja_turun,
    "fungsi_dewasa_naik": fungsi_dewasa_naik,
    "fungsi_dewasa_turun": fungsi_dewasa_turun,
    "trapesium_down_bayi": trapesium_down_bayi,
    "trapesium_up_pemuda": trapesium_up_pemuda,
    "trapesium_down_pemuda": trapesium_down_pemuda,
    "trapesium_up_lansia": trapesium_up_lansia,
}

# Mapping tabel untuk setiap kategori variabel
tabel_variabel = {
    "Anak": "tb_domain_usia_anak",
    "Remaja": "tb_domain_usia_remaja",
    "Dewasa": "tb_domain_usia_dewasa",
    "Bayi": "tb_domain_usia_bayi",
    "Pemuda": "tb_domain_usia_pemuda",
    "Lansia": "tb_domain_usia_lansia"
}

# ==========================================================
# 4. FUNGSI HITUNG FUZZIFIKASI UNTUK VARIABEL TERTENTU
# ==========================================================
def hitung_mu_variabel(nama_tabel, x):
    cursor = db.cursor()
    query = f"""
        SELECT b_bawah, b_atas, fungsi
        FROM {nama_tabel}
        WHERE %s >= b_bawah AND %s <= b_atas
        ORDER BY b_bawah ASC
        LIMIT 1
    """
    cursor.execute(query, (x, x))
    data = cursor.fetchone()
    cursor.close()

    if data is None:
        return 0.0, "konstanta 0", "0 - 0"

    b_bawah, b_atas, nama_fungsi = data
    interval_str = f"{int(b_bawah)} - {int(b_atas)}"

    if nama_fungsi == "0":
        return 0.0, "konstanta 0", interval_str
    elif nama_fungsi == "1":
        return 1.0, "konstanta 1", interval_str

    if nama_fungsi in fungsi:
        fungsi_y = fungsi[nama_fungsi]
        nilai = fungsi_y(x)
        return nilai, nama_fungsi, interval_str

    return 0.0, nama_fungsi, interval_str

# ==========================================================
# 5. MENAMPILKAN TABEL REKAPITULASI (SESUAI GAMBAR)
# ==========================================================
# Data sampel pengujian seperti pada gambar
sampel_uji = [
    (1, "Anak", 4),
    (2, "Anak", 9),
    (3, "Anak", 13),
    (4, "Remaja", 8),
    (5, "Remaja", 12),
    (6, "Remaja", 17),
    (7, "Dewasa", 10),
    (8, "Dewasa", 19),
    (9, "Dewasa", 22),
    (10, "Dewasa", 30),
]

# Cetak Header Tabel
print("| No | Variabel | Input Usia | Interval Database | Fungsi               | mu(x)  |")
print("|--:|:---------|-----------:|:------------------|:---------------------|-------:|")

# Cetak Baris Tabel
for no, var, age_in in sampel_uji:
    tabel_nm = tabel_variabel[var]
    mu_val, f_name, interval = hitung_mu_variabel(tabel_nm, age_in)
    print(f"| {no:>2} | {var:<8} | {age_in:>10} | {interval:<17} | {f_name:<20} | {mu_val:>6.4f} |")

print("\n")

# ==========================================================
# 6. INPUT INTERAKTIF & HASIL FUZZIFIKASI (SESUAI GAMBAR)
# ==========================================================
input_str = input("Masukkan usia untuk fuzzifikasi (Enter untuk lewati): ")

if input_str.strip():
    usia_val = float(input_str)
    
    print("=================================")
    print("HASIL FUZZIFIKASI")
    print("=================================")
    print(f"Usia : {usia_val}")
    
    # Hitung mu untuk masing-masing kategori utama
    mu_anak, _, _ = hitung_mu_variabel(tabel_variabel["Anak"], usia_val)
    mu_remaja, _, _ = hitung_mu_variabel(tabel_variabel["Remaja"], usia_val)
    mu_dewasa, _, _ = hitung_mu_variabel(tabel_variabel["Dewasa"], usia_val)

    print(f"  mu Anak   : {round(mu_anak, 4)}")
    print(f"  mu Remaja : {round(mu_remaja, 4)}")
    print(f"  mu Dewasa : {round(mu_dewasa, 4)}")
    print("=================================")

db.close()

