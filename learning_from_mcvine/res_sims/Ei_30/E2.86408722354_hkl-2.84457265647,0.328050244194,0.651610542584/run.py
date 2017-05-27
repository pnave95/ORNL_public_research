#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E2.86408722354_hkl-2.84457265647,0.328050244194,0.651610542584/sample/sampleassembly.xml'
psi = -0.0021917866714823322
hkl2Q = array([[-0.65863108,  0.93578922,  0.        ],
       [ 0.6617029 ,  0.46572251, -0.80916512],
       [-0.6617029 , -0.46572251, -0.80916512]])
pp = array([ 1.82708122,  2.3794483 ,  0.6706249 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0070317995255264575
Q = array([ 1.65942318, -2.81260974, -0.79270733])
E = 2.8640872235365755
hkl_projection = array([ 0.43415818, -0.355148  , -0.47120862])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
