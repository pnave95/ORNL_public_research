#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-20.3949424633_hkl-8.03071135011,1.68421372979,-2.15959524733/sample/sampleassembly.xml'
psi = -0.006509775231552422
hkl2Q = array([[-0.65458423,  0.93862445,  0.        ],
       [ 0.66370771,  0.46286095, -0.80916512],
       [-0.66370771, -0.46286095, -0.80916512]])
pp = array([-1.15454766,  2.76893837, -0.18495681])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.004784553976600785
Q = array([ 7.80794267, -5.75867296,  0.38466214])
E = -20.394942463321925
hkl_projection = array([-0.17334117, -0.457761  , -0.39600954])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
