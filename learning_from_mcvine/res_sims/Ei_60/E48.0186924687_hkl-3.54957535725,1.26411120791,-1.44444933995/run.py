#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E48.0186924687_hkl-3.54957535725,1.26411120791,-1.44444933995/sample/sampleassembly.xml'
psi = -0.009498664262391439
hkl2Q = array([[-0.65177587,  0.94057673,  0.        ],
       [ 0.66508819,  0.46087513, -0.80916512],
       [-0.66508819, -0.46087513, -0.80916512]])
pp = array([ 1.57712537,  2.55199443, -0.17815071])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0059598979491424552
Q = array([ 4.11495917, -2.09033979,  0.14592333])
E = 48.018692468711563
hkl_projection = array([ 0.00774008,  0.53035782,  0.4102619 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
