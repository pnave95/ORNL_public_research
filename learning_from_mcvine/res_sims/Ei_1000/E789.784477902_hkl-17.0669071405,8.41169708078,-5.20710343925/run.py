#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E789.784477902_hkl-17.0669071405,8.41169708078,-5.20710343925/sample/sampleassembly.xml'
psi = -0.011346627724075973
hkl2Q = array([[-0.6500366 ,  0.94177959,  0.        ],
       [ 0.66593873,  0.45964529, -0.80916512],
       [-0.66593873, -0.45964529, -0.80916512]])
pp = array([ 0.57735471,  2.94391942,  0.7778833 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0014594140426106689
Q = array([ 20.16340107,  -9.81344722,  -2.59304539])
E = 789.78447790177233
hkl_projection = array([ 0.02799805,  0.22467361,  0.81718379])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
