#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-116.138595107_hkl-16.0557542646,3.78062244599,-0.92765953666/sample/sampleassembly.xml'
psi = -0.0038194440111890666
hkl2Q = array([[-0.65710707,  0.93686001,  0.        ],
       [ 0.66246006,  0.46464486, -0.80916512],
       [-0.66246006, -0.46464486, -0.80916512]])
pp = array([-0.60485004,  2.93839351,  0.52770875])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002330926218713118
Q = array([ 13.6693984 , -12.85431501,  -2.30851806])
E = -116.1385951068653
hkl_projection = array([-0.54762121,  0.89279221, -0.4501257 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
