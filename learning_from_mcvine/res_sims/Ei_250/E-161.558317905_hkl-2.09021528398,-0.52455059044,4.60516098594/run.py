#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-161.558317905_hkl-2.09021528398,-0.52455059044,4.60516098594/sample/sampleassembly.xml'
psi = 0.0016483792182047016
hkl2Q = array([[-0.6622198 ,  0.93325307,  0.        ],
       [ 0.65990958,  0.46826011, -0.80916512],
       [-0.65990958, -0.46826011, -0.80916512]])
pp = array([ 2.84530985,  0.95090056,  0.72133124])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023148344521464969
Q = array([-2.00096384, -4.35273917, -3.30188759])
E = -161.55831790530891
hkl_projection = array([-0.75731548, -0.82594422,  0.28104048])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
