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
| Topik | Metode Sugeno dan Tsukamoto |
| Repository | LOGIKA-FUZZY/MODUL 2/Pertemuan 9 |
| Tanggal | 24 Oktober 2026 |

## B. Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa diharapkan mampu:

1. Memahami prinsip kerja metode inferensi Takagi-Sugeno-Kang (TSK atau Sugeno) Orde 0 dan Orde 1.
2. Memahami prinsip kerja metode inferensi Tsukamoto yang menggunakan fungsi keanggotaan monoton.
3. Melakukan perhitungan manual untuk proses inferensi Sugeno dan Tsukamoto menggunakan teknik rata-rata terbobot (*Weighted Average*).
4. Mengimplementasikan algoritma Sugeno dan Tsukamoto secara modular menggunakan bahasa pemrograman Python.
5. Membandingkan karakteristik, akurasi, efisiensi komputasi, dan pemilihan metode antara Mamdani, Sugeno, dan Tsukamoto.

## C. Requirement

Perangkat lunak yang digunakan dalam praktikum ini adalah:

| Komponen | Keterangan |
|---|---|
| Sistem Operasi | Windows 11 Home Single Language 64-bit (10.0, Build 26100) |
| Browser | Google Chrome Version 130.0.6723.117 (Official Build) (64-bit) |
| Tools | Visual Studio Code |

## D. Dasar Teori

### 1. Metode Sugeno (Takagi-Sugeno-Kang)

Metode Sugeno diperkenalkan oleh Takagi, Sugeno, dan Kang pada tahun 1985. Pada metode ini, konsekuen atau bagian THEN dari aturan fuzzy bukan berupa himpunan fuzzy, melainkan nilai tegas (*crisp*) atau persamaan matematika.

Metode Sugeno memiliki dua jenis, yaitu:

#### a. Sugeno Orde 0 (Konstanta)

Pada Sugeno Orde 0, konsekuen setiap aturan berbentuk nilai konstanta skalar.

Bentuk aturan:

\[
\text{IF }x\text{ is }A_i
\text{ AND }y\text{ is }B_i
\text{ THEN }z_i=k_i
\]

Keterangan:

- \(x\) dan \(y\) = variabel input.
- \(A_i\) dan \(B_i\) = himpunan fuzzy.
- \(z_i\) = nilai output aturan.
- \(k_i\) = nilai konstanta.

#### b. Sugeno Orde 1 (Fungsi Linear)

Pada Sugeno Orde 1, konsekuen berupa persamaan linear yang melibatkan variabel input.

Bentuk aturan:

\[
\text{IF }x\text{ is }A_i
\text{ AND }y\text{ is }B_i
\text{ THEN }z_i=p_ix+q_iy+r_i
\]

Keterangan:

- \(p_i\), \(q_i\), dan \(r_i\) = koefisien persamaan.
- \(x\) dan \(y\) = variabel input.
- \(z_i\) = nilai output dari aturan ke-i.

#### c. Defuzzifikasi Sugeno dengan Rata-Rata Terbobot

Karena setiap aturan menghasilkan nilai tegas, metode Sugeno tidak memerlukan proses integrasi kurva seperti pada metode Mamdani. Nilai akhir diperoleh menggunakan rata-rata terbobot (*Weighted Average*).

Rumus:

\[
z^*=
\frac{\sum_{i=1}^{N}\alpha_i z_i}
{\sum_{i=1}^{N}\alpha_i}
\]

Keterangan:

- \(z^*\) = hasil akhir defuzzifikasi.
- \(\alpha_i\) = nilai firing strength setiap aturan.
- \(z_i\) = nilai output dari setiap aturan.
- \(N\) = jumlah aturan yang aktif.

### 2. Metode Tsukamoto

Metode Tsukamoto merupakan metode inferensi fuzzy yang menggunakan konsekuen berupa himpunan fuzzy dengan fungsi keanggotaan monoton. Artinya, fungsi keanggotaan harus selalu naik atau selalu turun.

Untuk mendapatkan nilai output tegas, setiap aturan mencari nilai \(z_i\) menggunakan fungsi invers berdasarkan nilai firing strength.

Terdapat dua bentuk fungsi monoton yang digunakan:

#### a. Fungsi Keanggotaan Monoton Naik

Rumus:

\[
z_i=a+\alpha_i(b-a)
\]

#### b. Fungsi Keanggotaan Monoton Turun

Rumus:

\[
z_i=b-\alpha_i(b-a)
\]

Keterangan:

- \(z_i\) = nilai output tegas aturan ke-i.
- \(\alpha_i\) = firing strength aturan ke-i.
- \(a\) = batas bawah rentang output.
- \(b\) = batas atas rentang output.

Setelah nilai tegas dari setiap aturan diperoleh, hasil akhir dihitung menggunakan rata-rata terbobot.

\[
z^*=
\frac{\sum_{i=1}^{N}\alpha_i z_i}
{\sum_{i=1}^{N}\alpha_i}
\]

Dengan demikian, setiap aturan menghasilkan nilai output tegas berdasarkan fungsi keanggotaan monoton, kemudian seluruh hasil digabungkan menggunakan rata-rata terbobot.

## E. Contoh Perhitungan Manual

### Studi Kasus: Penentuan Harga Rumah

Pada contoh ini digunakan tiga variabel input dan satu variabel output.

| Komponen | Nilai |
|---|---:|
| Lokasi Rumah (\(x\)) | 15 |
| Luas Tanah (\(y\)) | 120 m² |
| Luas Bangunan (\(w\)) | 80 m² |
| Output Harga Rumah | Skala 1–23 |

### 1. Fuzzifikasi

Berdasarkan parameter fungsi keanggotaan yang digunakan, diperoleh hasil fuzzifikasi sebagai berikut:

**Lokasi Rumah:**
- Sangat Strategis = 0,5
- Strategis = 0,333

**Luas Tanah:**
- Sedang = 1

**Luas Bangunan:**
- Sedang = 1

### 2. Menentukan Aturan yang Aktif

Berdasarkan tabel aturan harga rumah, terdapat dua aturan yang aktif.

**R05:**

IF Lokasi Sangat Strategis AND Luas Tanah Sedang AND Luas Bangunan Sedang THEN Harga Rumah Mahal.

Nilai firing strength:

\[
\alpha_1=\min(0,5;1;1)
\]

\[
\alpha_1=0,5
\]

**R14:**

IF Lokasi Strategis AND Luas Tanah Sedang AND Luas Bangunan Sedang THEN Harga Rumah Normal.

Nilai firing strength:

\[
\alpha_2=\min(0,333;1;1)
\]

\[
\alpha_2=0,333
\]

Jadi, nilai firing strength yang digunakan adalah:

- R05 = 0,5
- R14 = 0,333

### 3. Perhitungan Sugeno Orde 0

Pada Sugeno Orde 0, setiap aturan menghasilkan nilai konstanta. Dalam contoh ini digunakan nilai puncak fungsi keanggotaan harga rumah sebagai nilai konstanta.

- R05: Harga Mahal = 15
- R14: Harga Normal = 11

Diketahui:

\[
z_1=15
\]

\[
z_2=11
\]

Menggunakan rumus rata-rata terbobot:

\[
z^*=
\frac{\sum\alpha_i z_i}{\sum\alpha_i}
\]

Substitusi nilai:

\[
z^*=
\frac{(0,5\times15)+(0,333\times11)}
{0,5+0,333}
\]

\[
z^*=\frac{7,5+3,663}{0,833}
\]

\[
z^*=\frac{11,163}{0,833}
\]

\[
\boxed{z^*\approx13,401}
\]

Jadi, hasil perhitungan Sugeno Orde 0 adalah sekitar **13,401** pada skala harga rumah.

### 4. Perhitungan Tsukamoto

Pada metode Tsukamoto, konsekuen harus menggunakan fungsi keanggotaan monoton.

Dalam contoh ini digunakan fungsi monoton naik dengan rentang output harga rumah 1–23.

Rumus fungsi monoton naik:

\[
z_i=a+\alpha_i(b-a)
\]

Dengan \(a=1\) dan \(b=23\), diperoleh:

\[
z_i=1+\alpha_i(23-1)
\]

\[
z_i=1+22\alpha_i
\]

Perhitungan setiap aturan:

**R05:**

\[
z_1=1+22(0,5)
\]

\[
z_1=12
\]

**R14:**

\[
z_2=1+22(0,333)
\]

\[
z_2=8,326
\]

Selanjutnya, menghitung hasil akhir menggunakan rata-rata terbobot:

\[
z^*=
\frac{(0,5\times12)+(0,333\times8,326)}
{0,5+0,333}
\]

\[
z^*=\frac{6+2,7716}{0,833}
\]

\[
z^*=\frac{8,7716}{0,833}
\]

\[
\boxed{z^*\approx10,530}
\]

Jadi, hasil perhitungan Tsukamoto adalah sekitar **10,530** pada skala harga rumah.

## F. Implementasi dalam Python

Pada bagian ini dilakukan implementasi metode Sugeno Orde 0, Sugeno Orde 1, dan Tsukamoto menggunakan bahasa pemrograman Python.

### 1. Program Python

```python
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
    fungsi_invers_list: list lambda fungsi invers
    untuk setiap aturan
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
```

### 2. Output Program

Program menampilkan hasil perhitungan dari tiga metode, yaitu Sugeno Orde 0, Sugeno Orde 1, dan Tsukamoto.

Hasil yang ditampilkan meliputi:

- Nilai input lokasi, luas tanah, dan luas bangunan.
- Nilai firing strength dari aturan R05 dan R14.
- Nilai output setiap aturan pada Sugeno Orde 0.
- Nilai output setiap aturan pada Sugeno Orde 1.
- Nilai output setiap aturan pada Tsukamoto.
- Hasil akhir perhitungan dari ketiga metode.

*Catatan: Nilai output lengkap dapat dilihat pada hasil eksekusi program di Visual Studio Code.*

## G. Matriks Perbandingan Mamdani, Sugeno, dan Tsukamoto

Berikut perbandingan karakteristik ketiga metode inferensi fuzzy berdasarkan beberapa kriteria.

| Kriteria | Metode Mamdani | Metode Sugeno (TSK) | Metode Tsukamoto |
|---|---|---|---|
| Bentuk Konsekuen | Himpunan fuzzy berupa kategori harga rumah (Sangat Murah, Murah, Normal, Mahal, Sangat Mahal). | Konstanta (Orde 0) atau fungsi linear (Orde 1) sebagai nilai keluaran harga rumah. | Himpunan fuzzy dengan fungsi keanggotaan monoton. |
| Kecepatan Komputasi | Relatif lebih lambat karena memerlukan proses agregasi dan defuzzifikasi. | Cepat karena menggunakan perhitungan rata-rata terbobot. | Relatif cepat karena menggunakan fungsi invers dan rata-rata terbobot. |
| Representasi Penalaran | Alami dan mudah dipahami karena menggunakan kategori harga rumah. | Kurang intuitif untuk bahasa manusia karena konsekuennya berupa nilai atau persamaan matematika. | Cukup mudah dipahami, tetapi konsekuennya harus memiliki fungsi keanggotaan monoton. |
| Cocok untuk | Sistem pendukung keputusan yang menentukan kategori harga rumah berdasarkan kondisi rumah. | Sistem prediksi harga rumah yang membutuhkan hasil berupa nilai numerik. | Sistem penentuan harga rumah yang memiliki hubungan keputusan monoton. |
| Optimasi Matematika | Relatif lebih sulit diintegrasikan dengan metode pembelajaran mesin karena proses defuzzifikasi. | Mudah dikombinasikan dengan Neural Network, misalnya ANFIS. | Membutuhkan fungsi keanggotaan monoton dan perhitungan invers. |

Berdasarkan tabel tersebut, setiap metode memiliki kelebihan dan karakteristik masing-masing. Mamdani lebih mudah dipahami karena menggunakan kategori fuzzy, Sugeno lebih sederhana dalam menghasilkan nilai numerik, sedangkan Tsukamoto menggunakan fungsi keanggotaan monoton untuk memperoleh output setiap aturan.

## H. Tugas Praktikum 9

### 1. Implementasi Sistem Sugeno dan Tsukamoto

Pada tugas ini dibuat program untuk membandingkan hasil metode Sugeno Orde 0 dan Tsukamoto dalam sistem penentuan harga rumah.

Program menggunakan tiga variabel input, yaitu lokasi, luas tanah, dan luas bangunan. Pengujian dilakukan dengan lima variasi input untuk mengetahui perbedaan hasil dari kedua metode.

### 2. Program Python

```python
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

    return (
        np.sum(np.array(alphas) * np.array(z_values))
        / total_alpha
    )


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

    return (
        np.sum(np.array(alphas) * np.array(z_values))
        / total_alpha
    )


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

plt.savefig(
    "grafik_perbandingan_harga_rumah.png",
    dpi=200
)

plt.show()
```

### 3. Output Program

Program melakukan pengujian menggunakan lima variasi input lokasi, luas tanah, dan luas bangunan. Hasil perhitungan ditampilkan dalam bentuk tabel perbandingan yang berisi:

- Nomor pengujian.
- Nilai lokasi.
- Luas tanah.
- Luas bangunan.
- Hasil metode Sugeno.
- Hasil metode Tsukamoto.
- Selisih hasil kedua metode.

Selain tabel, program menghasilkan grafik batang untuk membandingkan hasil Sugeno Orde 0 dan Tsukamoto pada setiap skenario pengujian.

**Nama file grafik yang dihasilkan:**

`grafik_perbandingan_harga_rumah.png`

*Catatan: Screenshot output tabel dan grafik dimasukkan setelah program dijalankan.*

## I. Pertanyaan Analisis

### 1. Mengapa metode Sugeno jauh lebih disukai dibandingkan Mamdani pada sistem kontrol industri waktu-nyata (*real-time industrial control*)?

**Jawaban:**

Metode Sugeno lebih disukai karena proses perhitungannya lebih sederhana dan cepat dibandingkan Mamdani. Sugeno menggunakan nilai output berupa konstanta atau persamaan matematika sehingga tidak memerlukan proses agregasi dan defuzzifikasi seperti pada Mamdani.

Hal ini membuat waktu komputasi lebih singkat dan cocok digunakan pada sistem kontrol industri yang membutuhkan keputusan secara cepat dan terus-menerus.

### 2. Apa syarat mutlak yang harus dipenuhi oleh fungsi keanggotaan konsekuen pada metode Tsukamoto? Mengapa kurva segitiga simetris tidak dapat digunakan sebagai konsekuen Tsukamoto?

**Jawaban:**

Syarat mutlak fungsi keanggotaan konsekuen pada metode Tsukamoto adalah harus bersifat monoton, yaitu selalu naik atau selalu turun. Hal ini diperlukan agar nilai keluaran *crisp* dapat dicari melalui proses invers berdasarkan nilai α-predikat setiap aturan.

Kurva segitiga simetris tidak dapat digunakan secara keseluruhan karena memiliki bagian yang naik dan turun, sehingga tidak monoton dan dapat menghasilkan lebih dari satu nilai keluaran untuk satu derajat keanggotaan.

### 3. Pada kondisi apakah metode Sugeno Orde 1 menghasilkan akurasi yang lebih superior dibandingkan Sugeno Orde 0?

**Jawaban:**

Sugeno Orde 1 dapat menghasilkan akurasi yang lebih baik ketika hubungan antara input dan output bersifat kompleks atau berubah-ubah secara bertahap. Hal ini karena Sugeno Orde 1 menggunakan persamaan linear yang melibatkan variabel input, sedangkan Sugeno Orde 0 hanya menggunakan nilai konstanta sebagai output setiap aturan.

Dengan demikian, Sugeno Orde 1 lebih mampu menggambarkan perubahan output berdasarkan kondisi input, terutama ketika hubungan tersebut mendekati pola linear.

## J. Kesimpulan
Metode Sugeno dan Tsukamoto menawarkan alternatif inferensi berkecepatan komputasi tinggi tanpa memerlukan defuzzifikasi integrasi numerik yang berat. Sugeno sangat unggul dalam aplikasi kontrol teknik dan integrasi sistem cerdas adaptif, sementara Tsukamoto memberikan penalaran transparan berbasis fungsi monotonik terbalik.

