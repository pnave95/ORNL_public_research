#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-574.995892299_hkl-18.9003513201,-6.16577985611,3.80942556585/sample/sampleassembly.xml'
psi = -0.0014338324709470746
hkl2Q = array([[-0.65934018,  0.93528974,  0.        ],
       [ 0.66134972,  0.46622391, -0.80916512],
       [-0.66134972, -0.46622391, -0.80916512]])
pp = array([ 1.76343402,  2.42699412, -0.20725115])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011555953364564145
Q = array([  5.86466176, -22.32798398,   1.90667969])
E = -574.99589229915591
hkl_projection = array([-0.47208423, -0.74082586, -0.85947992])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
