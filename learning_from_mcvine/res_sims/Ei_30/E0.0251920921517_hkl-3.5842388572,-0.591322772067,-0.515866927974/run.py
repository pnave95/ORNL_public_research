#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E0.0251920921517_hkl-3.5842388572,-0.591322772067,-0.515866927974/sample/sampleassembly.xml'
psi = -0.0025315187040688366
hkl2Q = array([[-0.65831313,  0.93601293,  0.        ],
       [ 0.66186109,  0.46549768, -0.80916512],
       [-0.66186109, -0.46549768, -0.80916512]])
pp = array([ 1.2203231 ,  2.74058598, -0.72427011])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0069721367277685575
Q = array([ 2.30961021, -3.39001842,  0.89589928])
E = 0.025192092151701928
hkl_projection = array([ 0.6651088 ,  0.30508234,  0.71685064])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
