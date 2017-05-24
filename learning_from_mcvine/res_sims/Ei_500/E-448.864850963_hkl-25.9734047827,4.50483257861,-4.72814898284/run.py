#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-448.864850963_hkl-25.9734047827,4.50483257861,-4.72814898284/sample/sampleassembly.xml'
psi = -0.005498001481044406
hkl2Q = array([[-0.65553357,  0.93796168,  0.        ],
       [ 0.66323906,  0.46353223, -0.80916512],
       [-0.66323906, -0.46353223, -0.80916512]])
pp = array([-1.05479498,  2.80845288, -0.0252704 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016128773429918118
Q = array([ 23.1501128 , -20.08227378,   0.18069984])
E = -448.86485096278597
hkl_projection = array([ 0.69725687,  0.61169871, -0.45595857])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
