#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-15.8401111303_hkl-3.45960258287,-0.282854284653,1.19011943175/sample/sampleassembly.xml'
psi = -0.0012380185414483343
hkl2Q = array([[-0.65952331,  0.93516061,  0.        ],
       [ 0.66125841,  0.46635341, -0.80916512],
       [-0.66125841, -0.46635341, -0.80916512]])
pp = array([ 1.61772059,  2.52645604,  0.47288141])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067112068109412282
Q = array([ 1.30767229, -3.92221038, -0.73412731])
E = -15.840111130257171
hkl_projection = array([-0.5449774 , -0.39219942, -0.2709737 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
