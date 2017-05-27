#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-29.1745525326_hkl-7.04134988983,-3.39455749134,-0.983374595462/sample/sampleassembly.xml'
psi = -0.0014175179726885047
hkl2Q = array([[ -6.59355439e-01,   9.35278983e-01,   7.77218909e-17],
       [  6.61342111e-01,   4.66234702e-01,  -8.09165116e-01],
       [ -6.61342111e-01,  -4.66234702e-01,  -8.09165116e-01]])
pp = array([ 2.15691588,  2.08511724, -0.95806137])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023974075725110662
Q = array([ 3.04813556, -7.7098037 ,  3.54246993])
E = -29.174552532646601
hkl_projection = array([ 0.05195571, -0.13529382, -0.96422208])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
