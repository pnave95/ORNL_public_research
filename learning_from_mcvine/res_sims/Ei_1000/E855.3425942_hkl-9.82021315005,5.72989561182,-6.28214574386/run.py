#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E855.3425942_hkl-9.82021315005,5.72989561182,-6.28214574386/sample/sampleassembly.xml'
psi = -0.021073391600069033
hkl2Q = array([[-0.64084553,  0.94805769,  0.        ],
       [ 0.67037802,  0.45314622, -0.80916512],
       [-0.67037802, -0.45314622, -0.80916512]])
pp = array([ 2.68385738,  1.34048856, -0.15490705])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0015335335900895897
Q = array([ 14.34584819,  -3.86691744,   0.44686154])
E = 855.34259420018998
hkl_projection = array([ 0.11372872,  0.4800669 , -0.63118444])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
