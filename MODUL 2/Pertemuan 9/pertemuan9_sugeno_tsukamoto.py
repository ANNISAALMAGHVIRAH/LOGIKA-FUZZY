
import numpy as np

# ==========================================================
# 1. IMPLEMENTASI SISTEM SUGENO (ORDE 0 DAN ORDE 1)
# ==========================================================

def hitung_sugeno(alphas, z_values):
    """
    alphas: list firing strength [alpha_1, alpha_2, ...]
    z_values: list output tegas aturan [z_1, z_2, ...]
    """
    alphas = np.array(alphas)
    z_values = np.array(z_values)

    total_alpha = np.sum(alphas)
    if total_alpha == 0:
        return 0.0

    return np.sum(alphas * z_values) / total_alpha


# ==========================================================
# 2. IMPLEMENTASI SISTEM TSUKAMOTO
# ==========================================================

def invers_monoton_naik(alpha, a, b):
    """z = a + alpha * (b - a)"""
    return a + alpha * (b - a)


def invers_monoton_turun(alpha, a, b):
    """z = b - alpha * (b - a)"""
    return b - alpha * (b - a)


def hitung_tsukamoto(alphas, fungsi_invers_list):
    """
    fungsi_invers_list: list lambda fungsi invers untuk setiap aturan
    """
    z_values = [
        func(alpha)
        for alpha, func in zip(alphas, fungsi_invers_list)
    ]

    return hitung_sugeno(alphas, z_values), z_values


# ==========================================================
# 3. PENGUJIAN DAN KOMPARASI KASUS HARGA RUMAH
# ==========================================================

# Input crisp berdasarkan contoh perhitungan manual
lokasi = 15
luas_tanah = 120
luas_bangunan = 80

# Nilai alpha berdasarkan hasil fuzzifikasi
# R05 = Sangat Strategis AND Sedang AND Sedang
# R14 = Strategis AND Sedang AND Sedang

alphas_kasus = [0.5, 0.333]

# A. SUGENO ORDE 0
# R05: Harga Mahal = 15
# R14: Harga Normal = 11

z_sugeno0 = [15.0, 11.0]

hasil_sugeno0 = hitung_sugeno(
    alphas_kasus,
    z_sugeno0
)

# B. SUGENO ORDE 1
# Konsekuen berupa persamaan linear.
# Koefisien berikut merupakan contoh rancangan.

# R05
z1 = (
    0.05 * lokasi +
    0.03 * luas_tanah +
    0.04 * luas_bangunan +
    5
)

# R14
z2 = (
    0.04 * lokasi +
    0.02 * luas_tanah +
    0.03 * luas_bangunan +
    4
)

z_sugeno1 = [z1, z2]

hasil_sugeno1 = hitung_sugeno(
    alphas_kasus,
    z_sugeno1
)

# C. TSUKAMOTO
# Menggunakan fungsi monoton naik dengan rentang 1-23

fungsi_tsukamoto = [
    lambda a: invers_monoton_naik(a, 1.0, 23.0),
    lambda a: invers_monoton_naik(a, 1.0, 23.0)
]

hasil_tsukamoto, z_tsuka_values = hitung_tsukamoto(
    alphas_kasus,
    fungsi_tsukamoto
)

# ==========================================================
# 4. CETAK HASIL
# ==========================================================

print("=" * 65)
print("HASIL KOMPARASI METODE SUGENO DAN TSUKAMOTO")
print("SISTEM PENENTUAN HARGA RUMAH")
print("=" * 65)

print("\nINPUT CRISP")
print(f"Lokasi          : {lokasi}")
print(f"Luas Tanah      : {luas_tanah} m2")
print(f"Luas Bangunan   : {luas_bangunan} m2")

print("\nFIRING STRENGTH")
print(f"Alpha R05       : {alphas_kasus[0]:.3f}")
print(f"Alpha R14       : {alphas_kasus[1]:.3f}")

print("\nA. SUGENO ORDE 0")
print(f"z1 (R05)        : {z_sugeno0[0]:.3f}")
print(f"z2 (R14)        : {z_sugeno0[1]:.3f}")
print(f"Hasil           : {hasil_sugeno0:.3f}")

print("\nB. SUGENO ORDE 1")
print(f"z1 (R05)        : {z_sugeno1[0]:.3f}")
print(f"z2 (R14)        : {z_sugeno1[1]:.3f}")
print(f"Hasil           : {hasil_sugeno1:.3f}")

print("\nC. TSUKAMOTO")
print(f"z1 (R05)        : {z_tsuka_values[0]:.3f}")
print(f"z2 (R14)        : {z_tsuka_values[1]:.3f}")
print(f"Hasil           : {hasil_tsukamoto:.3f}")

print("=" * 65)
print("Output menggunakan skala harga rumah 1-23.")
print("=" * 65)
