import nest
import matplotlib.pyplot as plt
import numpy

# 批量创建三个同样配置的神经元簇
ndict = {"I_e": 200.0, "tau_m": 20.0}
nest.SetDefaults("iaf_psc_alpha", ndict)
neuronpop1 = nest.Create("iaf_psc_alpha", 100)
neuronpop2 = nest.Create("iaf_psc_alpha", 100)
neuronpop3 = nest.Create("iaf_psc_alpha", 100)

edict = {"I_e": 200.0, "tau_m": 20.0}
nest.CopyModel("iaf_psc_alpha", "exc_iaf_psc_alpha")
nest.SetDefaults("exc_iaf_psc_alpha", edict)

# 等同于下面
idict = {"I_e": 300.0}
nest.CopyModel("iaf_psc_alpha", "inh_iaf_psc_alpha", params=idict)

epop1 = nest.Create("exc_iaf_psc_alpha", 100)
epop2 = nest.Create("exc_iaf_psc_alpha", 100)
ipop1 = nest.Create("inh_iaf_psc_alpha", 30)
ipop2 = nest.Create("inh_iaf_psc_alpha", 30)

# 用不同的参数创建神经元
parameter_dict = {"I_e": [200.0, 150.0], "tau_m": 20.0, "V_m": [-77.0, -66.0]}
pop3 = nest.Create("iaf_psc_alpha", 2, params=parameter_dict)
# 打印下pop3的神经元参数
print(pop3.get(["I_e", "tau_m", "V_m"]))

# 给神经元簇设置参数
Vth=-55.
Vrest=-70.
dVms =  {"V_m": [Vrest+(Vth-Vrest)*numpy.random.rand() for x in range(len(epop1))]}
epop1.set(dVms)
#另一种设置随机参数的方式
epop1.set({"V_m": Vrest + nest.random.uniform(0.0, Vth-Vrest)})

# 构建神经元之间随机的连接
d = 1.0
Je = 2.0
Ke = 20
Ji = -4.0
Ki = 12
conn_dict_ex = {"rule": "fixed_indegree", "indegree": Ke}
conn_dict_in = {"rule": "fixed_indegree", "indegree": Ki}
syn_dict_ex = {"delay": d, "weight": Je}
syn_dict_in = {"delay": d, "weight": Ji}
nest.Connect(epop1, ipop1, conn_dict_ex, syn_dict_ex)
nest.Connect(ipop1, epop1, conn_dict_in, syn_dict_in)