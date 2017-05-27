#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E49.4100990558_hkl-4.38818421451,1.70827200634,-2.4155833443/sample/sampleassembly.xml'
psi = -0.012119151646447862
hkl2Q = array([[-0.64930886,  0.94228147,  0.        ],
       [ 0.66629362,  0.4591307 , -0.80916512],
       [-0.66629362, -0.4591307 , -0.80916512]])
pp = array([-0.25365115,  2.98925762, -0.76325429])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.00613895132502075
Q = array([ 5.5969854 , -2.2415161 ,  0.57233166])
E = 49.410099055764391
hkl_projection = array([ 0.64786046, -0.86822866,  0.28275046])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
