#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-349.147202812_hkl-10.7036474956,-0.564594491102,7.4641807133/sample/sampleassembly.xml'
psi = -0.0006080585628497528
hkl2Q = array([[-0.66011229,  0.93474496,  0.        ],
       [ 0.6609645 ,  0.46676988, -0.80916512],
       [-0.6609645 , -0.46676988, -0.80916512]])
pp = array([ 2.12868513,  2.11392989,  0.85814479])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016348937725500267
Q = array([  1.75887393, -13.75277093,  -5.58290449])
E = -349.14720281197333
hkl_projection = array([-0.54152891, -0.94425563,  0.14793629])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
