#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E9.25752823541_hkl-0.671144309167,0.316939654411,-0.0445097757369/sample/sampleassembly.xml'
psi = -0.0054845291705775115
hkl2Q = array([[ -6.55546206e-01,   9.37952847e-01,  -7.75003257e-17],
       [  6.63232818e-01,   4.63541168e-01,  -8.09165116e-01],
       [ -6.63232818e-01,  -4.63541168e-01,  -8.09165116e-01]])
pp = array([ 2.96803989,  0.436737  ,  0.20840694])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0071896993249127971
Q = array([ 0.67969123, -0.46195502, -0.22044075])
E = 9.2575282354052177
hkl_projection = array([ 0.03120799,  0.60922037,  0.44142157])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
