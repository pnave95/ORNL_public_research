#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E19.1441477561_hkl-1.99146290496,0.25694379637,-0.810328335302/sample/sampleassembly.xml'
psi = -0.0054654495896711034
hkl2Q = array([[ -6.55564102e-01,   9.37940339e-01,  -7.75013592e-17],
       [  6.63223974e-01,   4.63553822e-01,  -8.09165116e-01],
       [ -6.63223974e-01,  -4.63553822e-01,  -8.09165116e-01]])
pp = array([ 2.38799376,  1.81589806, -0.59216441])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0077885291520331211
Q = array([ 2.01337206, -1.37313532,  0.44777946])
E = 19.144147756090099
hkl_projection = array([-0.00158625, -0.82416795, -0.43902075])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
