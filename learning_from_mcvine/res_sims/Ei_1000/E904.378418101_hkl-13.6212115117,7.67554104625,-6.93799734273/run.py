#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E904.378418101_hkl-13.6212115117,7.67554104625,-6.93799734273/sample/sampleassembly.xml'
psi = -0.016721739626700875
hkl2Q = array([[-0.64496507,  0.94525998,  0.        ],
       [ 0.66839974,  0.45605917, -0.80916512],
       [-0.66839974, -0.45605917, -0.80916512]])
pp = array([ 1.48398045,  2.60725949,  0.25052512])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016496808884348428
Q = array([ 18.55289089,  -6.21094795,  -0.59679464])
E = 904.37841810053737
hkl_projection = array([-0.62674528, -0.41615918, -0.62088765])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
