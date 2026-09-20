import pytest
from src.quantum_engine import QuantumCircuitOptimizerEngine

def test_cnot_peephole_cancellation():
    engine = QuantumCircuitOptimizerEngine()
    gates = ["H(0)", "CNOT(0,1)", "CNOT(0,1)", "H(1)"]
    res = engine.optimize_cnot_chain(gates)
    assert res["cancelled_redundant_gates"] == 2
    assert res["cnot_gate_count"] == 0
    assert res["optimized_gate_count"] == 2
