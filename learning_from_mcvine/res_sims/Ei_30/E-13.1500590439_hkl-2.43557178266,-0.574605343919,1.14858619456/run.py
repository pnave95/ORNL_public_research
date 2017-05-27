#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-13.1500590439_hkl-2.43557178266,-0.574605343919,1.14858619456/sample/sampleassembly.xml'
psi = -0.0005650633637726799
hkl2Q = array([[-0.66015248,  0.93471657,  0.        ],
       [ 0.66094443,  0.4667983 , -0.80916512],
       [-0.66094443, -0.4667983 , -0.80916512]])
pp = array([ 2.20819648,  2.03073098,  0.30612725])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067350045775914653
Q = array([ 0.46891491, -3.08095218, -0.46444528])
E = -13.150059043857038
hkl_projection = array([-0.3042319 , -0.54441744,  0.88323146])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
