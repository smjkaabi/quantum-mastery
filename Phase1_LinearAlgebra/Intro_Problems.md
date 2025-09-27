# Foundations Problem Set – Linear Algebra & Vector Spaces

This problem set introduces core concepts of linear algebra that you will need for quantum mechanics and quantum computing.  Try to solve each exercise by hand before checking your answer in Python or another tool.

1. **Row reduction:** Row‑reduce the matrix
   \[
   A = \begin{pmatrix}
   1 & 2 & 3 \\
   4 & 5 & 6 \\
   7 & 8 & 10
   \end{pmatrix}
   \]
   to its reduced row‑echelon form.

2. **Rank:** Compute the rank of the matrix in problem 1.

3. **Inverse:** Find the inverse of the matrix
   \[
   B = \begin{pmatrix}
   2 & 1 \\
   3 & 2
   \end{pmatrix}
   \]
   (if it exists).

4. **Solving linear systems:** Solve the system of equations represented by the augmented matrix
   \[
   \begin{pmatrix}
   1 & -2 & 5 & | & 3 \\
   2 &  1 & 4 & | & 8 \\
   -1 &  1 & -1 & | & -2
   \end{pmatrix}
   \].

5. **Linear independence:** Determine whether the vectors \( (1,0,1),\,(2,1,3),\,(3,1,4) \) are linearly independent.

6. **Basis and dimension:** Find a basis for the subspace of \(\mathbb{R}^3\) spanned by \( (1,1,0), (2,2,1), (3,3,1) \).  What is the dimension of this subspace?

7. **Eigenvalues and eigenvectors:** Find the eigenvalues and eigenvectors of the matrix
   \[
   C = \begin{pmatrix}
   0 & 1 \\
   -2 & -3
   \end{pmatrix}.
   \]

8. **Determinant:** Compute the determinant of the matrix
   \[
   D = \begin{pmatrix}
   1 & 0 & 2 \\
   -1 & 3 & 1 \\
   4 & 0 & -2
   \end{pmatrix}.
   \]

9. **Diagonalization:** Determine whether the matrix
   \[
   E = \begin{pmatrix}
   3 & 1 \\
   0 & 2
   \end{pmatrix}
   \]
   is diagonalizable.  If so, find a matrix \(P\) and diagonal matrix \(D\) such that \(E = PDP^{-1}\).

10. **Orthonormal basis:** Use the Gram–Schmidt process to obtain an orthonormal basis for the span of \( (1,1,0) \) and \( (1,0,1) \) in \(\mathbb{R}^3\).

11. **Dot and cross products:** For \( \mathbf{u} = (1,2,3) \) and \( \mathbf{v} = (-1,0,2) \), compute the dot product \( \mathbf{u}\cdot\mathbf{v} \) and the cross product \( \mathbf{u}\times\mathbf{v} \).

12. **Projections:** Find the projection of \( \mathbf{v} = (3,1) \) onto \( \mathbf{u} = (1,2) \).

13. **Invertibility:** Determine whether the matrix
   \[
   F = \begin{pmatrix}
   4 & 1 & 0 \\
   0 & 3 & 2 \\
   0 & 0 & 5
   \end{pmatrix}
   \]
   is invertible.  Explain your reasoning.

14. **Least squares:** Solve the over‑determined system
   \[
   x + y = 1,\quad 2x + y = 0,\quad x + 2y = 1
   \]
   in the least‑squares sense.

15. **Linear transformation:** Decide whether the map \( T: \mathbb{R}^2 \to \mathbb{R}^2 \) defined by \(T(x,y) = (x+y, y^2)\) is a linear transformation.  Justify your answer.

16. **Matrix of a linear transformation:** Let \(T: \mathbb{R}^2 \to \mathbb{R}^2 \) be defined by \(T(x,y) = (2x - y, x + 3y)\).  Find the matrix representation of \(T\) with respect to the standard basis.

17. **Trace:** Compute the trace of the matrix
   \[
   G = \begin{pmatrix}
   2 & -1 & 0 \\
   -1 & 2 & -1 \\
   0 & -1 & 2
   \end{pmatrix}.
   \]

18. **Symmetric matrices:** Determine whether the matrix in problem 17 is symmetric.  What special properties do symmetric matrices have?

19. **Singular value decomposition (SVD):** Compute the singular values of the 2×2 matrix
   \[
   H = \begin{pmatrix}
   0 & 3 \\
   4 & 0
   \end{pmatrix}.
   \]

20. **Parametric solution:** Solve the system
   \[
   x + y + z = 2,\quad 2x - y + 3z = 5
   \]
   and express the solution set in parametric vector form.

---

As you work through these problems, focus on understanding the reasoning behind each step.  Linear algebra is the language of quantum mechanics, so mastery here will pay off later.
