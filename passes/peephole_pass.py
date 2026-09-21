"""
Quantum Circuit Optimization Passes
Implements peephole CNOT cancellation and NISQ fidelity estimation.
"""
from typing import Dict, Any, List
from ir.quantum_circuit_ir import QuantumCircuitIR, QuantumGate

class PeepholeCancellationPass:
    def run(self, circuit: QuantumCircuitIR) -> Dict[str, Any]:
        original_count = len(circuit.gates)
        optimized_gates: List[QuantumGate] = []
        cancelled_count = 0

        i = 0
        while i < len(circuit.gates):
            # CNOT self-inverse: CX(q0, q1) * CX(q0, q1) = Identity
            if i + 1 < len(circuit.gates):
                g1 = circuit.gates[i]
                g2 = circuit.gates[i+1]
                if g1.name in ["CX", "CNOT", "H"] and g1 == g2:
                    cancelled_count += 2
                    i += 2
                    continue
            optimized_gates.append(circuit.gates[i])
            i += 1

        circuit.gates = optimized_gates
        return {
            "initial_gate_count": original_count,
            "optimized_gate_count": len(circuit.gates),
            "cancelled_gates": cancelled_count,
            "compression_ratio": round(len(circuit.gates) / max(1, original_count), 3)
        }

class NISQFidelityEstimator:
    @staticmethod
    def estimate(circuit: QuantumCircuitIR, f_1q: float = 0.9995, f_2q: float = 0.9920) -> float:
        n_1q = circuit.count_1q_gates()
        n_2q = circuit.count_2q_gates()
        fidelity = (f_1q ** n_1q) * (f_2q ** n_2q)
        return round(fidelity, 4)
