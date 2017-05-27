#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E117.102522233_hkl-12.1065230041,-0.295499117898,-0.304454830477/sample/sampleassembly.xml'
psi = -0.0033456289792596627
hkl2Q = array([[-0.65755089,  0.93654855,  0.        ],
       [ 0.66223983,  0.4649587 , -0.80916512],
       [-0.66223983, -0.4649587 , -0.80916512]])
pp = array([ 1.67698295,  2.48751446, -0.10654436])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017393385998170504
Q = array([  7.96658584, -11.33418258,   0.48546181])
E = 117.10252223332861
hkl_projection = array([-0.81492762, -0.12236183, -0.3045286 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
