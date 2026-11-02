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
| Topik | Arsitektur Fuzzy Inference System (FIS) |
| Repository | LOGIKA-FUZZY/MODUL 2/Pertemuan 7 |
| Tanggal | 24 Oktober 2026 |

## B. Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa diharapkan mampu:

1. Memahami arsitektur lengkap dan empat komponen utama Fuzzy Inference System (FIS).
2. Menjelaskan aliran transformasi data dari nilai konkret (*crisp input*) menjadi derajat keanggotaan, evaluasi aturan, agregasi konsekuen, hingga keputusan konkret (*crisp output*).
3. Mengimplementasikan proses FIS secara modular menggunakan Python.
4. Memvisualisasikan setiap tahap komputasi inferensi fuzzy dalam bentuk grafik.
5. Menganalisis pengaruh agregasi konklusi terhadap bentuk daerah solusi fuzzy sebelum proses defuzzifikasi.

## C. Requirement

Perangkat dan aplikasi yang digunakan dalam praktikum ini adalah:

- **Sistem Operasi:** Windows 11 Home Single Language 64-bit (10.0, Build 26100).
- **Browser:** Google Chrome Version 130.0.6723.117 (Official Build) (64-bit).
- **Tools:** Visual Studio Code.
- **Bahasa Pemrograman:** Python.
- **Library:** NumPy dan Matplotlib.

## D. Dasar Teori

### 1. Arsitektur Empat Pilar Fuzzy Inference System

Fuzzy Inference System (FIS) merupakan sistem komputasi yang digunakan untuk mengolah nilai input menjadi output berdasarkan aturan fuzzy. FIS dapat menangani data yang memiliki nilai tidak pasti atau tidak selalu bernilai mutlak.

Secara umum, FIS memiliki empat komponen utama, yaitu:

1. **Basis Pengetahuan (Knowledge Base)**

   Berisi kumpulan fungsi keanggotaan dari setiap variabel dan aturan IF-THEN (*Rule Base*) yang digunakan sebagai dasar pengambilan keputusan.

2. **Unit Fuzzifikasi (Fuzzification Interface)**

   Mengubah nilai input tegas (*crisp input*) menjadi derajat keanggotaan pada himpunan fuzzy. Nilai derajat keanggotaan berada pada rentang 0 sampai 1.

3. **Mesin Inferensi (Inference Engine)**

   Melakukan evaluasi terhadap aturan fuzzy menggunakan operator logika, kemudian menerapkan proses implikasi dan agregasi untuk menggabungkan hasil dari aturan yang aktif.

4. **Unit Defuzzifikasi (Defuzzification Interface)**

   Mengubah hasil agregasi yang masih berbentuk fuzzy menjadi satu nilai tegas (*crisp output*). Salah satu metode yang dapat digunakan adalah Centroid.

### 2. Alur Komputasi Fuzzy Inference System

Secara sederhana, alur kerja FIS dapat digambarkan sebagai berikut:

```text
          INPUT CRISP
               |
               v
          FUZZIFIKASI
               |
               v
        KNOWLEDGE BASE
       (MF dan Rule Base)
               |
               v
        MESIN INFERENSI
       (Evaluasi Aturan)
               |
               v
           IMPLIKASI
               |
               v
           AGREGASI
               |
               v
         DEFUZZIFIKASI
               |
               v
          OUTPUT CRISP
```

Berdasarkan alur tersebut, nilai input yang awalnya berupa angka konkret diubah menjadi derajat keanggotaan. Selanjutnya, sistem mengevaluasi aturan fuzzy, menggabungkan hasil aturan yang aktif, dan menghasilkan nilai akhir melalui proses defuzzifikasi.

### 3. Contoh Kasus Perhitungan FIS

Pada praktikum ini digunakan contoh sistem rekomendasi diskon layanan TI. Sistem memiliki dua variabel input dan satu variabel output.

| Variabel | Nilai |
|---|---:|
| Lama Langganan | 15 bulan |
| Frekuensi Transaksi | 8 kali/bulan |
| Output | Besaran diskon (%) |

#### Tahap 1: Fuzzifikasi

Fuzzifikasi merupakan proses mengubah nilai input tegas menjadi derajat keanggotaan fuzzy.

Diketahui derajat keanggotaan lama langganan:

\[
\mu_{\text{Baru}}(15)=0
\]

\[
\mu_{\text{Lama}}(15)=0{,}75
\]

Untuk frekuensi transaksi:

\[
\mu_{\text{Jarang}}(8)=0{,}20
\]

\[
\mu_{\text{Sering}}(8)=0{,}80
\]

Berdasarkan nilai tersebut, pelanggan memiliki derajat keanggotaan sebesar 0,75 pada himpunan Lama dan 0,80 pada himpunan Sering. Nilai ini merupakan contoh derajat keanggotaan yang digunakan untuk menjelaskan proses perhitungan.

#### Tahap 2: Evaluasi Aturan dan Implikasi

Pada tahap ini, derajat keanggotaan input digunakan untuk menghitung kekuatan aturan (*firing strength*) menggunakan operator AND berupa minimum (MIN).

**Rule 1**

IF Lama Langganan Lama AND Frekuensi Jarang THEN Diskon Sedang.

\[
\begin{aligned}
\alpha_1 &= \min(0{,}75;0{,}20)\\
&=0{,}20
\end{aligned}
\]

Artinya, aturan pertama aktif dengan kekuatan 0,20. Fungsi keanggotaan Diskon Sedang dipotong pada ketinggian 0,20.

**Rule 2**

IF Lama Langganan Lama AND Frekuensi Sering THEN Diskon Besar.

\[
\begin{aligned}
\alpha_2 &= \min(0{,}75;0{,}80)\\
&=0{,}75
\end{aligned}
\]

Artinya, aturan kedua aktif dengan kekuatan 0,75. Fungsi keanggotaan Diskon Besar dipotong pada ketinggian 0,75.

#### Tahap 3: Agregasi dengan Operator MAX

Agregasi merupakan proses menggabungkan hasil implikasi dari seluruh aturan aktif menggunakan operator maksimum (MAX).

Rumus agregasi:

\[
\mu_{\text{Agg}}(z)=
\max\left(
\mu'_{\text{Sedang}}(z),
\mu'_{\text{Besar}}(z)
\right)
\]

Dengan:

\[
\mu'_{\text{Sedang}}(z)=
\min(0{,}20,\mu_{\text{Sedang}}(z))
\]

\[
\mu'_{\text{Besar}}(z)=
\min(0{,}75,\mu_{\text{Besar}}(z))
\]

Hasil dari proses tersebut adalah satu kurva fuzzy gabungan yang mencakup daerah Diskon Sedang dan Diskon Besar. Kurva gabungan inilah yang digunakan pada tahap defuzzifikasi.

#### Tahap 4: Defuzzifikasi dengan Metode Centroid

Defuzzifikasi bertujuan mengubah hasil agregasi fuzzy menjadi satu nilai diskon yang tegas.

Rumus centroid untuk data kontinu:

\[
z^*=
\frac{\int z\,\mu_{\text{Agg}}(z)\,dz}
{\int \mu_{\text{Agg}}(z)\,dz}
\]

Jika menggunakan sejumlah titik diskret, rumus pendekatannya adalah:

\[
z^*\approx
\frac{\sum_i z_i\mu_{\text{Agg}}(z_i)}
{\sum_i \mu_{\text{Agg}}(z_i)}
\]

Keterangan:

- \(z^*\) = nilai diskon akhir dalam persen.
- \(z_i\) = titik nilai diskon yang dihitung.
- \(\mu_{\text{Agg}}(z_i)\) = derajat keanggotaan hasil agregasi pada titik tersebut.

Dengan metode ini, hasil agregasi yang sebelumnya berbentuk kurva fuzzy dapat diubah menjadi satu angka yang dapat digunakan sebagai rekomendasi diskon.

## E. Implementasi Program Python

Pada bagian ini dibuat program Fuzzy Inference System menggunakan Python. Program terdiri dari fungsi keanggotaan segitiga dan trapesium, kelas FIS, proses fuzzifikasi, evaluasi aturan, implikasi, agregasi, dan defuzzifikasi.

### 1. Import Library

```python
import numpy as np
import matplotlib.pyplot as plt
```

Library NumPy digunakan untuk perhitungan numerik dan pengolahan array, sedangkan Matplotlib digunakan untuk membuat visualisasi grafik.

### 2. Fungsi Defuzzifikasi Centroid

```python
def defuzzifikasi_centroid(x_vals, mu_vals):
    total_mu = np.sum(mu_vals)

    if total_mu == 0:
        return 0.0

    return np.sum(x_vals * mu_vals) / total_mu
```

Fungsi tersebut digunakan untuk menghitung nilai crisp output menggunakan metode Centroid. Jika seluruh nilai agregasi bernilai nol, fungsi mengembalikan 0,0 sebagai penanganan dasar agar tidak terjadi pembagian dengan nol.

### 3. Fungsi Keanggotaan Segitiga dan Trapesium

```python
def trimf(x, params):
    a, b, c = params
    y = np.zeros_like(x, dtype=float)

    if b != a:
        idx = (x > a) & (x <= b)
        y[idx] = (x[idx] - a) / (b - a)

    if c != b:
        idx = (x > b) & (x < c)
        y[idx] = (c - x[idx]) / (c - b)

    y[x == b] = 1

    return np.clip(y, 0, 1)


def trapmf(x, params):
    a, b, c, d = params
    y = np.zeros_like(x, dtype=float)

    if b != a:
        idx = (x >= a) & (x < b)
        y[idx] = (x[idx] - a) / (b - a)

    idx = (x >= b) & (x <= c)
    y[idx] = 1

    if d != c:
        idx = (x > c) & (x <= d)
        y[idx] = (d - x[idx]) / (d - c)

    return np.clip(y, 0, 1)
```

Fungsi `trimf()` digunakan untuk membentuk fungsi keanggotaan segitiga, sedangkan `trapmf()` digunakan untuk membentuk fungsi keanggotaan trapesium. Kedua fungsi menghasilkan nilai derajat keanggotaan antara 0 sampai 1.

### 4. Membuat Kelas Fuzzy Inference System

```python
class FuzzyInferenceSystem:

    def __init__(self):
        self.input_variables = {}
        self.output_variable = None
        self.rules = []

    def add_input_variable(self, name, universe, mf_dict):
        self.input_variables[name] = {
            "universe": universe,
            "mf": mf_dict
        }

    def set_output_variable(self, name, universe, mf_dict):
        self.output_variable = {
            "name": name,
            "universe": universe,
            "mf": mf_dict
        }

    def add_rule(self, rule_tuple):
        self.rules.append(rule_tuple)

    def compute_details(self, input_values_dict):

        # Fuzzifikasi
        memberships = {}

        for name, value in input_values_dict.items():
            variable = self.input_variables[name]

            memberships[name] = {
                label: np.interp(
                    value,
                    variable["universe"],
                    mf
                )
                for label, mf in variable["mf"].items()
            }

        # Implikasi dan agregasi
        output = self.output_variable
        universe = output["universe"]

        aggregated = np.zeros_like(universe)
        firing_strengths = []

        for lama_set, frekuensi_set, diskon_set in self.rules:

            alpha = min(
                memberships["Lama Langganan"][lama_set],
                memberships["Frekuensi Transaksi"][frekuensi_set]
            )

            firing_strengths.append(alpha)

            # Implikasi Mamdani MIN
            implied = np.minimum(
                alpha,
                output["mf"][diskon_set]
            )

            # Agregasi MAX
            aggregated = np.maximum(
                aggregated,
                implied
            )

        # Memeriksa hasil agregasi
        if np.sum(aggregated) == 0:
            raise ValueError(
                "Tidak ada aturan fuzzy yang aktif!"
            )

        # Defuzzifikasi Centroid
        crisp_output = defuzzifikasi_centroid(
            universe,
            aggregated
        )

        return crisp_output, firing_strengths, aggregated

    def compute(self, input_values_dict):
        crisp_output, _, _ = self.compute_details(
            input_values_dict
        )

        return crisp_output
```

Kelas `FuzzyInferenceSystem` digunakan untuk menggabungkan seluruh proses FIS. Metode `add_input_variable()` digunakan untuk menambahkan variabel input, `set_output_variable()` untuk menentukan variabel output, dan `add_rule()` untuk menambahkan aturan fuzzy.

Metode `compute_details()` menjalankan proses fuzzifikasi, evaluasi aturan, implikasi, agregasi, dan defuzzifikasi. Sementara itu, metode `compute()` digunakan untuk mengambil hasil crisp output.

### 5. Menentukan Domain dan Fungsi Keanggotaan

```python
universe_lama = np.linspace(0, 24, 241)
universe_frekuensi = np.linspace(0, 15, 151)
universe_diskon = np.linspace(0, 30, 301)

mf_lama = {
    "Pendek": trapmf(universe_lama, [0, 0, 3, 9]),
    "Sedang": trimf(universe_lama, [3, 12, 21]),
    "Lama": trapmf(universe_lama, [15, 21, 24, 24])
}

mf_frekuensi = {
    "Rendah": trapmf(universe_frekuensi, [0, 0, 2, 6]),
    "Sedang": trimf(universe_frekuensi, [3, 7.5, 12]),
    "Tinggi": trapmf(universe_frekuensi, [9, 13, 15, 15])
}

mf_diskon = {
    "Rendah": trapmf(universe_diskon, [0, 0, 5, 12]),
    "Sedang": trimf(universe_diskon, [8, 15, 22]),
    "Tinggi": trapmf(universe_diskon, [18, 25, 30, 30])
}
```

Bagian ini menentukan domain atau rentang nilai untuk setiap variabel. Lama langganan memiliki rentang 0–24 bulan, frekuensi transaksi memiliki rentang 0–15 kali, dan diskon memiliki rentang 0–30 persen.

Setiap variabel kemudian dibagi menjadi beberapa himpunan fuzzy menggunakan fungsi keanggotaan segitiga dan trapesium.

### 6. Membuat Sistem dan Menambahkan Aturan

```python
fis = FuzzyInferenceSystem()

fis.add_input_variable(
    "Lama Langganan",
    universe_lama,
    mf_lama
)

fis.add_input_variable(
    "Frekuensi Transaksi",
    universe_frekuensi,
    mf_frekuensi
)

fis.set_output_variable(
    "Diskon",
    universe_diskon,
    mf_diskon
)

rules = [
    ("Pendek", "Rendah", "Rendah"),
    ("Pendek", "Sedang", "Rendah"),
    ("Pendek", "Tinggi", "Sedang"),
    ("Sedang", "Rendah", "Rendah"),
    ("Sedang", "Sedang", "Sedang"),
    ("Sedang", "Tinggi", "Tinggi"),
    ("Lama", "Rendah", "Sedang"),
    ("Lama", "Sedang", "Tinggi"),
    ("Lama", "Tinggi", "Tinggi")
]

for rule in rules:
    fis.add_rule(rule)
```

Pada bagian ini dibuat objek FIS, kemudian ditambahkan dua variabel input dan satu variabel output. Selanjutnya, dimasukkan sembilan aturan fuzzy yang menghubungkan kondisi lama langganan dan frekuensi transaksi dengan kategori diskon.

### 7. Menjalankan Proses FIS

```python
input_pengujian = {
    "Lama Langganan": 12,
    "Frekuensi Transaksi": 6
}

crisp = fis.compute(input_pengujian)

_, firing, agregasi = fis.compute_details(
    input_pengujian
)

print("HASIL PIPELINE FUZZY INFERENCE SYSTEM")
print("=" * 45)

for i, alpha in enumerate(firing, start=1):
    print(f"R{i}: α = {alpha:.4f}")

print("-" * 45)

print(f"Nilai Crisp Output : {crisp:.2f}%")
print(f"Rekomendasi Diskon : {crisp:.2f}%")
```

Bagian ini menjalankan proses FIS menggunakan input lama langganan 12 bulan dan frekuensi transaksi 6 kali. Program menampilkan nilai firing strength dari sembilan aturan serta nilai akhir diskon yang diperoleh melalui metode Centroid.

### 8. Visualisasi Implikasi, Agregasi, dan Centroid

```python
z = universe_diskon

plt.figure(figsize=(12, 6))

plt.plot(
    z,
    mf_diskon["Rendah"],
    'g--',
    label='Diskon Rendah',
    alpha=0.6
)

plt.plot(
    z,
    mf_diskon["Sedang"],
    'b--',
    label='Diskon Sedang',
    alpha=0.6
)

plt.plot(
    z,
    mf_diskon["Tinggi"],
    'r--',
    label='Diskon Tinggi',
    alpha=0.6
)

plt.fill_between(
    z,
    0,
    agregasi,
    color='purple',
    alpha=0.35,
    label='Daerah Agregasi Fuzzy'
)

plt.plot(
    z,
    agregasi,
    color='purple',
    linewidth=2.5
)

plt.axvline(
    x=crisp,
    color='black',
    linewidth=2.5,
    label=f'Centroid = {crisp:.2f}%'
)

plt.scatter(
    [crisp],
    [0],
    color='black',
    s=80,
    zorder=6
)

plt.title(
    'Pipeline FIS: Implikasi, Agregasi, dan Defuzzifikasi Centroid',
    fontsize=13,
    fontweight='bold'
)

plt.xlabel('Besaran Diskon (%)', fontsize=11)
plt.ylabel('Derajat Keanggotaan μ(z)', fontsize=11)

plt.xlim(0, 30)
plt.ylim(-0.05, 1.05)

plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', fontsize=10)

plt.tight_layout()

plt.savefig(
    'pipeline_fis_agregasi_defuzzifikasi.png',
    dpi=300
)

plt.show()
```

Kode tersebut digunakan untuk menampilkan grafik fungsi keanggotaan diskon Rendah, Sedang, dan Tinggi. Daerah hasil agregasi ditampilkan menggunakan warna ungu, sedangkan garis vertikal menunjukkan posisi nilai centroid atau hasil akhir defuzzifikasi.

### 9. Menampilkan Kesimpulan Hasil Sistem

```python
print("\nKeputusan Akhir Sistem FIS:")
print(f"Rekomendasi Diskon: {crisp:.2f}%")
```

Bagian terakhir menampilkan kembali nilai rekomendasi diskon sebagai hasil akhir dari proses Fuzzy Inference System.

## F. Tugas Praktikum 7

### Menggabungkan Fuzzifikasi, Evaluasi Aturan, dan Defuzzifikasi Menjadi Satu Fungsi Utuh

Pada tugas ini, seluruh tahapan FIS digabungkan ke dalam satu sistem menggunakan kelas `FuzzyInferenceSystem`. Sistem menerima nilai input, melakukan fuzzifikasi, mengevaluasi sembilan aturan, menjalankan implikasi MIN, menggabungkan hasil menggunakan MAX, dan menghasilkan nilai akhir dengan metode Centroid.

Program kemudian diuji menggunakan tiga kombinasi input yang berbeda.

### 1. Menentukan Tiga Kasus Pengujian

```python
kasus = [
    {"Lama Langganan": 3, "Frekuensi Transaksi": 2},
    {"Lama Langganan": 12, "Frekuensi Transaksi": 6},
    {"Lama Langganan": 24, "Frekuensi Transaksi": 15}
]
```

Ketiga kasus tersebut digunakan untuk mengetahui perbedaan hasil diskon berdasarkan kondisi lama langganan dan frekuensi transaksi.

### 2. Menjalankan Pengujian dan Membuat Grafik

```python
for nomor, data in enumerate(kasus, start=1):

    crisp = fis.compute(data)

    _, firing, aggregated = fis.compute_details(data)

    lama = data["Lama Langganan"]
    frekuensi = data["Frekuensi Transaksi"]

    fig, ax = plt.subplots(2, 2, figsize=(14, 9))

    fig.suptitle(
        f"FIS Mamdani - Pengujian Kasus {nomor}",
        fontsize=15,
        fontweight="bold"
    )

    # Grafik 1: Lama Langganan
    for label, mf in mf_lama.items():
        ax[0, 0].plot(
            universe_lama, mf,
            label=label, linewidth=2
        )

    ax[0, 0].axvline(
        lama, color="red", linestyle="--",
        label=f"Input = {lama}"
    )

    ax[0, 0].set_title("Variabel Input: Lama Langganan")
    ax[0, 0].set_xlabel("Lama Langganan (bulan)")
    ax[0, 0].set_ylabel("Derajat Keanggotaan")
    ax[0, 0].set_ylim(0, 1.1)
    ax[0, 0].grid(True, alpha=0.4)
    ax[0, 0].legend()

    # Grafik 2: Frekuensi Transaksi
    for label, mf in mf_frekuensi.items():
        ax[0, 1].plot(
            universe_frekuensi, mf,
            label=label, linewidth=2
        )

    ax[0, 1].axvline(
        frekuensi, color="red", linestyle="--",
        label=f"Input = {frekuensi}"
    )

    ax[0, 1].set_title("Variabel Input: Frekuensi Transaksi")
    ax[0, 1].set_xlabel("Frekuensi Transaksi (kali)")
    ax[0, 1].set_ylabel("Derajat Keanggotaan")
    ax[0, 1].set_ylim(0, 1.1)
    ax[0, 1].grid(True, alpha=0.4)
    ax[0, 1].legend()

    # Grafik 3: Output, Agregasi, dan Centroid
    for label, mf in mf_diskon.items():
        ax[1, 0].plot(
            universe_diskon, mf,
            linestyle="--", alpha=0.5,
            label=f"MF {label}"
        )

    ax[1, 0].fill_between(
        universe_diskon, 0, aggregated,
        color="green", alpha=0.35,
        label="Agregasi MAX"
    )

    ax[1, 0].plot(
        universe_diskon, aggregated,
        color="green", linewidth=2
    )

    ax[1, 0].axvline(
        crisp, color="black", linewidth=2.5,
        label=f"Centroid = {crisp:.2f}%"
    )

    ax[1, 0].set_title("Output Diskon dan Daerah Agregasi")
    ax[1, 0].set_xlabel("Besaran Diskon (%)")
    ax[1, 0].set_ylabel("Derajat Keanggotaan")
    ax[1, 0].set_xlim(0, 30)
    ax[1, 0].set_ylim(0, 1.1)
    ax[1, 0].grid(True, alpha=0.4)
    ax[1, 0].legend(fontsize=8)

    # Grafik 4: Firing Strength
    ax[1, 1].bar(
        range(1, 10),
        firing,
        color="seagreen"
    )

    ax[1, 1].set_title("Nilai Firing Strength (α) Tiap Aturan")
    ax[1, 1].set_xlabel("Nomor Aturan")
    ax[1, 1].set_ylabel("Nilai Firing Strength")
    ax[1, 1].set_xticks(range(1, 10))
    ax[1, 1].set_ylim(0, 1.1)
    ax[1, 1].grid(axis="y", alpha=0.4)

    for i, nilai in enumerate(firing):
        ax[1, 1].text(
            i + 1, nilai + 0.025,
            f"{nilai:.2f}",
            ha="center", fontsize=8
        )

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    plt.savefig(
        f"hasil_kasus_{nomor}.png",
        dpi=300
    )

    plt.show()

    # Menampilkan hasil pengujian
    print("=" * 55)
    print(f"HASIL PENGUJIAN KASUS {nomor}")
    print(f"Lama Langganan      : {lama} bulan")
    print(f"Frekuensi Transaksi : {frekuensi} kali")
    print(f"Diskon              : {crisp:.2f}%")
    print("\nNilai Firing Strength:")

    for i, alpha in enumerate(firing, start=1):
        print(f"R{i}: α = {alpha:.4f}")

print("=" * 55)
print("SELURUH PENGUJIAN SELESAI")
```

Program melakukan pengujian secara berulang untuk setiap kasus. Pada setiap pengujian, program menampilkan empat grafik, yaitu fungsi keanggotaan lama langganan, fungsi keanggotaan frekuensi transaksi, daerah agregasi dan centroid, serta nilai firing strength dari setiap aturan.

## G. Hasil Pengujian

Pengujian dilakukan menggunakan tiga kombinasi input yang sudah ditentukan dalam instruksi praktikum.

### 1. Hasil Pengujian Setiap Kasus

| Kasus | Lama Langganan | Frekuensi Transaksi | Hasil Diskon |
|---|---:|---:|---:|
| 1 | 3 bulan | 2 kali | 4,46% |
| 2 | 12 bulan | 6 kali | 15,00% |
| 3 | 24 bulan | 15 kali | 25,54% |

Hasil tersebut diperoleh menggunakan metode Centroid diskrit pada domain diskon 0–30 dengan 301 titik sampel.

### 2. Hasil Firing Strength

Berdasarkan fungsi keanggotaan dan aturan yang digunakan, nilai firing strength setiap kasus adalah sebagai berikut.

**Kasus 1: Lama Langganan 3 Bulan dan Frekuensi 2 Kali**

| Aturan | Nilai α |
|---|---:|
| R1 | 1,0000 |
| R2–R9 | 0,0000 |

Aturan pertama aktif karena kedua input memiliki derajat keanggotaan 1 pada himpunan Pendek dan Rendah.

**Kasus 2: Lama Langganan 12 Bulan dan Frekuensi 6 Kali**

| Aturan | Nilai α |
|---|---:|
| R1 | 0,0000 |
| R2 | 0,0000 |
| R3 | 0,0000 |
| R4 | 0,0000 |
| R5 | 0,6667 |
| R6 | 0,0000 |
| R7 | 0,0000 |
| R8 | 0,0000 |
| R9 | 0,0000 |

Pada kasus kedua, aturan kelima menjadi aturan yang aktif dengan nilai firing strength sekitar 0,6667. Hal ini terjadi karena lama langganan berada pada himpunan Sedang dengan derajat keanggotaan 1, sedangkan frekuensi transaksi memiliki derajat keanggotaan sekitar 0,6667 pada himpunan Rendah dan Sedang.

**Kasus 3: Lama Langganan 24 Bulan dan Frekuensi 15 Kali**

| Aturan | Nilai α |
|---|---:|
| R1–R8 | 0,0000 |
| R9 | 1,0000 |

Aturan kesembilan aktif dengan nilai firing strength 1 karena kedua input memiliki derajat keanggotaan 1 pada himpunan Lama dan Tinggi.

## H. Analisis Hasil

Berdasarkan hasil pengujian, terdapat perbedaan nilai diskon pada setiap kombinasi input.

Pada kasus pertama, pelanggan memiliki lama langganan 3 bulan dan frekuensi transaksi sebanyak 2 kali. Kedua input tersebut termasuk dalam himpunan Pendek dan Rendah dengan derajat keanggotaan 1. Aturan yang aktif adalah R1, sehingga sistem menghasilkan rekomendasi diskon sebesar 4,46%.

Pada kasus kedua, pelanggan memiliki lama langganan 12 bulan dan frekuensi transaksi sebanyak 6 kali. Lama langganan termasuk dalam himpunan Sedang dengan derajat keanggotaan 1. Sementara itu, frekuensi transaksi memiliki derajat keanggotaan sekitar 0,6667 pada himpunan Rendah dan Sedang. Aturan yang aktif adalah R5 dengan nilai firing strength sekitar 0,6667. Sistem menghasilkan diskon sebesar 15,00%.

Pada kasus ketiga, pelanggan memiliki lama langganan 24 bulan dan frekuensi transaksi sebanyak 15 kali. Kedua input termasuk dalam himpunan Lama dan Tinggi dengan derajat keanggotaan 1. Aturan yang aktif adalah R9, sehingga sistem menghasilkan rekomendasi diskon sebesar 25,54%.

Dari ketiga pengujian tersebut, terlihat bahwa semakin lama pelanggan berlangganan dan semakin sering melakukan transaksi, semakin besar diskon yang direkomendasikan oleh sistem. Hasil ini sesuai dengan aturan fuzzy yang telah dibuat.

## I. Pertanyaan Analisis

### 1. Mengapa FIS memerlukan tahap defuzzifikasi? Mengapa sistem kontrol atau pengambil keputusan tidak dapat langsung menggunakan fungsi keanggotaan agregasi fuzzy?

**Jawaban:**

FIS memerlukan tahap defuzzifikasi karena hasil dari proses agregasi masih berbentuk himpunan fuzzy atau derajat keanggotaan, bukan satu angka pasti. Sementara itu, sistem kontrol atau pengambil keputusan membutuhkan nilai yang jelas agar dapat digunakan untuk menentukan suatu keputusan. Oleh karena itu, defuzzifikasi digunakan untuk mengubah hasil fuzzy menjadi nilai crisp atau nilai tegas.

### 2. Apa perbedaan utama antara metode implikasi Clipping (Min) dan Scaling (Product)? Bagaimana pengaruh masing-masing terhadap bentuk kurva agregasi?

**Jawaban:**

Perbedaannya terletak pada cara mengubah fungsi keanggotaan output berdasarkan nilai firing strength (\(\alpha\)).

- **Clipping (Min):** Menggunakan nilai minimum antara \(\alpha\) dan derajat keanggotaan output. Bagian kurva yang memiliki nilai lebih tinggi dari \(\alpha\) akan terpotong rata pada tingkat tersebut.
- **Scaling (Product):** Mengalikan seluruh derajat keanggotaan output dengan nilai \(\alpha\). Akibatnya, tinggi kurva akan mengecil secara proporsional, tetapi bentuk asli kurva tetap dipertahankan.

Jadi, metode Clipping menghasilkan kurva dengan bagian atas yang terpotong, sedangkan Scaling menghasilkan kurva yang lebih rendah sesuai nilai firing strength.

### 3. Jika pada tahap agregasi seluruh nilai α = 0, apa yang terjadi pada rumus Centroid? Bagaimana strategi penanganan kesalahan (fallback mechanism) yang tepat?

**Jawaban:**

Jika seluruh nilai \(\alpha=0\), berarti tidak ada aturan fuzzy yang aktif sehingga hasil agregasi memiliki derajat keanggotaan nol.

Pada rumus Centroid:

\[
z^*=
\frac{\sum z_i\mu(z_i)}
{\sum \mu(z_i)}
\]

nilai penyebut atau \(\sum \mu(z_i)\) menjadi nol. Hal ini menyebabkan pembagian dengan nol sehingga nilai centroid tidak dapat dihitung.

Untuk mengatasinya, sistem perlu melakukan pemeriksaan sebelum proses defuzzifikasi. Jika seluruh nilai agregasi bernilai nol, sistem dapat menampilkan pesan bahwa tidak ada aturan yang aktif. Selain itu, dapat disediakan aturan cadangan (*fallback rule*) atau nilai default yang sudah ditentukan agar sistem tetap dapat memberikan respons.

## J. Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa Fuzzy Inference System merupakan sistem yang menggabungkan beberapa tahapan, yaitu fuzzifikasi, basis pengetahuan, evaluasi aturan, implikasi, agregasi, dan defuzzifikasi menjadi satu proses pengambilan keputusan.

Melalui implementasi menggunakan Python, setiap tahapan dapat dijalankan secara terstruktur dan menghasilkan nilai output berdasarkan aturan fuzzy yang telah dibuat. Pengujian pada tiga kombinasi input menunjukkan bahwa sistem mampu memberikan rekomendasi diskon yang berbeda sesuai dengan lama langganan dan frekuensi transaksi pelanggan.

Dengan demikian, FIS dapat digunakan untuk mengolah input yang memiliki nilai tidak pasti menjadi keputusan konkret. Visualisasi grafik juga membantu memahami proses pembentukan daerah agregasi hingga diperoleh nilai akhir menggunakan metode Centroid.
