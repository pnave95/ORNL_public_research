#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E34.4160488158_hkl-1.83500547473,0.499759022459,-0.779062221403/sample/sampleassembly.xml'
psi = -0.008691522180600432
hkl2Q = array([[-0.65253483,  0.94005035,  0.        ],
       [ 0.66471598,  0.4614118 , -0.80916512],
       [-0.66471598, -0.4614118 , -0.80916512]])
pp = array([ 2.84217882,  0.96021848, -0.19121079])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0053646278525955925
Q = array([ 2.0474579 , -1.13493432,  0.22600241])
E = 34.416048815777913
hkl_projection = array([ 0.3963771 , -0.20259314, -0.48741701])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
