#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E596.000891281_hkl-17.4135409149,4.51841215761,-2.9768694496/sample/sampleassembly.xml'
psi = -0.006964945039510562
hkl2Q = array([[-0.65415693,  0.9389223 ,  0.        ],
       [ 0.66391832,  0.4625588 , -0.80916512],
       [-0.66391832, -0.4625588 , -0.80916512]])
pp = array([ 1.21748966,  2.7418459 ,  0.26547298])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0013209803529705686
Q = array([ 16.36744325, -12.88295341,  -1.24736258])
E = 596.00089128137688
hkl_projection = array([ 0.03403683, -0.45565122, -0.49293251])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
