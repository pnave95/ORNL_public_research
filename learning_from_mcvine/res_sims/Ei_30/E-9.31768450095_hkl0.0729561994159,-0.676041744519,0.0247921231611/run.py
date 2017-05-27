#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-9.31768450095_hkl0.0729561994159,-0.676041744519,0.0247921231611/sample/sampleassembly.xml'
psi = 0.007242360937696672
hkl2Q = array([[-0.66743002,  0.92953405,  0.        ],
       [ 0.65727983,  0.47194429, -0.80916512],
       [-0.65727983, -0.47194429, -0.80916512]])
pp = array([ 2.99448002,  0.18190499, -0.36456401])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067869234205180625
Q = array([-0.50933712, -0.26293927,  0.52696848])
E = -9.3176845009452371
hkl_projection = array([ 0.51982522,  0.78223806,  0.00334808])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
