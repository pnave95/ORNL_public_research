#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-689.384291128_hkl-10.5438909592,-10.9199069556,0.670388599906/sample/sampleassembly.xml'
psi = 0.0002458186706154413
hkl2Q = array([[ -6.60910210e-01,   9.34180960e-01,  -7.78132442e-17],
       [  6.60565692e-01,   4.67334091e-01,  -8.09165116e-01],
       [ -6.60565692e-01,  -4.67334091e-01,  -8.09165116e-01]])
pp = array([ 2.49196558,  1.6703615 , -0.90743022])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011567333507205119
Q = array([ -0.68758641, -15.26644242,   8.29355271])
E = -689.38429112777021
hkl_projection = array([-0.58484696, -0.16343103,  0.35435363])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
