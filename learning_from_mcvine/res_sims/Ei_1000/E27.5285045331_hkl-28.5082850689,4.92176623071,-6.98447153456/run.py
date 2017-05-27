#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E27.5285045331_hkl-28.5082850689,4.92176623071,-6.98447153456/sample/sampleassembly.xml'
psi = -0.0068479249200229814
hkl2Q = array([[-0.6542668 ,  0.93884574,  0.        ],
       [ 0.66386419,  0.46263649, -0.80916512],
       [-0.66386419, -0.46263649, -0.80916512]])
pp = array([-0.61711611,  2.93584191, -0.2305222 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012023167337090711
Q = array([ 26.55614926, -21.25662206,   1.66906918])
E = 27.528504533063597
hkl_projection = array([-0.59963589, -0.20567193, -0.71257575])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
