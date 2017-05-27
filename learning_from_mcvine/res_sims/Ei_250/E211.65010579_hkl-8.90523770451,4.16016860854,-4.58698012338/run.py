#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E211.65010579_hkl-8.90523770451,4.16016860854,-4.58698012338/sample/sampleassembly.xml'
psi = -0.009708035897883641
hkl2Q = array([[-0.65157892,  0.94071318,  0.        ],
       [ 0.66518467,  0.46073587, -0.80916512],
       [-0.66518467, -0.46073587, -0.80916512]])
pp = array([-0.40850995,  2.97205646, -0.2361162 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0030537210684227298
Q = array([ 11.62093439,  -4.34714924,   0.34536099])
E = 211.65010579010379
hkl_projection = array([ 0.91368983,  0.98760789, -0.02101186])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
