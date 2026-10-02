# Solving the 1D Ising Model using the Transfer Matrix
Although the focus of this repository is to simulate the 2D Ising model with the Metropolis-Hastings algorithm, it is a rather fun mathematical exercise to solve the 1D system exactly. We will use the same method used by Lars Onsager to exactly solve the 2D model, namely, by use of the transfer matrix and periodic boundary conditions.

# 1. Periodic Boundary Conditions
While we generally work with metals or materials in real life, we often think of them as linear objects. That is, they have start and an end. Like a metal block or rod. This is known as free boundary conditions. However, mathematically, it is often more convenient to work with periodic boundary conditons where we assume the system is the system's edges are identified. Depending on the dimension, this is equivalent to viewing the system as a circle, torus etc. The reason we do so is because this often makes the computations much cleaner. 

In the 1D Ising model, this manifests as intepreting that the 1st electron and the last electron are nearest neighbours. So instead of visualising the electrons in a line, we visualise them as lying on a circle. Thus, when we view the Ising Hamiltonian (see ./ising_theory.md)

$$
-\beta H = K\sum_{(i, j)}s_is_j + h\sum_i s_i,
$$

the interaction term will consist of an extra term, namely, $Ks_1s_N$ reflecting that they are now nearest neighbours. Therefore, we can write this as

$$
-\beta H = K\sum_{i=1}^n s_i s_{i+1} + h \sum_{i=1}^N s_i
$$

where we intepret $s_{N+1} = s_1$. Indeed, this is exactly as found in [^1]. 

# 2. The Transfer Matrix
Consider the terms in the sum that give the partition function. They will be of the form

$$
\exp \{K\}
$$

## Sources
[^1]: Folk, R et al. (2024). "Ising's roots and transfer-matrix eigenvalues." 6-9.