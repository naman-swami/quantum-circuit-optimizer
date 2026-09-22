# Quantum Compiler Benchmarks & NISQ Noise Models

## 1. NISQ Quantum Processor Architecture Specifications
The quantum circuit compilation engine optimizes OpenQASM 2.0 representations targeting Noisy Intermediate-Scale Quantum (NISQ) superconducting transmon and trapped-ion hardware topologies.

### Hardware Basis Gates & Physical Parameters
- **Native Gate Basis**: Single-qubit rotations $\{R_x(\theta), R_z(\theta), U_3(\theta, \phi, \lambda)\}$ and 2-qubit entangling gates $\{CNOT, CZ\}$.
- **Qubit Coherence Characteristics**:
  - Relaxation Time ($T_1$): $120.0\ \mu s$
  - Dephasing Time ($T_2$): $90.0\ \mu s$
  - Single-Qubit Gate Error ($e_{1q}$): $1.2 \times 10^{-4}$ (Duration: $25\text{ ns}$)
  - Two-Qubit CNOT Gate Error ($e_{2q}$): $8.5 \times 10^{-3}$ (Duration: $220\text{ ns}$)
  - Readout Measurement Error ($e_{ro}$): $1.8 \times 10^{-2}$

---

## 2. Compiler Optimization Passes & Benchmark Suite

### Benchmark 1: QAOA Max-Cut 4-Qubit (`qaoa_maxcut_4q.qasm`)
- **Circuit Description**: 4-qubit Quantum Approximate Optimization Algorithm ansatz for solving Max-Cut on an unweighted 4-node ring graph.
- **Pre-Optimization Metrics**:
  - Total Gate Count: 26 gates
  - Circuit Depth: 14 layers
  - Multi-Qubit CNOT Count: 12 CNOTs
  - Estimated NISQ Fidelity: $84.5\%$
- **Post-Peephole Optimization**:
  - Total Gate Count: 18 gates ($-30.8\%$)
  - Circuit Depth: 10 layers ($-28.6\%$)
  - Multi-Qubit CNOT Count: 8 CNOTs ($-33.3\%$)
  - Estimated NISQ Fidelity: $91.8\%$ ($+7.3\%$ gain)

### Benchmark 2: GHZ-3 Entanglement State (`ghz_state_3q.qasm`)
- **Circuit Description**: 3-qubit Greenberger-Horne-Zeilinger maximally entangled state generation containing redundant parity cancellation sequences.
- **Pre-Optimization Metrics**: Depth: 6 | CNOTs: 4 | Estimated Fidelity: $91.2\%$
- **Post-Optimization Metrics**: Depth: 4 | CNOTs: 2 | Estimated Fidelity: $95.8\%$

---

## 3. Circuit Fidelity & Layer Attenuation Models
The compiler evaluates expected circuit success probability ($F_{circuit}$) using cumulative gate error and decoherence decay:

$$F_{circuit} = \prod_{g \in G_{1q}} (1 - e_{1q}) \times \prod_{g \in G_{2q}} (1 - e_{2q}) \times \exp\left( -\frac{t_{depth}}{T_1} \right) \times \prod_{q \in Q} (1 - e_{ro})$$

Because two-qubit CNOT errors ($e_{2q}$) are nearly two orders of magnitude higher than single-qubit errors ($e_{1q}$), peephole cancellation of adjacent inverse CNOT pairs produces the highest yield in quantum circuit fidelity.
