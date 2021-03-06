**********
extraction
**********

A framework to generate histograms, produce plots and datacards from NanoAOD files.
Also storage of fitting scripts and other stuff.

This repository uses `pre-commit <https://pre-commit.com>`_ hooks!
Look into ``.pre-commit-config.yaml`` for the configuration.


Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`

.. toctree::
   :maxdepth: 2

   source/config
   source/workflow
   source/python_scripts


Setup
#####

1. Clone repository: ``git clone git@github.com:WbWbX/extraction.git``
2. Source ``setup.sh`` to setup the required environments (found in `env`) and source the python environment.
3. Profit!

You can run ``buildDoc`` to update the documentation.


Workflow
########

The workflow is managed by `luigi <https://luigi.readthedocs.io/en/stable/>`_.
Just check the configs and run `lazy.sh`.

1. Merge
2. Fill Histograms
3. Generate plots and datacards
4. Perform fit & plot results

Logs, plots and datacards can be found in the corresponding folder.
Configuration is done in the ``config`` folder.


Folder structure
################

for data (WIP!):
::

    <data folder (as definded in config/general)>
    │
    |-- 2016
    │   |-- 2016_data_NanoAOD.root
    │   |-- ...
    │
    |-- 2017
    │   |-- 2017_data_NanoAOD.root
    │   |-- ...
    │
    `-- 2018
        |-- 2018_data_NanoAOD.root
        |-- ...



and for MC:
::

    <mc folder (as definded in config/general)>
    │
    |-- 2016
    |   |-- signal_NanoAOD.root
    |   |-- background_1_NanoAOD.root
    |   |-- background_2_NanoAOD.root
    |   |-- ...
    |   |
    |   |-- some region
    |   |   |-- nom
    |   |   |   |-- signal_hist.root
    |   |   |   |--  background_1_hist.root
    |   |   |   |--  background_2_hist.root
    |   |   |   |--  ...
    |   |   |
    |   |   |-- some_systematicUP
    |   |   |   |-- signal_hist.root
    |   |   |   |--  background_1_hist.root
    |   |   |   |--  background_2_hist.root
    |   |   |   |--  ...
    |   |   |
    |   |   |-- some_systematicDOWN
    |   |   |   |-- signal_hist.root
    |   |   |   |--  background_1_hist.root
    |   |   |   |--  background_2_hist.root
    |   |   |   |--  ...
    |   |   |
    |   |   |-- <one folder per systematic variation (UP and DOWN)>
    |   |   |   |--  ...
    |   |   |
    |   |   |--  ...
    |   |
    |   |-- <one folder per region>
    |   |
    |   |--  ...
    |
    |-- 2017
    |   |-- ...
    |
    `-- 2018
        |-- ...
