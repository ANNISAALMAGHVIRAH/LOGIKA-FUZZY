# LAPORAN PRAKTIKUM LOGIKA FUZZY 2026

# LAPORAN ASESMEN MODUL 1
# PEMODELAN FUZZY

## 1. JUDUL PROYEK & IDENTITAS MAHASISWA

Proyek ini berjudul **"Sistem Rekomendasi Beban SKS Mahasiswa Berdasarkan IPK dan Aktivitas Non-Akademik"**. Pemodelan fuzzy digunakan untuk menentukan batas rekomendasi jumlah Kredit Semester (SKS) mahasiswa secara adaptif dan kontinyu tanpa menggunakan pembatasan kaku (*rigid threshold*).

| Komponen | Keterangan |
|---|---|
| Nama | Annisa Almaghvirah |
| NIM | 240306037 |
| Topik | Sistem Rekomendasi Beban SKS Mahasiswa |
| Input 1 | IPK (Indeks Prestasi Kumulatif, skala 0.00–4.00) |
| Input 2 | Aktivitas Non-Akademik (Jam/Minggu) |
| Output | Rekomendasi Beban SKS (SKS) |
| Label Input 1 | Rendah, Sedang, Tinggi |
| Label Input 2 | Lengang, Moderat, Padat |
| Label Output | Minimal, Sedang, Maksimal |
| Implementasi | Python / NumPy / Matplotlib |

---

## 2. LATAR BELAKANG & DESKRIPSI PERMASALAHAN

Penentuan beban studi (jumlah SKS) yang ideal bagi seorang mahasiswa berpengaruh signifikan terhadap keberhasilan akademiknya. Pada sistem informasi akademik konvensional, penentuan jatah SKS umumnya hanya didasarkan pada Indeks Prestasi Kumulatif (IPK) secara kaku (misalnya: IPK otomatis mendapatkan jatah 24 SKS).

Namun, pendekatan tersebut mengabaikan variabel riil lain seperti tingkat kesibukan atau Aktivitas Non-Akademik (organisasi, kerja paruh waktu, maupun kepanitiaan). Mahasiswa dengan IPK 3.80 yang memiliki tingkat aktivitas 35 jam/minggu berisiko mengalami burnout jika dipaksa mengambil 24 SKS, sedangkan pembatasan kaku sering kali tidak adil pada nilai perbatasan (contoh: IPK 2.99 vs 3.00).

Logika Fuzzy hadir untuk memetakan nilai konkret masukan ke dalam derajat keanggotaan (μ). Proyek Tahap 1 (Pemodelan Fuzzy) ini berfokus pada formulasi variabel linguistik, perancangan fungsi keanggotaan, pembuatan skrip Python murni, serta pengujian fuzzifikasi pada 5 skenario kondisi riil mahasiswa.

---

## 3. PERANCANGAN SISTEM FUZZY

### 3.1 Semesta Pembicaraan dan Domain Variabel

| Jenis Variabel | Nama Variabel | Satuan | Semesta Pembicaraan | Daftar Label Linguistik | Parameter Kurva |
|---|---|---|---|---|---|
| Input 1 | IPK | Skala | 0.00–4.00 | Rendah, Sedang, Tinggi | Rendah: (0.0, 0.0, 2.0, 2.75); Sedang: (2.5, 3.0, 3.5); Tinggi: (3.25, 3.75, 4.0, 4.0) |
| Input 2 | Aktivitas | Jam/Minggu | 0–40 | Lengang, Moderat, Padat | Lengang: (0, 0, 8, 16); Moderat: (12, 20, 28); Padat: (24, 32, 40, 40) |
| Output | Rekomendasi | SKS | 12–24 | Minimal, Sedang, Maksimal | Minimal: (12, 12, 14, 17); Sedang: (15, 18, 21); Maksimal: (19, 22, 24, 24) |

---

### 3.2 Penurunan Matematis Fungsi Keanggotaan

Fungsi keanggotaan dirancang menggunakan kombinasi kurva trapesium bahu kiri/kanan (*trapmf*) dan kurva segitiga (*trimf*).

#### A. Variabel IPK

Semesta pembicaraan:

\[
x \in [0.00,4.00]
\]

##### 1) Label Rendah — Trapesium Bahu Kiri

Parameter:

\[
(a,b,c,d)=(0.0,0.0,2.0,2.75)
\]

Fungsi keanggotaan:

\[
\mu_{\text{Rendah}}(x)=
\begin{cases}
1, & x\leq2.0\\
\dfrac{2.75-x}{2.75-2.0}, & 2.0<x<2.75\\
0, & x\geq2.75
\end{cases}
\]

##### 2) Label Sedang — Segitiga

Parameter:

\[
(a,b,c)=(2.5,3.0,3.5)
\]

Fungsi keanggotaan:

\[
\mu_{\text{Sedang}}(x)=
\begin{cases}
0, & x\leq2.5\ \text{atau}\ x\geq3.5\\
\dfrac{x-2.5}{3.0-2.5}, & 2.5<x\leq3.0\\
\dfrac{3.5-x}{3.5-3.0}, & 3.0<x<3.5
\end{cases}
\]

##### 3) Label Tinggi — Trapesium Bahu Kanan

Parameter:

\[
(a,b,c,d)=(3.25,3.75,4.0,4.0)
\]

Fungsi keanggotaan:

\[
\mu_{\text{Tinggi}}(x)=
\begin{cases}
0, & x\leq3.25\\
\dfrac{x-3.25}{3.75-3.25}, & 3.25<x<3.75\\
1, & x\geq3.75
\end{cases}
\]

---

#### B. Variabel Aktivitas Non-Akademik

Semesta pembicaraan:

\[
y \in [0,40]
\]

##### 1) Label Lengang — Trapesium Bahu Kiri

Parameter:

\[
(a,b,c,d)=(0,0,8,16)
\]

Fungsi keanggotaan:

\[
\mu_{\text{Lengang}}(y)=
\begin{cases}
1, & y\leq8\\
\dfrac{16-y}{16-8}, & 8<y<16\\
0, & y\geq16
\end{cases}
\]

##### 2) Label Moderat — Segitiga

Parameter:

\[
(a,b,c)=(12,20,28)
\]

Fungsi keanggotaan:

\[
\mu_{\text{Moderat}}(y)=
\begin{cases}
0, & y\leq12\ \text{atau}\ y\geq28\\
\dfrac{y-12}{20-12}, & 12<y\leq20\\
\dfrac{28-y}{28-20}, & 20<y<28
\end{cases}
\]

##### 3) Label Padat — Trapesium Bahu Kanan

Parameter:

\[
(a,b,c,d)=(24,32,40,40)
\]

Fungsi keanggotaan:

\[
\mu_{\text{Padat}}(y)=
\begin{cases}
0, & y\leq24\\
\dfrac{y-24}{32-24}, & 24<y<32\\
1, & y\geq32
\end{cases}
\]

---

#### C. Variabel Rekomendasi SKS

Semesta pembicaraan:

\[
z \in [12,24]
\]

##### 1) Label Minimal — Trapesium Bahu Kiri

Parameter:

\[
(a,b,c,d)=(12,12,14,17)
\]

Fungsi keanggotaan:

\[
\mu_{\text{Minimal}}(z)=
\begin{cases}
1, & z\leq14\\
\dfrac{17-z}{17-14}, & 14<z<17\\
0, & z\geq17
\end{cases}
\]

##### 2) Label Sedang — Segitiga

Parameter:

\[
(a,b,c)=(15,18,21)
\]

Fungsi keanggotaan:

\[
\mu_{\text{Sedang}}(z)=
\begin{cases}
0, & z\leq15\ \text{atau}\ z\geq21\\
\dfrac{z-15}{18-15}, & 15<z\leq18\\
\dfrac{21-z}{21-18}, & 18<z<21
\end{cases}
\]

##### 3) Label Maksimal — Trapesium Bahu Kanan

Parameter:

\[
(a,b,c,d)=(19,22,24,24)
\]

Fungsi keanggotaan:

\[
\mu_{\text{Maksimal}}(z)=
\begin{cases}
0, & z\leq19\\
\dfrac{z-19}{22-19}, & 19<z<22\\
1, & z\geq22
\end{cases}
\]

---

### 3.3 Ilustrasi Grafik Desain

Seluruh kurva bersebelahan saling bersinggungan (*overlap*) tanpa celah (*gap*).

- **Variabel IPK:** overlap Rendah–Sedang berada pada rentang **2.50–2.75**, dan Sedang–Tinggi pada rentang **3.25–3.50**.
- **Variabel Aktivitas:** overlap Lengang–Moderat berada pada rentang **12–16 jam/minggu**, dan Moderat–Padat pada rentang **24–28 jam/minggu**.
- **Variabel Rekomendasi SKS:** overlap Minimal–Sedang berada pada rentang **15–17 SKS**, dan Sedang–Maksimal pada rentang **19–21 SKS**.

#### Grafik IPK

```mermaid
xychart-beta
    title "Fungsi Keanggotaan Variabel IPK"
    x-axis "IPK" [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.25, 3.5, 3.75, 4]
    y-axis "Derajat Keanggotaan (μ)" 0 --> 1
    line [1, 1, 1, 1, 1, 0.333, 0, 0, 0, 0, 0]
    line [0, 0, 0, 0, 0, 0, 1, 0.5, 0, 0, 0]
    line [0, 0, 0, 0, 0, 0, 0, 0, 0.5, 1, 1]
```

#### Grafik Aktivitas Non-Akademik

```mermaid
xychart-beta
    title "Fungsi Keanggotaan Variabel Aktivitas"
    x-axis "Jam/Minggu" [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
    y-axis "Derajat Keanggotaan (μ)" 0 --> 1
    line [1, 1, 1, 0.5, 0, 0, 0, 0, 0, 0, 0]
    line [0, 0, 0, 0, 0.5, 1, 0.5, 0, 0, 0, 0]
    line [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
```

#### Grafik Rekomendasi SKS

```mermaid
xychart-beta
    title "Fungsi Keanggotaan Variabel Rekomendasi SKS"
    x-axis "SKS" [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    y-axis "Derajat Keanggotaan (μ)" 0 --> 1
    line [1, 1, 1, 0.667, 0.333, 0, 0, 0, 0, 0, 0, 0, 0]
    line [0, 0, 0, 0, 0.333, 0.667, 1, 0.667, 0.333, 0, 0, 0, 0]
    line [0, 0, 0, 0, 0, 0, 0, 0, 0.333, 0.667, 1, 1, 1]
```

---

## 4. IMPLEMENTASI PYTHON

### 4.1 Source Code Lengkap

```python
import os
import matplotlib.pyplot as plt
import numpy as np

# ================================================================
# ASESMEN MODUL 1: PEMODELAN FUZZY
# Sistem Rekomendasi Beban SKS Mahasiswa
# Nama : Annisa Almaghvirah
# NIM  : 240306037
# ================================================================

def trimf(x, params):
    """Fungsi keanggotaan segitiga (a, b, c)."""
    a, b, c = params
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)

    if b > a:
        idx1 = (x >= a) & (x <= b)
        y[idx1] = (x[idx1] - a) / (b - a)

    if c > b:
        idx2 = (x >= b) & (x <= c)
        y[idx2] = np.maximum(
            y[idx2],
            (c - x[idx2]) / (c - b)
        )

    y[x == b] = 1.0
    return np.clip(y, 0.0, 1.0)


def trapmf(x, params):
    """Fungsi keanggotaan trapesium (a, b, c, d)."""
    a, b, c, d = params
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)

    if a == b:
        y[x <= c] = 1.0
    else:
        idx1 = (x >= a) & (x <= b)
        y[idx1] = (x[idx1] - a) / (b - a)

    y[(x >= b) & (x <= c)] = 1.0

    if c == d:
        y[x >= b] = 1.0
    else:
        idx2 = (x >= c) & (x <= d)
        y[idx2] = np.maximum(
            y[idx2],
            (d - x[idx2]) / (d - c)
        )

    return np.clip(y, 0.0, 1.0)


MODEL_FUZZY = {
    'IPK': {
        'unit': 'Skala',
        'semesta': (0.0, 4.0),
        'membership': {
            'Rendah': ('trapmf', (0.0, 0.0, 2.0, 2.75)),
            'Sedang': ('trimf', (2.5, 3.0, 3.5)),
            'Tinggi': ('trapmf', (3.25, 3.75, 4.0, 4.0)),
        },
    },

    'Aktivitas': {
        'unit': 'Jam/Minggu',
        'semesta': (0, 40),
        'membership': {
            'Lengang': ('trapmf', (0, 0, 8, 16)),
            'Moderat': ('trimf', (12, 20, 28)),
            'Padat': ('trapmf', (24, 32, 40, 40)),
        },
    },

    'Rekomendasi SKS': {
        'unit': 'SKS',
        'semesta': (12, 24),
        'membership': {
            'Minimal': ('trapmf', (12, 12, 14, 17)),
            'Sedang': ('trimf', (15, 18, 21)),
            'Maksimal': ('trapmf', (19, 22, 24, 24)),
        },
    },
}


def hitung_derajat(tipe_kurva, params, nilai):
    val_arr = np.array([float(nilai)])

    if tipe_kurva == 'trimf':
        return float(trimf(val_arr, params)[0])
    elif tipe_kurva == 'trapmf':
        return float(trapmf(val_arr, params)[0])

    return 0.0


def fuzzifikasi(input_dict):
    """Fungsi pemetaan nilai masukan konkret ke derajat keanggotaan."""
    hasil = {}

    for var_name, nilai in input_dict.items():
        if var_name in MODEL_FUZZY:
            hasil[var_name] = {}

            for label, (tipe_kurva, params) in MODEL_FUZZY[
                var_name
            ]['membership'].items():

                deg = hitung_derajat(
                    tipe_kurva,
                    params,
                    nilai
                )

                hasil[var_name][label] = round(deg, 4)

    return hasil


def plot_variabel(output_dir='.'):
    """Menyimpan dan MENAMPILKAN grafik fungsi keanggotaan."""
    os.makedirs(output_dir, exist_ok=True)

    for var_name, var_info in MODEL_FUZZY.items():
        x_min, x_max = var_info['semesta']
        x = np.linspace(x_min, x_max, 500)

        plt.figure(figsize=(8, 4), dpi=100)

        for label, (tipe_kurva, params) in var_info[
            'membership'
        ].items():

            if tipe_kurva == 'trimf':
                y = trimf(x, params)
            elif tipe_kurva == 'trapmf':
                y = trapmf(x, params)

            plt.plot(x, y, linewidth=2, label=label)

        plt.title(
            f'Fungsi Keanggotaan Variabel: {var_name}'
        )
        plt.xlabel(
            f"{var_name} ({var_info['unit']})"
        )
        plt.ylabel(
            'Derajat Keanggotaan (μ)'
        )
        plt.grid(
            True,
            linestyle='--',
            alpha=0.5
        )
        plt.legend()

        filename = os.path.join(
            output_dir,
            f"MF_{var_name.replace(' ', '_')}.png"
        )

        plt.savefig(
            filename,
            bbox_inches='tight'
        )

        plt.show()


if __name__ == '__main__':
    print(
        '=== MENAMPILKAN GRAFIK FUNGSI KEANGGOTAAN ==='
    )

    plot_variabel()

    print(
        '\n=== CONTOH PENGUJJIAN FUZZIFIKASI ==='
    )

    sampel_input = {
        'IPK': 3.40,
        'Aktivitas': 26.0
    }

    hasil_fuzzifikasi = fuzzifikasi(
        sampel_input
    )

    print(
        f'Input: {sampel_input}'
    )

    print(
        f'Hasil Fuzzifikasi: {hasil_fuzzifikasi}'
    )
```

### 4.2 Penjelasan Modul & Struktur Data

- **Modularitas Fungsi (`trimf` & `trapmf`)**: Menggunakan perhitungan array NumPy murni tanpa bergantung pada *black-box library fuzzy*.
- **Kamus `MODEL_FUZZY`**: Menampung struktur data semesta pembicaraan, satuan, jenis kurva, dan koordinat parameter secara rapi.
- **Fungsi `fuzzifikasi()`**: Fungsi utama yang menerima masukan numerik IPK dan Aktivitas, lalu menghasilkan dictionary derajat keanggotaan (μ).
- **Fungsi `plot_variabel()`**: Melakukan rendering visual grafik fungsi keanggotaan menggunakan Matplotlib dan memanggil `plt.show()` agar grafik langsung tampil di layar monitor/Jupyter Notebook.

---

## 5. HASIL PENGUJIAN & EVALUASI FUZZIFIKASI

### 5.1 Tabel Pengujian 5 Skenario

| No | Kasus Uji | Input 1 (IPK) | Input 2 (Aktivitas) | Derajat Keanggotaan Input 1 (IPK) | Derajat Keanggotaan Input 2 (Aktivitas) | Analisis Awal |
|---:|---|---:|---:|---|---|---|
| 1 | Ekstrem Bawah | 1.80 | 35.0 jam | Rendah: 1.0000; Sedang: 0.0000; Tinggi: 0.0000 | Lengang: 0.0000; Moderat: 0.0000; Padat: 1.0000 | IPK rendah dengan tingkat kesibukan sangat tinggi. |
| 2 | Transisi Bawah | 2.60 | 14.0 jam | Rendah: 0.2000; Sedang: 0.2000; Tinggi: 0.0000 | Lengang: 0.2500; Moderat: 0.2500; Padat: 0.0000 | Terjadi persinggungan Rendah–Sedang & Lengang–Moderat. |
| 3 | Kondisi Normal | 3.00 | 20.0 jam | Rendah: 0.0000; Sedang: 1.0000; Tinggi: 0.0000 | Lengang: 0.0000; Moderat: 1.0000; Padat: 0.0000 | Akademik dan kesibukan berada di kondisi ideal. |
| 4 | Transisi Atas | 3.40 | 26.0 jam | Rendah: 0.0000; Sedang: 0.2000; Tinggi: 0.3000 | Lengang: 0.0000; Moderat: 0.2500; Padat: 0.2500 | Terjadi persinggungan Sedang–Tinggi & Moderat–Padat. |
| 5 | Ekstrem Atas | 3.90 | 5.0 jam | Rendah: 0.0000; Sedang: 0.0000; Tinggi: 1.0000 | Lengang: 1.0000; Moderat: 0.0000; Padat: 0.0000 | Mahasiswa berprestasi tinggi dengan waktu luang sangat banyak. |

### 5.2 Interpretasi Hasil Derajat Keanggotaan

#### 1) Kasus 1 (Ekstrem Bawah)

IPK 1.80 dan Aktivitas 35.0 jam berada di daerah plato, memberikan nilai mutlak:

\[
\mu_{\text{Rendah}}=1.0000
\]

\[
\mu_{\text{Padat}}=1.0000
\]

#### 2) Kasus 2 (Transisi Bawah)

IPK 2.60 berada pada area overlap.

\[
\mu_{\text{Rendah}}
=
\frac{2.75-2.60}{0.75}
=
0.2000
\]

\[
\mu_{\text{Sedang}}
=
\frac{2.60-2.50}{0.50}
=
0.2000
\]

Aktivitas 14.0 jam menghasilkan:

\[
\mu_{\text{Lengang}}=0.2500
\]

\[
\mu_{\text{Moderat}}=0.2500
\]

#### 3) Kasus 3 (Kondisi Normal)

IPK 3.00 dan Aktivitas 20.0 jam tepat menyentuh titik puncak segitiga, sehingga:

\[
\mu_{\text{Sedang}}=1.0000
\]

\[
\mu_{\text{Moderat}}=1.0000
\]

#### 4) Kasus 4 (Transisi Atas)

IPK 3.40 memberikan:

\[
\mu_{\text{Sedang}}
=
\frac{3.50-3.40}{0.50}
=
0.2000
\]

\[
\mu_{\text{Tinggi}}
=
\frac{3.40-3.25}{0.50}
=
0.3000
\]

Aktivitas 26.0 jam memicu persinggungan Moderat–Padat:

\[
\mu_{\text{Moderat}}=0.2500
\]

\[
\mu_{\text{Padat}}=0.2500
\]

#### 5) Kasus 5 (Ekstrem Atas)

IPK 3.90 dan Aktivitas 5.0 jam memberikan derajat keanggotaan mutlak:

\[
\mu_{\text{Tinggi}}=1.0000
\]

\[
\mu_{\text{Lengang}}=1.0000
\]

---

## 6. KESIMPULAN & RENCANA PENGEMBANGAN MODUL 2

### a. Kesimpulan

Pemodelan Fuzzy Sistem Rekomendasi Beban SKS berhasil dibangun dengan 2 input (IPK & Aktivitas) serta 1 output (Rekomendasi SKS).

- Perancangan Kurva Keanggotaan memenuhi kriteria teknis dengan *overlapping* tanpa *gap*.
- Implementasi Fungsi Python murni sukses melakukan fuzzifikasi pada 5 skenario sampel secara presisi dan mampu menampilkan grafik secara otomatis.

### b. Rencana Pengembangan Modul 2

- Menyusun 9 basis aturan (*rule base*) berlogika AND yang menghubungkan kombinasi IPK dan Aktivitas ke variabel Rekomendasi SKS.
- Mengimplementasikan mesin inferensi Mamdani (Min-Max Aggregation).
- Menerapkan perhitungan defuzzifikasi (Centroid) untuk menghasilkan rekomendasi tegas jumlah SKS.
