
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# ==========================================================
# 1. DEFINISI SEMESTA DAN BENTUK KURVA AGREGASI
# ==========================================================

# Semesta output: Harga Rumah (skala 1-23)
z = np.arange(1, 23.01, 0.01)

# Fungsi keanggotaan output Harga Rumah
mf_sangat_murah = fuzz.trapmf(z, [1, 1, 3, 7])
mf_murah = fuzz.trimf(z, [3, 7, 11])
mf_normal = fuzz.trimf(z, [7, 11, 15])
mf_mahal = fuzz.trimf(z, [11, 15, 19])
mf_sangat_mahal = fuzz.trapmf(z, [15, 19, 23, 23])

# Mengelompokkan fungsi keanggotaan
mf_harga = {
    "Sangat Murah": mf_sangat_murah,
    "Murah": mf_murah,
    "Normal": mf_normal,
    "Mahal": mf_mahal,
    "Sangat Mahal": mf_sangat_mahal
}

# Simulasi firing strength setiap skenario
skenario = {
    "Skenario A": {
        "R01": (1.0, "Murah")
    },

    "Skenario B": {
        "R04": (0.2, "Normal"),
        "R05": (0.3, "Mahal"),
        "R07": (0.2, "Mahal"),
        "R08": (0.3, "Sangat Mahal"),
        "R13": (0.2, "Murah"),
        "R14": (0.6, "Normal"),
        "R16": (0.2, "Normal"),
        "R17": (0.4, "Mahal")
    },

    "Skenario C": {
        "R27": (1.0, "Mahal")
    }
}

# Proses implikasi MIN dan agregasi MAX
kurva_agregasi = {}

for nama_skenario, aturan in skenario.items():

    agregasi = np.zeros_like(z)

    for nama_rule, (alpha, konsekuen) in aturan.items():

        # Implikasi MIN
        hasil_potong = np.fmin(
            alpha,
            mf_harga[konsekuen]
        )

        # Agregasi MAX
        agregasi = np.fmax(
            agregasi,
            hasil_potong
        )

    if np.max(agregasi) == 0:
        raise ValueError(f"Agregasi {nama_skenario} kosong!")

    kurva_agregasi[nama_skenario] = agregasi


# ==========================================================
# 2. PERHITUNGAN 5 METODE DEFUZZIFIKASI DENGAN SCIKIT-FUZZY
# ==========================================================

defuzz_methods = ['centroid', 'bisector', 'mom', 'som', 'lom']
hasil_defuzz = {}

for nama_skenario, agregasi in kurva_agregasi.items():

    hasil = {}

    for method in defuzz_methods:
        val = fuzz.defuzz(z, agregasi, method)
        hasil[method] = val

    hasil_defuzz[nama_skenario] = hasil



# ==========================================================
# 3. MENAMPILKAN HASIL DAN VISUALISASI
# ==========================================================

print("=" * 70)
print("HASIL KOMPARASI METODE DEFUZZIFIKASI MAMDANI")
print("SISTEM PENENTUAN HARGA RUMAH")
print("=" * 70)

# Menampilkan hasil setiap skenario
for nama_skenario, hasil in hasil_defuzz.items():

    print("\n", nama_skenario)

    for metode, nilai in hasil.items():
        print(f"Metode {metode.upper():<10}: {nilai:.3f}")

# Menampilkan tabel perbandingan
print("\nTABEL PERBANDINGAN HASIL")

print(
    f"{'Skenario':<15}"
    f"{'Centroid':<12}"
    f"{'Bisector':<12}"
    f"{'MOM':<12}"
    f"{'SOM':<12}"
    f"{'LOM':<12}"
)

for nama_skenario, hasil in hasil_defuzz.items():

    print(
        f"{nama_skenario:<15}"
        f"{hasil['centroid']:<12.3f}"
        f"{hasil['bisector']:<12.3f}"
        f"{hasil['mom']:<12.3f}"
        f"{hasil['som']:<12.3f}"
        f"{hasil['lom']:<12.3f}"
    )

# Warna setiap metode
colors = {
    'centroid': 'red',
    'bisector': 'purple',
    'mom': 'black',
    'som': 'green',
    'lom': 'orange'
}

# Membuat 3 grafik dalam 1 gambar
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

for ax, (nama_skenario, agregasi) in zip(
    axes, kurva_agregasi.items()
):

    # Kurva agregasi
    ax.plot(
        z,
        agregasi,
        color='blue',
        linewidth=2.5,
        label='Kurva Agregasi Fuzzy'
    )

    ax.fill_between(
        z,
        0,
        agregasi,
        color='skyblue',
        alpha=0.4
    )

    # Garis hasil lima metode defuzzifikasi
    for method, nilai in hasil_defuzz[nama_skenario].items():

        ax.axvline(
            x=nilai,
            color=colors[method],
            linestyle='--',
            linewidth=2,
            label=f'{method.upper()} ({nilai:.2f})'
        )

        # Titik penanda hasil defuzzifikasi
        idx = np.abs(z - nilai).argmin()

        ax.scatter(
            [nilai],
            [agregasi[idx]],
            color=colors[method],
            s=50,
            zorder=6
        )

    ax.set_title(
        nama_skenario,
        fontsize=13,
        fontweight='bold'
    )

    ax.set_xlabel('Skala Harga Rumah')
    ax.set_ylabel('Derajat Keanggotaan μ(z)')

    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(fontsize=8)

# Judul keseluruhan gambar
fig.suptitle(
    'Perbandingan 5 Metode Defuzzifikasi Mamdani\n'
    'Sistem Penentuan Harga Rumah',
    fontsize=15,
    fontweight='bold'
)

plt.tight_layout()

# Menyimpan satu gambar gabungan
plt.savefig(
    'komparasi_semua_skenario.png',
    dpi=300,
    bbox_inches='tight'
)

plt.show()
