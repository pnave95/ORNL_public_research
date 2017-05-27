#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-20.4534767039_hkl-3.98653773504,-0.888583089987,0.617123450074/sample/sampleassembly.xml'
psi = -0.0013687049533724705
hkl2Q = array([[ -6.59401092e-01,   9.35246797e-01,   7.77245657e-17],
       [  6.61319352e-01,   4.66266984e-01,  -8.09165116e-01],
       [ -6.61319352e-01,  -4.66266984e-01,  -8.09165116e-01]])
pp = array([ 1.32748972,  2.69031058, -0.13338169])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066525842321691151
Q = array([ 1.63297446, -4.43045789,  0.21965567])
E = -20.453476703904212
hkl_projection = array([-0.50712554, -0.0009154 , -0.57360606])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
