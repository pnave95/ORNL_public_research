#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/3-generate-samples-for-fitting/tmp.use_res_comps/E-416.880701737_hkl-25.9019565755,-4.63317610171,-3.62894128981/sample/sampleassembly.xml'
psi = -0.003615019675276979
hkl2Q = array([[ -6.57298572e-01,   9.36725658e-01,  -7.76018576e-17],
       [  6.62365065e-01,   4.64780277e-01,  -8.09165116e-01],
       [ -6.62365065e-01,  -4.64780277e-01,  -8.09165116e-01]])
pp = array([ 0.67693144,  2.92262961, -0.79010009])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011706602554855045
Q = array([ 16.360149  , -24.72977586,   6.68541718])
E = -416.88070173723963
hkl_projection = array([0, 0, 1])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
