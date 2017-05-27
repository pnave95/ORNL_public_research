#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-121.758760254_hkl-3.32386758416,-2.70928048606,2.45868031956/sample/sampleassembly.xml'
psi = 0.0007882476572042303
hkl2Q = array([[ -6.61416840e-01,   9.33822326e-01,   7.78431283e-17],
       [  6.60312099e-01,   4.67692333e-01,  -8.09165116e-01],
       [ -6.60312099e-01,  -4.67692333e-01,  -8.09165116e-01]])
pp = array([ 2.73458608,  1.23370944, -0.04531272])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023227768099221813
Q = array([-1.21400505, -5.5209174 ,  0.20277691])
E = -121.75876025421617
hkl_projection = array([-0.75294277, -0.13726729, -0.24431599])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
