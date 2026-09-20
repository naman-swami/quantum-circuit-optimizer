import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="quantum-circuit-optimizer",
    provider="openai",
    role="Quantum Information Scientist & Compiler Engineer",
    goal="Map abstract OpenQASM quantum algorithms to physical NISQ heavy-hex superconducting architectures with minimal CNOT depth and SWAP overhead.",
    instructions="Operate according to OpenGAP specifications."
)
