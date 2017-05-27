#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E168.392326937_hkl-4.14670084936,2.34140480618,-1.31251476496/sample/sampleassembly.xml'
psi = -0.00840855831820981
hkl2Q = array([[ -6.52800806e-01,   9.39865670e-01,   7.73425963e-17],
       [  6.64585389e-01,   4.61599877e-01,  -8.09165116e-01],
       [ -6.64585389e-01,  -4.61599877e-01,  -8.09165116e-01]])
pp = array([ 2.80857126,  1.05447971,  0.39711466])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0027254464984745666
Q = array([ 5.13531122, -2.21069295, -0.83254193])
E = 168.39232693743514
hkl_projection = array([ 0.47313072, -0.86299709, -0.44977213])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
