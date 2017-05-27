#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-465.074612764_hkl-21.6903414064,-4.31068910977,-3.81425338458/sample/sampleassembly.xml'
psi = -0.003228747695873658
hkl2Q = array([[-0.65766035,  0.93647169,  0.        ],
       [ 0.66218548,  0.4650361 , -0.80916512],
       [-0.66218548, -0.4650361 , -0.80916512]])
pp = array([ 0.24328993,  2.99011873, -0.95692236])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016219383469852603
Q = array([ 13.93614506, -20.54325126,   6.57442004])
E = -465.07461276403177
hkl_projection = array([ 0.92287393,  0.48130462,  0.92471795])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
