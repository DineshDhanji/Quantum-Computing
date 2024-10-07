from qiskit.circuit import Parameter, ParameterVector
from qiskit import QuantumCircuit


def ansatz_kazuma(num_qubits, reps):
    parameters = ParameterVector("θ", num_qubits * (reps + 1))
    circuit = QuantumCircuit(num_qubits, name="Kazuma")

    # for i in range(num_qubits):
    #     circuit.h(i)

    for layer in range(reps):
        # Apply parameterized Ry gates
        for i in range(num_qubits):
            circuit.ry(parameters[num_qubits * layer + i], i)

        # Apply entangling CNOT gates between neighboring qubits
        for i in range(num_qubits - 1):
            circuit.cx(i, i + 1)

    #     # Apply additional layer of Rz gates
        for i in range(num_qubits):
            circuit.rz(parameters[num_qubits * reps + i], i)

    # for i in range(num_qubits):
    #     circuit.h(i)

    return circuit

def ansatz_aqua(num_qubits, reps):
    # Adjusting the size of ParameterVector to fit all layers
    parameters = ParameterVector("θ", num_qubits * (3 * reps + 3))
    circuit = QuantumCircuit(num_qubits, name="Kazuma")
    
    # Initial layer with parameterized single-qubit rotations (Rx, Ry, Rz)
    for i in range(num_qubits):
        circuit.rx(parameters[i], i)
        circuit.ry(parameters[num_qubits + i], i)
        circuit.rz(parameters[2 * num_qubits + i], i)

    # Repeated layers with entanglement and rotations
    for layer in range(reps):
        # Parameterized Ry gates
        for i in range(num_qubits):
            circuit.ry(parameters[3 * num_qubits + num_qubits * layer + i], i)
        
        # Entangling CNOT gates
        for i in range(num_qubits - 1):
            circuit.cx(i, i + 1)
        # Optionally, entangle the last and first qubit
        circuit.cx(num_qubits - 1, 0)

        # Additional parameterized Rx and Rz gates
        for i in range(num_qubits):
            circuit.rx(parameters[3 * num_qubits + num_qubits * (layer + 1) + i], i)
            circuit.rz(parameters[3 * num_qubits + num_qubits * (layer + 1) + i], i)

    # Final layer with parameterized single-qubit rotations (Rx, Ry, Rz)
    for i in range(num_qubits):
        circuit.rx(parameters[-3 * num_qubits + i], i)
        circuit.ry(parameters[-2 * num_qubits + i], i)
        circuit.rz(parameters[-num_qubits + i], i)

    return circuit