#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E369.016531034_hkl-25.6596816232,6.7593271141,-12.2575498274/sample/sampleassembly.xml'
psi = -0.010509569000619152
hkl2Q = array([[-0.6508247 ,  0.94123514,  0.        ],
       [ 0.66555375,  0.46020256, -0.80916512],
       [-0.66555375, -0.46020256, -0.80916512]])
pp = array([-1.28050177,  2.71299009, -0.7837579 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012627528824886969
Q = array([ 29.35670829, -15.40017852,   4.44897002])
E = 369.01653103357603
hkl_projection = array([ 0.984447  , -0.66774104, -0.73748685])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
