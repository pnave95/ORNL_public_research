#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E7.81828526091_hkl-6.65825509126,1.39640472469,-1.32119840869/sample/sampleassembly.xml'
psi = -0.005929479463856683
hkl2Q = array([[-0.6551288 ,  0.93824444,  0.        ],
       [ 0.66343901,  0.46324602, -0.80916512],
       [-0.66343901, -0.46324602, -0.80916512]])
pp = array([-0.45081964,  2.96593352,  0.03618372])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0049652440461973807
Q = array([ 6.16497858, -4.98815199, -0.06085433])
E = 7.8182852609136972
hkl_projection = array([-0.65602635, -0.17104689,  0.66515912])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
