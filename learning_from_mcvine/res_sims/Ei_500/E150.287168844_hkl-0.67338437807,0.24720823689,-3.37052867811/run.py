#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E150.287168844_hkl-0.67338437807,0.24720823689,-3.37052867811/sample/sampleassembly.xml'
psi = 0.012438038376076512
hkl2Q = array([[ -6.72250546e-01,   9.26053765e-01,  -7.84961456e-17],
       [  6.54818897e-01,   4.75352920e-01,  -8.09165116e-01],
       [ -6.54818897e-01,  -4.75352920e-01,  -8.09165116e-01]])
pp = array([ 2.98903658, -0.25624272, -0.59081354])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017620572573119159
Q = array([ 2.82164551,  1.09611167,  2.52728195])
E = 150.28716884359551
hkl_projection = array([ 0.05318202, -0.46493394, -0.35369407])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
