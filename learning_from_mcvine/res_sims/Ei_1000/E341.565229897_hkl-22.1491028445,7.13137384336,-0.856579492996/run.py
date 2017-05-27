#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E341.565229897_hkl-22.1491028445,7.13137384336,-0.856579492996/sample/sampleassembly.xml'
psi = -0.006347951958324739
hkl2Q = array([[-0.65473611,  0.93851851,  0.        ],
       [ 0.6636328 ,  0.46296834, -0.80916512],
       [-0.6636328 , -0.46296834, -0.80916512]])
pp = array([ 0.39761093,  2.97353419,  0.88346333])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012593141642814115
Q = array([ 19.80288535, -17.08917348,  -5.0773447 ])
E = 341.56522989677205
hkl_projection = array([ 0.69805007, -0.36090336, -0.62970299])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
