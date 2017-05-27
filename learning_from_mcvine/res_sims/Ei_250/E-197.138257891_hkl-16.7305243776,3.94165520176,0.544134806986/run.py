#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-197.138257891_hkl-16.7305243776,3.94165520176,0.544134806986/sample/sampleassembly.xml'
psi = -0.0033763362331736585
hkl2Q = array([[ -6.57522134e-01,   9.36568745e-01,   7.76148590e-17],
       [  6.62254111e-01,   4.64938360e-01,  -8.09165116e-01],
       [ -6.62254111e-01,  -4.64938360e-01,  -8.09165116e-01]])
pp = array([-0.46842389,  2.96320419,  0.76337425])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023018908969011458
Q = array([ 13.25071194, -14.08964867,  -3.62974479])
E = -197.13825789149735
hkl_projection = array([ 0.53043151, -0.13064605,  0.73371031])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
