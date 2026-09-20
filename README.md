# QuBit — Quantum Circuit Synthesis & Gate Depth Minimizer

[![OpenGAP Compliant](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](https://opengap.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Autonomous quantum compilation assistant optimizing unitary circuit decompositions, qubit topology mapping, and error-mitigated gate synthesis.

## Domain Category
**Developer tools**

## Architecture
- **OpenGAP Specification**: `0.1.0`
- **Role**: Quantum Information Scientist & Compiler Engineer
- **Primary Goal**: Map abstract OpenQASM quantum algorithms to physical NISQ heavy-hex superconducting architectures with minimal CNOT depth and swap overhead.

## Skills Included
- **`circuit-depth-reduction`**: Applying commutation rules, peephole optimizations, and Clifford+T synthesis to reduce circuit execution depth.
- **`qubit-routing-mapping`**: Solving Sabre Swap graph layout problems to embed multi-qubit gates into hardware coupling constraints.
- **`readout-error-mitigation`**: Constructing inverted assignment calibration matrices to correct measurement readout distortion.

## Tools Schema
- **`synthesize-clifford-t`**: Decompose arbitrary unitary rotation gates into canonical single-qubit gates and T-depth minimized sequences.
- **`optimize-swap-routing`**: Compute minimal SWAP insertion schedule for a directed coupling graph architecture.
- **`compute-circuit-fidelity`**: Estimate total circuit quantum volume and randomized benchmarking survival probability.

## Explainability & Verification
Full explainability compliance under OpenGAP Checkpoint 2 is detailed in [EXPLAINABILITY.md](EXPLAINABILITY.md), covering:
- Decision Reasoning
- Data Sources and Inputs Used
- Confidence Scoring Methodology
- Source Attribution Protocol
- Bias Awareness
- Limitation Taxonomy per Domain
- Uncertainty Quantification Approach

## Multi-Framework Compatibility
Adapters and visa export configurations are included in `exports/`:
- Anthropic Claude (`claude-system-prompt.txt`)
- OpenAI Assistants (`openai-assistant.json`)
- LangChain (`langchain-agent.json`)
- CrewAI (`crewai-agent.json`)
- AutoGen (`autogen-agent.json`)

## License
MIT License
