
# ==========================================================
# 1. KELAS STRUKTUR ATURAN FUZZY
# ==========================================================
class FuzzyRule:
    def __init__(self, rule_id, antecedent, consequent, operator='AND'):
        """
        antecedent: dict berisi pasangan {'nama_variabel': 'nama_label'}
                    contoh: {'lokasi': 'Strategis', 'tanah': 'Sedang'}
        consequent: dict berisi {'nama_variabel': 'nama_label'}
                    contoh: {'harga': 'Normal'}
        """
        self.rule_id = rule_id
        self.antecedent = antecedent
        self.consequent = consequent
        self.operator = operator.upper()

    def hitung_firing_strength(self, derajat_fuzzifikasi):
        """
        derajat_fuzzifikasi: dict bersarang berisi derajat keanggotaan input,
        contoh: {'lokasi': {'Sangat Strategis': 0.2,
                            'Strategis': 0.8,
                            'Tidak Strategis': 0.0},
                 'tanah': {'Kecil': 0.0,
                           'Sedang': 0.6,
                           'Luas': 0.4},
                 'bangunan': {'Sempit': 0.2,
                              'Sedang': 0.8,
                              'Luas': 0.0}}
        """
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
            raise ValueError(f"Operator {self.operator} tidak dikenali.")

    def __str__(self):
        syarat = f" {self.operator} ".join([f"{var} is {lbl}" for var, lbl in self.antecedent.items()])
        hasil = ", ".join([f"{var} is {lbl}" for var, lbl in self.consequent.items()])
        return f"[{self.rule_id}] IF {syarat} THEN {hasil}"


# ==========================================================
# 2. INISIALISASI BASIS ATURAN (RULE BASE)
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
# 3. EVALUASI ATURAN TERHADAP DATA INPUT
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

print("=" * 90)
print("HASIL EVALUASI BASIS ATURAN FUZZY")
print("SISTEM PENENTUAN HARGA RUMAH")
print("=" * 90)

aturan_aktif = []
for rule in rule_base:
    alpha = rule.hitung_firing_strength(derajat_input_sampel)
    output_var = list(rule.consequent.keys())[0]
    output_lbl = rule.consequent[output_var]
    status = f"AKTIF (alpha = {alpha:.2f})" if alpha > 0 else "NONAKTIF"
    print(f"{rule} --> {status}")
    if alpha > 0:
        aturan_aktif.append((rule.rule_id, output_lbl, alpha))

print("\n" + "=" * 90)
print("RINGKASAN ATURAN YANG TERPICU (FIRING RULES):")
print("=" * 90)
for r_id, konklusi, alpha in aturan_aktif:
    print(f" - {r_id:<4} : Harga Rumah = {konklusi:<15} dengan alpha = {alpha:.2f}")
