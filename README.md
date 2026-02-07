Quantum Chip Design and Simulation

This repository contains the work for the design and simulation of a prototype quantum computing chip based on a superconducting transmon qubit architecture. The goal of this project is to demonstrate the complete design-to-validation workflow of a small-scale quantum chip using open-source simulation tools, without performing physical fabrication.

A 5-qubit linear topology was selected to model realistic qubit interactions while keeping the design simple and scalable. The project focuses on quantum circuit design, simulation of gate operations, analysis of noise and decoherence effects, and development of a conceptual, fabrication-aware chip layout.

What was done in this project

Designed a 5-qubit quantum circuit representing the logical behavior of a quantum chip

Implemented single-qubit and two-qubit gates to demonstrate quantum operations and entanglement

Performed ideal quantum simulations to verify correct gate execution

Performed noise-aware simulations using depolarizing noise models to study decoherence effects

Designed a conceptual physical layout including qubits, readout resonators, coupling bus, and control lines

Documented a standard fabrication process flow at the design level

All validation was performed through simulation.

Tools and Technologies Used

Python – programming language

Qiskit – quantum circuit design and simulation

Qiskit Aer – simulator backend

Matplotlib – visualization of measurement results

All tools used are open-source.

How to run the simulations

Install required dependencies:

pip install qiskit qiskit-aer matplotlib


Run the ideal quantum simulation:

python sim.py


Run the noise-aware simulation:

python noise.py


The simulations generate measurement histograms that demonstrate circuit behavior under ideal and noisy conditions.

Results Summary

Successful validation of single-qubit and two-qubit gate operations

Clear demonstration of multi-qubit entanglement

Expected degradation in output fidelity under noise

Design verified to be compatible with superconducting fabrication constraints

Scope and Limitations

This project is limited to design and simulation-based validation

No physical fabrication or experimental testing was performed

Noise models are simplified representations of real hardware behavior

Future work includes electromagnetic simulation, physical fabrication, cryogenic testing, and experimental benchmarking.
