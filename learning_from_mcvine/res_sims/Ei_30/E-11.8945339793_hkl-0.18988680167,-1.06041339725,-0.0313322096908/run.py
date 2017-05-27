#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-11.8945339793_hkl-0.18988680167,-1.06041339725,-0.0313322096908/sample/sampleassembly.xml'
psi = 0.0031117394317997475
hkl2Q = array([[-0.66358478,  0.93228301,  0.        ],
       [ 0.65922364,  0.4692253 , -0.80916512],
       [-0.65922364, -0.4692253 , -0.80916512]])
pp = array([ 2.96639224,  0.44779132, -0.59945515])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067658975577604367
Q = array([-0.55238865, -0.65989917,  0.88340246])
E = -11.89453397927015
hkl_projection = array([ 0.13886154,  0.2343758 , -0.16442429])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
