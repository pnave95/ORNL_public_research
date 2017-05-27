#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E73.784548974_hkl-13.120360018,-1.29130296681,-1.06717998151/sample/sampleassembly.xml'
psi = -0.0032572150025603672
hkl2Q = array([[-0.65763369,  0.93649041,  0.        ],
       [ 0.66219872,  0.46501724, -0.80916512],
       [-0.66219872, -0.46501724, -0.80916512]])
pp = array([ 1.49583252,  2.60047785, -0.40050297])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017240800175483152
Q = array([  8.47997688, -12.39131244,   1.90840213])
E = 73.784548973964206
hkl_projection = array([ 0.97145157,  0.43272317,  0.67311892])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
