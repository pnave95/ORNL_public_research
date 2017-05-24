#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-2.22487195019_hkl0.23320232411,-0.398292150423,-0.582127426913/sample/sampleassembly.xml'
psi = -0.000510767803824945
hkl2Q = array([[ -6.60203232e-01,   9.34680728e-01,  -7.77716379e-17],
       [  6.60919081e-01,   4.66834183e-01,  -8.09165116e-01],
       [ -6.60919081e-01,  -4.66834183e-01,  -8.09165116e-01]])
pp = array([ 2.99533182, -0.16729398, -0.43687333])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048955090774479302
Q = array([-0.03246069,  0.30379031,  0.79332132])
E = -2.2248719501860919
hkl_projection = array([ 0.41980624,  0.41244985, -0.98579344])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
