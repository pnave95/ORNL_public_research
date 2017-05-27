#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E17.8525008193_hkl-8.76049614373,-3.76164090125,-1.3332732572/sample/sampleassembly.xml'
psi = -0.002123016244875047
hkl2Q = array([[-0.65869544,  0.93574392,  0.        ],
       [ 0.66167087,  0.46576801, -0.80916512],
       [-0.66167087, -0.46576801, -0.80916512]])
pp = array([ 2.32531078,  1.89550251, -0.83768395])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017134844650425456
Q = array([ 4.1637187 , -9.32863701,  4.12262681])
E = 17.852500819270233
hkl_projection = array([-0.3764457 ,  0.58012106, -0.57807423])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
