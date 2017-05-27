#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E9.35633256898_hkl-10.3273018758,2.85215796825,-3.27793283238/sample/sampleassembly.xml'
psi = -0.007663917617564621
hkl2Q = array([[-0.65350049,  0.93937931,  0.        ],
       [ 0.66424148,  0.46209463, -0.80916512],
       [-0.66424148, -0.46209463, -0.80916512]])
pp = array([-1.20625106,  2.74680876, -0.13777777])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034189177822682186
Q = array([ 10.82075739,  -6.86857167,   0.34452217])
E = 9.3563325689806334
hkl_projection = array([-0.45918476,  0.96968676,  0.24759718])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
