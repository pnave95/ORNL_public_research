#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E87.9450459328_hkl-7.49281358735,3.00123478559,-4.11791511316/sample/sampleassembly.xml'
psi = -0.012437914197500809
hkl2Q = array([[-0.64900846,  0.9424884 ,  0.        ],
       [ 0.66643994,  0.45891829, -0.80916512],
       [-0.66643994, -0.45891829, -0.80916512]])
pp = array([-1.28741207,  2.70971773, -0.64521322])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0039178750941041528
Q = array([ 9.60738526, -3.79478182,  0.90357877])
E = 87.945045932813883
hkl_projection = array([-0.12440757,  0.23747572, -0.09906289])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
