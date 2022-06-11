"""
QCG Open Project: Solving Boolean SAT Problem using Grover's Algorithm
Creator: Anikesh Parashar
GitHub: an1k3sh
"""

A=4
B=3
C=2
D=1
E=0

#Importing the Required Libraries
from qiskit import *
import matplotlib.pyplot as plt
import numpy as np

#Defining the Oracle Circuit
oracle=QuantumCircuit(5,name='oracle')
oracle.x(2) #X Gate
oracle.h(2) #Hadamard Gate
oracle.mct([0,1],2) #Multi-Controlled Toffoli Gate
oracle.h(2) #Hadamard Gate
oracle.x(2) #X Gate
oracle.x(4) #X Gate
oracle.h(4) #Hadamard Gate
oracle.mct([0,1,2,3],4) #Multi-Controlled Toffoli Gate
oracle.h(4) #Hadamard Gate
oracle.x(4) #X Gate
oracle.to_gate()

#Defining Reflection Circuit
reflection=QuantumCircuit(5,name='reflection')
reflection.h([0,1,2,3,4]) #Hadamard Gate
reflection.x([0,1,2,3,4]) #X Gate
reflection.h(4) #Hadamard Gate
reflection.mct([0,1,2,3],4)  #Multi-Controlled Toffoli Gate
reflection.h(4) #Hadamard Gate
reflection.x([0,1,2,3,4]) #X Gate
reflection.h([0,1,2,3,4]) #Hadamard Gate
reflection.to_gate()

#Backend using StateVector and QASM Simulator
sv_backend=Aer.get_backend('statevector_simulator')
qasm_backend=Aer.get_backend('qasm_simulator')

#Final Quantum Circuit
circ=QuantumCircuit(5,5) #Quantum Circuit with 5 Quantum Registers and 5 Classical Registers
circ.h([A,B,C,D,E])  #Hadamard Gate
circ.append(oracle,[A,B,C,D,E]) #Appending Oracle Circuit
circ.append(reflection,[A,B,C,D,E]) #Appending Reflection Circuit
circ.append(oracle,[A,B,C,D,E]) #Appending Oracle Circuit
circ.append(reflection,[A,B,C,D,E]) #Appending Reflection Circuit

#Measurement of State-Vectors for each Quantum State
job1=execute(circ,sv_backend)
result1=job1.result()
sv=result1.get_statevector()
print("TABLE 1: STATE VECTORS")
print("+"+(23*"-")+"+")
print("| State Vectors\t\t|")
print("+"+(23*"-")+"+")
for i in list(np.around(sv,10)):
    print("| "+str(i)+"\t|")
print("+"+(23*"-")+"+")

circ.measure([A,B,C,D,E],[A,B,C,D,E]) #Measurement of each qubit

#Measurement of Quantum State to which the system collapses for finite measurements/shots
shot_count=1000000
job2=execute(circ,qasm_backend,shots=shot_count)
result2=job2.result()
counts=result2.get_counts()

#Printing the Occurence Statistics of the states
print("\nTABLE 2: STATISTICS")
print("(Shots: "+str(shot_count)+")")
print("+"+(15*"-")+"+"+(23*"-")+"+")
print("| Quantum State\t| Number of Occurences\t|")
print("+"+(15*"-")+"+"+(23*"-")+"+")
for i in counts:
    print("| "+i+"\t\t| "+"{:6d}".format(counts[i])+"\t\t|")
print("+"+(15*"-")+"+"+(23*"-")+"+")

states=list(counts.keys())
probabilities=list(np.divide(np.array(list(counts.values())),shot_count))

#Plot of Probability for each Quantum State
fig=plt.figure(figsize=[15,7.5])
bar_plot=plt.bar(states,probabilities,color='blue',width=0.8)
plt.bar_label(bar_plot,label_type='edge',rotation='vertical',padding=3)
plt.ylim(0,0.2)
plt.xlabel('States')
plt.ylabel('Probabilities')
plt.xticks(rotation=45)
plt.title('Possible Invitation Combinations')
plt.show()