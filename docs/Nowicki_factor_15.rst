Notes on: Nowicki, M., & Skrzypczyński, P. (2015): Indoor navigation with a smartphone fusing inertial and wifi data via factor graph optimization
==================================================================================================================================================

`View on DOI <http://dx.doi.org/10.1007/978-3-319-29003-4_16>`_

.. code-block:: bibtex

   @article{Nowicki_factor_15,
     author    = {Nowicki, Michał and Skrzypczyński, Piotr},
     title     = {Indoor Navigation with a Smartphone Fusing Inertial and WiFi
                  Data via Factor Graph Optimization},
     journal   = {Mobile Computing, Applications, and Services},
     pages     = {280–298},
     year      = {2015},
     doi       = {10.1007/978-3-319-29003-4_16},
     url       = {http://dx.doi.org/10.1007/978-3-319-29003-4_16},
     isbn      = {9783319290034},
     issn      = {1867-822X},
     publisher = {Springer International Publishing},
   }


3.3 WiFi Fingerprinting
-----------------------

It is possible to:

1. compare the current WiFi scan to a pre-existing database of fingerprints
   taken at known locations,

2. compare the current WiFi scan to the WiFi fingerprints recorded earlier
   during the system operation.

The **former** method assumes that before the start of a navigation task a small
set of WiFi scans is taken in known poses of the user, and these fingerprints
are stored in the memory of the smartphone. The procedure to obtain these WiFi
fingerprints is straightforward and fast, as only WiFi scans in few selected
locations are needed. The **latter** operation mode assumes no prior knowledge
of the environment as only the WiFi scans taken during the system operation are
compared. The matching of WiFi fingerprints provides localization constraints
equivalent to the loop closure mechanism in SLAM, as it detects previously
visited locations (either known a priori or discovered) and allows to reduce the
dead reckoning drift.
