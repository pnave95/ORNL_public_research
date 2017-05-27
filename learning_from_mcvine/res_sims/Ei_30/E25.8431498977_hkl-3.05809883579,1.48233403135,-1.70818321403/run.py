#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E25.8431498977_hkl-3.05809883579,1.48233403135,-1.70818321403/sample/sampleassembly.xml'
psi = -0.010989849740418561
hkl2Q = array([[-0.65037257,  0.94154761,  0.        ],
       [ 0.6657747 ,  0.45988285, -0.80916512],
       [-0.6657747 , -0.45988285, -0.80916512]])
pp = array([-0.61141266,  2.93703499, -0.38010628])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0089916109175104432
Q = array([ 4.11306924, -1.41208147,  0.18274928])
E = 25.84314989774613
hkl_projection = array([ 0.58632564,  0.00614334,  0.96867849])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
