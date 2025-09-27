# Foundations Problem Set – Quantum Mechanics Basics

These problems introduce the key concepts and mathematical tools of quantum mechanics.  Start by ensuring you understand the definitions and techniques involved, then attempt the calculations.  If you get stuck, consult Griffiths’ *Introduction to Quantum Mechanics* or lecture notes from your course.

1. **Normalization:** The wavefunction \(\psi(x) = A e^{-\alpha x^2}\) describes a particle on the real line.  Find the normalization constant \(A\) in terms of \(\alpha\).

2. **Probability:** A particle in one dimension has wavefunction \(\psi(x) = \sqrt{\frac{2}{L}}\,\sin\big(\frac{\pi x}{L}\big)\) for \(0 < x < L\) and zero elsewhere.  What is the probability of finding the particle between \(x = 0\) and \(x = L/2\)?

3. **Expectation value:** For the state in problem 2, compute the expectation value of the position \(\langle x \rangle\).

4. **Commutators:** Compute the commutator \([\hat{x}, \hat{p}]\) where \(\hat{x}\) is the position operator and \(\hat{p} = -i\hbar \frac{d}{dx}\) is the momentum operator.

5. **Particle in a box:** Write down the time‑independent Schrödinger equation for a particle in an infinite potential well of width \(L\).  Show that the energy eigenvalues are \(E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2}\).

6. **Harmonic oscillator:** For the one‑dimensional harmonic oscillator with potential \(V(x) = \frac{1}{2}m\omega^2 x^2\), write the ground state energy and the general expression for the energy levels.

7. **Spin‑1/2 system:** Consider a spin‑1/2 particle in the state \(|\psi\rangle = \frac{1}{\sqrt{2}}(|\uparrow_z\rangle + |\downarrow_z\rangle)\).  What is the probability of measuring \(S_z = +\hbar/2\)?  What is the probability of measuring \(S_x = +\hbar/2\)?

8. **Pauli matrices:** Show that the Pauli matrices \(\sigma_x, \sigma_y, \sigma_z\) satisfy \(\sigma_i^2 = I\) and \([\sigma_i, \sigma_j] = 2i \epsilon_{ijk} \sigma_k\), where \(\epsilon_{ijk}\) is the Levi‑Civita symbol.

9. **Uncertainty principle:** Use the commutator from problem 4 to derive the Heisenberg uncertainty relation \(\Delta x \Delta p \ge \frac{\hbar}{2}\).

10. **Hermitian operators:** Explain why Hermitian (self‑adjoint) operators have real eigenvalues.  Give an example of a non‑Hermitian operator and a complex eigenvalue.

11. **Measurement:** A two‑state system is in the normalized state \(|\psi\rangle = \frac{3}{5}|0\rangle + \frac{4}{5}|1\rangle\).  What is the probability of measuring \(|1\rangle\)?  What state does the system collapse into after measurement?

12. **Bra–ket notation:** Express the inner product \(\langle \phi|\psi \rangle\) in terms of components if \(|\phi\rangle = (a,b)\) and \(|\psi\rangle = (c,d)\) in some basis.

13. **Expectation of an operator:** For the state \(|\psi\rangle\) in problem 11 and the operator
    \[
    \hat{A} = \begin{pmatrix}
    0 & 1 \\
    1 & 0
    \end{pmatrix},
    \]
    compute \(\langle \psi | \hat{A} | \psi \rangle\).

14. **Orthonormal basis:** Show that the states \(|0\rangle\) and \(|1\rangle\) form an orthonormal basis for a two‑dimensional Hilbert space.

15. **Potential step:** For a particle encountering a potential step of height \(V_0\) at \(x=0\), write down the form of the wavefunction in the regions \(x<0\) and \(x>0\).  Explain qualitatively what happens when the particle energy \(E\) is (a) greater than \(V_0\) and (b) less than \(V_0\).

16. **Normalization constant:** If \(\psi(x) = A (e^{-x^2})\) on the domain \(-\infty < x < \infty\), find \(A\) such that \(\psi\) is normalized.

17. **Ladder operators:** Define the annihilation operator \(\hat{a}\) and creation operator \(\hat{a}^\dagger\) for the harmonic oscillator.  Show that \([\hat{a}, \hat{a}^\dagger] = 1\).

18. **Unitarity:** Determine whether the following matrix is unitary:
    \[
    U = \frac{1}{\sqrt{2}} \begin{pmatrix}
    1 & 1 \\
    -1 & 1
    \end{pmatrix}.
    \]

19. **Commutator practice:** Compute the commutator \([\hat{x}^2, \hat{p}]\) where \(\hat{x}\) and \(\hat{p}\) are the usual position and momentum operators.

20. **Operator functions:** Let \(\hat{p} = -i\hbar \frac{d}{dx}\).  Evaluate \(\hat{p}\,\hat{x}\,\psi(x) - \hat{x}\,\hat{p}\,\psi(x)\) for a general wavefunction \(\psi(x)\) and check your result against the commutator in problem 4.

---

Record your answers and derivations in this file or in separate notes.  The goal is not just to get the right number, but to understand why the mathematics works.  This understanding will be vital when you start exploring quantum algorithms.
