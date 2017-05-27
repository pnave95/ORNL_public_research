#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E0.367731806719_hkl-2.08383260163,0.0790986662453,0.819925913429/sample/sampleassembly.xml'
psi = -0.001430818604298691
hkl2Q = array([[-0.659343  ,  0.93528775,  0.        ],
       [ 0.66134831,  0.46622591, -0.80916512],
       [-0.66134831, -0.46622591, -0.80916512]])
pp = array([ 2.36355251,  1.84759832,  0.58580313])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0069671252165932956
Q = array([ 0.88401559, -2.29437597, -0.72745933])
E = 0.36773180671913508
hkl_projection = array([-0.62152833,  0.18629687,  0.59677586])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
