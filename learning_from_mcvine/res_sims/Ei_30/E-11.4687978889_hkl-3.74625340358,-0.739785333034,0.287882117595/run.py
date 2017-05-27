#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-11.4687978889_hkl-3.74625340358,-0.739785333034,0.287882117595/sample/sampleassembly.xml'
psi = -0.0016684237375345005
hkl2Q = array([[-0.65912075,  0.93544439,  0.        ],
       [ 0.66145907,  0.46606875, -0.80916512],
       [-0.66145907, -0.46606875, -0.80916512]])
pp = array([ 1.36197515,  2.67301771, -0.24537662])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067539348494260196
Q = array([ 1.7894734 , -3.98337542,  0.36566432])
E = -11.468797888929604
hkl_projection = array([ 0.43502529,  0.66439724, -0.82309763])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
