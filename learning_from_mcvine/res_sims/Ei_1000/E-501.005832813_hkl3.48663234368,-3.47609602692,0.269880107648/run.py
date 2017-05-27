#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-501.005832813_hkl3.48663234368,-3.47609602692,0.269880107648/sample/sampleassembly.xml'
psi = -0.01675974874440859
hkl2Q = array([[-0.64492914,  0.9452845 ,  0.        ],
       [ 0.66841708,  0.45603377, -0.80916512],
       [-0.66841708, -0.45603377, -0.80916512]])
pp = array([ 2.99476596, -0.17713511, -0.28946913])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011601678960341162
Q = array([-4.75250521,  1.5875679 ,  2.59435808])
E = -501.00583281342261
hkl_projection = array([ 0.50069367,  0.53971289,  0.44292604])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
