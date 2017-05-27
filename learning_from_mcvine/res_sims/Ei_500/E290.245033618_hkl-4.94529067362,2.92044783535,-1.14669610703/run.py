#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E290.245033618_hkl-4.94529067362,2.92044783535,-1.14669610703/sample/sampleassembly.xml'
psi = -0.01024162860280928
hkl2Q = array([[-0.65107687,  0.94106072,  0.        ],
       [ 0.66543042,  0.46038087, -0.80916512],
       [-0.66543042, -0.46038087, -0.80916512]])
pp = array([ 2.8833692 ,  0.82836105,  0.4274534 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018637835476252953
Q = array([ 5.92616567, -2.78138354, -1.43525802])
E = 290.24503361843108
hkl_projection = array([ 0.77925834,  0.73879308, -0.47047139])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
