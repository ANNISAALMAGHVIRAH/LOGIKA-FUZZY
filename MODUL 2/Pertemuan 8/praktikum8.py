
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import pandas as pd

# 1. Menentukan domain harga rumah
z = np.arange(1, 23.01, 0.01)

# 2. Membuat fungsi keanggotaan harga rumah
sangat_murah = fuzz.trapmf(z, [1, 1, 3, 7])
murah = fuzz.trimf(z, [3, 7, 11])
normal = fuzz.trimf(z, [7, 11, 15])
mahal = fuzz.trimf(z, [11, 15, 19])
sangat_mahal = fuzz.trapmf(z, [15, 19, 23, 23])

# 3. Menentukan nilai firing strength
alpha_murah = 0.5
alpha_normal = 0.8
alpha_mahal = 0.2

# 4. Melakukan pemotongan fungsi keanggotaan
potong_murah = np.fmin(alpha_murah, murah)
potong_normal = np.fmin(alpha_normal, normal)
potong_mahal = np.fmin(alpha_mahal, mahal)

# 5. Menggabungkan hasil pemotongan dengan operator MAX
agregasi = np.fmax(
    potong_murah,
    np.fmax(potong_normal, potong_mahal)
)

# 6. Menghitung lima metode defuzzifikasi
hasil = {
    "Centroid": fuzz.defuzz(z, agregasi, 'centroid'),
    "Bisector": fuzz.defuzz(z, agregasi, 'bisector'),
    "MOM": fuzz.defuzz(z, agregasi, 'mom'),
    "SOM": fuzz.defuzz(z, agregasi, 'som'),
    "LOM": fuzz.defuzz(z, agregasi, 'lom')
}

# 7. Menampilkan hasil perhitungan
print("HASIL DEFUZZIFIKASI HARGA RUMAH")
for metode, nilai in hasil.items():
    print(f"{metode}: {nilai:.2f}")

# 8. Membuat tabel perbandingan
print("\nTABEL PERBANDINGAN")
print("+------------------------+--------------+")
print("| Metode Defuzzifikasi   | Nilai Output |")
print("+------------------------+--------------+")

for metode, nilai in hasil.items():
    print(f"| {metode:<22} | {nilai:>12.6f} |")

print("+------------------------+--------------+")

# 9. Membuat grafik visualisasi
plt.figure(figsize=(12, 6))

plt.plot(z, murah, label="Murah", linestyle="--")
plt.plot(z, normal, label="Normal", linestyle="--")
plt.plot(z, mahal, label="Mahal", linestyle="--")

plt.fill_between(
    z, agregasi, alpha=0.3,
    label="Hasil Agregasi"
)

warna = ['red', 'purple', 'black', 'green', 'orange']

for (metode, nilai), warna_garis in zip(hasil.items(), warna):
    plt.axvline(
        nilai,
        color=warna_garis,
        linestyle=":",
        label=f"{metode} = {nilai:.2f}"
    )

plt.title("Perbandingan Metode Defuzzifikasi Harga Rumah")
plt.xlabel("Nilai Harga Rumah")
plt.ylabel("Derajat Keanggotaan")
plt.legend()
plt.grid()
plt.savefig("defuzzifikasi_tugas_8_harga_rumah.png",
            dpi=300, bbox_inches="tight")
plt.show()
