#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E54.4204223351_hkl-2.06860544384,1.88156826297,-1.74325331933/sample/sampleassembly.xml'
psi = -0.052844511464300845
hkl2Q = array([[-0.61040633,  0.9679362 ,  0.        ],
       [ 0.68443425,  0.43162246, -0.80916512],
       [-0.68443425, -0.43162246, -0.80916512]])
pp = array([ 2.90120004,  0.76356946,  0.19523369])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.006791441954056023
Q = array([ 3.7436419 , -0.43772369, -0.11191963])
E = 54.420422335050162
hkl_projection = array([-0.89001991,  0.199198  ,  0.75447195])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
