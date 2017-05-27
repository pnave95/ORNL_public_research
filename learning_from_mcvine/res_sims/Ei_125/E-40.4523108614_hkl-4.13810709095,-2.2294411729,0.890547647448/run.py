#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-40.4523108614_hkl-4.13810709095,-2.2294411729,0.890547647448/sample/sampleassembly.xml'
psi = -0.0006079489565043363
hkl2Q = array([[-0.6601124 ,  0.93474488,  0.        ],
       [ 0.66096445,  0.46676995, -0.80916512],
       [-0.66096445, -0.46676995, -0.80916512]])
pp = array([ 2.40434159,  1.79419663, -0.36507597])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033189642860739542
Q = array([ 0.66941411, -5.32439146,  1.08338594])
E = -40.4523108614232
hkl_projection = array([ 0.03113986, -0.11553951,  0.26885537])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
