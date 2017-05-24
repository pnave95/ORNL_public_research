#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-129.300456683_hkl-5.0443248317,-4.78587760602,0.192148075713/sample/sampleassembly.xml'
psi = -2.2226309510833694e-05
hkl2Q = array([[-0.66065978,  0.93435808,  0.        ],
       [ 0.66069093,  0.46715701, -0.80916512],
       [-0.66069093, -0.46715701, -0.80916512]])
pp = array([ 2.52559454,  1.61906522, -0.85501336])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023331982344435712
Q = array([ 0.04364611, -7.03872527,  3.71708569])
E = -129.30045668311374
hkl_projection = array([ 0.34470058,  0.38259796, -0.58579157])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
