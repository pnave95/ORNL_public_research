#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-308.474156557_hkl-31.4260201576,2.91024034494,-12.3491613894/sample/sampleassembly.xml'
psi = -0.007491500408390256
hkl2Q = array([[-0.65366244,  0.93926662,  0.        ],
       [ 0.6641618 ,  0.46220915, -0.80916512],
       [-0.6641618 , -0.46220915, -0.80916512]])
pp = array([-1.07134803,  2.80218012, -0.952711  ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011810731985339956
Q = array([ 30.67672077, -22.46437666,   7.63764565])
E = -308.47415655676855
hkl_projection = array([-0.15460732,  0.97793157, -0.88756532])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
