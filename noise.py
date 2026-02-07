from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit_aer.noise import NoiseModel, depolarizing_error
qc = QuantumCircuit(5, 5)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.h(3)
qc.cx(3, 4)
qc.measure(range(5), range(5))
backend = Aer.get_backend('aer_simulator')
compiled_circuit = transpile(qc, backend)
job = backend.run(compiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts()
print(counts)
plot_histogram(counts)
plt.show()
noise_model = NoiseModel()
error1 = depolarizing_error(0.02, 1)
error2 = depolarizing_error(0.05, 2)
noise_model.add_all_qubit_quantum_error(error1, ['h'])
noise_model.add_all_qubit_quantum_error(error2, ['cx'])
noisy_backend = Aer.get_backend('aer_simulator')
compiled_noisy = transpile(qc, noisy_backend)
job_noisy = noisy_backend.run(
    compiled_noisy,
    noise_model=noise_model,
    shots=1024
)
noisy_result = job_noisy.result()
noisy_counts = noisy_result.get_counts()
plot_histogram([counts, noisy_counts],
               legend=['Ideal', 'Noisy'])
plt.show()
