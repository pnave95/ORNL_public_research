#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E183.37849817_hkl-13.6833917625,0.362707391875,-2.67583759415/sample/sampleassembly.xml'
psi = -0.0045893262211248636
hkl2Q = array([[-0.6563856 ,  0.93736562,  0.        ],
       [ 0.66281759,  0.46413471, -0.80916512],
       [-0.66281759, -0.46413471, -0.80916512]])
pp = array([ 1.12375161,  2.78157911, -0.45605047])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017777506550666086
Q = array([ 10.9955824 , -11.41604686,   1.87170427])
E = 183.3784981699331
hkl_projection = array([ 0.56845304,  0.27936461,  0.29918183])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
