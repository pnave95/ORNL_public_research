#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison_v2/res_sims/Ei_1000/E-763.537741337_hkl-10.6846419456,-8.60343159127,5.10873913798/sample/sampleassembly.xml'
psi = 0.0006624716557243732
hkl2Q = array([[ -6.61299382e-01,   9.33905508e-01,   7.78361948e-17],
       [  6.60370918e-01,   4.67609277e-01,  -8.09165116e-01],
       [ -6.60370918e-01,  -4.67609277e-01,  -8.09165116e-01]])
pp = array([ 2.47992779,  1.68818191, -0.2912569 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011465437094112072
Q = array([ -1.98937166, -16.39038422,   2.82778323])
E = -763.5377413368949
hkl_projection = array([-0.4007532 ,  0.03081046, -0.59327579])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
