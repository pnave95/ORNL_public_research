#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E570.04130004_hkl-7.55324632548,2.43240107083,-2.64854626881/sample/sampleassembly.xml'
psi = -0.009592324447086215
hkl2Q = array([[-0.65168777,  0.94063778,  0.        ],
       [ 0.66513135,  0.46081284, -0.80916512],
       [-0.66513135, -0.46081284, -0.80916512]])
pp = array([ 2.83550589,  0.97974811, -0.03597251])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0013096253429578167
Q = array([ 8.3018556 , -4.76350305,  0.17489715])
E = 570.0413000397466
hkl_projection = array([ 0.85207765, -0.59091428,  0.76087416])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
