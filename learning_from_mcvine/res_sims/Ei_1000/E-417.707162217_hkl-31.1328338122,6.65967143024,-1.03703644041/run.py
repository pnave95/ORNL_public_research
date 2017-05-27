#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-417.707162217_hkl-31.1328338122,6.65967143024,-1.03703644041/sample/sampleassembly.xml'
psi = -0.005447586175995172
hkl2Q = array([[-0.65558086,  0.93792863,  0.        ],
       [ 0.66321569,  0.46356567, -0.80916512],
       [-0.66321569, -0.46356567, -0.80916512]])
pp = array([-0.39751879,  2.9735465 ,  0.52779068])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011672050253981998
Q = array([ 25.51466731, -25.63244657,  -4.5496401 ])
E = -417.70716221652822
hkl_projection = array([ 0.63687069,  0.1813247 ,  0.49948577])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
