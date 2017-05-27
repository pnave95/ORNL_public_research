#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E4.97977961107_hkl-4.38420456504,0.864451679709,-0.493681195599/sample/sampleassembly.xml'
psi = -0.004044539628886073
hkl2Q = array([[-0.65689617,  0.93700789,  0.        ],
       [ 0.66256464,  0.46449574, -0.80916512],
       [-0.66256464, -0.46449574, -0.80916512]])
pp = array([ 0.03389886,  2.99980847,  0.2588259 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.007058352203003263
Q = array([ 3.779818  , -3.47718736, -0.30001454])
E = 4.9797796110692971
hkl_projection = array([-0.22996022, -0.03708205, -0.23085986])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
