#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E77.0338540289_hkl-3.86076216343,-1.23378366559,-1.66748714505/sample/sampleassembly.xml'
psi = -0.002972701734731516
hkl2Q = array([[ -6.57900112e-01,   9.36303271e-01,   7.76368655e-17],
       [  6.62066392e-01,   4.65205630e-01,  -8.09165116e-01],
       [ -6.62066392e-01,  -4.65205630e-01,  -8.09165116e-01]])
pp = array([ 2.76947474,  1.15326045, -0.79324251])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025045257639787089
Q = array([ 2.82713636, -3.41308294,  2.34760713])
E = 77.033854028916892
hkl_projection = array([ 0.96681762,  0.7454253 ,  0.58800442])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
