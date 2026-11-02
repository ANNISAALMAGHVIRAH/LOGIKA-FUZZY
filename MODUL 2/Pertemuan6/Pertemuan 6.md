# LAPORAN PRAKTIKUM
# LOGIKA FUZZY

<br>

**Annisa Almaghvirah**  
**240306037**  
[GitHub: ANNISAALMAGHVIRAH](https://github.com/ANNISAALMAGHVIRAH)

**Program Studi Teknologi Informasi**  
Fakultas Dakwah dan Ilmu Komunikasi  
Universitas Islam Negeri Mataram  
2026

---

## Identitas Praktikum

| Keterangan | Isi |
|---|---|
| Modul | Modul 2 |
| Pertemuan | 6 |
| Topik | Fuzzy Rule dan Knowledge Base |
| Repository | LOGIKA-FUZZY / MODUL 2 / Pertemuan 6 |
| Tanggal | 24 Oktober 2026 |
| Sistem Operasi | Windows 11 Home Single Language 64-bit (10.0, Build 26100) |
| Browser | Google Chrome Version 130.0.6723.117 (Official Build) (64-bit) |
| Tools | Visual Studio Code |

---

## 1. Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa diharapkan mampu:

1. Memahami konsep struktur proposisi aturan fuzzy, yaitu bagian *Antecedent* (premis atau kondisi) dan *Consequent* (konklusi atau tindakan).
2. Menyusun basis aturan (*Rule Base*) dan basis pengetahuan (*Knowledge Base*) berdasarkan logika pakar atau karakteristik domain masalah.
3. Menghitung nilai kekuatan pemicu (*Firing Strength* atau α-predikat) untuk aturan berkondisi majemuk menggunakan operator AND atau OR.
4. Mengimplementasikan struktur data *Rule Base* dalam bahasa pemrograman Python.
5. Melakukan pengujian evaluasi aturan terhadap berbagai kombinasi input data.
6. Menganalisis kondisi aktivasi aturan (*Rule Firing*) serta teknik menangani aturan yang tidak aktif.

## 2. Dasar Teori

### 2.1 Struktur Aturan Fuzzy IF-THEN

Aturan fuzzy IF-THEN merupakan bentuk penalaran yang digunakan untuk menggambarkan hubungan antara kondisi input dengan hasil keputusan. Pada sistem penentuan harga rumah, terdapat tiga variabel input dan satu variabel output.

| Variabel | Jenis | Himpunan Linguistik |
|---|---|---|
| Lokasi | Input | Sangat Strategis, Strategis, Tidak Strategis |
| Luas Tanah | Input | Kecil, Sedang, Luas |
| Luas Bangunan | Input | Sempit, Sedang, Luas |
| Harga Rumah | Output | Sangat Murah, Murah, Normal, Mahal, Sangat Mahal |

Struktur aturan yang digunakan adalah:

```text
IF A AND B AND C THEN D
```

Contoh aturan:

```text
IF Lokasi is Sangat Strategis
AND Luas Tanah is Kecil
AND Luas Bangunan is Sempit
THEN Harga Rumah is Murah.
```

Keterangan:

- **Antecedent:** Lokasi Sangat Strategis, Luas Tanah Kecil, dan Luas Bangunan Sempit.
- **Consequent:** Harga Rumah Murah.

### 2.2 Nilai Kekuatan Pemicu (Firing Strength / α-predikat)

*Firing Strength* merupakan nilai yang menunjukkan seberapa kuat suatu aturan fuzzy aktif berdasarkan derajat keanggotaan input.

Karena aturan pada sistem penentuan harga rumah menggunakan operator AND, perhitungan dilakukan menggunakan metode MIN, yaitu mengambil nilai derajat keanggotaan yang paling kecil.

Rumus:

\[
\alpha_i=\min\left(\mu_A(x),\mu_B(y),\mu_C(z)\right)
\]

Keterangan:

- \(\mu_A(x)\): Derajat keanggotaan lokasi.
- \(\mu_B(y)\): Derajat keanggotaan luas tanah.
- \(\mu_C(z)\): Derajat keanggotaan luas bangunan.
- \(\alpha_i\): Nilai *Firing Strength*.

Jika salah satu derajat keanggotaan bernilai 0, maka aturan tersebut tidak aktif karena hasil operasi MIN akan bernilai 0.

### 2.3 Matriks Basis Aturan (Rule Matrix)

Pada sistem ini terdapat tiga variabel input. Setiap variabel memiliki tiga himpunan linguistik. Oleh karena itu, jumlah kombinasi aturan yang dapat dibentuk adalah:

\[
R=3\times3\times3=27
\]

Berikut matriks basis aturan yang digunakan.

**A. Lokasi Sangat Strategis**

| Luas Tanah | Bangunan Sempit | Bangunan Sedang | Bangunan Luas |
|---|---|---|---|
| Kecil | Murah (R01) | Normal (R02) | Mahal (R03) |
| Sedang | Normal (R04) | Mahal (R05) | Sangat Mahal (R06) |
| Luas | Mahal (R07) | Sangat Mahal (R08) | Sangat Mahal (R09) |

**B. Lokasi Strategis**

| Luas Tanah | Bangunan Sempit | Bangunan Sedang | Bangunan Luas |
|---|---|---|---|
| Kecil | Sangat Murah (R10) | Murah (R11) | Normal (R12) |
| Sedang | Murah (R13) | Normal (R14) | Mahal (R15) |
| Luas | Normal (R16) | Mahal (R17) | Sangat Mahal (R18) |

**C. Lokasi Tidak Strategis**

| Luas Tanah | Bangunan Sempit | Bangunan Sedang | Bangunan Luas |
|---|---|---|---|
| Kecil | Sangat Murah (R19) | Sangat Murah (R20) | Murah (R21) |
| Sedang | Sangat Murah (R22) | Murah (R23) | Normal (R24) |
| Luas | Murah (R25) | Normal (R26) | Mahal (R27) |

### 2.4 Contoh Perhitungan Manual Firing Strength

Misalkan suatu rumah memiliki hasil fuzzifikasi sebagai berikut. Nilai berikut merupakan data simulasi untuk pengujian.

| Variabel | Himpunan | Derajat Keanggotaan |
|---|---|---:|
| Lokasi | Sangat Strategis | 0,2 |
| Lokasi | Strategis | 0,8 |
| Lokasi | Tidak Strategis | 0,0 |
| Luas Tanah | Kecil | 0,0 |
| Luas Tanah | Sedang | 0,6 |
| Luas Tanah | Luas | 0,4 |
| Luas Bangunan | Sempit | 0,2 |
| Luas Bangunan | Sedang | 0,8 |
| Luas Bangunan | Luas | 0,0 |

Perhitungan dilakukan menggunakan operator MIN.

**1. Aturan R04**

IF Lokasi Sangat Strategis AND Luas Tanah Sedang AND Luas Bangunan Sempit THEN Harga Rumah Normal.

\[
\alpha_4=\min(0,2;0,6;0,2)
\]

\[
\boxed{\alpha_4=0,2}
\]

**2. Aturan R14**

IF Lokasi Strategis AND Luas Tanah Sedang AND Luas Bangunan Sedang THEN Harga Rumah Normal.

\[
\alpha_{14}=\min(0,8;0,6;0,8)
\]

\[
\boxed{\alpha_{14}=0,6}
\]

**3. Aturan R17**

IF Lokasi Strategis AND Luas Tanah Luas AND Luas Bangunan Sedang THEN Harga Rumah Mahal.

\[
\alpha_{17}=\min(0,8;0,4;0,8)
\]

\[
\boxed{\alpha_{17}=0,4}
\]

**4. Aturan R27**

IF Lokasi Tidak Strategis AND Luas Tanah Luas AND Luas Bangunan Luas THEN Harga Rumah Mahal.

\[
\alpha_{27}=\min(0,0;0,4;0,0)
\]

\[
\boxed{\alpha_{27}=0,0}
\]

Aturan R27 tidak aktif karena terdapat derajat keanggotaan bernilai 0 pada kondisi inputnya.

Dari perhitungan tersebut, dapat diketahui bahwa setiap aturan memiliki nilai *Firing Strength* yang berbeda sesuai dengan derajat keanggotaan input.

## 3. Implementasi Program Python

Program berikut digunakan untuk membuat struktur aturan fuzzy, menyimpan 27 aturan IF-THEN, menghitung nilai *Firing Strength*, dan menguji beberapa kombinasi input.

### 3.1 Kode Program Lengkap

```python
# ==========================================================
# 1. KELAS STRUKTUR ATURAN FUZZY
# ==========================================================

class FuzzyRule:
    def __init__(self, rule_id, antecedent, consequent, operator='AND'):
        self.rule_id = rule_id
        self.antecedent = antecedent
        self.consequent = consequent
        self.operator = operator.upper()

    def hitung_firing_strength(self, derajat_fuzzifikasi):
        nilai_derajat = []

        for var_nama, label_nama in self.antecedent.items():
            deg = derajat_fuzzifikasi[var_nama].get(label_nama, 0.0)
            nilai_derajat.append(deg)

        if not nilai_derajat:
            return 0.0

        if self.operator == 'AND':
            return min(nilai_derajat)

        elif self.operator == 'OR':
            return max(nilai_derajat)

        else:
            raise ValueError(
                f"Operator {self.operator} tidak dikenali."
            )

    def __str__(self):
        syarat = f" {self.operator} ".join(
            [f"{var} is {lbl}"
             for var, lbl in self.antecedent.items()]
        )

        hasil = ", ".join(
            [f"{var} is {lbl}"
             for var, lbl in self.consequent.items()]
        )

        return f"[{self.rule_id}] IF {syarat} THEN {hasil}"


# ==========================================================
# 2. INISIALISASI BASIS ATURAN (27 RULES)
# ==========================================================

rule_base = [

    # LOKASI SANGAT STRATEGIS
    FuzzyRule("R01", {"lokasi": "Sangat Strategis", "tanah": "Kecil", "bangunan": "Sempit"}, {"harga": "Murah"}),
    FuzzyRule("R02", {"lokasi": "Sangat Strategis", "tanah": "Kecil", "bangunan": "Sedang"}, {"harga": "Normal"}),
    FuzzyRule("R03", {"lokasi": "Sangat Strategis", "tanah": "Kecil", "bangunan": "Luas"}, {"harga": "Mahal"}),
    FuzzyRule("R04", {"lokasi": "Sangat Strategis", "tanah": "Sedang", "bangunan": "Sempit"}, {"harga": "Normal"}),
    FuzzyRule("R05", {"lokasi": "Sangat Strategis", "tanah": "Sedang", "bangunan": "Sedang"}, {"harga": "Mahal"}),
    FuzzyRule("R06", {"lokasi": "Sangat Strategis", "tanah": "Sedang", "bangunan": "Luas"}, {"harga": "Sangat Mahal"}),
    FuzzyRule("R07", {"lokasi": "Sangat Strategis", "tanah": "Luas", "bangunan": "Sempit"}, {"harga": "Mahal"}),
    FuzzyRule("R08", {"lokasi": "Sangat Strategis", "tanah": "Luas", "bangunan": "Sedang"}, {"harga": "Sangat Mahal"}),
    FuzzyRule("R09", {"lokasi": "Sangat Strategis", "tanah": "Luas", "bangunan": "Luas"}, {"harga": "Sangat Mahal"}),

    # LOKASI STRATEGIS
    FuzzyRule("R10", {"lokasi": "Strategis", "tanah": "Kecil", "bangunan": "Sempit"}, {"harga": "Sangat Murah"}),
    FuzzyRule("R11", {"lokasi": "Strategis", "tanah": "Kecil", "bangunan": "Sedang"}, {"harga": "Murah"}),
    FuzzyRule("R12", {"lokasi": "Strategis", "tanah": "Kecil", "bangunan": "Luas"}, {"harga": "Normal"}),
    FuzzyRule("R13", {"lokasi": "Strategis", "tanah": "Sedang", "bangunan": "Sempit"}, {"harga": "Murah"}),
    FuzzyRule("R14", {"lokasi": "Strategis", "tanah": "Sedang", "bangunan": "Sedang"}, {"harga": "Normal"}),
    FuzzyRule("R15", {"lokasi": "Strategis", "tanah": "Sedang", "bangunan": "Luas"}, {"harga": "Mahal"}),
    FuzzyRule("R16", {"lokasi": "Strategis", "tanah": "Luas", "bangunan": "Sempit"}, {"harga": "Normal"}),
    FuzzyRule("R17", {"lokasi": "Strategis", "tanah": "Luas", "bangunan": "Sedang"}, {"harga": "Mahal"}),
    FuzzyRule("R18", {"lokasi": "Strategis", "tanah": "Luas", "bangunan": "Luas"}, {"harga": "Sangat Mahal"}),

    # LOKASI TIDAK STRATEGIS
    FuzzyRule("R19", {"lokasi": "Tidak Strategis", "tanah": "Kecil", "bangunan": "Sempit"}, {"harga": "Sangat Murah"}),
    FuzzyRule("R20", {"lokasi": "Tidak Strategis", "tanah": "Kecil", "bangunan": "Sedang"}, {"harga": "Sangat Murah"}),
    FuzzyRule("R21", {"lokasi": "Tidak Strategis", "tanah": "Kecil", "bangunan": "Luas"}, {"harga": "Murah"}),
    FuzzyRule("R22", {"lokasi": "Tidak Strategis", "tanah": "Sedang", "bangunan": "Sempit"}, {"harga": "Sangat Murah"}),
    FuzzyRule("R23", {"lokasi": "Tidak Strategis", "tanah": "Sedang", "bangunan": "Sedang"}, {"harga": "Murah"}),
    FuzzyRule("R24", {"lokasi": "Tidak Strategis", "tanah": "Sedang", "bangunan": "Luas"}, {"harga": "Normal"}),
    FuzzyRule("R25", {"lokasi": "Tidak Strategis", "tanah": "Luas", "bangunan": "Sempit"}, {"harga": "Murah"}),
    FuzzyRule("R26", {"lokasi": "Tidak Strategis", "tanah": "Luas", "bangunan": "Sedang"}, {"harga": "Normal"}),
    FuzzyRule("R27", {"lokasi": "Tidak Strategis", "tanah": "Luas", "bangunan": "Luas"}, {"harga": "Mahal"}),
]


# ==========================================================
# 3. FUNGSI EVALUASI ATURAN
# ==========================================================

def evaluasi_aturan(nama_skenario, derajat_input):
    print("\n" + "=" * 60)
    print("PENGUJIAN", nama_skenario)
    print("=" * 60)

    aturan_aktif = []

    for rule in rule_base:
        alpha = rule.hitung_firing_strength(derajat_input)

        if alpha > 0:
            aturan_aktif.append((rule, alpha))

    print("Daftar aturan yang aktif:")

    for rule, alpha in aturan_aktif:
        output = rule.consequent["harga"]
        print(
            f"{rule.rule_id}: {rule} | "
            f"Harga = {output} | Alpha = {alpha:.2f}"
        )

    if not aturan_aktif:
        print("Tidak ada aturan yang aktif.")

    print("Jumlah aturan aktif:", len(aturan_aktif))


# ==========================================================
# 4. DATA INPUT SKENARIO A
# ==========================================================

skenario_A = {
    "lokasi": {
        "Sangat Strategis": 1.0,
        "Strategis": 0.0,
        "Tidak Strategis": 0.0
    },
    "tanah": {
        "Kecil": 1.0,
        "Sedang": 0.0,
        "Luas": 0.0
    },
    "bangunan": {
        "Sempit": 1.0,
        "Sedang": 0.0,
        "Luas": 0.0
    }
}


# ==========================================================
# 5. DATA INPUT SKENARIO B
# ==========================================================

skenario_B = {
    "lokasi": {
        "Sangat Strategis": 0.3,
        "Strategis": 0.7,
        "Tidak Strategis": 0.0
    },
    "tanah": {
        "Kecil": 0.0,
        "Sedang": 0.6,
        "Luas": 0.4
    },
    "bangunan": {
        "Sempit": 0.2,
        "Sedang": 0.8,
        "Luas": 0.0
    }
}


# ==========================================================
# 6. DATA INPUT SKENARIO C
# ==========================================================

skenario_C = {
    "lokasi": {
        "Sangat Strategis": 0.0,
        "Strategis": 0.0,
        "Tidak Strategis": 1.0
    },
    "tanah": {
        "Kecil": 0.0,
        "Sedang": 0.0,
        "Luas": 1.0
    },
    "bangunan": {
        "Sempit": 0.0,
        "Sedang": 0.0,
        "Luas": 1.0
    }
}


# ==========================================================
# 7. DATA INPUT CONTOH PERHITUNGAN MANUAL
# ==========================================================

derajat_input_sampel = {
    "lokasi": {
        "Sangat Strategis": 0.2,
        "Strategis": 0.8,
        "Tidak Strategis": 0.0
    },
    "tanah": {
        "Kecil": 0.0,
        "Sedang": 0.6,
        "Luas": 0.4
    },
    "bangunan": {
        "Sempit": 0.2,
        "Sedang": 0.8,
        "Luas": 0.0
    }
}


# ==========================================================
# 8. MENJALANKAN PENGUJIAN
# ==========================================================

evaluasi_aturan("CONTOH DATA FUZZIFIKASI", derajat_input_sampel)
evaluasi_aturan("SKENARIO A", skenario_A)
evaluasi_aturan("SKENARIO B", skenario_B)
evaluasi_aturan("SKENARIO C", skenario_C)
```

### 3.2 Penjelasan Implementasi

Kode tersebut terdiri dari beberapa bagian utama.

1. **Kelas FuzzyRule** digunakan untuk menyimpan identitas aturan, kondisi input (*antecedent*), hasil aturan (*consequent*), dan operator yang digunakan.
2. **Basis aturan (Rule Base)** berisi 27 aturan berdasarkan kombinasi lokasi, luas tanah, dan luas bangunan.
3. **Fungsi hitung_firing_strength()** digunakan untuk menghitung kekuatan pemicu setiap aturan. Operator MIN digunakan untuk AND, sedangkan operator MAX digunakan untuk OR.
4. **Fungsi evaluasi_aturan()** digunakan untuk memeriksa seluruh aturan dan menampilkan aturan yang aktif beserta nilai alpha.
5. **Data skenario pengujian** digunakan untuk menguji aturan dengan beberapa kombinasi derajat keanggotaan.

Dengan implementasi tersebut, sistem dapat mengevaluasi setiap aturan secara independen. Beberapa aturan dapat aktif secara bersamaan apabila masing-masing memiliki nilai *Firing Strength* lebih dari 0.

### 3.3 Hasil Output Program

Hasil keluaran program bergantung pada eksekusi kode di Python. Berdasarkan perhitungan dari data yang digunakan, ringkasan hasil yang diharapkan adalah:

**Contoh data fuzzifikasi:**

| Aturan | Konklusi Harga | Alpha | Status |
|---|---|---:|---|
| R04 | Normal | 0,2 | Aktif |
| R05 | Mahal | 0,2 | Aktif |
| R07 | Mahal | 0,2 | Aktif |
| R08 | Sangat Mahal | 0,2 | Aktif |
| R13 | Murah | 0,2 | Aktif |
| R14 | Normal | 0,6 | Aktif |
| R16 | Normal | 0,4 | Aktif |
| R17 | Mahal | 0,4 | Aktif |

Aturan lainnya tidak aktif karena nilai *Firing Strength*-nya sama dengan 0.

**Catatan:** Tabel di atas merupakan ringkasan hasil perhitungan untuk data fuzzifikasi contoh. Untuk bukti output praktikum, jalankan kode tersebut di Visual Studio Code dan lampirkan tangkapan layar hasil eksekusinya.

## 4. Skenario Pengujian Basis Aturan

Pengujian dilakukan menggunakan tiga skenario kondisi rumah yang berbeda. Tujuannya untuk mengetahui aturan yang aktif berdasarkan nilai derajat keanggotaan setiap variabel input.

### 4.1 Data Skenario Pengujian

| Skenario | Deskripsi Kasus | Fuzzifikasi Lokasi | Fuzzifikasi Luas Tanah | Fuzzifikasi Luas Bangunan | Aturan Terpacu |
|---|---|---|---|---|---|
| A | Lokasi sangat strategis, tanah kecil, bangunan sempit | Sangat Strategis: 1,0; lainnya: 0 | Kecil: 1,0; lainnya: 0 | Sempit: 1,0; lainnya: 0 | R01 |
| B | Lokasi memiliki keanggotaan Sangat Strategis dan Strategis, tanah Sedang dan Luas, bangunan Sempit dan Sedang | Sangat Strategis: 0,3; Strategis: 0,7; Tidak Strategis: 0 | Kecil: 0; Sedang: 0,6; Luas: 0,4 | Sempit: 0,2; Sedang: 0,8; Luas: 0 | R04, R05, R07, R08, R13, R14, R16, R17 |
| C | Lokasi tidak strategis, tanah luas, bangunan luas | Tidak Strategis: 1,0; lainnya: 0 | Luas: 1,0; lainnya: 0 | Luas: 1,0; lainnya: 0 | R27 |

### 4.2 Perhitungan Nilai Alpha

**Skenario A – Aturan R01**

\[
\alpha_1=\min(1,0;1,0;1,0)=1,0
\]

Aturan R01 aktif dengan nilai alpha 1,0 dan menghasilkan kategori harga Murah.

**Skenario B – Aturan yang Aktif**

| Aturan | Perhitungan Alpha | Hasil |
|---|---|---:|
| R04 | min(0,3; 0,6; 0,2) | 0,2 |
| R05 | min(0,3; 0,6; 0,8) | 0,3 |
| R07 | min(0,3; 0,4; 0,2) | 0,2 |
| R08 | min(0,3; 0,4; 0,8) | 0,3 |
| R13 | min(0,7; 0,6; 0,2) | 0,2 |
| R14 | min(0,7; 0,6; 0,8) | 0,6 |
| R16 | min(0,7; 0,4; 0,2) | 0,2 |
| R17 | min(0,7; 0,4; 0,8) | 0,4 |

Contoh perhitungan:

\[
\alpha_{14}=\min(0,7;0,6;0,8)=0,6
\]

\[
\alpha_{17}=\min(0,7;0,4;0,8)=0,4
\]

Terdapat delapan aturan aktif pada skenario B. Nilai alpha terbesar terdapat pada aturan R14 sebesar 0,6.

**Skenario C – Aturan R27**

\[
\alpha_{27}=\min(1,0;1,0;1,0)=1,0
\]

Aturan R27 aktif dengan nilai alpha 1,0 dan menghasilkan kategori harga Mahal.

### 4.3 Ringkasan Hasil Pengujian

| Skenario | Aturan Aktif | Nilai Alpha |
|---|---|---|
| A | R01 | α₁ = 1,0 |
| B | R04, R05, R07, R08, R13, R14, R16, R17 | α₄ = 0,2; α₅ = 0,3; α₇ = 0,2; α₈ = 0,3; α₁₃ = 0,2; α₁₄ = 0,6; α₁₆ = 0,2; α₁₇ = 0,4 |
| C | R27 | α₂₇ = 1,0 |

### 4.4 Analisis Hasil Pengujian

Berdasarkan ketiga skenario tersebut, dapat diketahui bahwa setiap kombinasi nilai derajat keanggotaan menghasilkan aturan fuzzy yang berbeda.

Pada skenario A, aturan R01 aktif dengan nilai alpha 1,0 dan menghasilkan kategori harga rumah Murah. Hal ini terjadi karena seluruh kondisi pada aturan R01 memiliki derajat keanggotaan sebesar 1,0.

Pada skenario B, terdapat delapan aturan aktif dengan nilai alpha yang berbeda-beda. Hal tersebut terjadi karena beberapa variabel memiliki derajat keanggotaan lebih dari nol pada beberapa himpunan sekaligus. Nilai alpha terbesar adalah 0,6 pada aturan R14 yang menghasilkan kategori harga Normal.

Sementara itu, pada skenario C, aturan R27 aktif dengan nilai alpha 1,0 dan menghasilkan kategori harga Mahal.

Dengan demikian, pengujian menunjukkan bahwa sistem mampu mengaktifkan beberapa aturan secara bersamaan berdasarkan derajat keanggotaan masing-masing variabel input.

## 5. Tugas Praktikum 6

**Kasus: Sistem Penentuan Harga Rumah**

Variabel yang digunakan dalam sistem ini adalah:

- Lokasi dengan tiga himpunan linguistik: Sangat Strategis, Strategis, dan Tidak Strategis.
- Luas Tanah dengan tiga himpunan linguistik: Kecil, Sedang, dan Luas.
- Luas Bangunan dengan tiga himpunan linguistik: Sempit, Sedang, dan Luas.

Variabel output yang digunakan adalah Harga Rumah dengan lima himpunan linguistik, yaitu Sangat Murah, Murah, Normal, Mahal, dan Sangat Mahal.

Jumlah aturan diperoleh dari kombinasi tiga variabel input yang masing-masing memiliki tiga himpunan linguistik:

\[
R=3\times3\times3=27
\]

Matriks basis aturan yang digunakan dalam tugas praktikum ini sama dengan matriks pada bagian 2.3, yaitu 27 aturan dari R01 sampai R27.

Program Python yang digunakan untuk tugas praktikum adalah implementasi pada bagian 3.1. Program tersebut telah memuat kelas aturan, basis aturan, fungsi evaluasi, dan tiga skenario pengujian.

## 6. Pertanyaan Analisis

### 6.1 Apa yang akan terjadi pada sistem inferensi fuzzy jika suatu kombinasi input tidak memicu satu pun aturan (\(\alpha_i=0\) untuk semua i)? Bagaimana cara mencegah kondisi tersebut (*completeness of rule base*)?

**Jawaban:**

Jika semua nilai *Firing Strength* (\(\alpha_i\)) bernilai 0, berarti tidak ada aturan yang aktif untuk memproses kombinasi input tersebut. Akibatnya, sistem tidak memiliki hasil inferensi fuzzy yang dapat digunakan untuk menentukan output.

Kondisi ini dapat dicegah dengan menerapkan *completeness of rule base*, yaitu memastikan seluruh kemungkinan kombinasi input sudah tercakup dalam basis aturan. Selain itu, fungsi keanggotaan perlu dirancang agar seluruh rentang nilai input memiliki derajat keanggotaan pada minimal satu himpunan fuzzy.

Pada sistem penentuan harga rumah, seluruh kombinasi dari Lokasi, Luas Tanah, dan Luas Bangunan harus memiliki aturan. Karena setiap variabel memiliki tiga himpunan fuzzy, maka diperlukan 27 aturan.

### 6.2 Jika dua aturan yang aktif menghasilkan konklusi yang sama, misalnya R6 dan R8 sama-sama menghasilkan Prioritas = Tinggi, bagaimanakah kedua nilai α tersebut digabungkan pada tahap agregasi?

**Jawaban:**

Jika dua atau lebih aturan menghasilkan konklusi yang sama, nilai *Firing Strength* dari aturan tersebut digabungkan menggunakan operator MAX pada tahap agregasi.

Artinya, sistem akan mengambil nilai alpha yang paling besar dari aturan-aturan yang menghasilkan kategori output yang sama.

Contohnya, jika aturan R04 dan R14 sama-sama menghasilkan kategori harga Normal, dengan nilai:

\[
\alpha_{04}=0,2
\]

\[
\alpha_{14}=0,6
\]

Maka hasil agregasinya adalah:

\[
\mu_{\text{Normal}}=\max(0,2;0,6)=0,6
\]

Jadi, nilai hasil agregasi untuk kategori harga Normal adalah 0,6.

### 6.3 Mengapa urutan aturan (*rule ordering*) pada basis aturan fuzzy tidak memengaruhi hasil akhir sistem? Jelaskan perbedaan karakteristik ini dibandingkan struktur if-elif-else imperatif!

**Jawaban:**

Urutan aturan pada sistem fuzzy tidak memengaruhi hasil akhir karena setiap aturan dievaluasi secara independen. Semua aturan diperiksa untuk mengetahui nilai *Firing Strength* masing-masing. Jika beberapa aturan memiliki nilai alpha lebih dari 0, aturan-aturan tersebut tetap dapat aktif secara bersamaan.

Hal ini berbeda dengan struktur `if-elif-else` pada pemrograman imperatif. Pada struktur tersebut, ketika salah satu kondisi sudah terpenuhi, program akan menjalankan perintah pada kondisi tersebut dan melewati kondisi berikutnya.

Dengan demikian, sistem fuzzy memungkinkan beberapa aturan aktif secara bersamaan dan hasilnya dapat digabungkan melalui proses agregasi. Sementara itu, struktur `if-elif-else` hanya menjalankan satu cabang kondisi pertama yang terpenuhi.

## 7. Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa:

1. Aturan fuzzy IF-THEN digunakan untuk menggambarkan hubungan antara kondisi input dan hasil keputusan melalui bagian *Antecedent* dan *Consequent*.
2. Basis aturan pada sistem penentuan harga rumah terdiri dari 27 aturan yang diperoleh dari kombinasi tiga variabel input, yaitu lokasi, luas tanah, dan luas bangunan.
3. Nilai *Firing Strength* digunakan untuk mengetahui seberapa kuat suatu aturan aktif. Pada aturan dengan operator AND, perhitungan dilakukan menggunakan metode MIN.
4. Hasil pengujian menunjukkan bahwa beberapa aturan dapat aktif secara bersamaan apabila nilai derajat keanggotaan input lebih dari nol.
5. Aturan yang tidak aktif memiliki nilai alpha sebesar 0, sedangkan aturan yang aktif memiliki nilai alpha lebih dari 0.
6. Implementasi Python membantu menyimpan basis aturan dan mengevaluasi setiap aturan secara sistematis berdasarkan derajat keanggotaan input.

Dengan demikian, praktikum ini memberikan pemahaman mengenai penyusunan *Rule Base*, perhitungan *Firing Strength*, serta evaluasi aturan fuzzy sebagai bagian penting dalam proses pengambilan keputusan menggunakan *Fuzzy Inference System*.
