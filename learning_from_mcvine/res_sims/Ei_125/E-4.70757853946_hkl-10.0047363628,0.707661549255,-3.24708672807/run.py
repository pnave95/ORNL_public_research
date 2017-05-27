#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-4.70757853946_hkl-10.0047363628,0.707661549255,-3.24708672807/sample/sampleassembly.xml'
psi = -0.005895808003785018
hkl2Q = array([[-0.65516039,  0.93822238,  0.        ],
       [ 0.66342341,  0.46326836, -0.80916512],
       [-0.66342341, -0.46326836, -0.80916512]])
pp = array([-0.53679793,  2.95158398, -0.8028209 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034042941893419106
Q = array([ 9.17837956, -7.55455783,  2.05481427])
E = -4.7075785394615366
hkl_projection = array([ 0.14592632, -0.89556844,  0.67614805])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
