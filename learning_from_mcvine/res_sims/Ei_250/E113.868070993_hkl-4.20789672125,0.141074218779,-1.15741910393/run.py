#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E113.868070993_hkl-4.20789672125,0.141074218779,-1.15741910393/sample/sampleassembly.xml'
psi = -0.0038994573898120553
hkl2Q = array([[-0.6570321 ,  0.93691258,  0.        ],
       [ 0.66249724,  0.46459186, -0.80916512],
       [-0.66249724, -0.46459186, -0.80916512]])
pp = array([ 2.73439895,  1.23412414, -0.30394823])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002554868554813718
Q = array([ 3.62497148, -3.33916195,  0.82239083])
E = 113.86807099255839
hkl_projection = array([-0.86172316, -0.07876922, -0.6712315 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
