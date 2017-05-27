#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-276.393376989_hkl-12.915806327,-6.09374780001,0.303036292368/sample/sampleassembly.xml'
psi = -0.0013533152168318054
hkl2Q = array([[-0.65941549,  0.93523665,  0.        ],
       [ 0.66131218,  0.46627716, -0.80916512],
       [-0.66131218, -0.46627716, -0.80916512]])
pp = array([ 1.80249763,  2.39812475, -0.74603281])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016436409332098924
Q = array([  4.28661149, -15.06200975,   4.68564175])
E = -276.39337698863824
hkl_projection = array([-0.69930868,  0.7845103 ,  0.08554676])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
