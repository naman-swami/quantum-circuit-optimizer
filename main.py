import json
import argparse
from src.quantum_engine import QuantumCircuitOptimizerEngine

def main():
    parser = argparse.ArgumentParser(description="Quantum Circuit Optimizer CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated CNOT cancellation & NISQ fidelity calculation")
    args = parser.parse_args()

    engine = QuantumCircuitOptimizerEngine()
    gates = ["H(0)", "CNOT(0,1)", "CNOT(0,1)", "RZ(1)", "CNOT(1,2)", "H(2)"]
    report = engine.optimize_cnot_chain(gates)
    print("="*60)
    print(" QUBIT QUANTUM COMPILATION AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
