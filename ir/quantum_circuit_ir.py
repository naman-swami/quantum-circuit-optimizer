"""
Quantum Intermediate Representation (QIR)
Abstract representation of quantum circuits with gate DAG and parameter tracking.
"""
from typing import List, Dict, Any

class QuantumGate:
    def __init__(self, name: str, qubits: List[int], params: List[float] = None):
        self.name = name.upper()
        self.qubits = qubits
        self.params = params or []

    def __eq__(self, other):
        if not isinstance(other, QuantumGate):
            return False
        return self.name == other.name and self.qubits == other.qubits and self.params == other.params

    def __repr__(self):
        p_str = f"({', '.join(str(p) for p in self.params)})" if self.params else ""
        q_str = f"[{', '.join(str(q) for q in self.qubits)}]"
        return f"{self.name}{p_str}{q_str}"

class QuantumCircuitIR:
    def __init__(self, num_qubits: int = 4):
        self.num_qubits = num_qubits
        self.gates: List[QuantumGate] = []

    def add_gate(self, name: str, qubits: List[int], params: List[float] = None):
        self.gates.append(QuantumGate(name, qubits, params))

    @classmethod
    def from_qasm_file(cls, filepath: str) -> "QuantumCircuitIR":
        circuit = cls()
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("//") or line.startswith("OPENQASM") or line.startswith("include") or line.startswith("creg") or line.startswith("measure"):
                    continue
                if line.startswith("qreg"):
                    # parse size
                    parts = line.split("[")
                    if len(parts) > 1:
                        size = int(parts[1].split("]")[0])
                        circuit.num_qubits = size
                    continue

                clean = line.rstrip(";")
                if clean.startswith("h "):
                    q = int(clean.split("[")[1].split("]")[0])
                    circuit.add_gate("H", [q])
                elif clean.startswith("cx "):
                    targets = clean.split()[1].split(",")
                    q0 = int(targets[0].split("[")[1].split("]")[0])
                    q1 = int(targets[1].split("[")[1].split("]")[0])
                    circuit.add_gate("CX", [q0, q1])
                elif clean.startswith("rz("):
                    param_val = float(clean.split("(")[1].split(")")[0])
                    q = int(clean.split("[")[1].split("]")[0])
                    circuit.add_gate("RZ", [q], [param_val])
        return circuit

    def count_2q_gates(self) -> int:
        return sum(1 for g in self.gates if len(g.qubits) > 1)

    def count_1q_gates(self) -> int:
        return sum(1 for g in self.gates if len(g.qubits) == 1)
