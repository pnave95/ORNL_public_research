#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-40.5105882473_hkl0.679594601845,-0.350455829589,1.30039991135/sample/sampleassembly.xml'
psi = 0.043218049083434636
hkl2Q = array([[-0.70043157,  0.90492651,  0.        ],
       [ 0.63987967,  0.49527991, -0.80916512],
       [-0.63987967, -0.49527991, -0.80916512]])
pp = array([ 2.99872148,  0.08757545,  0.33217394])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047072323659472599
Q = array([-1.53235854, -0.20265251, -0.76866161])
E = -40.510588247341303
hkl_projection = array([-0.13218498, -0.10119143,  0.81505682])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
