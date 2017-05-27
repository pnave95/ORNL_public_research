#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-16.937753109_hkl-4.91628678737,0.517193234785,0.600549554147/sample/sampleassembly.xml'
psi = -0.002547249570275787
hkl2Q = array([[-0.6582984 ,  0.93602328,  0.        ],
       [ 0.66186841,  0.46548727, -0.80916512],
       [-0.66186841, -0.46548727, -0.80916512]])
pp = array([ 0.40854285,  2.97205194,  0.57924863])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067053465260359267
Q = array([ 3.18121283, -4.64056019, -0.90443847])
E = -16.937753109018086
hkl_projection = array([-0.64463734,  0.18734973, -0.51763842])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
