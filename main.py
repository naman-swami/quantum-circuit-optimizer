import argparse
import os
from ir.quantum_circuit_ir import QuantumCircuitIR
from passes.peephole_pass import PeepholeCancellationPass, NISQFidelityEstimator

def main():
    parser = argparse.ArgumentParser(description="Quantum Circuit Optimizer CLI")
    parser.add_argument("--demo", action="store_true", help="Optimize QAOA benchmark circuit")
    parser.add_argument("--qasm", type=str, help="Path to input .qasm file")
    args = parser.parse_args()

    benchmarks_dir = os.path.join(os.path.dirname(__file__), "benchmarks")

    if args.demo or args.qasm:
        path = args.qasm if args.qasm else os.path.join(benchmarks_dir, "qaoa_maxcut_4q.qasm")
        circuit = QuantumCircuitIR.from_qasm_file(path)
        f_pre = NISQFidelityEstimator.estimate(circuit)

        print("=== QUANTUM CIRCUIT OPTIMIZATION REPORT ===")
        print(f"Target Circuit: {path}")
        print(f"Initial Gate Count: {len(circuit.gates)} (1Q: {circuit.count_1q_gates()}, 2Q: {circuit.count_2q_gates()})")
        print(f"Pre-Optimization Fidelity: {f_pre * 100:.2f}%\n")

        pass_opt = PeepholeCancellationPass()
        stats = pass_opt.run(circuit)
        f_post = NISQFidelityEstimator.estimate(circuit)

        print(f"Peephole Pass Result:")
        print(f"  Cancelled Redundant Gates: {stats['cancelled_gates']}")
        print(f"  Final Gate Count: {stats['optimized_gate_count']}")
        print(f"  Post-Optimization Fidelity: {f_post * 100:.2f}%")
        print(f"  Fidelity Gain: +{(f_post - f_pre) * 100:.2f}%\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
