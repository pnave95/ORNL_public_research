#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E169.453784326_hkl-1.32899675509,3.74354910985,0.0812083798265/sample/sampleassembly.xml'
psi = 0.03008110062366459
hkl2Q = array([[-0.6884835 ,  0.9140497 ,  0.        ],
       [ 0.64633074,  0.48683135, -0.80916512],
       [-0.64633074, -0.48683135, -0.80916512]])
pp = array([ 2.99681765, -0.13814472,  0.75247935])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017769298364381748
Q = array([ 3.28207572,  0.5681732 , -3.09486034])
E = 169.45378432570544
hkl_projection = array([ 0.98298375,  0.38854771, -0.0751482 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
