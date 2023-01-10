=============
API
=============

**DiscTransformation**

This is a demonstration so will be largely conducted in the terminal. An example file is also provided in the example module for automated test run of DiscTransformation. These could also be used as a template for sampling.

An example of the code that execute DiscTransformation on the built-in example pdb

.. code-block:: python

    >>> import Disctransformation as DT
    >>> DT.example_single_run()

Above code will take default input and generate output in the output directory listed in the input file. Default input directory is Disctransformation/example/input/.

Following are the default input and output files:

    1. ``gpcr_dimer.txt`` : Disctransformation default input file to illustrate single run. See Input file format for more details.

    2. ``DT_GPCR_Dimer.ps`` : Default output file corresponds to the above input file. This post-script file displays the orientation of the Quasi-2D model.

Above command is equivalent to the following command:

.. code-block:: python

    >>> DT.example_single_run(
    >>>     input_dtfile = './Disctransformation/example/input/gpcr_dimer.txt')

Above Disctransformation run, uses the ``gpcr_dimer.txt`` as input to construct the gpcr dimer model with the given parameters. The model assumes whiole gpcr as a 2D disc aligned on the z-axis. Parameters for how to assemble the dimer can be provided in the input file. See Input-file format for more details.

To run the Disctransformation with the pdb coordinates, provide the pdb file as an input file as follows:

.. code-block:: python

    >>> DT.example_single_run_withpdb(
    >>>     input_dtfile = './Disctransformation/example/input/gpcr_dimer.txt', 
    >>>     input_pdb = './Disctransformation/example/input/GPCR_Helices.pdb',
    >>>     output_dir = './Disctransformation/example/output_gpcr/')
    

Above command generates a Quasi-2D model in both ps and pdb format. The models will be generated in the output_gpcr. Generating PDB models are generally very slow. If you do a large smapling (see below), then avoid generating pdb models duriong the sampling. Instead save the Disctransformation input file (see Input-file format description) for all samples, then choose your model (either by visualizing PS formatted file or using scoring functions!) and then rerun the Disctransformation with the choosen input file.

To construct the gpcr trimer, use the gpcr_trimer input file. The illustrates how to make a trimer or n-mer model:

.. code-block:: python

    >>> DT.example_single_run(
    >>>     input_dtfile = './Disctransformation/example/input/gpcr_trimer.txt')

To construct the gpcr trimer with pdb coordinates use the following:

.. code-block:: python

    >>> DT.example_single_run_withpdb(
    >>>     input_dtfile = './Disctransformation/example/input/gpcr_trimer.txt', 
    >>>     input_pdb = './Disctransformation/example/input/GPCR_Helices.pdb',
    >>>     output_dir = './Disctransformation/example/output_gpcr/')

All above Disctransformation runs are single runs with a given input file. This means you need to provide the configuration of the model and Disctransformation just builds it. However, in most cases, you wouldn't know the model configuration (else why would you need a Disctransformation!!). Disctransformation can sample a large number of models very efficiently (given you dont generate PDB models during sampling!). 

Use the following wrapper over Disctransformation to do the sampling and scoring for a trimer with single interacting mode 'A' between the discs. See Input-file format for details of how to coarse/fine grain sampling.

.. code-block:: python

    >>> DT.example_sampling_run(
    >>>     input_dtfile = './Disctransformation/example/input/gpcr_trimer_sample_1mode.txt', 
    >>>     input_pdb = './Disctransformation/example/input/GPCR_Helices.pdb',
    >>>     output_dir = './Disctransformation/example/output_gpcr_ensemble_1mode/')


Above example samples all possible models with the resolution specified in the input file. All models will be generated and stored in the output directory. A sampling list is also generated in the output directory for users for debug purpose. This file can be used to coarse/fine grain sampling.

Use the following to sample and score a trimer with two interacting modes 'A' and 'B' between discs.

.. code-block:: python

    >>> DT.example_sampling_run(
    >>>     input_dtfile = './Disctransformation/example/input/gpcr_trimer_sample_2mode.txt', 
    >>>     input_pdb = './Disctransformation/example/input/GPCR_Helices.pdb',
    >>>     output_dir = './Disctransformation/example/output_gpcr_ensemble_2mode/')


You can skip automatic PCA based alignment of PDB coordinates which re-orient your protein. Use align_flag == False

.. code-block:: python

    >>> DT.example_single_run_withpdb(
    >>>     input_dtfile = './Disctransformation/example/input/gpcr_dimer.txt', 
    >>>     input_pdb = './Disctransformation/example/input/GPCR_Helices.pdb',
    >>>     output_dir = './Disctransformation/example/output_gpcr/',
    >>>     align_flag = False)

Similarly

.. code-block:: python

    >>> DT.example_sampling_run(
    >>>     input_dtfile = './Disctransformation/example/input/gpcr_trimer_sample_1mode.txt', 
    >>>     input_pdb = './Disctransformation/example/input/GPCR_Helices.pdb',
    >>>     output_dir = './Disctransformation/example/output_gpcr_ensemble_1mode/',
    >>>     align_flag = False)

