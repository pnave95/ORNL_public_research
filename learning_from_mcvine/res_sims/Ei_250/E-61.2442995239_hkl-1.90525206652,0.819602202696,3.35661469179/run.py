#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-61.2442995239_hkl-1.90525206652,0.819602202696,3.35661469179/sample/sampleassembly.xml'
psi = 0.000502701383128144
hkl2Q = array([[-0.66115016,  0.93401115,  0.        ],
       [ 0.66044562,  0.46750376, -0.80916512],
       [-0.66044562, -0.46750376, -0.80916512]])
pp = array([ 2.90400054,  0.75284849,  0.85786062])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023710603508179558
Q = array([-0.41590107, -2.96558957, -3.37924903])
E = -61.244299523875128
hkl_projection = array([-0.95911208,  0.29612743, -0.60492667])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
