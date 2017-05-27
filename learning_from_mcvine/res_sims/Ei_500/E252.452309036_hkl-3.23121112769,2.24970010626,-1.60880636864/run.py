#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E252.452309036_hkl-3.23121112769,2.24970010626,-1.60880636864/sample/sampleassembly.xml'
psi = -0.017622717977401607
hkl2Q = array([[-0.64411315,  0.9458407 ,  0.        ],
       [ 0.66881037,  0.45545677, -0.80916512],
       [-0.66881037, -0.45545677, -0.80916512]])
pp = array([ 2.97910004,  0.35350101,  0.14114392])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018230381753218078
Q = array([ 4.66187471, -1.29882808, -0.51858886])
E = 252.45230903647462
hkl_projection = array([-0.24330845,  0.90416202,  0.59176003])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
