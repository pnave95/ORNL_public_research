#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-196.341175896_hkl1.06668981995,-3.3532299945,-0.617885144148/sample/sampleassembly.xml'
psi = 0.036367193393613086
hkl2Q = array([[-0.69421566,  0.90970379,  0.        ],
       [ 0.64325772,  0.4908846 , -0.80916512],
       [-0.64325772, -0.4908846 , -0.80916512]])
pp = array([ 2.99936588,  0.06167904, -0.53225062])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016538434409993006
Q = array([-2.50004447, -0.37236688,  3.21328784])
E = -196.34117589563488
hkl_projection = array([-0.96542723,  0.32155944, -0.75868177])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
