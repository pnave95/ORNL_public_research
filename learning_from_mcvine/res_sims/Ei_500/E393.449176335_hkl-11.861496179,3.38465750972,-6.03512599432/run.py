#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E393.449176335_hkl-11.861496179,3.38465750972,-6.03512599432/sample/sampleassembly.xml'
psi = -0.009854417288835217
hkl2Q = array([[ -6.51441211e-01,   9.40808546e-01,   7.72650838e-17],
       [  6.65252102e-01,   4.60638498e-01,  -8.09165116e-01],
       [ -6.65252102e-01,  -4.60638498e-01,  -8.09165116e-01]])
pp = array([ 0.69087673,  2.91936454, -0.91800657])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0020706033010420332
Q = array([ 13.99359822,  -6.82028204,   2.14466664])
E = 393.44917633526359
hkl_projection = array([ 0.57276564, -0.97457024, -0.36913123])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
