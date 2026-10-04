import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# 1. DEFINISI FUNGSI KEANGGOTAAN LINGUISTIK (SESUAI GRAFIK)
#    VARIABEL: USIA | DOMAIN: 0 - 150 TAHUN
# ==========================================================

# ----------------------------------------------------------
# 1) BAYI / ANAK USIA DINI
# a = 0, b = 0, c = 2, d = 5
# ----------------------------------------------------------
def mf_bayi(x):
    kondisi = [
        x <= 2,
        (x > 2) & (x < 5),
        x >= 5
    ]
    pilihan = [
        1.0,
        (5.0 - x) / (5.0 - 2.0),
        0.0
    ]
    return np.select(kondisi, pilihan)

# ----------------------------------------------------------
# 2) ANAK-ANAK
# a = 3, b = 5, c = 7, d = 12
# ----------------------------------------------------------
def mf_anak(x):
    kondisi = [
        x <= 3,
        (x > 3) & (x < 5),
        (x >= 5) & (x <= 7),
        (x > 7) & (x < 12),
        x >= 12
    ]
    pilihan = [
        0.0,
        (x - 3.0) / (5.0 - 3.0),
        1.0,
        (12.0 - x) / (12.0 - 7.0),
        0.0
    ]
    return np.select(kondisi, pilihan)

# ----------------------------------------------------------
# 3) REMAJA (ADOLESCENT)
# a = 10, b = 12, c = 15, d = 17
# ----------------------------------------------------------
def mf_remaja(x):
    kondisi = [
        x <= 10,
        (x > 10) & (x < 12),
        (x >= 12) & (x <= 15),
        (x > 15) & (x < 17),
        x >= 17
    ]
    pilihan = [
        0.0,
        (x - 10.0) / (12.0 - 10.0),
        1.0,
        (17.0 - x) / (17.0 - 15.0),
        0.0
    ]
    return np.select(kondisi, pilihan)

# ----------------------------------------------------------
# 4) PEMUDA (YOUTH)
# a = 15, b = 18, c = 20, d = 24
# ----------------------------------------------------------
def mf_pemuda(x):
    kondisi = [
        x <= 15,
        (x > 15) & (x < 18),
        (x >= 18) & (x <= 20),
        (x > 20) & (x < 24),
        x >= 24
    ]
    pilihan = [
        0.0,
        (x - 15.0) / (18.0 - 15.0),
        1.0,
        (24.0 - x) / (24.0 - 20.0),
        0.0
    ]
    return np.select(kondisi, pilihan)

# ----------------------------------------------------------
# 5) DEWASA (ADULT)
# a = 20, b = 30, c = 55, d = 65
# ----------------------------------------------------------
def mf_dewasa(x):
    kondisi = [
        x <= 20,
        (x > 20) & (x < 30),
        (x >= 30) & (x <= 55),
        (x > 55) & (x < 65),
        x >= 65
    ]
    pilihan = [
        0.0,
        (x - 20.0) / (30.0 - 20.0),
        1.0,
        (65.0 - x) / (65.0 - 55.0),
        0.0
    ]
    return np.select(kondisi, pilihan)

# ----------------------------------------------------------
# 6) LANJUT USIA (ELDERLY/LANSIA)
# a = 60, b = 80, c = 150, d = 150
# ----------------------------------------------------------
def mf_lansia(x):
    kondisi = [
        x <= 60,
        (x > 60) & (x < 80),
        (x >= 80) & (x <= 150)
    ]
    pilihan = [
        0.0,
        (x - 60.0) / (80.0 - 60.0),
        1.0
    ]
    return np.select(kondisi, pilihan)

# ==========================================================
# 2. STRUKTUR VARIABEL LINGUISTIK
# ==========================================================

variabel_usia = {
    "nama": "Usia",
    "satuan": "tahun",
    "semesta": (0.0, 150.0),
    "label": {
        "Bayi / Anak Usia Dini": mf_bayi,
        "Anak-anak": mf_anak,
        "Remaja": mf_remaja,
        "Pemuda": mf_pemuda,
        "Dewasa": mf_dewasa,
        "Lansia": mf_lansia
    }
}

# ==========================================================
# 3. FUNGSI FUZZIFIKASI
# ==========================================================

def fuzzifikasi(nilai_crisp, variabel):
    hasil = {}
    u_min, u_max = variabel["semesta"]

    if not (u_min <= nilai_crisp <= u_max):
        raise ValueError(f"Input {nilai_crisp} di luar domain [{u_min}, {u_max}]")

    for nama_label, fungsi_mf in variabel["label"].items():
        derajat = float(fungsi_mf(np.array([nilai_crisp]))[0])
        hasil[nama_label] = round(derajat, 4)

    return hasil

# ==========================================================
# 4. MEMBUAT DOMAIN USIA & VISUALISASI GRAFIK
# ==========================================================

x_semesta = np.linspace(0.0, 150.0, 1000)

y_bayi = mf_bayi(x_semesta)
y_anak = mf_anak(x_semesta)
y_remaja = mf_remaja(x_semesta)
y_pemuda = mf_pemuda(x_semesta)
y_dewasa = mf_dewasa(x_semesta)
y_lansia = mf_lansia(x_semesta)

plt.figure(figsize=(14, 7))

plt.plot(x_semesta, y_bayi, label="Bayi / Anak Usia Dini", linewidth=2.5)
plt.plot(x_semesta, y_anak, label="Anak-anak", linewidth=2.5)
plt.plot(x_semesta, y_remaja, label="Remaja", linewidth=2.5)
plt.plot(x_semesta, y_pemuda, label="Pemuda", linewidth=2.5)
plt.plot(x_semesta, y_dewasa, label="Dewasa", linewidth=2.5)
plt.plot(x_semesta, y_lansia, label="Lansia", linewidth=2.5)

# ==========================================================
# 5. CONTOH INPUT CRISP (MISALKAN INPUT x = 18 TAHUN)
# ==========================================================

x_uji = 18
derajat_uji = fuzzifikasi(x_uji, variabel_usia)

plt.axvline(x=x_uji, linestyle="--", linewidth=1.8, label=f"Input x = {x_uji} tahun")

for label, derajat in derajat_uji.items():
    if derajat > 0:
        plt.scatter(x_uji, derajat, s=70, zorder=5)

# ==========================================================
# 6. PENGATURAN GRAFIK
# ==========================================================

plt.title("FUNGSI KEANGGOTAAN TRAPESIUM - VARIABEL USIA", fontsize=14, fontweight="bold")
plt.xlabel("Usia (tahun)", fontsize=11)
plt.ylabel("Derajat Keanggotaan μ(x)", fontsize=11)

plt.xlim(0, 150)
plt.ylim(-0.05, 1.1)

plt.xticks(np.arange(0, 151, 10))
plt.yticks(np.arange(0, 1.1, 0.1))

plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
plt.tight_layout()

plt.savefig("fungsi_keanggotaan_usia.png", dpi=300, bbox_inches="tight")
plt.show()

# ==========================================================
# 7. HASIL FUZZIFIKASI
# ==========================================================

print("=" * 60)
print(f"HASIL FUZZIFIKASI USIA = {x_uji} {variabel_usia['satuan']}")
print("=" * 60)

for label, derajat in derajat_uji.items():
    print(f"{label:<25} : μ = {derajat}")

