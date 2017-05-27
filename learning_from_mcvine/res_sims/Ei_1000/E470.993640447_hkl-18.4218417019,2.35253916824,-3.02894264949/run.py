#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E470.993640447_hkl-18.4218417019,2.35253916824,-3.02894264949/sample/sampleassembly.xml'
psi = -0.005790044349562831
hkl2Q = array([[ -6.55259617e-01,   9.38153082e-01,  -7.74837843e-17],
       [  6.63374406e-01,   4.63338519e-01,  -8.09165116e-01],
       [ -6.63374406e-01,  -4.63338519e-01,  -8.09165116e-01]])
pp = array([ 1.19882694,  2.75005708, -0.10177571])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012782955124283138
Q = array([ 15.64102624, -14.78905976,   0.5473221 ])
E = 470.99364044734762
hkl_projection = array([-0.62602916, -0.23713745, -0.22181278])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
