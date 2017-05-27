#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-441.722678082_hkl-30.8468899567,0.258490788059,-6.23010340747/sample/sampleassembly.xml'
psi = -0.005178973738939453
hkl2Q = array([[-0.65583277,  0.9377525 ,  0.        ],
       [ 0.66309115,  0.4637438 , -0.80916512],
       [-0.66309115, -0.4637438 , -0.80916512]])
pp = array([-0.28175324,  2.98673988, -0.55683904])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011659856390901782
Q = array([ 24.53293075, -25.91770275,   4.83202062])
E = -441.72267808227417
hkl_projection = array([-0.28425702, -0.09635448, -0.39232972])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
