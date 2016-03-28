# disctransformation
DiscTransformation is a software package which packs the 2D objects in a given
geometry. The 2D objects can be approximations of molecular objects (entire
molecules, domains of molecules etc.) whose size can be altered by the user. The
objects are packed in accordance to a user specified arrangement that follows a
particular interaction topology. Sampling algorithms such as Monte Carlo, Divide and
conquer could be used in conjunction with DiscTransformation to get the optimal
packing of the objects. DiscTransformation can be used for the development of new
model representations and combining various scoring schemes to solve the packing
optimization problems. The result can be visually inspected and evaluated using the
output written by the code.
Relevance of DiscTransformation to the molecular architectures:
DiscTransformation is useful in instances where molecular interactions can be
envisaged as quasi-2D problems, or when the focus of the problem is on a cross section
of the structure. For instance, the packing of helices in a bundle could be represented
in 2D. The modes of interactions between helices, each of which could be
approximated by a disc, are obtained from experimental sources (for instance, FRET or
chemical cross-linking). DiscTransformation has the capacity to distinguish between
different vertical orientations of the helices (N above and C below or vice versa could
be denoted as parallel and anti-parallel orientations respectively in the input file). The
program is hence a quick visual guide to the possible solutions to the molecular
arrangement problem. For further analysis, other (external) scoring schemes could be
incorporated to distinguish between the different solutions.
