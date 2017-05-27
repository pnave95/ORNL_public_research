#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E5.77448325692_hkl-0.784925878262,-0.225226779157,-0.176353158696/sample/sampleassembly.xml'
psi = -0.002376726157741159
hkl2Q = array([[-0.65845801,  0.93591101,  0.        ],
       [ 0.66178902,  0.46560012, -0.80916512],
       [-0.66178902, -0.46560012, -0.80916512]])
pp = array([ 2.92549156,  0.664454  , -0.28507711])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0070815391793611071
Q = array([ 0.48449671, -0.75737634,  0.32494448])
E = 5.774483256919865
hkl_projection = array([ 0.87302863,  0.12721366, -0.59219159])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
