#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E17.4470205949_hkl-4.02180847498,1.47724477291,-2.02791420907/sample/sampleassembly.xml'
psi = -0.008588938944521009
hkl2Q = array([[ -6.52631262e-01,   9.39983408e-01,  -7.73329088e-17],
       [  6.64668642e-01,   4.61479991e-01,  -8.09165116e-01],
       [ -6.64668642e-01,  -4.61479991e-01,  -8.09165116e-01]])
pp = array([-1.39441288,  2.65624034, -0.54722329])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0076386949798973001
Q = array([ 4.9545272, -2.1628725,  0.4455825])
E = 17.447020594857818
hkl_projection = array([ 0.79495216,  0.12334135, -0.48872081])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
