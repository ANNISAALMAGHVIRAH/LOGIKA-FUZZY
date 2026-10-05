# LAPORAN ASESMEN MODUL 1

# PEMODELAN FUZZY

**Annisa Almaghvirah**  
**NIM: 240306037**  
GitHub: https://github.com/ANNISAALMAGHVIRAH

Program Studi Teknologi Informasi  
Fakultas Dakwah dan Ilmu Komunikasi  
Universitas Islam Negeri Mataram  
2026

---

## 1. JUDUL PROYEK & IDENTITAS MAHASISWA

Proyek ini berjudul **"Sistem Rekomendasi Beban SKS Mahasiswa Berdasarkan IPK dan Aktivitas Non-Akademik"**. Pemodelan fuzzy digunakan untuk menentukan batas rekomendasi jumlah Kredit Semester (SKS) mahasiswa secara adaptif dan kontinyu tanpa menggunakan pembatasan kaku (*rigid threshold*).

| Komponen | Keterangan |
|---|---|
| Nama | Annisa Almaghvirah |
| Nim | 240306037 |
| Topik | Sistem Rekomendasi Beban SKS Mahasiswa |
| Input 1 | IPK (Indeks Prestasi Kumulatif, skala 0.00–4.00) |
| Input 2 | Aktivitas Non-Akademik (Jam/Minggu) |
| Output | Rekomendasi Beban SKS (SKS) |
| Label Input 1 | Rendah, Sedang, Tinggi |
| Label Input 2 | Lengang, Moderat, Padat |
| Label Output | Minimal, Sedang, Maksimal |
| Implementasi | Python / NumPy / Matplotlib |

## 2. LATAR BELAKANG & DESKRIPSI PERMASALAHAN

Penentuan beban studi (jumlah SKS) yang ideal bagi seorang mahasiswa berpengaruh signifikan terhadap keberhasilan akademiknya. Pada sistem informasi akademik konvensional, penentuan jatah SKS umumnya hanya didasarkan pada Indeks Prestasi Kumulatif (IPK) secara kaku (misalnya: IPK otomatis mendapatkan jatah 24 SKS).

Namun, pendekatan tersebut mengabaikan variabel riil lain seperti tingkat kesibukan atau Aktivitas Non-Akademik (organisasi, kerja paruh waktu, maupun kepanitiaan). Mahasiswa dengan IPK 3.80 yang memiliki tingkat aktivitas 35 jam/minggu berisiko mengalami burnout jika dipaksa mengambil 24 SKS, sedangkan pembatasan kaku sering kali tidak adil pada nilai perbatasan (contoh: IPK 2.99 vs 3.00).

Logika Fuzzy hadir untuk memetakan nilai konkret masukan ke dalam derajat keanggotaan (μ). Proyek Tahap 1 (Pemodelan Fuzzy) ini berfokus pada formulasi variabel linguistik, perancangan fungsi keanggotaan, pembuatan skrip Python murni, serta pengujian fuzzifikasi pada 5 skenario kondisi riil mahasiswa.

## 3. PERANCANGAN SISTEM FUZZY

### 3.1 Semesta Pembicaraan dan Domain Variabel

| Jenis Variabel | Nama Variabel | Satuan | Semesta Pembicaraan | Daftar Label Linguistik | Parameter Kurva |
|---|---|---|---|---|---|
| Input 1 | IPK | Skala | 0.00–4.00 | Rendah, Sedang, Tinggi | Rendah: (0.0, 0.0, 2.0, 2.75); Sedang: (2.5, 3.0, 3.5); Tinggi: (3.25, 3.75, 4.0, 4.0) |
| Input 2 | Aktivitas | Jam/Minggu | 0–40 | Lengang, Moderat, Padat | Lengang: (0, 0, 8, 16); Moderat: (12, 20, 28); Padat: (24, 32, 40, 40) |
| Output | Rekomendasi | SKS | 12–24 | Minimal, Sedang, Maksimal | Minimal: (12, 12, 14, 17); Sedang: (15, 18, 21); Maksimal: (19, 22, 24, 24) |

### 3.2 Penurunan Matematis Fungsi Keanggotaan

Fungsi keanggotaan dirancang menggunakan kombinasi kurva trapesium bahu kiri/kanan (trapmf) dan kurva segitiga (trimf).

#### 1. IPK (x)

**1) Label Rendah (Trapesium Bahu Kiri [0.0, 0.0, 2.0, 2.75])**

**μ Rendah (x) =**

⎧ 1, jika x ≤ 2.0  
⎪ (2.75 − x) / (2.75 − 2.0), jika 2.0 < x < 2.75  
⎩ 0, jika x ≥ 2.75

**2) Label Sedang (Segitiga [2.5, 3.0, 3.5])**

**μ Sedang (x) =**

⎧ 0, jika x ≤ 2.5 atau x ≥ 3.5  
⎪ (x − 2.5) / (3.0 − 2.5), jika 2.5 < x ≤ 3.0  
⎩ (3.5 − x) / (3.5 − 3.0), jika 3.0 < x < 3.5

**3) Label Tinggi (Trapesium Bahu Kanan [3.25, 3.75, 4.0, 4.0])**

**μ Tinggi (x) =**

⎧ 0, jika x ≤ 3.25  
⎪ (x − 3.25) / (3.75 − 3.25), jika 3.25 < x < 3.75  
⎩ 1, jika x ≥ 3.75

#### 2. Aktivitas Non-Akademik (y)

**1) Label Lengang (Trapesium Bahu Kiri [0, 0, 8, 16])**

**μ Lengang (y) =**

⎧ 1, jika y ≤ 8  
⎪ (16 − y) / (16 − 8), jika 8 < y < 16  
⎩ 0, jika y ≥ 16

**2) Label Moderat (Segitiga [12, 20, 28])**

**μ Moderat (y) =**

⎧ 0, jika y ≤ 12 atau y ≥ 28  
⎪ (y − 12) / (20 − 12), jika 12 < y ≤ 20  
⎩ (28 − y) / (28 − 20), jika 20 < y < 28

**3) Label Padat (Trapesium Bahu Kanan [24, 32, 40, 40])**

**μ Padat (y) =**

⎧ 0, jika y ≤ 24  
⎪ (y − 24) / (32 − 24), jika 24 < y < 32  
⎩ 1, jika y ≥ 32

#### 3. Rekomendasi SKS (z)

**a) Label Minimal (Trapesium Bahu Kiri [12, 12, 14, 17])**

**μ Minimal (z) =**

⎧ 1, jika z ≤ 14  
⎪ (17 − z) / (17 − 14), jika 14 < z < 17  
⎩ 0, jika z ≥ 17

**b) Label Sedang (Segitiga [15, 18, 21])**

**μ Sedang (z) =**

⎧ 0, jika z ≤ 15 atau z ≥ 21  
⎪ (z − 15) / (18 − 15), jika 15 < z ≤ 18  
⎩ (21 − z) / (21 − 18), jika 18 < z < 21

**c) Label Maksimal (Trapesium Bahu Kanan [19, 22, 24, 24])**

**μ Maksimal (z) =**

⎧ 0, jika z ≤ 19  
⎪ (z − 19) / (22 − 19), jika 19 < z < 22  
⎩ 1, jika z ≥ 22

### 3.3 Ilustrasi Grafik Desain

Seluruh kurva bersebelahan saling bersinggungan (*overlap*) tanpa celah (*gap*).

- Variabel IPK: Overlap Rendah–Sedang berada pada rentang **2.50–2.75**, dan Sedang–Tinggi pada rentang **3.25–3.50**.
- Variabel Aktivitas: Overlap Lengang–Moderat berada pada rentang **12–16 jam/minggu**, dan Moderat–Padat pada rentang **24–28 jam/minggu**.
- Variabel Rekomendasi SKS: Overlap Minimal–Sedang berada pada rentang **15–17 SKS**, dan Sedang–Maksimal pada rentang **19–21 SKS**.

> Grafik fungsi keanggotaan pada laporan Word menggunakan `matplotlib` dari source code pada Bagian 4. Grafik tersebut tidak saya ubah nilainya atau parameternya.

## 4. IMPLEMENTASI PYTHON

### 4.1 Source Code Lengkap

```python
import os
import matplotlib.pyplot as plt
import numpy as np

# ===================================================================
# ASESMEN MODUL 1: PEMODELAN FUZZY
# Sistem Rekomendasi Beban SKS Mahasiswa
# Nama : Annisa Almaghvirah
# NIM : 240306037
# ===================================================================

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
        y[idx2] = np.maximum(y[idx2], (c - x[idx2]) / (c - b))
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
        y[idx2] = np.maximum(y[idx2], (d - x[idx2]) / (d - c))
    return np.clip(y, 0.0, 1.0)

# Dictionary Model Fuzzy
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
    """Fungsi pemetaan nilai masukan konkret ke derajat
    keanggotaan."""
    hasil = {}
    for var_name, nilai in input_dict.items():
        if var_name in MODEL_FUZZY:
            hasil[var_name] = {}
            for label, (tipe_kurva, params) in MODEL_FUZZY[var_name][
                'membership'
            ].items():
                deg = hitung_derajat(tipe_kurva, params, nilai)
                hasil[var_name][label] = round(deg, 4)
    return hasil

def plot_variabel(output_dir='.'):
    """Menyimpan dan MENAMPILKAN grafik fungsi keanggotaan."""
    os.makedirs(output_dir, exist_ok=True)
    for var_name, var_info in MODEL_FUZZY.items():
        x_min, x_max = var_info['semesta']
        x = np.linspace(x_min, x_max, 500)
        plt.figure(figsize=(8, 4), dpi=100)
        for label, (tipe_kurva, params) in var_info['membership'].items():
            if tipe_kurva == 'trimf':
                y = trimf(x, params)
            elif tipe_kurva == 'trapmf':
                y = trapmf(x, params)
            plt.plot(x, y, linewidth=2, label=label)
        plt.title(f'Fungsi Keanggotaan Variabel: {var_name}')
        plt.xlabel(f"{var_name} ({var_info['unit']})")
        plt.ylabel('Derajat Keanggotaan (μ)')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend()
        filename = os.path.join(output_dir, f"MF_{var_name.replace(' ', '_')}.png")
        plt.savefig(filename, bbox_inches='tight')
        # Menampilkan grafik langsung ke layar
        plt.show()

# Menjalankan fungsi untuk menampilkan grafik dan pengujian
if __name__ == '__main__':
    print('=== MENAMPILKAN GRAFIK FUNGSI KEANGGOTAAN ===')
    plot_variabel()
    print('\n=== CONTOH PENGUJJIAN FUZZIFIKASI ===')
    sampel_input = {'IPK': 3.40, 'Aktivitas': 26.0}
    hasil_fuzzifikasi = fuzzifikasi(sampel_input)
    print(f'Input: {sampel_input}')
    print(f'Hasil Fuzzifikasi: {hasil_fuzzifikasi}')
```

### 4.2 Penjelasan Modul & Struktur Data

- **Modularitas Fungsi (trimf & trapmf):** Menggunakan perhitungan array NumPy murni tanpa bergantung pada black-box library fuzzy.
- **Kamus MODEL_FUZZY:** Menampung struktur data semesta pembicaraan, satuan, jenis kurva, dan koordinat parameter secara rapi.
- **Fungsi fuzzifikasi():** Fungsi utama yang menerima masukan numerik IPK dan Aktivitas, lalu menghasilkan dictionary derajat keanggotaan (μ).
- **Fungsi plot_variabel():** Melakukan rendering visual grafik fungsi keanggotaan menggunakan matplotlib dan memanggil plt.show() agar grafik langsung tampil di layar monitor/Jupyter Notebook.

## 5. HASIL PENGUJIAN & EVALUASI FUZZIFIKASI

### 5.1 Tabel Pengujian 5 Skenario

| No | Kasus Uji | Input 1 (IPK) | Input 2 (Aktivitas) | Derajat Keanggotaan Input 1 (IPK) | Derajat Keanggotaan Input 2 (Aktivitas) | Analisis Awal |
|---|---|---:|---:|---|---|---|
| 1 | Ekstrem Bawah | 1.80 | 35.0 jam | Rendah: 1.0000; Sedang: 0.0000; Tinggi: 0.0000 | Lengang: 0.0000; Moderat: 0.0000; Padat: 1.0000 | IPK rendah dengan tingkat kesibukan sangat tinggi. |
| 2 | Transisi Bawah | 2.60 | 14.0 jam | Rendah: 0.2000; Sedang: 0.2000; Tinggi: 0.0000 | Lengang: 0.2500; Moderat: 0.2500; Padat: 0.0000 | Terjadi persinggungan Rendah–Sedang & Lengang–Moderat. |
| 3 | Kondisi Normal | 3.00 | 20.0 jam | Rendah: 0.0000; Sedang: 1.0000; Tinggi: 0.0000 | Lengang: 0.0000; Moderat: 1.0000; Padat: 0.0000 | Akademik dan kesibukan berada di kondisi ideal. |
| 4 | Transisi Atas | 3.40 | 26.0 jam | Rendah: 0.0000; Sedang: 0.2000; Tinggi: 0.3000 | Lengang: 0.0000; Moderat: 0.2500; Padat: 0.2500 | Terjadi persinggungan Sedang–Tinggi & Moderat–Padat. |
| 5 | Ekstrem Atas | 3.90 | 5.0 jam | Rendah: 0.0000; Sedang: 0.0000; Tinggi: 1.0000 | Lengang: 1.0000; Moderat: 0.0000; Padat: 0.0000 | Mahasiswa berprestasi tinggi dengan waktu luang sangat banyak. |

### 5.2 Interpretasi Hasil Derajat Keanggotaan

1. **Kasus 1 (Ekstrem Bawah):** IPK 1.80 dan Aktivitas 35.0 jam berada di daerah plato, memberikan nilai mutlak **1.0000 pada label Rendah** dan **1.0000 pada label Padat**.

2. **Kasus 2 (Transisi Bawah):** IPK 2.60 berada pada area overlap, menghasilkan **μ Rendah = 0.2000** dan **μ Sedang = 0.2000**. Aktivitas 14.0 jam menghasilkan **μ Lengang = 0.2500** dan **μ Moderat = 0.2500**.

3. **Kasus 3 (Kondisi Normal):** IPK 3.00 dan Aktivitas 20.0 jam tepat menyentuh titik puncak segitiga (μ = 1.0000), bernilai mutlak pada label **Sedang** dan **Moderat**.

4. **Kasus 4 (Transisi Atas):** IPK 3.40 memberikan **μ Sedang = 0.2000** dan **μ Tinggi = 0.3000**. Aktivitas 26.0 jam memicu persinggungan Moderat–Padat masing-masing **0.2500**.

5. **Kasus 5 (Ekstrem Atas):** IPK 3.90 dan Aktivitas 5.0 jam memberikan derajat keanggotaan mutlak **μ Tinggi = 1.0000** dan **μ Lengang = 1.0000**.

## 6. KESIMPULAN & RENCANA PENGEMBANGAN MODUL 2

### a. Kesimpulan

Pemodelan Fuzzy Sistem Rekomendasi Beban Sks Berhasil Dibangun Dengan 2 Input (Ipk & Aktivitas) Serta 1 Output (Rekomendasi Sks).

- Perancangan Kurva Keanggotaan Memenuhi Kriteria Teknis Dengan Overlapping Tanpa Gap.
- Implementasi Fungsi Python Murni Sukses Melakukan Fuzzifikasi Pada 5 Skenario Sampel Secara Presisi Dan Mampu Menampilkan Grafik Secara Otomatis.

### b. Rencana Pengembangan Modul 2

- Menyusun 9 Basis Aturan (Rule Base) Berlogika And (∧) Yang Menghubungkan Kombinasi Ipk Dan Aktivitas Ke Variabel Rekomendasi Sks.
- Mengimplementasikan Mesin Inferensi Mamdani (Min-Max Aggregation).
- Menerapkan Perhitungan Defuzzifikasi (Centroid) Untuk Menghasilkan Rekomendasi Tegas Jumlah Sks (z).
