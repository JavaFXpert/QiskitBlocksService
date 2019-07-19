from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, BasicAer, execute


def run_qasm(qasm, backend_to_run='qasm_simulator'):
    circuit = QuantumCircuit.from_qasm_str(qasm)
    backend = BasicAer.get_backend(backend_to_run)
    job_sim = execute(circuit, backend, shots=1)
    result_sim = job_sim.result()
    return result_sim.get_counts(circuit)


def get_statevector(qasm, backend_to_run='statevector_simulator'):
    circuit = QuantumCircuit.from_qasm_str(qasm)
    backend = BasicAer.get_backend(backend_to_run)
    job_sim = execute(circuit, backend)
    result_sim = job_sim.result()
    output_state = result_sim.get_statevector(circuit, decimals=3)
    return output_state
