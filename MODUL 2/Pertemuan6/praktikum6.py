# ==========================================
# 1. CLASS FUZZY RULE
# ==========================================

class FuzzyRule:
    def __init__(self, id_rule, lokasi, tanah, bangunan, harga):
        self.id_rule = id_rule
        self.lokasi = lokasi
        self.tanah = tanah
        self.bangunan = bangunan
        self.harga = harga

    def hitung_firing_strength(self, derajat_input):
        alpha = min(
            derajat_input["lokasi"].get(self.lokasi, 0),
            derajat_input["tanah"].get(self.tanah, 0),
            derajat_input["bangunan"].get(self.bangunan, 0)
        )
        return alpha

    def __str__(self):
        return (
            f"IF Lokasi {self.lokasi} AND "
            f"Tanah {self.tanah} AND "
            f"Bangunan {self.bangunan} "
            f"THEN Harga {self.harga}"
        )


# ==========================================
# 2. BASIS ATURAN (27 RULES)
# ==========================================

rule_base = [

    # Lokasi Sangat Strategis
    FuzzyRule("R01", "Sangat Strategis", "Kecil", "Sempit", "Murah"),
    FuzzyRule("R02", "Sangat Strategis", "Kecil", "Sedang", "Normal"),
    FuzzyRule("R03", "Sangat Strategis", "Kecil", "Luas", "Mahal"),
    FuzzyRule("R04", "Sangat Strategis", "Sedang", "Sempit", "Normal"),
    FuzzyRule("R05", "Sangat Strategis", "Sedang", "Sedang", "Mahal"),
    FuzzyRule("R06", "Sangat Strategis", "Sedang", "Luas", "Sangat Mahal"),
    FuzzyRule("R07", "Sangat Strategis", "Luas", "Sempit", "Mahal"),
    FuzzyRule("R08", "Sangat Strategis", "Luas", "Sedang", "Sangat Mahal"),
    FuzzyRule("R09", "Sangat Strategis", "Luas", "Luas", "Sangat Mahal"),

    # Lokasi Strategis
    FuzzyRule("R10", "Strategis", "Kecil", "Sempit", "Sangat Murah"),
    FuzzyRule("R11", "Strategis", "Kecil", "Sedang", "Murah"),
    FuzzyRule("R12", "Strategis", "Kecil", "Luas", "Normal"),
    FuzzyRule("R13", "Strategis", "Sedang", "Sempit", "Murah"),
    FuzzyRule("R14", "Strategis", "Sedang", "Sedang", "Normal"),
    FuzzyRule("R15", "Strategis", "Sedang", "Luas", "Mahal"),
    FuzzyRule("R16", "Strategis", "Luas", "Sempit", "Normal"),
    FuzzyRule("R17", "Strategis", "Luas", "Sedang", "Mahal"),
    FuzzyRule("R18", "Strategis", "Luas", "Luas", "Sangat Mahal"),

    # Lokasi Tidak Strategis
    FuzzyRule("R19", "Tidak Strategis", "Kecil", "Sempit", "Sangat Murah"),
    FuzzyRule("R20", "Tidak Strategis", "Kecil", "Sedang", "Sangat Murah"),
    FuzzyRule("R21", "Tidak Strategis", "Kecil", "Luas", "Murah"),
    FuzzyRule("R22", "Tidak Strategis", "Sedang", "Sempit", "Sangat Murah"),
    FuzzyRule("R23", "Tidak Strategis", "Sedang", "Sedang", "Murah"),
    FuzzyRule("R24", "Tidak Strategis", "Sedang", "Luas", "Normal"),
    FuzzyRule("R25", "Tidak Strategis", "Luas", "Sempit", "Murah"),
    FuzzyRule("R26", "Tidak Strategis", "Luas", "Sedang", "Normal"),
    FuzzyRule("R27", "Tidak Strategis", "Luas", "Luas", "Mahal")
]


# ==========================================
# 3. FUNGSI EVALUASI ATURAN
# ==========================================

def evaluasi_aturan(nama_skenario, derajat_input):
    print("\n====================================")
    print("PENGUJIAN", nama_skenario)
    print("====================================")

    aturan_aktif = []

    for rule in rule_base:
        alpha = rule.hitung_firing_strength(derajat_input)

        if alpha > 0:
            aturan_aktif.append((rule, alpha))

    print("Daftar aturan yang aktif:")

    for rule, alpha in aturan_aktif:
        print(f"{rule.id_rule}: {rule} | Alpha = {alpha}")

    if not aturan_aktif:
        print("Tidak ada aturan yang aktif.")

    print("Jumlah aturan aktif:", len(aturan_aktif))


# ==========================================
# 4. DATA INPUT SKENARIO A
# ==========================================

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


# ==========================================
# 5. DATA INPUT SKENARIO B
# ==========================================

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


# ==========================================
# 6. DATA INPUT SKENARIO C
# ==========================================

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


# ==========================================
# 7. MENJALANKAN PENGUJIAN
# ==========================================

evaluasi_aturan("SKENARIO A", skenario_A)
evaluasi_aturan("SKENARIO B", skenario_B)
evaluasi_aturan("SKENARIO C", skenario_C)
