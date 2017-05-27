#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-38.6084564858_hkl0.916807446054,-0.606979849986,0.135133184152/sample/sampleassembly.xml'
psi = -0.01023070053975511
hkl2Q = array([[ -6.51087155e-01,   9.41053605e-01,   7.72449632e-17],
       [  6.65425386e-01,   4.60388142e-01,  -8.09165116e-01],
       [ -6.65425386e-01,  -4.60388142e-01,  -8.09165116e-01]])
pp = array([ 2.9948653 , -0.17544749, -0.12854643])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.003318498574190195
Q = array([-1.0907424 ,  0.52110491,  0.38180186])
E = -38.608456485838772
hkl_projection = array([-0.72446501,  0.99844853,  0.14626857])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
