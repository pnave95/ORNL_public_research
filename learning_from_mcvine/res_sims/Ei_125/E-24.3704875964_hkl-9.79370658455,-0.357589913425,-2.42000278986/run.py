#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-24.3704875964_hkl-9.79370658455,-0.357589913425,-2.42000278986/sample/sampleassembly.xml'
psi = -0.004593866992468562
hkl2Q = array([[-0.65638135,  0.9373686 ,  0.        ],
       [ 0.6628197 ,  0.4641317 , -0.80916512],
       [-0.6628197 , -0.4641317 , -0.80916512]])
pp = array([ 0.0032962 ,  2.99999819, -0.81995892])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033631966427846252
Q = array([ 7.79541418, -8.22308188,  2.24753112])
E = -24.370487596412062
hkl_projection = array([ 0.25864544, -0.38602119,  0.18840999])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
