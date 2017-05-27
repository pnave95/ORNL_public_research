#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E821.420488081_hkl-13.2876722952,4.24338742568,-7.31967203531/sample/sampleassembly.xml'
psi = -0.012524408893846584
hkl2Q = array([[-0.64892694,  0.94254453,  0.        ],
       [ 0.66647963,  0.45886064, -0.80916512],
       [-0.66647963, -0.45886064, -0.80916512]])
pp = array([ 1.87091534,  2.34513875, -0.80870823])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0014989546040981971
Q = array([ 16.32927214,  -7.21839   ,   2.48922219])
E = 821.42048808113532
hkl_projection = array([-0.76051534, -0.94077945, -0.51506411])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
