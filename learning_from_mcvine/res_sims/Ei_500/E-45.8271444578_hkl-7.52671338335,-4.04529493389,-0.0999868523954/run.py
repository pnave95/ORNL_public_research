#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-45.8271444578_hkl-7.52671338335,-4.04529493389,-0.0999868523954/sample/sampleassembly.xml'
psi = -0.0012612321356924466
hkl2Q = array([[-0.6595016 ,  0.93517592,  0.        ],
       [ 0.66126924,  0.46633805, -0.80916512],
       [-0.66126924, -0.46633805, -0.80916512]])
pp = array([ 2.49236566,  1.66976447, -0.63081145])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016894595156243257
Q = array([ 2.35496867, -8.87864844,  3.35421742])
E = -45.82714445780033
hkl_projection = array([-0.32898088,  0.53208406,  0.88642521])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
