#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E103.086280887_hkl-5.07206012555,2.44780909252,-1.77800534427/sample/sampleassembly.xml'
psi = -0.01056747930268338
hkl2Q = array([[-0.65077019,  0.94127282,  0.        ],
       [ 0.6655804 ,  0.46016402, -0.80916512],
       [-0.6655804 , -0.46016402, -0.80916512]])
pp = array([ 1.53900791,  2.57516109,  0.49324229])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0042291849140399362
Q = array([ 6.11336479, -2.82962462, -0.54198183])
E = 103.0862808871278
hkl_projection = array([-0.80335637,  0.36521935, -0.58754706])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
