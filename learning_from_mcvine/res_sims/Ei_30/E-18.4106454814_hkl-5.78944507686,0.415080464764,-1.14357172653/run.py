#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-18.4106454814_hkl-5.78944507686,0.415080464764,-1.14357172653/sample/sampleassembly.xml'
psi = -0.0038283501649459778
hkl2Q = array([[-0.65709872,  0.93686586,  0.        ],
       [ 0.6624642 ,  0.46463896, -0.80916512],
       [-0.6624642 , -0.46463896, -0.80916512]])
pp = array([-0.63490462,  2.93204641, -0.36775627])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066790217250202229
Q = array([ 4.83678826, -4.6997229 ,  0.58946972])
E = -18.410645481383057
hkl_projection = array([-0.15355694,  0.3852303 ,  0.31349947])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
