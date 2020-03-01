.. ufengger's bibtex documentation master file, created by
   sphinx-quickstart on Sun Mar  1 12:59:50 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ufengger's bibtex's documentation!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Mathematical Definitions
========================

Fast Fourier Transforms are efficient algorithms for
calculating the discrete Fourier transform (DFT),

.. math:: x_j = \sum_{k=0}^{n-1} z_k \exp(-2 \pi i j k / n) 

The DFT usually arises as an approximation to the continuous Fourier
transform when functions are sampled at discrete intervals in space or
time.  The naive evaluation of the discrete Fourier transform is a
matrix-vector multiplication :math:`W\vec{z}`.
A general matrix-vector multiplication takes
:math:`O(n^2)` operations for :math:`n` data-points.  Fast Fourier
transform algorithms use a divide-and-conquer strategy to factorize the
matrix :math:`W` into smaller sub-matrices, corresponding to the integer
factors of the length :math:`n`.  If :math:`n` can be factorized into a
product of integers :math:`f_1 f_2 \ldots f_m`
then the DFT can be computed in :math:`O(n \sum f_i)`
operations.  For a radix-2 FFT this gives an operation count of
:math:`O(n \log_2 n)`.
