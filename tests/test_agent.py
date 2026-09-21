import os
import pytest
from ir.quantum_circuit_ir import QuantumCircuitIR, QuantumGate
from passes.peephole_pass import PeepholeCancellationPass, NISQFidelityEstimator

def test_ir_parsing_from_qasm():
    bench_dir = os.path.join(os.path.dirname(__file__), "..", "benchmarks")
    qasm_path = os.path.join(bench_dir, "ghz_state_3q.qasm")
    circuit = QuantumCircuitIR.from_qasm_file(qasm_path)
    assert circuit.num_qubits == 3
    assert len(circuit.gates) == 3
    assert circuit.count_1q_gates() == 1
    assert circuit.count_2q_gates() == 2

def test_peephole_cnot_cancellation():
    circuit = QuantumCircuitIR(2)
    circuit.add_gate("H", [0])
    circuit.add_gate("CX", [0, 1])
    circuit.add_gate("CX", [0, 1]) # Redundant pair
    circuit.add_gate("H", [1])
    
    pass_opt = PeepholeCancellationPass()
    stats = pass_opt.run(circuit)
    
    assert stats["cancelled_gates"] == 2
    assert stats["optimized_gate_count"] == 2
    assert len(circuit.gates) == 2

def test_fidelity_estimation():
    circuit = QuantumCircuitIR(2)
    circuit.add_gate("H", [0])
    circuit.add_gate("CX", [0, 1])
    f = NISQFidelityEstimator.estimate(circuit, f_1q=0.999, f_2q=0.990)
    expected = round(0.999 * 0.990, 4)
    assert f == expected
