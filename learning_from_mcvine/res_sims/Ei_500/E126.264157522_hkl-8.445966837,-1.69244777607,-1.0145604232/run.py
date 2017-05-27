#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E126.264157522_hkl-8.445966837,-1.69244777607,-1.0145604232/sample/sampleassembly.xml'
psi = -0.0029558673428499893
hkl2Q = array([[-0.65791587,  0.9362922 ,  0.        ],
       [ 0.66205856,  0.46521678, -0.80916512],
       [-0.66205856, -0.46521678, -0.80916512]])
pp = array([ 2.36184919,  1.84977524, -0.49272182])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017480330548437632
Q = array([ 5.10793453, -8.2232574 ,  2.1904166 ])
E = 126.26415752200842
hkl_projection = array([ 0.53231059, -0.86344383,  0.34966935])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
