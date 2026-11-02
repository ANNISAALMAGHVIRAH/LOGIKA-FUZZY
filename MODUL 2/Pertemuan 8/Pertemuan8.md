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
   - Centroid (*Center of Gravity / COG*).
   - Bisector (pembagi luas area seimbang).
   - Mean of Maximum (MOM).
   - Smallest of Maximum (SOM).
   - Largest of Maximum (LOM).
4. Mengimplementasikan sistem Mamdani menggunakan Python dan pustaka Scikit-Fuzzy.
5. Membandingkan perbedaan dan sensitivitas nilai output dari masing-masing metode defuzzifikasi.

## C. Requirement

Perangkat dan aplikasi yang digunakan dalam praktikum ini adalah:

- **Sistem Operasi:** Windows 11 Home Single Language 64-bit (10.0, Build 26100).
- **Browser:** Google Chrome Version 130.0.6723.117 (Official Build) (64-bit).
- **Tools:** Visual Studio Code.
- **Bahasa Pemrograman:** Python.
- **Library:** NumPy, Matplotlib, dan Scikit-Fuzzy.

Instalasi pustaka Scikit-Fuzzy dilakukan menggunakan perintah:

```bash
pip install scikit-fuzzy
```

## D. Dasar Teori

### 1. Karakteristik Metode Mamdani

Metode Mamdani merupakan salah satu metode inferensi fuzzy yang diperkenalkan oleh Ebrahim Mamdani pada tahun 1975. Metode ini banyak digunakan karena proses penalarannya mudah dipahami dan menggunakan aturan berbentuk IF-THEN.

Beberapa karakteristik utama metode Mamdani adalah:

1. **Konsekuen aturan:** Berupa himpunan fuzzy, bukan fungsi linear atau konstanta.
2. **Implikasi:** Menggunakan operator Minimum (MIN) untuk memotong fungsi keanggotaan output berdasarkan nilai firing strength atau \(\alpha\)-predikat.
3. **Agregasi:** Menggabungkan seluruh hasil implikasi aturan menggunakan operator Maksimum (MAX).
4. **Defuzzifikasi:** Mengubah hasil agregasi fuzzy menjadi nilai tegas (*crisp output*) menggunakan metode tertentu.

Rumus agregasi pada metode Mamdani adalah:

\[
\mu_{\text{Agg}}(z)=
\max_i
\left[
\min\left(\alpha_i,\mu_{C_i}(z)\right)
\right]
\]

Keterangan:

- \(\mu_{\text{Agg}}(z)\) = derajat keanggotaan hasil agregasi.
- \(\alpha_i\) = nilai firing strength aturan ke-i.
- \(\mu_{C_i}(z)\) = fungsi keanggotaan output dari aturan ke-i.
- MIN = operator untuk proses implikasi.
- MAX = operator untuk proses agregasi.

### 2. Ragam Metode Defuzzifikasi

Setelah proses agregasi menghasilkan satu kurva fuzzy pada semesta output \(Z\), diperlukan proses defuzzifikasi untuk memperoleh satu nilai crisp yang mewakili hasil tersebut.

Terdapat lima metode defuzzifikasi yang digunakan dalam praktikum ini.

#### a. Centroid (Center of Gravity / COG)

Centroid merupakan metode yang menghitung titik pusat atau titik keseimbangan dari seluruh luas daerah hasil agregasi fuzzy. Metode ini mempertimbangkan seluruh bentuk kurva sehingga hasilnya cenderung lebih halus.

Rumus:

\[
z^*_{\text{Centroid}}=
\frac{\int z\cdot\mu_{\text{Agg}}(z)\,dz}
{\int\mu_{\text{Agg}}(z)\,dz}
\]

Metode ini cocok digunakan ketika keputusan ingin mempertimbangkan seluruh daerah hasil agregasi.

#### b. Bisector

Bisector merupakan metode yang mencari titik yang membagi luas daerah hasil agregasi menjadi dua bagian yang sama besar.

Rumus:

\[
\int_{-\infty}^{z^*}\mu_{\text{Agg}}(z)\,dz
=
\int_{z^*}^{\infty}\mu_{\text{Agg}}(z)\,dz
\]

Metode ini menghasilkan nilai yang membagi luas kurva fuzzy menjadi dua bagian seimbang.

#### c. Mean of Maximum (MOM)

MOM menghitung nilai rata-rata dari seluruh titik yang memiliki derajat keanggotaan maksimum.

Rumus:

\[
z^*_{\text{MOM}}=
\frac{\sum_{z\in M}z}{|M|}
\]

Dengan:

\[
M=\{z\mid\mu(z)=\mu_{\max}\}
\]

Metode ini hanya memperhatikan titik-titik yang memiliki nilai keanggotaan tertinggi.

#### d. Smallest of Maximum (SOM)

SOM mengambil nilai terkecil atau paling kiri dari seluruh titik yang memiliki derajat keanggotaan maksimum.

Rumus:

\[
z^*_{\text{SOM}}=
\min\{z\mid\mu(z)=\mu_{\max}\}
\]

Metode ini memilih batas bawah dari daerah dengan keanggotaan tertinggi.

#### e. Largest of Maximum (LOM)

LOM mengambil nilai terbesar atau paling kanan dari seluruh titik yang memiliki derajat keanggotaan maksimum.

Rumus:

\[
z^*_{\text{LOM}}=
\max\{z\mid\mu(z)=\mu_{\max}\}
\]

Metode ini memilih batas atas dari daerah dengan keanggotaan tertinggi.

### 3. Perbedaan Lima Metode Defuzzifikasi

| Metode | Prinsip Perhitungan |
|---|---|
| Centroid | Menghitung titik pusat seluruh luas kurva agregasi. |
| Bisector | Mencari titik yang membagi luas kurva menjadi dua bagian sama besar. |
| MOM | Menghitung rata-rata seluruh titik dengan keanggotaan maksimum. |
| SOM | Mengambil titik terkecil dengan keanggotaan maksimum. |
| LOM | Mengambil titik terbesar dengan keanggotaan maksimum. |

## E. Implementasi dalam Python

Pada praktikum ini, metode Mamdani diterapkan pada sistem penentuan harga rumah. Program menggunakan Scikit-Fuzzy untuk membuat fungsi keanggotaan dan menghitung lima metode defuzzifikasi.

### 1. Import Library

```python
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
```

Library NumPy digunakan untuk perhitungan numerik, Matplotlib untuk membuat grafik, dan Scikit-Fuzzy untuk membantu proses perhitungan fungsi keanggotaan serta defuzzifikasi.

### 2. Menentukan Semesta Output dan Fungsi Keanggotaan

```python
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
```

Bagian ini menentukan rentang nilai output harga rumah dari skala 1 sampai 23. Selanjutnya, dibuat lima fungsi keanggotaan, yaitu Sangat Murah, Murah, Normal, Mahal, dan Sangat Mahal.

### 3. Menentukan Skenario dan Firing Strength

```python
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
```

Bagian ini menentukan nilai firing strength dan kategori output dari setiap aturan yang aktif pada tiga skenario pengujian. Setiap aturan memiliki nilai \(\alpha\) dan konsekuen yang digunakan untuk membentuk kurva agregasi.

### 4. Melakukan Implikasi MIN dan Agregasi MAX

```python
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
        raise ValueError(
            f"Agregasi {nama_skenario} kosong!"
        )

    kurva_agregasi[nama_skenario] = agregasi
```

Pada tahap ini, setiap fungsi keanggotaan output dipotong menggunakan nilai firing strength dengan operator MIN. Selanjutnya, hasil pemotongan dari seluruh aturan digabungkan menggunakan operator MAX.

Hasilnya adalah kurva agregasi yang digunakan sebagai dasar untuk menghitung nilai crisp.

### 5. Menghitung Lima Metode Defuzzifikasi

```python
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
```

Bagian ini menghitung lima metode defuzzifikasi untuk setiap skenario. Hasil perhitungan disimpan ke dalam variabel `hasil_defuzz` agar dapat ditampilkan dan dibandingkan.

### 6. Menampilkan Hasil Perhitungan

```python
print("=" * 70)
print("HASIL KOMPARASI METODE DEFUZZIFIKASI MAMDANI")
print("SISTEM PENENTUAN HARGA RUMAH")
print("=" * 70)

for nama_skenario, hasil in hasil_defuzz.items():

    print("\n", nama_skenario)

    for metode, nilai in hasil.items():
        print(f"Metode {metode.upper():<10}: {nilai:.3f}")

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
```

Kode tersebut menampilkan hasil dari setiap metode defuzzifikasi, kemudian menyusun hasilnya ke dalam tabel perbandingan agar lebih mudah dianalisis.

### 7. Visualisasi Hasil Defuzzifikasi

```python
colors = {
    'centroid': 'red',
    'bisector': 'purple',
    'mom': 'black',
    'som': 'green',
    'lom': 'orange'
}

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

Bagian ini menampilkan kurva agregasi fuzzy untuk setiap skenario. Garis vertikal dengan warna berbeda menunjukkan posisi hasil dari metode Centroid, Bisector, MOM, SOM, dan LOM.

Dengan visualisasi tersebut, perbedaan posisi nilai akhir dari setiap metode dapat dilihat secara langsung.

## F. Analisis Hasil Komparasi Metode

Berdasarkan hasil pengujian pada Skenario B dalam sistem penentuan harga rumah, diperoleh perbandingan lima metode defuzzifikasi sebagai berikut.

| Metode | Nilai Output | Karakteristik Utama | Rekomendasi pada Kasus Harga Rumah |
|---|---:|---|---|
| Centroid (COG) | ≈12,014 | Mempertimbangkan seluruh luas kurva agregasi. | Estimasi harga berdasarkan seluruh aturan yang aktif. |
| Bisector | ≈11,830 | Membagi luas kurva agregasi menjadi dua bagian sama besar. | Estimasi dengan mempertimbangkan keseimbangan luas kurva. |
| MOM | ≈11,000 | Mengambil rata-rata titik dengan derajat keanggotaan maksimum. | Estimasi berdasarkan nilai dengan keanggotaan tertinggi. |
| SOM | ≈9,400 | Memilih batas bawah dari daerah dengan keanggotaan maksimum. | Estimasi dengan mengambil nilai yang lebih rendah. |
| LOM | ≈12,600 | Memilih batas atas dari daerah dengan keanggotaan maksimum. | Estimasi dengan mengambil nilai yang lebih tinggi. |

Berdasarkan tabel tersebut, Centroid menghasilkan nilai sekitar 12,014, sedangkan Bisector menghasilkan nilai sekitar 11,830. Kedua metode memiliki hasil yang berdekatan karena sama-sama mempertimbangkan luas daerah hasil agregasi.

MOM menghasilkan nilai sekitar 11,000 karena mengambil rata-rata titik yang memiliki derajat keanggotaan maksimum. Sementara itu, SOM menghasilkan nilai paling rendah, yaitu sekitar 9,400, dan LOM menghasilkan nilai paling tinggi, yaitu sekitar 12,600.

Perbedaan hasil tersebut menunjukkan bahwa pemilihan metode defuzzifikasi dapat memengaruhi nilai akhir yang dihasilkan oleh sistem meskipun menggunakan kurva agregasi yang sama.

## G. Tugas Praktikum 7

### Studi Kasus: Sistem Penentuan Harga Rumah

Pada tugas ini, metode Mamdani diterapkan untuk menentukan nilai harga rumah berdasarkan tiga konsekuen fuzzy, yaitu Murah, Normal, dan Mahal. Setiap konsekuen memiliki nilai firing strength yang berbeda.

### 1. Import Library dan Menentukan Domain

```python
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import pandas as pd

# Menentukan domain harga rumah
z = np.arange(1, 23.01, 0.01)
```

Library yang digunakan adalah NumPy, Matplotlib, Scikit-Fuzzy, dan Pandas. Domain harga rumah ditentukan pada rentang 1 sampai 23 dengan interval 0,01.

### 2. Membuat Fungsi Keanggotaan Harga Rumah

```python
sangat_murah = fuzz.trapmf(z, [1, 1, 3, 7])
murah = fuzz.trimf(z, [3, 7, 11])
normal = fuzz.trimf(z, [7, 11, 15])
mahal = fuzz.trimf(z, [11, 15, 19])
sangat_mahal = fuzz.trapmf(z, [15, 19, 23, 23])
```

Bagian ini membentuk lima kategori fungsi keanggotaan harga rumah menggunakan fungsi segitiga dan trapesium.

### 3. Menentukan Nilai Firing Strength

```python
alpha_murah = 0.5
alpha_normal = 0.8
alpha_mahal = 0.2
```

Nilai firing strength ditentukan untuk tiga kategori output, yaitu Murah sebesar 0,5, Normal sebesar 0,8, dan Mahal sebesar 0,2.

### 4. Melakukan Pemotongan Fungsi Keanggotaan

```python
potong_murah = np.fmin(alpha_murah, murah)
potong_normal = np.fmin(alpha_normal, normal)
potong_mahal = np.fmin(alpha_mahal, mahal)
```

Setiap fungsi keanggotaan output dipotong menggunakan operator MIN berdasarkan nilai firing strength masing-masing.

### 5. Melakukan Agregasi MAX

```python
agregasi = np.fmax(
    potong_murah,
    np.fmax(potong_normal, potong_mahal)
)
```

Hasil pemotongan dari ketiga kategori kemudian digabungkan menggunakan operator MAX sehingga menghasilkan satu kurva agregasi fuzzy.

### 6. Menghitung Lima Metode Defuzzifikasi

```python
hasil = {
    "Centroid": fuzz.defuzz(z, agregasi, 'centroid'),
    "Bisector": fuzz.defuzz(z, agregasi, 'bisector'),
    "MOM": fuzz.defuzz(z, agregasi, 'mom'),
    "SOM": fuzz.defuzz(z, agregasi, 'som'),
    "LOM": fuzz.defuzz(z, agregasi, 'lom')
}
```

Pada bagian ini dilakukan perhitungan menggunakan lima metode defuzzifikasi. Hasil setiap metode disimpan dalam dictionary `hasil`.

### 7. Menampilkan Hasil Perhitungan

```python
print("HASIL DEFUZZIFIKASI HARGA RUMAH")

for metode, nilai in hasil.items():
    print(f"{metode}: {nilai:.2f}")

print("\nTABEL PERBANDINGAN")
print("+------------------------+--------------+")
print("| Metode Defuzzifikasi   | Nilai Output |")
print("+------------------------+--------------+")

for metode, nilai in hasil.items():
    print(f"| {metode:<22} | {nilai:>12.6f} |")

print("+------------------------+--------------+")
```

Kode tersebut menampilkan hasil dari kelima metode defuzzifikasi dalam bentuk teks dan tabel agar perbedaannya lebih mudah dilihat.

### 8. Membuat Grafik Visualisasi

```python
plt.figure(figsize=(12, 6))

plt.plot(z, murah, label="Murah", linestyle="--")
plt.plot(z, normal, label="Normal", linestyle="--")
plt.plot(z, mahal, label="Mahal", linestyle="--")

plt.fill_between(
    z,
    0,
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

Grafik tersebut menampilkan fungsi keanggotaan Murah, Normal, dan Mahal beserta daerah agregasi. Garis vertikal menunjukkan hasil dari setiap metode defuzzifikasi sehingga perbedaan nilai output dapat dibandingkan secara visual.

### 9. Analisis Tugas Praktikum

Berdasarkan hasil pengujian, metode yang paling sesuai untuk sistem penentuan harga rumah adalah Centroid. Metode ini menghitung titik keseimbangan dari seluruh daerah hasil agregasi fuzzy.

Dengan demikian, seluruh kategori harga yang aktif, seperti Murah, Normal, dan Mahal, ikut diperhitungkan dalam menentukan nilai akhir. Metode Centroid juga memberikan hasil yang mempertimbangkan bentuk keseluruhan kurva, bukan hanya titik dengan derajat keanggotaan tertinggi.

Namun, pemilihan metode tetap perlu disesuaikan dengan kebutuhan sistem. Jika sistem membutuhkan proses yang lebih sederhana, metode lain seperti MOM dapat menjadi alternatif.

## H. Pertanyaan Analisis

### 1. Mengapa metode Centroid memiliki komputasi yang lebih berat dibandingkan MOM pada mikrokontroler atau sistem berdaya rendah (*embedded systems*)?

**Jawaban:**

Metode Centroid membutuhkan perhitungan luas dan titik keseimbangan dari seluruh kurva hasil agregasi. Perhitungannya melibatkan banyak operasi matematika, seperti perkalian, penjumlahan, dan pembagian pada setiap titik data.

Sementara itu, metode MOM hanya mencari titik-titik yang memiliki derajat keanggotaan paling tinggi, kemudian menghitung nilai rata-ratanya. Karena prosesnya lebih sederhana, MOM membutuhkan komputasi yang lebih ringan dibandingkan Centroid.

### 2. Dalam skenario darurat (*emergency braking system* pada mobil otonom), metode manakah antara SOM dan LOM yang lebih tepat digunakan untuk menentukan besarnya gaya rem? Jelaskan implikasi keselamatannya!

**Jawaban:**

Pemilihan metode SOM atau LOM harus disesuaikan dengan arti nilai output yang digunakan oleh sistem. Jika nilai output yang lebih kecil mewakili gaya pengereman yang lebih kuat, maka SOM dapat dipilih karena mengambil nilai terkecil dari daerah dengan derajat keanggotaan maksimum.

Namun, sistem pengereman tidak boleh hanya mengandalkan pemilihan nilai terkecil. Kondisi kendaraan, kecepatan, permukaan jalan, dan risiko roda terkunci juga harus diperhitungkan agar pengereman tetap aman dan kendaraan tidak kehilangan kendali.

### 3. Jika kurva agregasi memiliki dua puncak terpisah yang simetris (*bimodal distribution*), apakah kelemahan metode MOM?

**Jawaban:**

Kelemahan metode MOM adalah menghasilkan nilai rata-rata dari seluruh titik yang memiliki derajat keanggotaan maksimum. Jika terdapat dua puncak yang terpisah dan simetris, hasil MOM bisa berada di tengah-tengah kedua puncak tersebut.

Padahal, nilai tengah tersebut belum tentu memiliki derajat keanggotaan yang tinggi. Akibatnya, hasil yang diperoleh bisa kurang mewakili kondisi sebenarnya karena berada di antara dua daerah dengan nilai keanggotaan maksimum.

## I. Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa metode Mamdani merupakan metode inferensi fuzzy yang menggunakan operator MIN pada proses implikasi dan operator MAX pada proses agregasi. Hasil dari kedua proses tersebut kemudian diubah menjadi nilai tegas melalui tahap defuzzifikasi.

Pada praktikum ini, digunakan lima metode defuzzifikasi, yaitu Centroid, Bisector, MOM, SOM, dan LOM. Setiap metode memiliki cara perhitungan dan karakteristik yang berbeda sehingga dapat menghasilkan nilai output yang berbeda meskipun menggunakan kurva agregasi yang sama.

Melalui implementasi Python menggunakan Scikit-Fuzzy, proses pemotongan fungsi keanggotaan, agregasi, perhitungan defuzzifikasi, dan visualisasi dapat dilakukan dengan lebih mudah. Untuk sistem penentuan harga rumah, metode Centroid dapat digunakan karena mempertimbangkan seluruh daerah hasil agregasi dalam menentukan nilai akhir.

Dengan demikian, pemilihan metode defuzzifikasi perlu disesuaikan dengan kebutuhan sistem, tingkat ketelitian, dan karakteristik keputusan yang ingin dihasilkan.
