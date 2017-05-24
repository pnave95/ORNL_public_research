#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E1.58581795896_hkl-3.87342634708,-0.184661612265,-0.42766209546/sample/sampleassembly.xml'
psi = -0.0028663494404919986
hkl2Q = array([[-0.65799969,  0.9362333 ,  0.        ],
       [ 0.66201691,  0.46527604, -0.80916512],
       [-0.66201691, -0.46527604, -0.80916512]])
pp = array([ 0.90342586,  2.86073797, -0.40343411])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0069813734029414163
Q = array([ 2.70958375, -3.51336841,  0.49547098])
E = 1.5858179589597832
hkl_projection = array([ 0.79286949, -0.33609124, -0.60447769])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
