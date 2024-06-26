import nest
import matplotlib.pyplot as plt


pop1 = nest.Create("iaf_psc_alpha", 10)
pop1.set({"I_e": 376.0})
pop2 = nest.Create("iaf_psc_alpha", 10)
multimeters = nest.Create("multimeter", 10)
multimeters.set({"record_from":["V_m"]})

# 默认是all_to_all的方式
# nest.Connect(pop1, pop2, syn_spec={"weight":20.0})
# 可以设置成one_to_one, 相当于pop1中的神经元和pop2中的神经元一一对应的连接
nest.Connect(pop1, pop2, "one_to_one", syn_spec={"weight":20.0, "delay":1.0})

nest.Connect(multimeters, pop2, "one_to_one")

# 设置仿真的时间长度
nest.Simulate(1000.0)

for i in range(len(multimeters)):
    dmm = multimeters[i].get()
    # print("查看万用表的数据: ", dmm)
    # print("查看下dmm的数据结构: ", dmm)

    Vms = dmm["events"]["V_m"]
    ts = dmm["events"]["times"]

    plt.figure(1)
    plt.plot(ts, Vms)

    plt.show()