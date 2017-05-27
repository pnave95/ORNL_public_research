#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E113.040949463_hkl-25.492582777,5.44356344974,-1.73223899598/sample/sampleassembly.xml'
psi = -0.005707320002381322
hkl2Q = array([[-0.65533722,  0.93809887,  0.        ],
       [ 0.66333607,  0.46339339, -0.80916512],
       [-0.66333607, -0.46339339, -0.80916512]])
pp = array([ 0.09055676,  2.99863293,  0.43736787])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012142696516884062
Q = array([ 21.46620703, -20.58934372,  -3.00307428])
E = 113.04094946298255
hkl_projection = array([-0.68994521, -0.97680031, -0.23391667])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
