#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-156.928039162_hkl-3.03550566398,-3.42633420278,2.41178330646/sample/sampleassembly.xml'
psi = 0.0011884311901791428
hkl2Q = array([[-0.66179049,  0.93355756,  0.        ],
       [ 0.66012488,  0.46795654, -0.80916512],
       [-0.66012488, -0.46795654, -0.80916512]])
pp = array([ 2.75348725,  1.19092736, -0.17565815])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023077062330997813
Q = array([-1.84501787, -5.56580455,  0.82093919])
E = -156.92803916180782
hkl_projection = array([-0.69778075,  0.6129639 , -0.79662301])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
