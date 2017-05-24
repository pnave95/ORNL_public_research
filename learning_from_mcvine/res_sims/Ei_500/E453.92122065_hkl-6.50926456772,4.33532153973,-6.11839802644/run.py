#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E453.92122065_hkl-6.50926456772,4.33532153973,-6.11839802644/sample/sampleassembly.xml'
psi = -0.037641045314317126
hkl2Q = array([[ -6.25051207e-01,   9.58544397e-01,   7.58354557e-17],
       [  6.77793243e-01,   4.41977947e-01,  -8.09165116e-01],
       [ -6.77793243e-01,  -4.41977947e-01,  -8.09165116e-01]])
pp = array([ 2.81945529,  1.02502286, -0.91340946])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023962560395740717
Q = array([ 11.15408416,  -1.61910557,   1.44280329])
E = 453.92122065031674
hkl_projection = array([-0.63239422, -0.34403655,  0.95884932])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
