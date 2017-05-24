#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-0.979049574125_hkl-20.6880374739,3.68594940357,-6.33617772086/sample/sampleassembly.xml'
psi = -0.0065249010581916135
hkl2Q = array([[-0.65457003,  0.93863435,  0.        ],
       [ 0.66371471,  0.46285091, -0.80916512],
       [-0.66371471, -0.46285091, -0.80916512]])
pp = array([-0.88904623,  2.8652394 , -0.41573272])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.00169866713435888
Q = array([ 20.1936026 , -14.77975198,   2.14447231])
E = -0.9790495741250993
hkl_projection = array([ 0.99893751,  0.4487793 ,  0.11969932])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
