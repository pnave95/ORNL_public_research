#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E287.620105529_hkl-7.38076775041,0.447324514194,-2.99473536155/sample/sampleassembly.xml'
psi = -0.006370740867129971
hkl2Q = array([[-0.65471472,  0.93853343,  0.        ],
       [ 0.66364335,  0.46295322, -0.80916512],
       [-0.66364335, -0.46295322, -0.80916512]])
pp = array([ 2.54040043,  1.59573358, -0.61670482])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018659476584814243
Q = array([ 7.11659748, -5.33358457,  2.06127599])
E = 287.62010552949891
hkl_projection = array([ 0.6997074 , -0.82367219, -0.10556471])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
