#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E258.580967838_hkl-16.1968802499,6.92559955576,-3.56439593257/sample/sampleassembly.xml'
psi = -0.00809662388823522
hkl2Q = array([[-0.65309395,  0.93966199,  0.        ],
       [ 0.66444137,  0.46180716, -0.80916512],
       [-0.66444137, -0.46180716, -0.80916512]])
pp = array([-0.55151333,  2.94886979,  0.77301784])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018421809282146817
Q = array([ 17.54807147, -10.37523775,  -2.71976872])
E = 258.58096783811686
hkl_projection = array([-0.356415  ,  0.41395508, -0.22269725])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
