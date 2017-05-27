#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E2.44830200211_hkl-0.520358985212,-0.582634923046,-0.529143021732/sample/sampleassembly.xml'
psi = -0.00223036460830245
hkl2Q = array([[-0.65859498,  0.93581463,  0.        ],
       [ 0.66172087,  0.46569698, -0.80916512],
       [-0.66172087, -0.46569698, -0.80916512]])
pp = array([ 2.9686312 ,  0.43269945, -0.76046879])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.007030746145418279
Q = array([ 0.30730911, -0.51187057,  0.89961193])
E = 2.4483020021111024
hkl_projection = array([-0.97098739, -0.86564682, -0.49613377])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
