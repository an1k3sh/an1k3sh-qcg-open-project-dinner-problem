# QCG Open Project - Solving Boolean SAT Problem using Grover’s Algorithm

Link for [Problem Statement](https://app.simplenote.com/p/Pbbh5y)

The project makes the use of Grover's Algorithm to solve a dinner problem thrown by Frank to celebrate Alice and Bob's engagement, involving 5 friends: Alice (A), Bob (B), Charles (C), Dave (D) and Eve (E), such that:
 * Alice and Bob always come (since the party is thrown for them)
 * Charles comes only if Dave comes without Eve.

This problem can be represented algebraically by the equation: `f = A·B·(C'+D·E') = A·B·(C'+C·D·E') = A·B·C' + A·B·C·D·E'`

The set of values `(A,B,C,D,E)` where the value of `f` is 1 (True) satisfy the conditions and are a viable invitation condition.

To solve the problem using Quantum Computing, [Grover's Algorithm](https://www.youtube.com/watch?v=0RPFWZj7Jm0) is used. The quantum circuit used 5 qubits, where each qubits denotes a particular friend, in the order `[Alice-Bob-Charles-Dave-Eve]`.

## Quantum Circuits

### Oracle Circuit

The Oracle circuit is used to invert the amplitudes of those states which satsfy the condition.

First, the states where `A·B·C'` is 1 (True) are inverted. This requires a series of gates which change `|C› = |0›` to `|C› = -|0›` if `|A› = |B› = |1›`, while no change happens if `|C› = |1›`.

It is implemented by using and X gate on the the qubit representing C to change `|0›` state to `|1›` and `|1›` state to `|0›`, followed by a multi-controlled Z gate with A and B as controls to invert the phase if `|A› = |B› = |1›` and using another X gate on C to get back to the original state with the amplitude modified accordingly. The multi-controlled Z gate is constructed by using an Hadamard gate followed by a multi-controlled Toffoli gate (with A and B) as controls.

Next, similar operations are performed to invert the states where `A·B·C·D·E'` is 1 (True). This requires a series of gates which change `|E› = |0›` to `|E› = -|0›` if `|A› = |B› = |C› = |D› = |1›`, while no change happens if `|E› = |1›`.

It is implemented by using and X gate on the the qubit representing E to change `|0›` state to `|1›` and `|1›` state to `|0›`, followed by a multi-controlled Z gate with A, B, C and D as controls to invert the phase if `|A› = |B› = |C› = |D› = |1›` and using another X gate on E to get back to the original state with the amplitude modified accordingly. The multi-controlled Z gate is constructed by using an Hadamard gate followed by a multi-controlled Toffoli gate (with A, B, C and D) as controls.

### Reflector Circuit

A detailed explanation of the reflector circuit can be found [here](https://qiskit.org/textbook/ch-algorithms/grover.html#3.1-Qiskit-Implementation-)

### Final Circuit

There are 5 expected solution states (4 states through the expression `A·B·C'` and 1 through `A·B·C·D·E'`, and these two expressions can never be satisfied simultaneously).

Time complexity of Grover's Algorithm = `O(√(N/M))`
where, `N` = No. of input states and `M` = No. of solution states

For this problem, there are 2<sup>5</sup> = 32 cases(states) possible, out of which 5 are the solutions (`N = 32` and `M = 5`). Thus, 2 iterations over the oracle-reflector pair is required.

Conclusively, the main quantum circuit consists of an Hadamard Gate for each qubit and the oracle and reflector circuits twice pairwise.

## Measurements and Output

The final state vector is measured for each state and the state to which the system collapses is measured for a finite number of measurement shots.

The ouput consists of:
 * State-Vector Table
 * Occurence Statistics Table
 * Probability v/s State plot
