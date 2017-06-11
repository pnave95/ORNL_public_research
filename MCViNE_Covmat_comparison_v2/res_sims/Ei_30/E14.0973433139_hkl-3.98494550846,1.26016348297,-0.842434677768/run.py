#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison_v2/res_sims/Ei_30/E14.0973433139_hkl-3.98494550846,1.26016348297,-0.842434677768/sample/sampleassembly.xml'
psi = -0.005405830844049234
hkl2Q = array([[ -6.55620020e-01,   9.37901253e-01,  -7.75045889e-17],
       [  6.63196336e-01,   4.63593362e-01,  -8.09165116e-01],
       [ -6.63196336e-01,  -4.63593362e-01,  -8.09165116e-01]])
pp = array([-0.2036034 ,  2.99308297,  0.36619392])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0074088255181702445
Q = array([ 4.00704545, -2.76273484, -0.33801158])
E = 14.097343313881872
hkl_projection = array([ 0.76502478,  0.03341273,  0.72924867])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
