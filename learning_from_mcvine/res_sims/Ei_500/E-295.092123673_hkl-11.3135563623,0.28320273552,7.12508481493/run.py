#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-295.092123673_hkl-11.3135563623,0.28320273552,7.12508481493/sample/sampleassembly.xml'
psi = -0.0010153054861956887
hkl2Q = array([[-0.65973157,  0.93501371,  0.        ],
       [ 0.66115453,  0.46650066, -0.80916512],
       [-0.66115453, -0.46650066, -0.80916512]])
pp = array([ 2.03106568,  2.20788863,  0.96116049])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016454243291715684
Q = array([  2.94036892, -13.7700728 ,  -5.99452786])
E = -295.09212367254133
hkl_projection = array([ 0.31956253, -0.9324485 ,  0.2868157 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
