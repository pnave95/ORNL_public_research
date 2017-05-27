#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-52.5865226027_hkl-4.63429910584,-0.631823688978,2.4433428196/sample/sampleassembly.xml'
psi = -0.0008497171624697786
hkl2Q = array([[-0.65988638,  0.93490445,  0.        ],
       [ 0.66107728,  0.46661014, -0.80916512],
       [-0.66107728, -0.46661014, -0.80916512]])
pp = array([ 1.81479603,  2.38883138,  0.60712156])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0046787077607938756
Q = array([ 1.02518818, -5.76753072, -1.46581809])
E = -52.586522602717658
hkl_projection = array([-0.91810209,  0.56277392, -0.97821873])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
