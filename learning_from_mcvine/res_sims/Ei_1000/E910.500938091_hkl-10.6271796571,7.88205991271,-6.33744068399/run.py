#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E910.500938091_hkl-10.6271796571,7.88205991271,-6.33744068399/sample/sampleassembly.xml'
psi = -0.025493324577443785
hkl2Q = array([[ -6.36648932e-01,   9.50880912e-01,  -7.64466404e-17],
       [  6.72374341e-01,   4.50178777e-01,  -8.09165116e-01],
       [ -6.72374341e-01,  -4.50178777e-01,  -8.09165116e-01]])
pp = array([ 2.52351163,  1.62230978,  0.5474409 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016786190676300731
Q = array([ 16.32660992,  -3.7038649 ,  -1.249852  ])
E = 910.50093809091913
hkl_projection = array([ 0.90072922, -0.18573791, -0.45686936])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
