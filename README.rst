Blending ToolKit
================

|PyPI| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/BlendingToolKit.svg
   :target: https://pypi.org/project/BlendingToolKit/
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/BlendingToolKit
   :target: https://pypi.org/project/BlendingToolKit
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/BlendingToolKit
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/BlendingToolKit/latest.svg?label=Read%20the%20Docs
   :target: https://BlendingToolKit.readthedocs.io/
   :alt: Read the documentation at https://BlendingToolKit.readthedocs.io/
.. |Tests| image:: https://github.com/ismael-mendoza/BlendingToolKit/workflows/Tests/badge.svg
   :target: https://github.com/ismael-mendoza/BlendingToolKit/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/ismael-mendoza/BlendingToolKit/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/ismael-mendoza/BlendingToolKit
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


**NOTE:** BTK is currently in development and rapidly changing, as such the documentation and most jupyter notebooks are deprecated. We will release a new stable version of BTK in the near future and fix these issues. 


Introduction
------------

Framework for fast generation and analysis of galaxy blends catalogs. This toolkit is a convenient way of
producing multi-band postage stamp images of blend scenes.

Documentation can be found at https://blendingtoolkit.readthedocs.io/en/latest/

Workflow
--------

<img src="docs/source/images/flow_chart.png" alt="btk workflow" width="450"/>


Running BlendingToolKit
-----------------------

- BlendingToolKit (btk) requires an input catalog that contains information required to simulate galaxies and blends.

- This repository includes sample input catalogs with a small number of galaxies that can be used to draw blend images with btk. See [tutorials](https://github.com/LSSTDESC/BlendingToolKit/tree/master/notebooks) to learn how to run btk with these catalogs.

- CatSim Catalog corresponding to one square degree of sky and processed WeakLensingDeblending catalogs can be downloaded from [here](https://stanford.app.box.com/s/s1nzjlinejpqandudjyykjejyxtgylbk).

- [Cosmo DC2](https://arxiv.org/abs/1907.06530) catalog requires pre-processing in order to be used as input catalog to btk. Refer to this [notebook](https://github.com/LSSTDESC/WeakLensingDeblending/blob/cosmoDC2_ingestion/notebooks/wld_ingestion_cosmoDC2.ipynb) on how to convert the DC2 catalog into a CatSim-like catalog that can be analyzed with btk.

Requirements
------------

The code is intended to run in python >=3.7.
To run btk you need to install
- [WeakLensingDeblending](https://github.com/LSSTDESC/WeakLensingDeblending)
- [GalSim](https://github.com/GalSim-developers/GalSim/)
- numpy
- astropy
- fitsio
- scipy
- lmfit

More detailed installation instructions can be found [here](https://blendingtoolkit.readthedocs.io/en/latest/install.html).

Optional
--------

The tutorials include examples of using btk with some detection, deblending or measurement packages including
- [scarlet](https://github.com/fred3m/scarlet/) (multi-band deblender)
- [sep](https://sep.readthedocs.io/en/v1.0.x/index.html) (Source Extraction and Photometry)
- [lsst](https://pipelines.lsst.io) (LSST science pipeline)


Installation
------------

You can install *Blending ToolKit* via pip_ from PyPI_:

.. code:: console

   $ pip install BlendingToolKit


Usage
-----

Please see the `Command-line Reference <Usage_>`_ for details.


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the MIT_ license,
*Blending ToolKit* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.


.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _MIT: http://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/ismael-mendoza/BlendingToolKit/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://BlendingToolKit.readthedocs.io/en/latest/usage.html
