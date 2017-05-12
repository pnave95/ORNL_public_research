#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[ 1.1  0.   0. ]/out.res_comps_tmp1/sample/sampleassembly.xml'
psi = 0.6331165431200033
hkl2Q = array([[-1.08544615,  0.36235761, -0.        ],
       [ 0.25622552,  0.76752633, -0.80916512],
       [-0.25622552, -0.76752633, -0.80916512]])
pp = array([ 1.61690262,  2.5269796 ,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0095085381805373355
Q = array([ 3.14691492, -1.05054366,  0.        ])
E = 27.0
hkl_projection = array([ 1.1,  0. ,  0. ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
