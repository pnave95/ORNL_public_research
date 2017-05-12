#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[ 1.1  0.   0. ]/out.res_comps_tmp12/sample/sampleassembly.xml'
psi = 0.12262971468350206
hkl2Q = array([[-0.77001041,  0.84651069,  0.        ],
       [ 0.59857345,  0.54447958, -0.80916512],
       [-0.59857345, -0.54447958, -0.80916512]])
pp = array([ 0.33579948,  2.98114721,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0049160953674105409
Q = array([ 4.81102503, -5.28899877,  0.        ])
E = 1.875
hkl_projection = array([ 1.1,  0. ,  0. ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
