#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-54.3084735797_hkl-4.85861311894,-1.49173068094,1.73880369077/sample/sampleassembly.xml'
psi = -0.000845901927571248
hkl2Q = array([[-0.65988995,  0.93490193,  0.        ],
       [ 0.6610755 ,  0.46661266, -0.80916512],
       [-0.6610755 , -0.46661266, -0.80916512]])
pp = array([ 1.74772111,  2.43833364,  0.08057851])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.004661017537600543
Q = array([ 1.07052286, -6.04973503, -0.19992286])
E = -54.308473579741431
hkl_projection = array([-0.44688421, -0.02507428, -0.53669255])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
