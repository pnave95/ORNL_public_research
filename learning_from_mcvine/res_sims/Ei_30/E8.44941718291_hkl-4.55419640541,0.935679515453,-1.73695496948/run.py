#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E8.44941718291_hkl-4.55419640541,0.935679515453,-1.73695496948/sample/sampleassembly.xml'
psi = -0.005846744654920276
hkl2Q = array([[-0.65520642,  0.93819023,  0.        ],
       [ 0.66340068,  0.4633009 , -0.80916512],
       [-0.66340068, -0.4633009 , -0.80916512]])
pp = array([-0.88585691,  2.86622706, -0.61241657])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0071883434093180376
Q = array([ 4.75696626, -3.03446862,  0.64836415])
E = 8.4494171829103024
hkl_projection = array([ 0.70608101,  0.61545409,  0.14251389])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
