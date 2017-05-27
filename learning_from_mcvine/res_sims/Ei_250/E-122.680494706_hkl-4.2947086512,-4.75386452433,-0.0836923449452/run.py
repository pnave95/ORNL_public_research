#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-122.680494706_hkl-4.2947086512,-4.75386452433,-0.0836923449452/sample/sampleassembly.xml'
psi = 0.00014302544045804452
hkl2Q = array([[-0.66081418,  0.93424889,  0.        ],
       [ 0.66061373,  0.46726619, -0.80916512],
       [-0.66061373, -0.46726619, -0.80916512]])
pp = array([ 2.62906977,  1.44498863, -0.9131005 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023383530579133933
Q = array([-0.24717548, -6.19454035,  3.91438227])
E = -122.68049470593633
hkl_projection = array([-0.36650103,  0.30945389, -0.41606675])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
