#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E68.29767239_hkl-11.5271182634,0.539550616241,-3.06845416808/sample/sampleassembly.xml'
psi = -0.003922761396810657
hkl2Q = array([[-0.65701027,  0.93692789,  0.        ],
       [ 0.66250807,  0.46457642, -0.80916512],
       [-0.66250807, -0.46457642, -0.80916512]])
pp = array([ 0.3460944 ,  2.97996958, -0.66834617])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024866068631560195
Q = array([ 9.96376737, -9.12388468,  2.04630054])
E = 68.297672389951913
hkl_projection = array([-0.72676573, -0.71700291,  0.65048411])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
