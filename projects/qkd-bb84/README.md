# QKD – BB84 (+ Decoy States, noise & distance)

## Goal
Reproduce and extend BB84 with:
- classical bit-flip & depolarizing noise,
- fiber attenuation (dB/km) → secure key rate vs distance,
- decoy-state variant (signal/decoy intensities).

## Run (quick test)
```bash
python scripts/run_qkd_bb84.py
```

## Next
- Implement depolarizing channel.
- Plot QBER vs noise and secret key rate vs distance.
- Export figures to `assets/figures/`.
