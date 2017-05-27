#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E236.832561214_hkl-7.1827473064,4.31941919718,-4.72585228144/sample/sampleassembly.xml'
psi = -0.014926798547897987
hkl2Q = array([[-0.64666071,  0.94410079,  0.        ],
       [ 0.66758007,  0.45725817, -0.80916512],
       [-0.66758007, -0.45725817, -0.80916512]])
pp = array([ 0.38264856,  2.97549661, -0.36993465])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0037544296571572809
Q = array([ 10.68324344,  -2.64521306,   0.32887147])
E = 236.83256121394714
hkl_projection = array([ 0.39545947, -0.53801421, -0.13691628])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
