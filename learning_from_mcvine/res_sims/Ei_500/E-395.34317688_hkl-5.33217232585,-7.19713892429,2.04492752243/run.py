#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-395.34317688_hkl-5.33217232585,-7.19713892429,2.04492752243/sample/sampleassembly.xml'
psi = 0.0013141109218614746
hkl2Q = array([[-0.66190781,  0.93347438,  0.        ],
       [ 0.66006607,  0.4680395 , -0.80916512],
       [-0.66006607, -0.4680395 , -0.80916512]])
pp = array([ 2.67060057,  1.36670867, -0.61246201])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016240929975814041
Q = array([-2.57096792, -9.30309844,  4.16898974])
E = -395.34317688048833
hkl_projection = array([-0.19216257,  0.87928852, -0.1565771 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
