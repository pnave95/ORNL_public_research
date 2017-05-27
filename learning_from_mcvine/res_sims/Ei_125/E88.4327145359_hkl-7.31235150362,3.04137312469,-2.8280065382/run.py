#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E88.4327145359_hkl-7.31235150362,3.04137312469,-2.8280065382/sample/sampleassembly.xml'
psi = -0.010136589105506275
hkl2Q = array([[-0.65117572,  0.94099233,  0.        ],
       [ 0.66538206,  0.46045076, -0.80916512],
       [-0.66538206, -0.46045076, -0.80916512]])
pp = array([-0.60652162,  2.93804893,  0.12140101])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0039005683058991277
Q = array([ 8.66700563, -4.1783063 , -0.1726488 ])
E = 88.432714535866097
hkl_projection = array([ 0.64629614, -0.67491158, -0.8051035 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
