#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E153.85452443_hkl-16.2128945853,3.1773552156,3.85019382202/sample/sampleassembly.xml'
psi = -0.003599970347417879
hkl2Q = array([[-0.65731267,  0.93671577,  0.        ],
       [ 0.66235807,  0.46479025, -0.80916512],
       [-0.66235807, -0.46479025, -0.80916512]])
pp = array([ 1.82468324,  2.38128769,  0.87363965])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012269683166013319
Q = array([ 10.21128092, -15.4996028 ,  -5.68644754])
E = 153.85452443026793
hkl_projection = array([-0.51457256,  0.33865847, -0.33974644])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
