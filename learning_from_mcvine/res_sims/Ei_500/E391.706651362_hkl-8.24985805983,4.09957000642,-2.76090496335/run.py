#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E391.706651362_hkl-8.24985805983,4.09957000642,-2.76090496335/sample/sampleassembly.xml'
psi = -0.010370843418663575
hkl2Q = array([[-0.65095527,  0.94114484,  0.        ],
       [ 0.6654899 ,  0.46029488, -0.80916512],
       [-0.6654899 , -0.46029488, -0.80916512]])
pp = array([ 2.32871299,  1.89132118,  0.44473994])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0020428687000140352
Q = array([ 9.93586535, -4.60646983, -1.08320106])
E = 391.70665136202854
hkl_projection = array([-0.74779895, -0.4651273 ,  0.77435258])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
