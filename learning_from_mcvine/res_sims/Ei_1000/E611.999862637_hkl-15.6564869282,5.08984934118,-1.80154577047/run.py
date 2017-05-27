#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E611.999862637_hkl-15.6564869282,5.08984934118,-1.80154577047/sample/sampleassembly.xml'
psi = -0.0070552750809681816
hkl2Q = array([[-0.65407211,  0.93898139,  0.        ],
       [ 0.66396011,  0.46249883, -0.80916512],
       [-0.66396011, -0.46249883, -0.80916512]])
pp = array([ 1.6019758 ,  2.53646871,  0.58616054])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0013328430763058837
Q = array([ 14.81608291, -11.51388764,  -2.66078054])
E = 611.99986263740288
hkl_projection = array([-0.66062697,  0.61056872,  0.37702394])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
