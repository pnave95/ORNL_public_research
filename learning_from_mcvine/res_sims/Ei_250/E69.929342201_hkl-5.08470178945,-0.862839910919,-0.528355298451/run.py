#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E69.929342201_hkl-5.08470178945,-0.862839910919,-0.528355298451/sample/sampleassembly.xml'
psi = -0.002282568018225992
hkl2Q = array([[ -6.58546129e-01,   9.35849009e-01,   7.76745505e-17],
       [  6.61745180e-01,   4.65662434e-01,  -8.09165116e-01],
       [ -6.61745180e-01,  -4.65662434e-01,  -8.09165116e-01]])
pp = array([ 2.54701823,  1.58514924, -0.36310846])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024801721079582605
Q = array([ 3.1271671 , -4.91427005,  1.12570663])
E = 69.929342201001589
hkl_projection = array([ 0.94991176,  0.45592696, -0.7281535 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
