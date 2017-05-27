#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-109.533123508_hkl-1.82527267746,-3.51025316394,1.26436729993/sample/sampleassembly.xml'
psi = 0.0023808815048144633
hkl2Q = array([[-0.66290324,  0.93276775,  0.        ],
       [ 0.6595664 ,  0.46874337, -0.80916512],
       [-0.6595664 , -0.46874337, -0.80916512]])
pp = array([ 2.78116105,  1.12478586, -0.51871563])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032370998518729882
Q = array([-1.93920006, -3.94062719,  1.8172925 ])
E = -109.53312350803817
hkl_projection = array([-0.37744608,  0.97465793,  0.61009592])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
