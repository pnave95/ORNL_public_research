#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E433.468028904_hkl-5.10874080594,4.86283004322,-4.96893243293/sample/sampleassembly.xml'
psi = -0.08075753277850023
hkl2Q = array([[-0.58315404,  0.98459522,  0.        ],
       [ 0.69621395,  0.41235217, -0.80916512],
       [-0.69621395, -0.41235217, -0.80916512]])
pp = array([ 2.95818164,  0.49916071, -0.04391374])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0022031424605532539
Q = array([ 9.82419306, -0.97589312,  0.08585435])
E = 433.46802890437959
hkl_projection = array([-0.84527048, -0.84993777,  0.08108813])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
