#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E36.2945414585_hkl-1.56725119404,0.35679729156,-1.35163352617/sample/sampleassembly.xml'
psi = -0.015084684532398376
hkl2Q = array([[-0.64651164,  0.94420287,  0.        ],
       [ 0.66765225,  0.45715277, -0.80916512],
       [-0.66765225, -0.45715277, -0.80916512]])
pp = array([ 2.93308554,  0.63008665, -0.72584324])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0054529777214822467
Q = array([ 2.15388383, -0.69878921,  0.80498678])
E = 36.294541458535946
hkl_projection = array([ 0.99973901,  0.38754891,  0.11458958])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
