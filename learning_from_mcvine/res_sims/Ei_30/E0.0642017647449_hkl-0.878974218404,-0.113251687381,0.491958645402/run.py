#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E0.0642017647449_hkl-0.878974218404,-0.113251687381,0.491958645402/sample/sampleassembly.xml'
psi = -0.0006059499364774363
hkl2Q = array([[-0.66011426,  0.93474356,  0.        ],
       [ 0.66096351,  0.46677127, -0.80916512],
       [-0.66096351, -0.46677127, -0.80916512]])
pp = array([ 2.87076423,  0.87104116,  0.2417501 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0069411335106369975
Q = array([ 0.18020147, -1.10411029, -0.30643646])
E = 0.064201764744893808
hkl_projection = array([-0.75483033,  0.80571565,  0.0463051 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
