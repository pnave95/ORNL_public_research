#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E813.435724546_hkl-7.14117715479,5.87024563256,-5.98116044093/sample/sampleassembly.xml'
psi = -0.04752115107584898
hkl2Q = array([[-0.61555033,  0.96467308,  0.        ],
       [ 0.68212688,  0.43525981, -0.80916512],
       [-0.68212688, -0.43525981, -0.80916512]])
pp = array([ 2.952496  ,  0.53175874, -0.02757907])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0014710160481488717
Q = array([ 12.47991662,  -1.73046058,   0.08974839])
E = 813.43572454612263
hkl_projection = array([ 0.04066337,  0.78556905,  0.44298864])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
