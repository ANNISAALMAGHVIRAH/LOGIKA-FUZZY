
import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# 1. FUNGSI KEANGGOTAAN
# ==========================================================

def trapmf(x, a, b, c, d):
    if x < a or x > d:
        return 0.0
    elif b <= x <= c:
        return 1.0
    elif a <= x < b:
        return (x - a) / (b - a) if b != a else 1.0
    else:
        return (d - x) / (d - c) if d != c else 1.0


def trimf(x, a, b, c):
    if x < a or x > c:
        return 0.0
    elif x == b:
        return 1.0
    elif x < b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)


# ==========================================================
# 2. IMPLEMENTASI SUGENO ORDE 0
# ==========================================================

def hitung_sugeno(alphas, z_values):
    total_alpha = np.sum(alphas)

    if total_alpha == 0:
        return None

    return np.sum(np.array(alphas) * np.array(z_values)) / total_alpha


# ==========================================================
# 3. IMPLEMENTASI TSUKAMOTO
# ==========================================================

def invers_monoton_naik(alpha, a, b):
    return a + alpha * (b - a)


def invers_monoton_turun(alpha, a, b):
    return b - alpha * (b - a)


def hitung_tsukamoto(alphas, z_values):
    total_alpha = np.sum(alphas)

    if total_alpha == 0:
        return None

    return np.sum(np.array(alphas) * np.array(z_values)) / total_alpha


# ==========================================================
# 4. FUNGSI MENGHITUNG ALPHA 4 ATURAN
# ==========================================================

def hitung_alpha(lokasi, tanah, bangunan):

    # R01: Sangat Strategis, Kecil, Sempit
    alpha_R01 = min(
        trapmf(lokasi, 0, 0, 10, 20),
        trapmf(tanah, 36, 36, 60, 100),
        trapmf(bangunan, 21, 21, 36, 60)
    )

    # R05: Sangat Strategis, Sedang, Sedang
    alpha_R05 = min(
        trapmf(lokasi, 0, 0, 10, 20),
        trimf(tanah, 72, 120, 168),
        trimf(bangunan, 45, 80, 115)
    )

    # R14: Strategis, Sedang, Sedang
    alpha_R14 = min(
        trimf(lokasi, 10, 25, 40),
        trimf(tanah, 72, 120, 168),
        trimf(bangunan, 45, 80, 115)
    )

    # R27: Tidak Strategis, Luas, Luas
    alpha_R27 = min(
        trapmf(lokasi, 30, 40, 50, 50),
        trapmf(tanah, 140, 170, 200, 200),
        trapmf(bangunan, 90, 115, 150, 150)
    )

    return [
        alpha_R01,
        alpha_R05,
        alpha_R14,
        alpha_R27
    ]


# ==========================================================
# 5. KONSEKUEN SUGENO ORDE 0
# ==========================================================

# Nilai output:
# R01 = Murah (7)
# R05 = Mahal (15)
# R14 = Normal (11)
# R27 = Mahal (15)

z_sugeno = [7, 15, 11, 15]


# ==========================================================
# 6. KONSEKUEN TSUKAMOTO
# ==========================================================

def hitung_z_tsukamoto(alphas):

    alpha_R01, alpha_R05, alpha_R14, alpha_R27 = alphas

    # R01 = Murah, monoton turun [3, 11]
    z_R01 = invers_monoton_turun(alpha_R01, 3, 11)

    # R05 = Mahal, monoton naik [11, 19]
    z_R05 = invers_monoton_naik(alpha_R05, 11, 19)

    # R14 = Normal, monoton naik [7, 11]
    z_R14 = invers_monoton_naik(alpha_R14, 7, 11)

    # R27 = Mahal, monoton naik [11, 19]
    z_R27 = invers_monoton_naik(alpha_R27, 11, 19)

    return [z_R01, z_R05, z_R14, z_R27]


# ==========================================================
# 7. PENGUJIAN 5 VARIASI INPUT
# ==========================================================

data_pengujian = [
    (5, 50, 30),
    (15, 120, 80),
    (25, 150, 100),
    (35, 180, 130),
    (45, 190, 140)
]

hasil_pengujian = []

for nomor, (lokasi, tanah, bangunan) in enumerate(
    data_pengujian, start=1
):

    alphas = hitung_alpha(lokasi, tanah, bangunan)

    # Sugeno Orde 0
    hasil_sugeno = hitung_sugeno(alphas, z_sugeno)

    # Tsukamoto
    z_tsukamoto = hitung_z_tsukamoto(alphas)
    hasil_tsukamoto = hitung_tsukamoto(
        alphas, z_tsukamoto
    )

    if hasil_sugeno is not None and hasil_tsukamoto is not None:
        selisih = abs(hasil_sugeno - hasil_tsukamoto)
        harga_sugeno = hasil_sugeno * 100_000_000
        harga_tsukamoto = hasil_tsukamoto * 100_000_000
    else:
        selisih = None
        harga_sugeno = None
        harga_tsukamoto = None

    hasil_pengujian.append({
        "No": nomor,
        "Lokasi": lokasi,
        "Tanah": tanah,
        "Bangunan": bangunan,
        "Alpha": alphas,
        "Sugeno": hasil_sugeno,
        "Tsukamoto": hasil_tsukamoto,
        "Selisih": selisih,
        "Harga Sugeno": harga_sugeno,
        "Harga Tsukamoto": harga_tsukamoto
    })


# ==========================================================
# 8. TABEL PERBANDINGAN HASIL
# ==========================================================

print("\n" + "=" * 105)
print("TABEL PERBANDINGAN SUGENO DAN TSUKAMOTO")
print("SISTEM PENENTUAN HARGA RUMAH")
print("=" * 105)

print(
    f"{'No':<5}"
    f"{'Lokasi':<10}"
    f"{'Tanah':<10}"
    f"{'Bangunan':<12}"
    f"{'Sugeno':<13}"
    f"{'Tsukamoto':<13}"
    f"{'Selisih':<12}"
)

print("-" * 105)

for data in hasil_pengujian:
    if data["Sugeno"] is not None:
        print(
            f"{data['No']:<5}"
            f"{data['Lokasi']:<10}"
            f"{data['Tanah']:<10}"
            f"{data['Bangunan']:<12}"
            f"{data['Sugeno']:<13.3f}"
            f"{data['Tsukamoto']:<13.3f}"
            f"{data['Selisih']:<12.3f}"
        )
    else:
        print(
            f"{data['No']:<5}"
            f"{data['Lokasi']:<10}"
            f"{data['Tanah']:<10}"
            f"{data['Bangunan']:<12}"
            "Tidak ada aturan aktif"
        )

print("=" * 105)
print("Keterangan: 1 skala output = Rp100.000.000")


# ==========================================================
# 9. GRAFIK PERBANDINGAN SUGENO DAN TSUKAMOTO
# ==========================================================

label = [
    f"S{i}" for i in range(1, len(hasil_pengujian) + 1)
]

nilai_sugeno = [
    data["Sugeno"] if data["Sugeno"] is not None else 0
    for data in hasil_pengujian
]

nilai_tsukamoto = [
    data["Tsukamoto"] if data["Tsukamoto"] is not None else 0
    for data in hasil_pengujian
]

x = np.arange(len(label))
lebar = 0.35

plt.figure(figsize=(10, 6))

plt.bar(
    x - lebar / 2,
    nilai_sugeno,
    lebar,
    label="Sugeno Orde 0"
)

plt.bar(
    x + lebar / 2,
    nilai_tsukamoto,
    lebar,
    label="Tsukamoto"
)

plt.xlabel("Skenario Pengujian")
plt.ylabel("Nilai Output Harga Rumah (Skala 1–23)")
plt.title("Perbandingan Hasil Metode Sugeno dan Tsukamoto")

plt.xticks(x, label)
plt.ylim(0, 23)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend()

plt.tight_layout()
plt.savefig("grafik_perbandingan_harga_rumah.png", dpi=200)
plt.show()
