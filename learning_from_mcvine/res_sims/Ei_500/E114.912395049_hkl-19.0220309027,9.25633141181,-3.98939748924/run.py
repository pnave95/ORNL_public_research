#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E114.912395049_hkl-19.0220309027,9.25633141181,-3.98939748924/sample/sampleassembly.xml'
psi = -0.008638781819909363
hkl2Q = array([[-0.65258441,  0.94001594,  0.        ],
       [ 0.66469164,  0.46144686, -0.80916512],
       [-0.66469164, -0.46144686, -0.80916512]])
pp = array([-1.29092054,  2.70804804,  0.98066066])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001756227538729492
Q = array([ 21.21780611, -11.76881215,  -4.2618192 ])
E = 114.91239504866451
hkl_projection = array([-0.32300391,  0.03265645, -0.39585175])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
