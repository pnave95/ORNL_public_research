#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E711.042416067_hkl-15.3923790619,4.45847344518,-4.44778108888/sample/sampleassembly.xml'
psi = -0.00846963013024801
hkl2Q = array([[-0.65274341,  0.93990554,  0.        ],
       [ 0.66461358,  0.46155929, -0.80916512],
       [-0.66461358, -0.46155929, -0.80916512]])
pp = array([  1.52649854e+00,   2.58259602e+00,   2.15749155e-03])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0013790140893322729
Q = array([  1.59664916e+01,  -1.03566178e+01,  -8.65188173e-03])
E = 711.04241606668916
hkl_projection = array([ 0.9827262 ,  0.26562638, -0.29353939])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
