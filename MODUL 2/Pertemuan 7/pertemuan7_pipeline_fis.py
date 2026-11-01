import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# 1. FUNGSI DEFUZZIFIKASI CENTROID
# ==========================================================

def defuzzifikasi_centroid(x_vals, mu_vals):
    total_mu = np.sum(mu_vals)

    if total_mu == 0:
        return 0.0

    return np.sum(x_vals * mu_vals) / total_mu

# ==========================================================
# 2. MENENTUKAN INPUT PENGUJIAN
# ==========================================================

input_pengujian = {
    "Lama Langganan": 12,
    "Frekuensi Transaksi": 6
}

# ==========================================================
# 3. MEMBANGUN MODEL FUZZY INFERENCE SYSTEM
# ==========================================================

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

    # Proses fuzzifikasi, inferensi, implikasi, dan agregasi
    def compute_details(self, input_values_dict):

        memberships = {}

        # Fuzzifikasi
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

        output = self.output_variable
        universe = output["universe"]

        aggregated = np.zeros_like(universe)
        firing_strengths = []

        # Evaluasi aturan fuzzy
        for lama_set, frekuensi_set, diskon_set in self.rules:

            alpha = min(
                memberships["Lama Langganan"][lama_set],
                memberships["Frekuensi Transaksi"][frekuensi_set]
            )

            firing_strengths.append(alpha)

            # Implikasi menggunakan MIN
            implied = np.minimum(
                alpha,
                output["mf"][diskon_set]
            )

            # Agregasi menggunakan MAX
            aggregated = np.maximum(
                aggregated,
                implied
            )

        # Memeriksa apakah ada aturan yang aktif
        if np.sum(aggregated) == 0:
            raise ValueError(
                "Tidak ada aturan fuzzy yang aktif!"
            )

        # Defuzzifikasi centroid
        crisp_output = defuzzifikasi_centroid(
            universe,
            aggregated
        )

        return crisp_output, firing_strengths, aggregated

    # Mengembalikan nilai crisp output
    def compute(self, input_values_dict):

        crisp_output, _, _ = self.compute_details(
            input_values_dict
        )

        return crisp_output

# ==========================================================
# 4. MENENTUKAN UNIVERSE DAN FUNGSI KEANGGOTAAN
# ==========================================================

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
# ==========================================================
# 5. MEMBANGUN SISTEM DAN MENAMBAHKAN RULE
# ==========================================================

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


# ==========================================================
# 6. PROSES FUZZY INFERENCE SYSTEM
# ==========================================================

crisp = fis.compute(input_pengujian)

_, firing, agregasi = fis.compute_details(
    input_pengujian
)

z = universe_diskon

print("HASIL PIPELINE FUZZY INFERENCE SYSTEM")
print("=" * 45)

for i, alpha in enumerate(firing, start=1):
    print(f"R{i}: α = {alpha:.4f}")

print("-" * 45)

print(f"Nilai Crisp Output : {crisp:.2f}%")
print(f"Rekomendasi Diskon : {crisp:.2f}%")

# ==========================================================
# 7. VISUALISASI FUNGSI KEANGGOTAAN OUTPUT
# ==========================================================

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

# ==========================================================
# 8. VISUALISASI IMPLIKASI DAN AGREGASI
# ==========================================================

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

# ==========================================================
# 9. GARIS CENTROID
# ==========================================================

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

# ==========================================================
# 10. PENGATURAN GRAFIK
# ==========================================================

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

# ==========================================================
# 11. KESIMPULAN HASIL SISTEM
# ==========================================================

print("\nKeputusan Akhir Sistem FIS:")
print(f"Rekomendasi Diskon: {crisp:.2f}%")
