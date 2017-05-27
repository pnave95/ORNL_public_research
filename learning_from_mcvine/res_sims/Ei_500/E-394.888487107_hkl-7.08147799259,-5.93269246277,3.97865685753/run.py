#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-394.888487107_hkl-7.08147799259,-5.93269246277,3.97865685753/sample/sampleassembly.xml'
psi = 0.0007865452378592443
hkl2Q = array([[-0.66141525,  0.93382345,  0.        ],
       [ 0.66031289,  0.46769121, -0.80916512],
       [-0.66031289, -0.46769121, -0.80916512]])
pp = array([ 2.52231345,  1.62417205, -0.22830463])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016200964346098879
Q = array([ -1.86079423, -11.24830116,   1.58113745])
E = -394.88848710662853
hkl_projection = array([ 0.87424413, -0.06771091, -0.43435193])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
