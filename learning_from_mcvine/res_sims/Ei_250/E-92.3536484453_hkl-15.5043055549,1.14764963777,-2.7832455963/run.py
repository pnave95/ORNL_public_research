#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-92.3536484453_hkl-15.5043055549,1.14764963777,-2.7832455963/sample/sampleassembly.xml'
psi = -0.0036187443762752034
hkl2Q = array([[ -6.57295083e-01,   9.36728107e-01,   7.76016547e-17],
       [  6.62366796e-01,   4.64777810e-01,  -8.09165116e-01],
       [ -6.62366796e-01,  -4.64777810e-01,  -8.09165116e-01]])
pp = array([-0.41449636,  2.97122749, -0.30972126])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023395514396189741
Q = array([ 12.79459828, -12.69632591,   1.32346719])
E = -92.3536484453372
hkl_projection = array([ 0.43932149, -0.89059898, -0.08921161])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
