=================
Input File Format
=================

**DiscTransformation Input Files**

Disctransformation needs a minimum one input file to generate configurations. This file is specified by the parameter ``input_dtfile`` in the example wrapper functions. The input file is in text format with parameters starting with tag ``@``. All blank lines and lines start with ``#`` will be ignored.


A single runs examples such as ``example_single_run()`` and ``example_single_run_withpdb()`` uses a ten argument file. These are tagged as @ARG1, @ARG2 .. @ARG10. These are the core arguments for a Disctransformation. Arguments @ARG8 and @ARG9 are optional.


A sampling/ensemble run example ``example_sampling_run()`` uses extra six arguments tagged as @ARG11, @ARG12, @ARG13, @ARG14, @ARG15, @ARG16. Sampling runs ignores arguments @ARG3, @ARG5. Arguments @ARG8 and @ARG9 are optional.

Disctransformation also requires PDB file as input, if a user wants to generate a PDB model from the Disctransformation Model. This can be specified by the parameter 'input_pdb'. This is also accompanied by parameter 'output_dir' that specifies the directory to store all generated models.

A typical input file for the 'single run' looks like following:

.. code-block:: python
    
    @ARG1 2
    @ARG2 23
    @ARG3 0
    @ARG4 yes
    @ARG5 A:30:150:1:0
    @ARG6
    -A
    --
    @ARG7 ./Disctransformation/example/output_gpcr/DT_GPCR_Dimer.ps
    @ARG8 46
    @ARG9 20
    @ARG10 1972243

And input file for the 'sampling run' looks like following:

.. code-block:: python
    
    @ARG1 3
    @ARG2 23 #Set 0 If you want to auto-calculate radius using pdb file
    @ARG4 yes
    @ARG6
    -A-
    --A
    ---
    @ARG7 ./Disctransformation/example/output_gpcr_ensemble_1mode/DT_GPCR_Trimer.ps
    @ARG11 0.5 
    @ARG12 120
    @ARG13 5
    @ARG14 yes
    @ARG15 yes
    @ARG16 yes

Following are the details of each parameters.

ARG(1):Number of Disc, N (discs will be labeled 0..(N-1))

ARG(2):Radius of Discs

ARG(3):Overlap distanvce or Distance between the circumference of the discs. Distance between disc centres would hence be = (2*radius + specified distance). Negative numbers would make the discs to overlap.

ARG(4): Add label to each disc (Yes/No)

ARG(5): List of Modes of association: Mode name (column 1), rotation of disc x about its radius vector (column 2), rotation of disc y about its radius vector (column 3), Relative arrangement of the discs, 1 for parallel and 0 for anti-parallel (column 4), Relative axial distance between disc (third dimension) (column 5). Each disc can have multiple neighbours. The program will NOT check for logical consistency of the relative placement of disc, for example, confliciting assignments of neighbours - in which case the last neighbour assignment overwites previous records.   

ARG(6): Square Adjacency matrix providing the connections between discs numbered from 0 to N-1. 

ARG(7): Output file for printing the model for visualization.

ARG(8): Maximum distance between two disc centers for possible interaction. This will be used to identify new interactions that might happen.  This includes 2*ARG(2)+ARG(3)+relaxtion distance. Default value is 50 having relaxation distance 5 units

ARG(9): Minimum distance allowed between any two discs centers. Below that any distance will be treated as clash. This can be taken as (2 * radius - overlapp% of radius). For example: for radius 27 and overlapp percentage as 50% of along the radius. Then arg(7) is (2*27- 0.5*27)=40.5

ARG(10): Unique identifier to be used during sampling to identify the best model. 


#ARGUMENTS @ARG11 to @ARG16 will be skipped for single runs. These arguments are used only for automated sampling. See example input files.

ARG(11): Maximum Disc overlap fraction for starting configurations for sampling. For instance, With radius=20 and overlap fraction = 0.5, indicates starting disc configuration will overlap 50% of disc.

ARG(12): Rotation step for each disc for sampling.

ARG(13): Translation step for each disc til disc overlap is zero during sampling.

ARG(14): (yes/no) Save Disc Models for All samples; Avoid slow.

ARG(15): (yes/no) Save PDB Models for All samples; Avoid very slow.

ARG(16): (yes/no) Save Disctransformation Input files for All samples; This file can be used after sampling to generate PDB models for best configuration.


