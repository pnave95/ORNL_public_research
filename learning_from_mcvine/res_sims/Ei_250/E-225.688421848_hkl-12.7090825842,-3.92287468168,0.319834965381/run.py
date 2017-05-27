#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-225.688421848_hkl-12.7090825842,-3.92287468168,0.319834965381/sample/sampleassembly.xml'
psi = -0.001441332314890572
hkl2Q = array([[ -6.59333166e-01,   9.35294685e-01,   7.77205861e-17],
       [  6.61353214e-01,   4.66218953e-01,  -8.09165116e-01],
       [ -6.61353214e-01,  -4.66218953e-01,  -8.09165116e-01]])
pp = array([ 1.09747244,  2.79205198, -0.58710673])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0022877025995426078
Q = array([  5.57358999, -13.86476904,   2.91545405])
E = -225.68842184836606
hkl_projection = array([ 0.60408553, -0.94976588,  0.08792798])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
