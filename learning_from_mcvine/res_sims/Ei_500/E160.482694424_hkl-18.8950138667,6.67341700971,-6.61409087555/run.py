#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E160.482694424_hkl-18.8950138667,6.67341700971,-6.61409087555/sample/sampleassembly.xml'
psi = -0.008718693965989453
hkl2Q = array([[-0.65250929,  0.94006808,  0.        ],
       [ 0.66472852,  0.46139374, -0.80916512],
       [-0.66472852, -0.46139374, -0.80916512]])
pp = array([-1.2926749 ,  2.70721104,  0.01117268])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017604172419449738
Q = array([ 21.16175746, -11.63182645,  -0.04800464])
E = 160.48269442434366
hkl_projection = array([-0.21692312, -0.5109904 ,  0.36304159])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
