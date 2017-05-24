#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E108.772042231_hkl-2.1902172391,0.631959440799,-1.45420861072/sample/sampleassembly.xml'
psi = -0.009300891180536841
hkl2Q = array([[-0.65196187,  0.94044781,  0.        ],
       [ 0.66499703,  0.46100666, -0.80916512],
       [-0.66499703, -0.46100666, -0.80916512]])
pp = array([ 2.97351148,  0.39778072, -0.24102558])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.00254322794835409
Q = array([ 2.81523368, -1.09804764,  0.66533535])
E = 108.77204223095055
hkl_projection = array([-0.91304763, -0.30855847,  0.37472784])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
