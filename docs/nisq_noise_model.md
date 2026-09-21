# NISQ Compiler & Fidelity Model Reference

## Quantum Gate Noise Model
In Noisy Intermediate-Scale Quantum (NISQ) devices, physical multi-qubit gates are the dominant source of circuit decoherence.

$$\mathcal{F}_{\text{circuit}} = (F_{1q})^{N_{1q}} \times (F_{2q})^{N_{2q}}$$

- **1Q Gate Fidelity ($F_{1q}$)**: $\approx 99.95\%$ ($0.9995$)
- **2Q CNOT Fidelity ($F_{2q}$)**: $\approx 99.20\%$ ($0.9920$)

## Peephole Involutory Identities
1. **CNOT Self-Inverse**: $CX_{i,j} \cdot CX_{i,j} = \mathbb{I}$
2. **Hadamard Self-Inverse**: $H_i \cdot H_i = \mathbb{I}$
3. **Pauli Z Self-Inverse**: $Z_i \cdot Z_i = \mathbb{I}$
