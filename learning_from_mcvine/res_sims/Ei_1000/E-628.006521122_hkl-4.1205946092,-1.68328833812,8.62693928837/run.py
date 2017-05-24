#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-628.006521122_hkl-4.1205946092,-1.68328833812,8.62693928837/sample/sampleassembly.xml'
psi = 0.00255976580154668
hkl2Q = array([[ -6.63070084e-01,   9.32649149e-01,  -7.79410470e-17],
       [  6.59482538e-01,   4.68861353e-01,  -8.09165116e-01],
       [ -6.59482538e-01,  -4.68861353e-01,  -8.09165116e-01]])
pp = array([ 2.84739429,  0.94464055,  0.61166721])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011558622571243536
Q = array([-4.06717206, -8.67713633, -5.61856013])
E = -628.00652112242074
hkl_projection = array([-0.41403906,  0.19663712,  0.62337221])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
