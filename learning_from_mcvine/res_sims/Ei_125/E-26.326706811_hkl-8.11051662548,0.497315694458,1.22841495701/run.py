#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-26.326706811_hkl-8.11051662548,0.497315694458,1.22841495701/sample/sampleassembly.xml'
psi = -0.0029597062534506583
hkl2Q = array([[-0.65791228,  0.93629472,  0.        ],
       [ 0.66206035,  0.46521423, -0.80916512],
       [-0.66206035, -0.46521423, -0.80916512]])
pp = array([ 1.0462959 ,  2.81163029,  0.49485598])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033466042337584887
Q = array([ 4.85197665, -7.93395168, -1.39640104])
E = -26.326706810982586
hkl_projection = array([-0.3300891 ,  0.66787622,  0.60775173])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
