#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-138.854033448_hkl-15.807387281,2.876795906,0.00998148233031/sample/sampleassembly.xml'
psi = -0.003276118552142192
hkl2Q = array([[-0.65761599,  0.93650285,  0.        ],
       [ 0.66220751,  0.46500473, -0.80916512],
       [-0.66220751, -0.46500473, -0.80916512]])
pp = array([-0.28163364,  2.98675116,  0.51792057])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023200181008797213
Q = array([ 12.2936167 , -13.47058091,  -2.33587956])
E = -138.85403344777393
hkl_projection = array([ 0.68407052,  0.28222523,  0.63397249])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
