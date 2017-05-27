#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E458.527967838_hkl-6.3659260899,5.70497367558,-4.90939234915/sample/sampleassembly.xml'
psi = -0.04312909667138164
hkl2Q = array([[-0.61978128,  0.96196026,  0.        ],
       [ 0.68020862,  0.43825155, -0.80916512],
       [-0.68020862, -0.43825155, -0.80916512]])
pp = array([ 2.84772231,  0.94365124,  0.41268985])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024089387183418524
Q = array([ 11.1654651 ,  -1.47200559,  -0.64375666])
E = 458.52796783790302
hkl_projection = array([ 0.92964151,  0.12143984, -0.5800371 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
