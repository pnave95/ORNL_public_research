#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E15.5422123404_hkl-6.25993614258,1.35336450707,-1.31373368099/sample/sampleassembly.xml'
psi = -0.006072073401927006
hkl2Q = array([[-0.654995  ,  0.93833785,  0.        ],
       [ 0.66350505,  0.46315141, -0.80916512],
       [-0.66350505, -0.46315141, -0.80916512]])
pp = array([-0.29800797,  2.98516185,  0.02063693])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0050429786143724358
Q = array([ 5.86986003, -4.63866472, -0.03206788])
E = 15.54221234035596
hkl_projection = array([-0.0264088 ,  0.38176518,  0.42440251])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
