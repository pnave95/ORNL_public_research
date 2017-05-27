#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-68.6976198276_hkl-14.7621702628,3.76061522241,-0.132200488104/sample/sampleassembly.xml'
psi = -0.0036692642095934843
hkl2Q = array([[-0.65724776,  0.93676131,  0.        ],
       [ 0.66239028,  0.46474435, -0.80916512],
       [-0.66239028, -0.46474435, -0.80916512]])
pp = array([-0.31217412,  2.98371368,  0.72882968])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023621324535232366
Q = array([ 12.28096659, -12.01946589,  -2.93598663])
E = -68.697619827607866
hkl_projection = array([ 0.03845493, -0.90596542, -0.82530467])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
