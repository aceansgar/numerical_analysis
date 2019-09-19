## conjugate method:
python interpolation.py --> generate inner_array_conjugate.mat<br>
python plot_img.py --> generate result image<br>

## steepest method:
python steepest.py<br>
python plot_img.py  (need to change parameters)<br>

Algorithm<br>


Minimization of E can be converted to a linear system<br>
Use conjugate gradient method to solve Ax=b<br>
However, A is not positive definite<br>
In this case, steepest descend method also performs well<br>
b-Ax < TOL cannot get convergence easily<br>
Set stepsize < TOL to achieve convergence<br>
Define a function to calculate product of a sparse matrix and a vector<br>
