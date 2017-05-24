#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-27.3683269028_hkl-0.9316471086,-0.754796066157,1.68761206886/sample/sampleassembly.xml'
psi = 0.0018345493596170805
hkl2Q = array([[-0.66239354,  0.93312977,  0.        ],
       [ 0.65982239,  0.46838296, -0.80916512],
       [-0.65982239, -0.46838296, -0.80916512]])
pp = array([ 2.76765962,  1.15760971,  0.43399061])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066013500492296444
Q = array([-0.99443855, -2.01333001, -0.75480217])
E = -27.368326902807013
hkl_projection = array([ 0.36331712,  0.03508707,  0.1470121 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
