#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E431.424870731_hkl-9.63355109024,4.54897324482,-4.48571048608/sample/sampleassembly.xml'
psi = -0.012022379769641324
hkl2Q = array([[-0.64940004,  0.94221863,  0.        ],
       [ 0.66624919,  0.45919518, -0.80916512],
       [-0.66624919, -0.45919518, -0.80916512]])
pp = array([ 1.68039482,  2.48521091,  0.02581414])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0021916905828798794
Q = array([ 12.27537918,  -4.92822817,  -0.05119002])
E = 431.42487073116229
hkl_projection = array([ 0.08905947,  0.17061691,  0.80918377])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
