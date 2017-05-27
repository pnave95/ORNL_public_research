#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-15.57862959_hkl-7.8079020895,1.39495525986,-3.13038116856/sample/sampleassembly.xml'
psi = -0.007438242718926884
hkl2Q = array([[ -6.53712465e-01,   9.39231805e-01,  -7.73947930e-17],
       [  6.64137179e-01,   4.62244517e-01,  -8.09165116e-01],
       [ -6.64137179e-01,  -4.62244517e-01,  -8.09165116e-01]])
pp = array([-1.37489734,  2.66639406, -0.71433543])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048288146811576657
Q = array([ 8.10956709, -5.24161802,  1.40424611])
E = -15.578629589982341
hkl_projection = array([-0.15980456, -0.49491244, -0.71751266])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
