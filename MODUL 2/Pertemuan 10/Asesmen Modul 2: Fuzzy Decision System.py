
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. FUNGSI KEANGGOTAAN FUZZY
# ==========================================

def trapezoid(x, a, b, c, d):
    x = np.asarray(x, dtype=float)

    rising = (
        np.ones_like(x)
        if a == b
        else np.clip((x - a) / (b - a), 0, 1)
    )

    falling = (
        np.ones_like(x)
        if c == d
        else np.clip((d - x) / (d - c), 0, 1)
    )

    return np.minimum(rising, falling)


def triangle(x, a, b, c):
    x = np.asarray(x, dtype=float)

    rising = np.clip((x - a) / (b - a), 0, 1)
    falling = np.clip((c - x) / (c - b), 0, 1)

    return np.minimum(rising, falling)


# ==========================================
# 2. DOMAIN VARIABEL OUTPUT HARGA RUMAH
# ==========================================

domain_harga = np.linspace(1, 23, 221)


# ==========================================
# 3. FUNGSI FUZZIFIKASI VARIABEL INPUT
# ==========================================

def fuzzifikasi_lokasi(nilai):
    return {
        "Sangat Strategis": float(
            trapezoid(nilai, 0, 0, 10, 20)
        ),
        "Strategis": float(
            triangle(nilai, 10, 25, 40)
        ),
        "Tidak Strategis": float(
            trapezoid(nilai, 30, 40, 50, 50)
        )
    }


def fuzzifikasi_tanah(nilai):
    return {
        "Kecil": float(
            trapezoid(nilai, 36, 36, 60, 100)
        ),
        "Sedang": float(
            triangle(nilai, 72, 120, 168)
        ),
        "Luas": float(
            trapezoid(nilai, 140, 170, 200, 200)
        )
    }


def fuzzifikasi_bangunan(nilai):
    return {
        "Sempit": float(
            trapezoid(nilai, 21, 21, 36, 60)
        ),
        "Sedang": float(
            triangle(nilai, 45, 80, 115)
        ),
        "Luas": float(
            trapezoid(nilai, 90, 115, 150, 150)
        )
    }


# ==========================================
# 4. FUNGSI KEANGGOTAAN OUTPUT
# ==========================================

def fungsi_output():
    return {
        "Sangat Murah": trapezoid(
            domain_harga, 1, 1, 3, 7
        ),
        "Murah": triangle(
            domain_harga, 3, 7, 11
        ),
        "Normal": triangle(
            domain_harga, 7, 11, 15
        ),
        "Mahal": triangle(
            domain_harga, 11, 15, 19
        ),
        "Sangat Mahal": trapezoid(
            domain_harga, 15, 19, 23, 23
        )
    }


# ==========================================
# 5. BASIS ATURAN FUZZY (27 RULES)
# ==========================================

aturan = [
    # Lokasi Sangat Strategis
    ("Sangat Strategis", "Kecil", "Sempit", "Murah"),
    ("Sangat Strategis", "Kecil", "Sedang", "Normal"),
    ("Sangat Strategis", "Kecil", "Luas", "Mahal"),
    ("Sangat Strategis", "Sedang", "Sempit", "Normal"),
    ("Sangat Strategis", "Sedang", "Sedang", "Mahal"),
    ("Sangat Strategis", "Sedang", "Luas", "Sangat Mahal"),
    ("Sangat Strategis", "Luas", "Sempit", "Mahal"),
    ("Sangat Strategis", "Luas", "Sedang", "Sangat Mahal"),
    ("Sangat Strategis", "Luas", "Luas", "Sangat Mahal"),

    # Lokasi Strategis
    ("Strategis", "Kecil", "Sempit", "Sangat Murah"),
    ("Strategis", "Kecil", "Sedang", "Murah"),
    ("Strategis", "Kecil", "Luas", "Normal"),
    ("Strategis", "Sedang", "Sempit", "Murah"),
    ("Strategis", "Sedang", "Sedang", "Normal"),
    ("Strategis", "Sedang", "Luas", "Mahal"),
    ("Strategis", "Luas", "Sempit", "Normal"),
    ("Strategis", "Luas", "Sedang", "Mahal"),
    ("Strategis", "Luas", "Luas", "Sangat Mahal"),

    # Lokasi Tidak Strategis
    ("Tidak Strategis", "Kecil", "Sempit", "Sangat Murah"),
    ("Tidak Strategis", "Kecil", "Sedang", "Sangat Murah"),
    ("Tidak Strategis", "Kecil", "Luas", "Murah"),
    ("Tidak Strategis", "Sedang", "Sempit", "Sangat Murah"),
    ("Tidak Strategis", "Sedang", "Sedang", "Murah"),
    ("Tidak Strategis", "Sedang", "Luas", "Normal"),
    ("Tidak Strategis", "Luas", "Sempit", "Murah"),
    ("Tidak Strategis", "Luas", "Sedang", "Normal"),
    ("Tidak Strategis", "Luas", "Luas", "Mahal")
]


# ==========================================
# 6. PROSES INFERENSI FUZZY MAMDANI
# ==========================================

def evaluasi_sistem_fuzzy(lokasi, tanah, bangunan):

    # Validasi nilai input
    if not 0 <= lokasi <= 50:
        raise ValueError("Lokasi harus berada pada rentang 0-50.")

    if not 36 <= tanah <= 200:
        raise ValueError("Luas tanah harus berada pada rentang 36-200.")

    if not 21 <= bangunan <= 150:
        raise ValueError("Luas bangunan harus berada pada rentang 21-150.")

    # Fuzzifikasi setiap variabel
    fuzzy_lokasi = fuzzifikasi_lokasi(lokasi)
    fuzzy_tanah = fuzzifikasi_tanah(tanah)
    fuzzy_bangunan = fuzzifikasi_bangunan(bangunan)

    # Fungsi keanggotaan output
    output_fuzzy = fungsi_output()

    # Menyiapkan agregasi
    agregasi = np.zeros_like(domain_harga)

    # Evaluasi 27 aturan
    for label_lokasi, label_tanah, label_bangunan, hasil in aturan:

        # Operator AND menggunakan MIN
        alpha = min(
            fuzzy_lokasi[label_lokasi],
            fuzzy_tanah[label_tanah],
            fuzzy_bangunan[label_bangunan]
        )

        # Implikasi menggunakan MIN
        hasil_implikasi = np.minimum(
            alpha,
            output_fuzzy[hasil]
        )

        # Agregasi menggunakan MAX
        agregasi = np.maximum(
            agregasi,
            hasil_implikasi
        )

    # Defuzzifikasi menggunakan Centroid
    luas_area = np.sum(agregasi)

    if luas_area == 0:
        raise ValueError(
            "Tidak ada aturan fuzzy yang aktif untuk input tersebut."
        )

    nilai_crisp = np.sum(
        domain_harga * agregasi
    ) / luas_area

    return nilai_crisp, agregasi


# ==========================================
# 7. INPUT DATA RUMAH DARI PENGGUNA
# ==========================================

print("==============================================")
print(" SISTEM PENDUKUNG KEPUTUSAN PENENTUAN HARGA RUMAH")
print("             METODE FUZZY MAMDANI")
print("==============================================")

lokasi = float(input("Masukkan nilai lokasi (0-50): "))
tanah = float(input("Masukkan luas tanah (36-200) m2: "))
bangunan = float(input("Masukkan luas bangunan (21-150) m2: "))


# ==========================================
# 8. MENAMPILKAN HASIL PENENTUAN HARGA RUMAH
# ==========================================

hasil, agregasi = evaluasi_sistem_fuzzy(
    lokasi, tanah, bangunan
)

# Konversi nilai output menjadi rupiah
harga_rumah = hasil * 100_000_000

print("\n========== HASIL PENENTUAN HARGA ==========")
print(f"Nilai Lokasi        : {lokasi}")
print(f"Luas Tanah          : {tanah} m2")
print(f"Luas Bangunan       : {bangunan} m2")
print(f"Nilai Defuzzifikasi : {hasil:.2f}")
print(f"Perkiraan Harga     : Rp{harga_rumah:,.0f}")
print("===========================================")


# ==========================================
# 9. MENAMPILKAN GRAFIK AGREGASI
# ==========================================

plt.figure(figsize=(10, 5))

plt.plot(
    domain_harga,
    agregasi,
    label="Hasil Agregasi Fuzzy",
    linewidth=2
)

plt.title(
    "Grafik Agregasi Fuzzy Penentuan Harga Rumah"
)
plt.xlabel("Domain Harga Rumah")
plt.ylabel("Derajat Keanggotaan")
plt.grid(True)
plt.legend()

plt.savefig(
    "grafik_agregasi_harga_rumah.png",
    dpi=300
)

plt.show()


# ==========================================
# 10. VISUALISASI DECISION SURFACE PLOT 3D
# ==========================================

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Menentukan nilai lokasi tetap
lokasi_tetap = 25

# Membuat rentang nilai luas tanah dan luas bangunan
tanah_range = np.linspace(36, 200, 25)
bangunan_range = np.linspace(21, 150, 25)

# Membuat grid untuk grafik 3D
X, Y = np.meshgrid(tanah_range, bangunan_range)

# Menyiapkan tempat untuk hasil harga rumah
Z = np.zeros_like(X)

# Menghitung harga rumah pada setiap kombinasi input
for i in range(X.shape[0]):
    for j in range(X.shape[1]):

        hasil, _ = evaluasi_sistem_fuzzy(
            lokasi_tetap,
            X[i, j],
            Y[i, j]
        )

        # Konversi hasil ke rupiah
        Z[i, j] = hasil * 100_000_000


# Membuat grafik 3D
fig = plt.figure(figsize=(11, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(
    X,
    Y,
    Z,
    cmap='viridis',
    edgecolor='none',
    alpha=0.9
)

# Memberikan label pada grafik
ax.set_xlabel('Luas Tanah (m2)')
ax.set_ylabel('Luas Bangunan (m2)')
ax.set_zlabel('Perkiraan Harga Rumah (Rp)')

ax.set_title(
    'Decision Surface Plot\n'
    'Sistem Penentuan Harga Rumah - Fuzzy Mamdani\n'
    '(Lokasi = 25)'
)

# Menambahkan skala warna
fig.colorbar(
    surf,
    ax=ax,
    shrink=0.5,
    aspect=5,
    label='Perkiraan Harga Rumah (Rp)'
)

# Mengatur sudut pandang grafik
ax.view_init(elev=30, azim=135)

plt.tight_layout()

# Menyimpan grafik
plt.savefig(
    'decision_surface_harga_rumah.png',
    dpi=300,
    bbox_inches='tight'
)

# Menampilkan grafik
plt.show()


# ==========================================
# 11. PENGUJIAN 5 SKENARIO KASUS RUMAH
# ==========================================

# Data pengujian
skenario = [
    {
        "Nama": "Skenario 1",
        "Kondisi": "Lokasi sangat strategis, ukuran kecil",
        "Lokasi": 5,
        "Tanah": 50,
        "Bangunan": 30
    },
    {
        "Nama": "Skenario 2",
        "Kondisi": "Lokasi tidak strategis, ukuran kecil",
        "Lokasi": 45,
        "Tanah": 50,
        "Bangunan": 30
    },
    {
        "Nama": "Skenario 3",
        "Kondisi": "Lokasi strategis, ukuran sedang",
        "Lokasi": 25,
        "Tanah": 120,
        "Bangunan": 80
    },
    {
        "Nama": "Skenario 4",
        "Kondisi": "Lokasi sangat strategis, ukuran besar",
        "Lokasi": 10,
        "Tanah": 180,
        "Bangunan": 130
    },
    {
        "Nama": "Skenario 5",
        "Kondisi": "Lokasi tidak strategis, ukuran besar",
        "Lokasi": 45,
        "Tanah": 180,
        "Bangunan": 130
    }
]

print("\n==============================================")
print(" HASIL PENGUJIAN 5 SKENARIO HARGA RUMAH")
print("==============================================")

for data in skenario:

    hasil, agregasi = evaluasi_sistem_fuzzy(
        data["Lokasi"],
        data["Tanah"],
        data["Bangunan"]
    )

    harga_rumah = hasil * 100_000_000

    print(f"\n{data['Nama']}")
    print(f"Kondisi             : {data['Kondisi']}")
    print(f"Lokasi              : {data['Lokasi']}")
    print(f"Luas Tanah          : {data['Tanah']} m2")
    print(f"Luas Bangunan       : {data['Bangunan']} m2")
    print(f"Nilai Defuzzifikasi : {hasil:.2f}")
    print(f"Perkiraan Harga     : Rp{harga_rumah:,.0f}")

print("\n==============================================")
print(" PENGUJIAN SELESAI")
print("==============================================")
