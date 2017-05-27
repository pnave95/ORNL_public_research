#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-54.3424320812_hkl-13.6723019272,2.24246478818,0.388683204564/sample/sampleassembly.xml'
psi = -0.003072425138506696
hkl2Q = array([[ -6.57806737e-01,   9.36368874e-01,   7.76314262e-17],
       [  6.62112780e-01,   4.65139604e-01,  -8.09165116e-01],
       [ -6.62112780e-01,  -4.65139604e-01,  -8.09165116e-01]])
pp = array([ 0.20112172,  2.99325075,  0.53372722])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023660234088660366
Q = array([ 10.2211448 , -11.94005073,  -2.12903317])
E = -54.34243208117698
hkl_projection = array([-0.98827993, -0.7420526 , -0.5034918 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
