import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# 1. FUNGSI KEANGGOTAAN SEGITIGA DAN TRAPESIUM
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


# ==========================================================
# 2. MEMBANGUN KELAS FUZZY INFERENCE SYSTEM
# ==========================================================

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

    # PROSES PERHITUNGAN FIS SECARA LENGKAP
    def compute_details(self, input_values_dict):

        # FUZZIFIKASI
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

        # IMPLIKASI DAN AGREGASI
        output = self.output_variable
        universe = output["universe"]

        aggregated = np.zeros_like(universe)
        firing_strengths = []

        for rule in self.rules:

            lama_set, frekuensi_set, diskon_set = rule

            # Evaluasi aturan menggunakan MIN
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

        # DEFUZZIFIKASI CENTROID
        total = np.sum(aggregated)

        if total == 0:
            raise ValueError("Tidak ada aturan fuzzy yang aktif.")

        crisp_output = np.sum(
            universe * aggregated
        ) / total

        return crisp_output, firing_strengths, aggregated

    # FUNGSI COMPUTE SESUAI INSTRUKSI PRAKTIKUM
    def compute(self, input_values_dict):

        crisp_output, _, _ = self.compute_details(input_values_dict)

        return crisp_output


# ==========================================================
# 3. MENENTUKAN DOMAIN VARIABEL
# ==========================================================

universe_lama = np.linspace(0, 24, 241)
universe_frekuensi = np.linspace(0, 15, 151)
universe_diskon = np.linspace(0, 30, 301)


# ==========================================================
# 4. FUNGSI KEANGGOTAAN INPUT
# ==========================================================

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


# ==========================================================
# 5. FUNGSI KEANGGOTAAN OUTPUT DISKON
# ==========================================================

mf_diskon = {
    "Rendah": trapmf(universe_diskon, [0, 0, 5, 12]),
    "Sedang": trimf(universe_diskon, [8, 15, 22]),
    "Tinggi": trapmf(universe_diskon, [18, 25, 30, 30])
}


# ==========================================================
# 6. MEMBUAT OBJEK SISTEM FUZZY
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


# ==========================================================
# 7. MENAMBAHKAN 9 ATURAN FUZZY
# ==========================================================

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
# 8. TIGA KASUS PENGUJIAN
# ==========================================================

kasus = [
    {"Lama Langganan": 3, "Frekuensi Transaksi": 2},
    {"Lama Langganan": 12, "Frekuensi Transaksi": 6},
    {"Lama Langganan": 24, "Frekuensi Transaksi": 15}
]


# ==========================================================
# 9. MENAMPILKAN HASIL DAN GRAFIK SETIAP KASUS
# ==========================================================

for nomor, data in enumerate(kasus, start=1):

    # Mengambil nilai crisp melalui compute()
    crisp = fis.compute(data)

    # Mengambil detail perhitungan untuk grafik
    _, firing, aggregated = fis.compute_details(data)

    lama = data["Lama Langganan"]
    frekuensi = data["Frekuensi Transaksi"]

    # Derajat keanggotaan input
    mu_lama = {
        label: np.interp(lama, universe_lama, mf)
        for label, mf in mf_lama.items()
    }

    mu_frekuensi = {
        label: np.interp(frekuensi, universe_frekuensi, mf)
        for label, mf in mf_frekuensi.items()
    }

    # Membuat grafik 2 x 2
    fig, ax = plt.subplots(2, 2, figsize=(14, 9))

    fig.suptitle(
        f"FIS Mamdani - Pengujian Kasus {nomor}",
        fontsize=15,
        fontweight="bold"
    )

    # GRAFIK 1: LAMA LANGGANAN
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

    # GRAFIK 2: FREKUENSI TRANSAKSI
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

    # GRAFIK 3: OUTPUT, AGREGASI, DAN CENTROID
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

    # GRAFIK 4: FIRING STRENGTH SETIAP ATURAN
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

    # MENAMPILKAN HASIL
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
