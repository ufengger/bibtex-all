Notes on: Matousek, J., & Gaertner, B. (2007): Understanding and using linear programming
=========================================================================================

`View on DouBan <https://book.douban.com/subject/2883208/>`_

.. code-block:: bibtex

   @Book{Mato_lp_07,
     author    = {Matousek, J. and Gaertner, B.},
     title     = {Understanding and using linear programming},
     year      = 2007,
     publisher = {Springer},
     url       = {https://book.douban.com/subject/2883208/},
   }

Duality of Linear Programming
-----------------------------

.. proof:proposition:: Farkas lemma

   Let :math:`A` be a real matrix with :math:`m` rows and :math:`n` columns, and
   let :math:`b \in \mathbb{R}^m` be a vector. Then exactly one of the following
   two possibilities occurs:

   1. There exists a vector :math:`x \in \mathbb{R}^n` satisfying :math:`A x =
      b` and :math:`x \geq 0`.

   2. There exists a vector :math:`y \in \mathbb{R}^m` such that
      :math:`y^{\mathrm{T}} A \geq 0` and :math:`y^{\mathrm{T}} b < 0`.

.. proof:remark::

   A reader with a systematic mind may like to see the variants of the Farkas
   lemma summarized in a table:

   .. csv-table::
      :header: "", "The system :math:`Ax\\leq b` ", "The system :math:`Ax=b`"
      :align: center

      "has a solution :math:`x\geq 0` iff", ":math:`y\geq 0,y^TA\geq 0` :math:`\Rightarrow y^Tb\geq 0`", ":math:`y^TA\geq 0` :math:`\Rightarrow y^Tb\geq 0`"
      "has a solution :math:`x\in\mathbb{R}^n` iff", ":math:`y\geq 0, y^TA=0` :math:`\Rightarrow y^Tb\geq 0`", ":math:`y^TA=0` :math:`\Rightarrow y^Tb=0`"

