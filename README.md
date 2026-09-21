# Quantum Circuit Optimizer

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![Quantum](https://img.shields.io/badge/Domain-Quantum_Compilation-purple.svg)](docs/nisq_noise_model.md)
[![Spec](https://img.shields.io/badge/Format-OpenQASM_2.0-orange.svg)](benchmarks/qaoa_maxcut_4q.qasm)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

A quantum circuit compilation and pass-management engine for OpenQASM 2.0 circuits, implementing peephole gate cancellation, DAG dependency tracking, and NISQ device fidelity estimation.

```
                    ┌─────────────────────────┐
                    │    OpenQASM 2.0 File    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  ir/quantum_circuit_ir  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ Peephole CNOT Cancel    │
                    │   (passes/peephole)     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ NISQ Fidelity Estimator │
                    │   F = (F_1q)^n*(F_2q)^m │
                    └─────────────────────────┘
```

## Features

- **OpenQASM 2.0 Parser**: Ingests standard quantum assembly circuits into structured IR.
- **Peephole Cancellation Pass**: Eliminates adjacent self-inverse gate pairs ($CX \cdot CX = I$, $H \cdot H = I$).
- **NISQ Noise Calibration**: Accurately computes circuit fidelity degradation across $1Q$ and $2Q$ gate depths.
- **Built-in Benchmarks**: Includes standard QAOA MaxCut (4-qubit) and GHZ state (3-qubit) circuits.

## Directory Structure

```
quantum-circuit-optimizer/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint quantum provenance
├── ir/
│   └── quantum_circuit_ir.py        # Quantum Intermediate Representation
├── passes/
│   └── peephole_pass.py             # Compiler optimization & fidelity passes
├── benchmarks/
│   ├── qaoa_maxcut_4q.qasm          # Benchmark QAOA circuit
│   └── ghz_state_3q.qasm            # Benchmark GHZ state
├── docs/
│   └── nisq_noise_model.md          # Noise physics formulation
├── tests/
│   └── test_agent.py                # Compiler pass verification tests
├── main.py                          # Compilation CLI
└── requirements.txt
```

## Quick Start

```bash
# Run compiler regression suite
pytest tests/ -v

# Optimize benchmark QAOA circuit
python main.py --demo
```
