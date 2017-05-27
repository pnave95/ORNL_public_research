#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-180.519685373_hkl-14.8768719767,-1.49103519905,-0.845213942272/sample/sampleassembly.xml'
psi = -0.00236269317797221
hkl2Q = array([[-0.65847114,  0.93590177,  0.        ],
       [ 0.66178249,  0.46560941, -0.80916512],
       [-0.66178249, -0.46560941, -0.80916512]])
pp = array([ 0.34668187,  2.97990129, -0.39603786])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023006004840744471
Q = array([  9.36859768, -14.22399129,   1.89041131])
E = -180.5196853733834
hkl_projection = array([ 0.36761209, -0.97722748, -0.47800277])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
