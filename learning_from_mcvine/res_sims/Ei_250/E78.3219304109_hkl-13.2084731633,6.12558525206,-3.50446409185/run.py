#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E78.3219304109_hkl-13.2084731633,6.12558525206,-3.50446409185/sample/sampleassembly.xml'
psi = -0.006827076718771155
hkl2Q = array([[-0.65428637,  0.9388321 ,  0.        ],
       [ 0.66385455,  0.46265033, -0.80916512],
       [-0.66385455, -0.46265033, -0.80916512]])
pp = array([-1.35216335,  2.67799445,  0.71487393])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025031985945301967
Q = array([ 15.035076  ,  -7.94519314,  -2.12091981])
E = 78.321930410869811
hkl_projection = array([ 0.08955048, -0.56572761,  0.80457888])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
