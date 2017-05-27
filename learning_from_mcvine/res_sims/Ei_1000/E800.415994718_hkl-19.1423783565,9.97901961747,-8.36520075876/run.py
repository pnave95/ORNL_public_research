#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E800.415994718_hkl-19.1423783565,9.97901961747,-8.36520075876/sample/sampleassembly.xml'
psi = -0.014165307530575221
hkl2Q = array([[-0.64737945,  0.94360809,  0.        ],
       [ 0.66723168,  0.4577664 , -0.80916512],
       [-0.66723168, -0.4577664 , -0.80916512]])
pp = array([-0.76366897,  2.90117385,  0.39195822])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0014596812735096834
Q = array([ 24.63222726,  -9.66553533,  -1.30584592])
E = 800.41599471820473
hkl_projection = array([-0.09994523, -0.46663418,  0.60483586])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
