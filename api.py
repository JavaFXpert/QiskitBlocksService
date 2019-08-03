#
# Copyright 2019 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, BasicAer, execute


def run_qasm(qasm, backend_to_run='qasm_simulator', num_shots_str='1'):
    circuit = QuantumCircuit.from_qasm_str(qasm)
    backend = BasicAer.get_backend(backend_to_run)
    job_sim = execute(circuit, backend, shots=int(num_shots_str))
    result_sim = job_sim.result()
    return result_sim.get_counts(circuit)


def get_statevector(qasm, backend_to_run='statevector_simulator'):
    circuit = QuantumCircuit.from_qasm_str(qasm)
    backend = BasicAer.get_backend(backend_to_run)
    job_sim = execute(circuit, backend)
    result_sim = job_sim.result()
    output_state = result_sim.get_statevector(circuit, decimals=3)
    return output_state
