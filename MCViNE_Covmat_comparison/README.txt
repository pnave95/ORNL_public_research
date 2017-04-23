This directory contains files for comparing two methods of estimating the resolution effects of the Oak Ridge National Laboratory SNS ARCS instrument.  

The first method is via MCViNE monte carlo resolution simulation, an accurate but not super fast method.  The second method involves estimating a correlation matrix, as described in the paper NIMA 736(2014)31-39.


If working on the analysis.sns.gov cluster, run the following bash commands in your terminal before trying to run any of the notebooks:

export PATH=/SNS/software/miniconda2/bin:$PATH
source activate mcvine unstable











