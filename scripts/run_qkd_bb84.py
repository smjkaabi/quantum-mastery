import numpy as np


def sample_bits(n): return np.random.randint(0, 2, size=n)

def bases(n): return np.random.randint(0, 2, size=n)  # 0=Z, 1=X

def simulate_bb84(n=1000, bit_flip_p=0.0, seed=42):
    rng = np.random.default_rng(seed)
    a_bits = rng.integers(0, 2, size=n)
    a_bases = rng.integers(0, 2, size=n)
    b_bases = rng.integers(0, 2, size=n)
    # Ideal: if bases match, Bob reads Alice's bit; add classical bit-flip noise
    meas = a_bits.copy()
    flips = rng.random(n) < bit_flip_p
    meas = np.bitwise_xor(meas, flips.astype(int))
    mask = (a_bases == b_bases)
    sifted_a = a_bits[mask]
    sifted_b = meas[mask]
    if len(sifted_a) == 0:
        return 0.5, 0
    qber = np.mean(sifted_a != sifted_b)
    return qber, len(sifted_a)


if __name__ == "__main__":
    for p in [0.0, 0.02, 0.05, 0.1]:
        qber, m = simulate_bb84(n=5000, bit_flip_p=p)
        print(f"noise={p:.2f}  sifted={m}  QBER={qber:.3f}")
