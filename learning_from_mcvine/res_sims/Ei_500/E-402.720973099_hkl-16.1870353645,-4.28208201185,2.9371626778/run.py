#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-402.720973099_hkl-16.1870353645,-4.28208201185,2.9371626778/sample/sampleassembly.xml'
psi = -0.0015152960880619277
hkl2Q = array([[-0.65926399,  0.93534345,  0.        ],
       [ 0.6613877 ,  0.46617004, -0.80916512],
       [-0.6613877 , -0.46617004, -0.80916512]])
pp = array([ 1.39396907,  2.65647327, -0.15621769])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016187547344485816
Q = array([  5.89680985, -18.50583304,   1.08826181])
E = -402.72097309862102
hkl_projection = array([ 0.23447014,  0.89964027,  0.10413078])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
