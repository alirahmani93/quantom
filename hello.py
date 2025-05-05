import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives import Sampler, StatevectorSampler

from qiskit_serverless import save_result
# from qiskit_serverless import *
# from qiskit_ibm_runtime import *

qc = QuantumCircuit(3)
print(f"{qc=}")
# print(f"{qc.h(0).add(qc.h(1))=}")
print(f"{qc.p(np.pi / 2, 0)=}")
print(f"{qc.cx(0, 2)=}")
print(f"{qc.cx(1, 2)=}")
print(f"{qc.cx(0, 1)=}")
print(f"{qc.ch(0, 1)=}")

qc_measured = qc.measure_all(inplace=False)
print(qc_measured)

sampler = StatevectorSampler()
job = sampler.run([qc_measured],shots=1000)
print(job)
result = job.result()
print(result)
# save_result(quasi_dists)


from qiskit.quantum_info import SparsePauliOp
operator = SparsePauliOp.from_list([("XZY", 1), ("XYX", 1), ("YXX", 1), ("YYY", -1)])
print(operator)


from qiskit.primitives import StatevectorEstimator
estimator = StatevectorEstimator()
job = estimator.run([(qc, operator)], precision=1e-3)
result = job.result()
print(f" > Expectation values: {result[0].data.evs}")


from qiskit import transpile
qc_transpiled = transpile(qc, basis_gates = ['cz', 'sx', 'rz'], coupling_map =[[0, 1], [1, 2]] , optimization_level=3)
print(qc_transpiled)