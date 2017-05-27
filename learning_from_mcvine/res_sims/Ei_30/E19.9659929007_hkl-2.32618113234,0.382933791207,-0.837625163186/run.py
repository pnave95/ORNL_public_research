#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E19.9659929007_hkl-2.32618113234,0.382933791207,-0.837625163186/sample/sampleassembly.xml'
psi = -0.005384909297652346
hkl2Q = array([[ -6.55639642e-01,   9.37887537e-01,   7.75057225e-17],
       [  6.63186637e-01,   4.63607237e-01,  -8.09165116e-01],
       [ -6.63186637e-01,  -4.63607237e-01,  -8.09165116e-01]])
pp = array([ 2.02964893,  2.20919108, -0.50302524])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.007859628350338866
Q = array([ 2.33459495, -1.61583633,  0.3679204 ])
E = 19.965992900717595
hkl_projection = array([-0.08873952, -0.34362842,  0.89067756])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
