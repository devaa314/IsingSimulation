# The Theory behind the (Classical) Ising Model
Before getting into the simulating the Ising Model using the Metropolis-Hastings algorithm, it is worth discussing the basic theory of the Ising Model including it's Hamiltonian, an exact 1D solution and mean-field theory (MFT).

## Table of Contents
1. [The Hamiltonian](#the-hamiltonian)
2. [Statistical Mechanics](#statistical-mechanics)
3. [Reduced Quantities and Notation](#reduced-quantities-and-notation)

## 1: The Hamiltonian
The Ising model, named after Ernst Ising, is significant in condensed matter physics because it is a mathematical model of ferromagnetism in statistical mechanics. Indeed, at a certain critical temperature, $T_c$, it exhibits a **magnetic phase transition**. The system exhibits ferromagnetism at temperatures below $T_c$ and can only sustain paramagnetism at temperatures above $T_c$ when exposed to external magnetic field $\vec{B}$. 

As one may expect, the net magnetisation of a system, like a metal, comes from the contribution of the individual magnetic moments of the particles contained therein. In a metal, like iron, the particles would consist of neutrons, protons and electrons. Each type of particle possesses their own magnetic moment. However, we may safely ignore the magnetic moments of neutrons and protons due to their significantly heavier masses when compared to the electron. In this case, we will assume the electrons have no orbital angular momentum, and thus its total angular momentum entirely comes from its spin angular momentum. 

The Ising model assumes we may model the system as a square lattice of electrons exposed to a uniform magnetic field $\vec{B}$, namely, pointing in the same direction and has the same mangnitude everywhere in the system; for simplicity we will orient our coordinates so that the magnetic field points in the $z$ direction so that $\vec{B} = B\hat{z}$. Consider a lattice of $N \times N$ electrons where we index the electrons with $i$. To write down the Ising Hamiltonian, we have to consider two types of interactions. The first type is the interaction of the electrons' magnetic moments with the external magnetic field. Since the magnetic field points in the $z$ direction and we are going to be interested in the magnetisation in the $z$ direction, we can assume each electron collapsed into one of the two eigenstates of the Pauli matrix $\sigma_z$ with eigenvalues $\pm 1$ at any given time. Thus, in this model, we can assign each electron a dimensionless spin variable $s_i \in \{+1, -1\}$. Thus, we have that the energy of the this interaction is given by

$$
-\mu_B Bs_i.
$$

where $\mu_B$ is the Bohr magneton. Note that we have implicitly cancelled out $\hbar$ and the g-factor here because we chose to work with the dimensionless spin variables $s_i$ instead of actual spin angular momenta $\pm \hbar/2$. The Hamiltonian will include such a term for each electron: $-\mu_B B\sum_is_i$. If the Hamiltonian only contained these terms, the system would not exhibit any ferromagnetism and would not be interesting. This is where the other type of term, the interaction terms, come in. In the Ising model, we only consider nearest neighbour interactions. We write the interaction strength to be $J$. Given nearest neighbour electrons $i$ and $j$, they have interaction energy

$$
-Js_is_j.
$$

We will further assume, quite justifiably, that all nearest neighbour interactions have the same strength. This is reasonable in a homogenous material. Thus, we arrive at the Ising model Hamiltonian

$$
H = -J\sum_{(i, j)}s_is_j -\mu_B B\sum_is_i
$$

where $(i, j)$ only ranges over nearest neighbour pairs. We will denote a particular configuration of spins $(s_1, s_2, \dots, s_N)$ by $s$ without an index.

## 2: Statistical Mechanics
Now that we have a classical ensemble of states, we may apply the Boltzmann distribution to assign probabilities to each microstate (spin coniguration)
$$
P(s) \propto \exp\left\{\frac{-H(s)}{k_BT}\right\} \Rightarrow P(s) = \frac{\exp\left\{\frac{-H(s)}{k_BT}\right\}}{Z}
$$

where $k_B$ is the Boltzmann constant, $T$ is temperature and $Z$ is the partition function

$$
Z = \sum_s \exp\left\{\frac{-H(s)}{k_BT}\right\}.
$$

$Z$ is really the pricipal quantity of interest. From it, *all* information about the system, including macroscopic properties which we care about, may be derived. Later on, we will want to classify the magnetic phase transition using the Ehrenfest classification so it would be good to compute the free energy as well. It is well known that the free energy is given by

$$
F = -k_b T \ln Z.
$$

Note the magnetisation can be written in terms of $F$. Indeed, the macroscopic magnetisation is the expected value of the magnetisation of each spin configuration. Thus, it can simply be written as

$$
M = -\frac{\mu_B}{N Z} \sum_s\exp\left\{\frac{-H(s)}{k_BT}\right\}\left[\sum_i s_i\right].
$$

Then if we write down the free energy in its full form

$$
F = -k_bT\ln\left[\sum_s \exp\left\{\frac{-H(s)}{k_BT}\right\}\right]
$$

and then evaluate the partial derivative $\partial F/ \partial B$, we exactly find

$$
M = \frac{1}{N} \frac{\partial F}{\partial B}.
$$

What we observe in experiments is the magnetisation does vary continuously as we vary temperature when $B$ is fixed. However, when temperature is brought below $T_c$, we will observe that the magnetisation suddenly starts rising in magnitude. Thus, we observe a discontinuity in the second derivative, or more commonly known as the magnetic susceptibility $\chi$

$$
\chi = \frac{\partial M}{\partial B} = \frac{1}{N}\frac{\partial^2 F}{\partial B^2}.
$$

Hence, under the Ehnrenfest classification, this magnetic phase transition is a second-order phase transition; our simulation will verify this.

## 3: Reduced Quantities and Notation
To conlude this small introduction, we will introduce some reduced quantities and notation to simplify the simulation. We choose to work with a reduced dimensional Hamiltonian $-\beta H$

$$
-\beta H = \frac{J}{k_bT}\sum_{(i, j)}s_is_j + \frac{\mu_B B}{k_bT} \sum_is_i.
$$

We will further define dimensionless quantities $K = J/k_bT$ and $h = {\mu_B B}/{k_bT}$ so we can write

$$
-\beta H = K\sum_{(i, j)}s_is_j + h \sum_is_i.
$$