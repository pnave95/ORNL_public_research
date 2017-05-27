#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-11.8424175435_hkl-5.61170311932,-0.468692938015,0.104632215311/sample/sampleassembly.xml'
psi = -0.00287094677880644
hkl2Q = array([[-0.65799538,  0.93623632,  0.        ],
       [ 0.66201905,  0.465273  , -0.80916512],
       [-0.66201905, -0.465273  , -0.80916512]])
pp = array([ 1.06388609,  2.80502164, -0.14967812])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048278634392067907
Q = array([ 3.31292256, -5.520633  ,  0.29458524])
E = -11.842417543515111
hkl_projection = array([ 0.76662788,  0.56966653, -0.95332949])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
