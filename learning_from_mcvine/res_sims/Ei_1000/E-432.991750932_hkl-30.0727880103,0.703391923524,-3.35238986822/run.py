#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-432.991750932_hkl-30.0727880103,0.703391923524,-3.35238986822/sample/sampleassembly.xml'
psi = -0.00466165118408888
hkl2Q = array([[-0.65631781,  0.93741309,  0.        ],
       [ 0.66285116,  0.46408677, -0.80916512],
       [-0.66285116, -0.46408677, -0.80916512]])
pp = array([-0.03850478,  2.99975289, -0.24440494])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011640531973556333
Q = array([ 22.42568587, -26.3083906 ,   2.14347673])
E = -432.99175093180259
hkl_projection = array([ 0.56105153, -0.4899866 , -0.43995553])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
