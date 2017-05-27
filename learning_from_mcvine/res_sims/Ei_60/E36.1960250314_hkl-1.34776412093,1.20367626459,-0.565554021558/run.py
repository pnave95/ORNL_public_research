#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E36.1960250314_hkl-1.34776412093,1.20367626459,-0.565554021558/sample/sampleassembly.xml'
psi = -0.021537028639765282
hkl2Q = array([[-0.64040591,  0.94835471,  0.        ],
       [ 0.67058804,  0.45283536, -0.80916512],
       [-0.67058804, -0.45283536, -0.80916512]])
pp = array([ 2.97017183,  0.42199441,  0.45681452])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0054260128724266596
Q = array([ 2.04954078, -0.47698841, -0.51634626])
E = 36.196025031421584
hkl_projection = array([-0.39685288,  0.15399888,  0.96629733])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
