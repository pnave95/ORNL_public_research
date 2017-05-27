#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-9.01720628279_hkl-5.39583705656,1.47382305397,-0.471590176621/sample/sampleassembly.xml'
psi = -0.004329966958114136
hkl2Q = array([[-0.65662869,  0.93719535,  0.        ],
       [ 0.66269719,  0.4643066 , -0.80916512],
       [-0.66269719, -0.4643066 , -0.80916512]])
pp = array([-0.71091885,  2.91454874,  0.56904098])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0068025901317059698
Q = array([ 4.83228132, -4.15368521, -0.81097188])
E = -9.0172062827892248
hkl_projection = array([-0.30572806, -0.72612609, -0.05814286])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
