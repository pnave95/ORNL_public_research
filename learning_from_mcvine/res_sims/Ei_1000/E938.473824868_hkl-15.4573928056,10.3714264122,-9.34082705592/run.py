#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E938.473824868_hkl-15.4573928056,10.3714264122,-9.34082705592/sample/sampleassembly.xml'
psi = -0.02293486151301482
hkl2Q = array([[-0.63907964,  0.94924896,  0.        ],
       [ 0.67122038,  0.45189755, -0.80916512],
       [-0.67122038, -0.45189755, -0.80916512]])
pp = array([-0.5235559 ,  2.95396161,  0.42730003])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017967719444975179
Q = array([ 23.1097712 ,  -5.76499505,  -0.83392505])
E = 938.47382486805373
hkl_projection = array([ 0.54335254, -0.38884211, -0.01149307])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
