#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E509.985081185_hkl-14.368649967,1.69070908506,-2.05191309472/sample/sampleassembly.xml'
psi = -0.0055468349157010675
hkl2Q = array([[ -6.55487765e-01,   9.37993689e-01,  -7.74969512e-17],
       [  6.63261698e-01,   4.63499844e-01,  -8.09165116e-01],
       [ -6.63261698e-01,  -4.63499844e-01,  -8.09165116e-01]])
pp = array([ 1.96588398,  2.26612007, -0.05640189])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001289451656327139
Q = array([ 11.9008122 , -11.74299819,   0.29227368])
E = 509.98508118459154
hkl_projection = array([ 0.17362039, -0.08235388,  0.6710856 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
