#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E7.24156610037_hkl-4.68550707555,0.813114511053,0.741003087205/sample/sampleassembly.xml'
psi = -0.0034378808843520256
hkl2Q = array([[-0.65746449,  0.93660921,  0.        ],
       [ 0.66228272,  0.4648976 , -0.80916512],
       [-0.66228272, -0.4648976 , -0.80916512]])
pp = array([ 1.39072697,  2.65817202,  0.76757263])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0049903094796327954
Q = array([ 3.12831268, -4.35496466, -1.25753775])
E = 7.2415661003698233
hkl_projection = array([ 0.46691633,  0.09941222,  0.55349864])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
