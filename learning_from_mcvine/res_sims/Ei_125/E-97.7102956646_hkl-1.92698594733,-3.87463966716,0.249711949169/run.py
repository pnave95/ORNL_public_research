#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-97.7102956646_hkl-1.92698594733,-3.87463966716,0.249711949169/sample/sampleassembly.xml'
psi = 0.0018736058071770676
hkl2Q = array([[-0.66242998,  0.9331039 ,  0.        ],
       [ 0.6598041 ,  0.46840873, -0.80916512],
       [-0.6598041 , -0.46840873, -0.80916512]])
pp = array([ 2.7822789 ,  1.12201788, -0.88233205])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032615257313204529
Q = array([-1.44477083, -3.72996042,  2.93316506])
E = -97.710295664628276
hkl_projection = array([-0.51336815, -0.43736264, -0.7950986 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
