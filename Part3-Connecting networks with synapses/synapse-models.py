import nest

nest.SetDefaults("stdp_synapse",{"tau_plus": 15.0})
nest.CopyModel("stdp_synapse","layer1_stdp_synapse",{"Wmax": 90.0})

nest.Create("iaf_psc_alpha", params={"tau_minus": 30.0})
conn_dict = {"rule": "fixed_indegree", "indegree": K}
syn_dict = {"synapse_model": "stdp_synapse", "alpha": 1.0}
nest.Connect(epop1, epop2, conn_dict, syn_dict)