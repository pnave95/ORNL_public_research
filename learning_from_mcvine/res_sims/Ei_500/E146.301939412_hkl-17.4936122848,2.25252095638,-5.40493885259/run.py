#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E146.301939412_hkl-17.4936122848,2.25252095638,-5.40493885259/sample/sampleassembly.xml'
psi = -0.006133839541134673
hkl2Q = array([[-0.65493705,  0.9383783 ,  0.        ],
       [ 0.66353366,  0.46311043, -0.80916512],
       [-0.66353366, -0.46311043, -0.80916512]])
pp = array([-0.21635888,  2.99218797, -0.59307866])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017600405073696533
Q = array([ 16.53819709, -12.86937671,   2.55082659])
E = 146.30193941230516
hkl_projection = array([-0.16103766, -0.38509494, -0.34877829])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
