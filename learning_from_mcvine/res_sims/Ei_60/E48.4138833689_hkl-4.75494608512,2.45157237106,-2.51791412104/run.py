#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E48.4138833689_hkl-4.75494608512,2.45157237106,-2.51791412104/sample/sampleassembly.xml'
psi = -0.014108285301894459
hkl2Q = array([[ -6.47433254e-01,   9.43571170e-01,   7.70388641e-17],
       [  6.67205573e-01,   4.57804444e-01,  -8.09165116e-01],
       [ -6.67205573e-01,  -4.57804444e-01,  -8.09165116e-01]])
pp = array([-1.22304014,  2.73937453, -0.06649262])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0059881698595771176
Q = array([ 6.3941793 , -2.21157704,  0.05368143])
E = 48.413883368907904
hkl_projection = array([-0.71120018,  0.62040879,  0.18386466])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
