#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-76.4681192196_hkl-11.2505274721,1.43848012151,-0.131747189152/sample/sampleassembly.xml'
psi = -0.004160946923604255
hkl2Q = array([[-0.65678709,  0.93708436,  0.        ],
       [ 0.6626187 ,  0.4644186 , -0.80916512],
       [-0.6626187 , -0.4644186 , -0.80916512]])
pp = array([-0.190743  ,  2.99393004,  0.3225848 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.003268310855552558
Q = array([ 8.42966318, -9.81345051, -1.05736271])
E = -76.468119219644052
hkl_projection = array([ 0.56293918, -0.00816118, -0.41867969])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
