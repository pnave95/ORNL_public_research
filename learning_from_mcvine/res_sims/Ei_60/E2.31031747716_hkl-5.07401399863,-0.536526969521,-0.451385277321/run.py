#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E2.31031747716_hkl-5.07401399863,-0.536526969521,-0.451385277321/sample/sampleassembly.xml'
psi = -0.003276232003756487
hkl2Q = array([[-0.65761588,  0.93650292,  0.        ],
       [ 0.66220757,  0.46500465, -0.80916512],
       [-0.66220757, -0.46500465, -0.80916512]])
pp = array([ 1.21693014,  2.74209428, -0.45748161])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0049298210845979632
Q = array([ 3.28037073, -4.79142021,  0.79938413])
E = 2.3103174771600621
hkl_projection = array([ 0.73963174, -0.75748203,  0.84290817])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
