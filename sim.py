from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
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