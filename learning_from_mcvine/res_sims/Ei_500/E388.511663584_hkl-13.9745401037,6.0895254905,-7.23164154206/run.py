#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E388.511663584_hkl-13.9745401037,6.0895254905,-7.23164154206/sample/sampleassembly.xml'
psi = -0.012287881937006109
hkl2Q = array([[-0.64914986,  0.94239102,  0.        ],
       [ 0.66637108,  0.45901827, -0.80916512],
       [-0.66637108, -0.45901827, -0.80916512]])
pp = array([-0.94474649,  2.84735914, -0.37299548])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0020317912049536186
Q = array([ 17.94841121,  -7.05482205,   0.92416047])
E = 388.51166358414673
hkl_projection = array([ 0.80330056,  0.94156456, -0.74462493])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
