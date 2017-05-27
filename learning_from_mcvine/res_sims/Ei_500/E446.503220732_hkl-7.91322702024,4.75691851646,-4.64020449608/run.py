#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E446.503220732_hkl-7.91322702024,4.75691851646,-4.64020449608/sample/sampleassembly.xml'
psi = -0.017438789894246933
hkl2Q = array([[ -6.44287101e-01,   9.45722212e-01,   7.68636394e-17],
       [  6.68726589e-01,   4.55579778e-01,  -8.09165116e-01],
       [ -6.68726589e-01,  -4.55579778e-01,  -8.09165116e-01]])
pp = array([ 2.39081081,  1.81218754,  0.05343969])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0022894832468749841
Q = array([ 11.38249612,  -3.20257535,  -0.09444091])
E = 446.50322073213113
hkl_projection = array([ 0.9486927 , -0.18549603,  0.9507608 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
