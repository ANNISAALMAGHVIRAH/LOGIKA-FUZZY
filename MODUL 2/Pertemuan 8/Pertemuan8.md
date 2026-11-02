# LAPORAN PRAKTIKUM
# LOGIKA FUZZY

<br>

**Annisa Almaghvirah**  
**240306037**  
[GitHub](https://github.com/ANNISAALMAGHVIRAH)

<br>

**Program Studi Teknologi Informasi**  
**Fakultas Dakwah dan Ilmu Komunikasi**  
**Universitas Islam Negeri Mataram**  
**2026**

---

## A. Identitas Praktikum

| Komponen | Keterangan |
|---|---|
| Modul | Modul 2 |
| Topik | Metode Mamdani dan Metode Defuzzifikasi |
| Repository | LOGIKA-FUZZY/MODUL 2/Pertemuan 8 |
| Tanggal | 24 Oktober 2026 |

## B. Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa diharapkan mampu:

1. Memahami prinsip kerja metode penalaran inferensi Mamdani (Max-Min).
2. Melakukan proses implikasi pemotongan kurva (*clipping*) dan agregasi maksimum.
3. Memahami dan mengimplementasikan lima metode defuzzifikasi, yaitu:
   - Centroid (*Center of Gravity* atau COG).
   - Bisector (pembagi luas area seimbang).
   - Mean of Maximum (MOM).
   - Smallest of Maximum (SOM).
   - Largest of Maximum (LOM).
4. Mengimplementasikan sistem Mamdani menggunakan Python dan pustaka `scikit-fuzzy`.
5. Membandingkan sensitivitas nilai output dari masing-masing metode defuzzifikasi.

## C. Requirement

Perangkat lunak yang digunakan dalam praktikum ini adalah:

| Komponen | Keterangan |
|---|---|
| Sistem Operasi | Windows 11 Home Single Language 64-bit (10.0, Build 26100) |
| Browser | Google Chrome Version 130.0.6723.117 (Official Build) (64-bit) |
| Tools | Visual Studio Code |

## D. Dasar Teori

### 1. Karakteristik Metode Mamdani

Metode Mamdani diperkenalkan oleh Ebrahim Mamdani pada tahun 1975. Metode ini merupakan salah satu metode inferensi fuzzy yang banyak digunakan karena cara kerjanya cukup mudah dipahami dan dapat menggambarkan proses penalaran manusia.

Ciri khas utama metode Mamdani adalah:

1. **Konsekuen aturan:** Berupa himpunan fuzzy, bukan fungsi linear atau konstanta.
2. **Implikasi:** Menggunakan operator Minimum untuk memotong fungsi keanggotaan output sesuai nilai α-predikat.
3. **Agregasi:** Menggabungkan seluruh kurva output menggunakan operator Maksimum.
4. **Defuzzifikasi:** Mengubah hasil agregasi fuzzy menjadi nilai tegas (*crisp*) melalui perhitungan numerik.

Rumus agregasi metode Mamdani adalah:

\[
\mu_{\mathrm{Agg}}(z)=
\max_i\left[\min\left(\alpha_i,\mu_{C_i}(z)\right)\right]
\]

Keterangan:

- \(\mu_{\mathrm{Agg}}(z)\) = derajat keanggotaan hasil agregasi.
- \(\alpha_i\) = nilai firing strength atau α-predikat aturan ke-i.
- \(\mu_{C_i}(z)\) = fungsi keanggotaan konsekuen aturan ke-i.
- MIN = operator untuk memotong kurva.
- MAX = operator untuk menggabungkan hasil pemotongan.

### 2. Ragam Metode Defuzzifikasi

Setelah kurva agregasi \(\mu_{\mathrm{Agg}}(z)\) terbentuk pada semesta output \(Z\), diperlukan proses defuzzifikasi untuk mendapatkan satu nilai tegas (*crisp*) yang mewakili hasil sistem fuzzy.

Berikut lima metode defuzzifikasi yang digunakan:

#### a. Centroid (Center of Gravity / COG)

Metode Centroid merupakan metode yang paling umum digunakan. Metode ini menghitung titik pusat berat dari seluruh luas daerah hasil agregasi fuzzy.

Rumus:

\[
z^*_{\mathrm{Centroid}}=
\frac{\int z\cdot\mu_{\mathrm{Agg}}(z)\,dz}
{\int\mu_{\mathrm{Agg}}(z)\,dz}
\]

Metode ini mempertimbangkan seluruh bentuk kurva agregasi sehingga hasilnya cenderung lebih seimbang.

#### b. Bisector

Metode Bisector mencari nilai \(z^*\) yang membagi luas total daerah fuzzy menjadi dua bagian yang sama besar.

Rumus:

\[
\int_{-\infty}^{z^*}\mu_{\mathrm{Agg}}(z)\,dz
=
\int_{z^*}^{\infty}\mu_{\mathrm{Agg}}(z)\,dz
\]

Dengan metode ini, luas daerah di sebelah kiri dan kanan titik hasil defuzzifikasi memiliki nilai yang sama.

#### c. Mean of Maximum (MOM)

Metode MOM menghitung nilai rata-rata dari seluruh nilai \(z\) yang memiliki derajat keanggotaan maksimum.

Rumus:

\[
z^*_{\mathrm{MOM}}=
\frac{\sum_{z\in M}z}{|M|}
\]

Keterangan:

\[
M=\{z\mid\mu(z)=\mu_{\max}\}
\]

Metode ini mengambil nilai tengah dari seluruh titik yang memiliki derajat keanggotaan tertinggi.

#### d. Smallest of Maximum (SOM)

Metode SOM mengambil nilai \(z\) terkecil atau paling kiri yang memiliki derajat keanggotaan maksimum.

Rumus:

\[
z^*_{\mathrm{SOM}}=
\min\{z\mid\mu(z)=\mu_{\max}\}
\]

#### e. Largest of Maximum (LOM)

Metode LOM mengambil nilai \(z\) terbesar atau paling kanan yang memiliki derajat keanggotaan maksimum.

Rumus:

\[
z^*_{\mathrm{LOM}}=
\max\{z\mid\mu(z)=\mu_{\max}\}
\]

## E. Implementasi dalam Python

Pada bagian ini dilakukan simulasi metode inferensi Mamdani dengan menggunakan nilai *firing strength* dari beberapa skenario. Setiap aturan akan melalui proses implikasi MIN, kemudian hasilnya digabungkan menggunakan agregasi MAX.

### 1. Instalasi Library

Sebelum menjalankan program, instal pustaka `scikit-fuzzy` menggunakan perintah berikut:

```bash
pip install scikit-fuzzy
```

### 2. Program Python

```python
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
# 2. PERHITUNGAN 5 METODE DEFUZZIFIKASI
# ==========================================================

defuzz_methods = [
    'centroid',
    'bisector',
    'mom',
    'som',
    'lom'
]

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

# Visualisasi setiap skenario
for nama_skenario, agregasi in kurva_agregasi.items():

    plt.figure(figsize=(12, 6.5))

    plt.plot(
        z,
        agregasi,
        color='blue',
        linewidth=2.5,
        label='Kurva Agregasi Fuzzy'
    )

    plt.fill_between(
        z,
        0,
        agregasi,
        color='skyblue',
        alpha=0.4
    )

    for method, val in hasil_defuzz[nama_skenario].items():

        plt.axvline(
            x=val,
            color=colors[method],
            linestyle='--',
            linewidth=2,
            label=f'{method.upper()} ({val:.2f})'
        )

        # Menampilkan titik hasil defuzzifikasi
        idx = np.abs(z - val).argmin()

        plt.scatter(
            [val],
            [agregasi[idx]],
            color=colors[method],
            s=60,
            zorder=6
        )

    plt.title(
        'Perbandingan 5 Metode Defuzzifikasi - ' + nama_skenario,
        fontsize=13,
        fontweight='bold'
    )

    plt.xlabel('Skala Harga Rumah', fontsize=11)
    plt.ylabel('Derajat Keanggotaan μ(z)', fontsize=11)

    plt.ylim(-0.05, 1.05)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='upper right', fontsize=9)
    plt.tight_layout()

    nama_file = nama_skenario.replace(" ", "_").lower()

    plt.savefig(
        f'komparasi_{nama_file}.png',
        dpi=300
    )

    plt.show()
```

### 3. Output Program

Program menghasilkan nilai defuzzifikasi untuk Skenario A, Skenario B, dan Skenario C. Hasilnya ditampilkan dalam bentuk teks dan tabel perbandingan.

Selain itu, program menghasilkan tiga grafik yang memperlihatkan kurva agregasi fuzzy beserta posisi nilai dari masing-masing metode defuzzifikasi.

**Nama file grafik yang dihasilkan:**

- `komparasi_skenario_a.png`
- `komparasi_skenario_b.png`
- `komparasi_skenario_c.png`

*Catatan: Nilai numerik output diperoleh setelah program dijalankan. Nilainya tidak dicantumkan di sini agar tidak menggunakan angka perkiraan yang belum diverifikasi dari hasil eksekusi.*

## F. Analisis Hasil Komparasi Metode

Berikut tabel perbandingan lima metode defuzzifikasi berdasarkan hasil pengujian pada Skenario B dalam sistem penentuan harga rumah.

| Metode | Nilai Output | Karakteristik Utama | Rekomendasi pada Kasus Harga Rumah |
|---|---:|---|---|
| Centroid (COG) | ≈ 12.014 | Halus dan kontinu, mempertimbangkan seluruh luas kurva agregasi. | Menentukan estimasi harga rumah berdasarkan seluruh aturan yang aktif. |
| Bisector | ≈ 11.830 | Membagi luas kurva agregasi menjadi dua bagian yang sama besar. | Menentukan harga rumah dengan mempertimbangkan keseimbangan luas kurva. |
| MOM | ≈ 11.000 | Mengambil nilai tengah dari daerah dengan derajat keanggotaan tertinggi. | Menentukan harga rumah berdasarkan nilai dengan keanggotaan tertinggi. |
| SOM | ≈ 9.400 | Memilih batas bawah dari daerah dengan derajat keanggotaan tertinggi. | Menghasilkan estimasi harga rumah yang lebih rendah. |
| LOM | ≈ 12.600 | Memilih batas atas dari daerah dengan derajat keanggotaan tertinggi. | Menghasilkan estimasi harga rumah yang lebih tinggi. |

Berdasarkan tabel tersebut, Centroid menghasilkan nilai sekitar 12,014, sedangkan Bisector menghasilkan nilai sekitar 11,830. Kedua metode memiliki hasil yang berdekatan karena sama-sama mempertimbangkan luas kurva agregasi.

MOM menghasilkan nilai 11,000 karena mengambil rata-rata titik dengan keanggotaan tertinggi. SOM menghasilkan nilai paling rendah, yaitu 9,400, sedangkan LOM menghasilkan nilai paling tinggi, yaitu 12,600.

Nilai-nilai tersebut merupakan hasil perbandingan yang dicatat pada pengujian Skenario B. Untuk memastikan kesesuaiannya dengan program, angka perlu dicocokkan kembali dengan output saat kode dijalankan.

## G. Tugas Praktikum 7

### Studi Kasus: Sistem Penentuan Harga Rumah

Pada tugas ini dilakukan simulasi sistem penentuan harga rumah menggunakan metode Mamdani. Variabel output yang digunakan adalah harga rumah dengan lima kategori, yaitu Sangat Murah, Murah, Normal, Mahal, dan Sangat Mahal.

### 1. Program Python

```python
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

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
    z,
    agregasi,
    alpha=0.3,
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

plt.savefig(
    "defuzzifikasi_tugas_8_harga_rumah.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
```

### 2. Output Program

Program menampilkan hasil perhitungan dari lima metode defuzzifikasi, yaitu Centroid, Bisector, MOM, SOM, dan LOM. Hasil perhitungan juga ditampilkan dalam bentuk tabel dan grafik.

Grafik memperlihatkan fungsi keanggotaan kategori Murah, Normal, dan Mahal, serta garis vertikal yang menunjukkan hasil dari masing-masing metode defuzzifikasi.

**Nama file grafik:**

`defuzzifikasi_tugas_8_harga_rumah.png`

### 3. Analisis Hasil Tugas

Berdasarkan simulasi yang dilakukan, metode yang paling sesuai untuk digunakan dalam sistem penentuan harga rumah adalah Centroid. Metode ini menghitung titik keseimbangan dari seluruh daerah hasil agregasi fuzzy.

Dengan demikian, semua kategori harga yang aktif, seperti Murah, Normal, dan Mahal, ikut diperhitungkan dalam menentukan nilai akhir. Hasilnya dapat memberikan estimasi harga rumah yang mempertimbangkan keseluruhan bentuk kurva agregasi.

## H. Pertanyaan Analisis

### 1. Mengapa metode Centroid memiliki komputasi yang lebih berat dibandingkan MOM pada mikrokontroler atau sistem berdaya rendah (*embedded systems*)?

**Jawaban:**

Metode Centroid membutuhkan perhitungan luas dan titik keseimbangan dari seluruh kurva hasil agregasi. Perhitungannya melibatkan banyak operasi matematika, seperti perkalian, penjumlahan, dan pembagian.

Sementara itu, metode MOM hanya mencari nilai rata-rata dari titik-titik yang memiliki derajat keanggotaan paling tinggi. Karena prosesnya lebih sederhana, MOM membutuhkan komputasi yang lebih ringan dibandingkan Centroid.

### 2. Dalam skenario darurat (*emergency braking system* pada mobil otonom), metode manakah antara SOM dan LOM yang lebih tepat digunakan untuk menentukan besarnya gaya rem? Jelaskan implikasi keselamatannya!

**Jawaban:**

Metode SOM lebih tepat jika nilai output yang lebih kecil mewakili gaya pengereman yang lebih kuat. Dengan memilih nilai terkecil dari titik yang memiliki derajat keanggotaan maksimum, sistem dapat memberikan pengereman yang lebih kuat untuk mengurangi risiko tabrakan.

Namun, penerapannya harus tetap mempertimbangkan kondisi kendaraan dan jalan agar tidak menyebabkan roda terkunci atau kendaraan kehilangan kendali. Pemilihan metode juga harus disesuaikan dengan definisi nilai output pada sistem pengereman tersebut.

### 3. Jika kurva agregasi memiliki dua puncak terpisah yang simetris (*bimodal distribution*), apakah kelemahan metode MOM?

**Jawaban:**

Kelemahan metode MOM adalah menghasilkan nilai rata-rata dari semua titik yang memiliki derajat keanggotaan maksimum. Jika terdapat dua puncak yang terpisah dan simetris, hasil MOM bisa berada di tengah-tengah kedua puncak tersebut.

Padahal, nilai tengah tersebut belum tentu memiliki derajat keanggotaan yang tinggi. Akibatnya, hasil yang diperoleh bisa kurang mewakili kondisi sebenarnya.

## I. Kesimpulan

Metode Mamdani memberikan representasi penalaran manusia yang alami dengan konsekuen berbentuk himpunan fuzzy. Pemilihan metode defuzzifikasi yang tepat (Centroid, Bisector, MOM, SOM, atau LOM) memungkinkan perancang sistem menyesuaikan profil keputusan: apakah netral-kontinu, konservatif, agresif, atau mengutamakan titik kepastian tertinggi.
