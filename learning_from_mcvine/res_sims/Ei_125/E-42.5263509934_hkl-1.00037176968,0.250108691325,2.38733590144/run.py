#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-42.5263509934_hkl-1.00037176968,0.250108691325,2.38733590144/sample/sampleassembly.xml'
psi = 0.001868986388665266
hkl2Q = array([[-0.66242567,  0.93310696,  0.        ],
       [ 0.65980626,  0.46840568, -0.80916512],
       [-0.65980626, -0.46840568, -0.80916512]])
pp = array([ 2.92606832,  0.66190949,  0.73019804])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033271851112531962
Q = array([-0.74748395, -1.93454324, -2.13412816])
E = -42.526350993422611
hkl_projection = array([ 0.27147287, -0.56039159,  0.16429893])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
