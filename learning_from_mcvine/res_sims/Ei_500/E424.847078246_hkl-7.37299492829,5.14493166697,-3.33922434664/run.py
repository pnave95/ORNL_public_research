#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E424.847078246_hkl-7.37299492829,5.14493166697,-3.33922434664/sample/sampleassembly.xml'
psi = -0.01646135915041962
hkl2Q = array([[-0.64521117,  0.94509201,  0.        ],
       [ 0.66828097,  0.45623319, -0.80916512],
       [-0.66828097, -0.45623319, -0.80916512]])
pp = array([ 2.57489097,  1.53945981,  0.72619769])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0021801521809923633
Q = array([ 10.42693872,  -3.09740503,  -1.46111537])
E = 424.84707824644101
hkl_projection = array([ 0.14455266, -0.371281  , -0.37573719])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
