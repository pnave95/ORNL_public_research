#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-23.0378879916_hkl-3.41805806,-0.88330861707,1.15344079659/sample/sampleassembly.xml'
psi = -0.0008142597566579487
hkl2Q = array([[-0.65991953,  0.93488105,  0.        ],
       [ 0.66106073,  0.46663358, -0.80916512],
       [-0.66106073, -0.46663358, -0.80916512]])
pp = array([ 1.72346944,  2.45553519,  0.12946176])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066288406107543147
Q = array([ 0.90922823, -4.14589338, -0.21858154])
E = -23.037887991598968
hkl_projection = array([ 0.86756481,  0.51430903, -0.31118343])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
