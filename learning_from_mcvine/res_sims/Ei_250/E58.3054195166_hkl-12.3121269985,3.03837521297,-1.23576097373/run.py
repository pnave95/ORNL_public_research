#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E58.3054195166_hkl-12.3121269985,3.03837521297,-1.23576097373/sample/sampleassembly.xml'
psi = -0.004107077881913918
hkl2Q = array([[ -6.56837568e-01,   9.37048974e-01,   7.75750821e-17],
       [  6.62593684e-01,   4.64454299e-01,  -8.09165116e-01],
       [ -6.62593684e-01,  -4.64454299e-01,  -8.09165116e-01]])
pp = array([ 0.03276663,  2.99982105,  0.45808323])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002466661800697839
Q = array([ 10.9190832 ,  -9.55192505,  -1.45861256])
E = 58.305419516566246
hkl_projection = array([-0.6772899 ,  0.41513462,  0.44948202])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
