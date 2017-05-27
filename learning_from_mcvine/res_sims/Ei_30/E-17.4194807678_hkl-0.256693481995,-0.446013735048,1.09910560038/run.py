#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-17.4194807678_hkl-0.256693481995,-0.446013735048,1.09910560038/sample/sampleassembly.xml'
psi = 0.003269302322304431
hkl2Q = array([[ -6.63731666e-01,   9.32178442e-01,   7.79804036e-17],
       [  6.59149697e-01,   4.69329162e-01,  -8.09165116e-01],
       [ -6.59149697e-01,  -4.69329162e-01,  -8.09165116e-01]])
pp = array([ 2.9379278 ,  0.60710809,  0.33265654])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066879278207477612
Q = array([-0.84808935, -0.96445369, -0.52845916])
E = -17.419480767814388
hkl_projection = array([-0.58999927,  0.51357558, -0.30730185])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
