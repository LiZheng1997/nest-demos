import nest
import matplotlib.pyplot as plt

neuron = nest.Create("iaf_psc_alpha")

noise_ex = nest.Create("poisson_generator")
noise_in = nest.Create("poisson_generator")
noise_ex.set(rate=80000.0)
noise_in.set(rate=15000.0)

neuron.set(I_e=0.0)

syn_dict_ex = {"weight": 1.2}
syn_dict_in = {"weight": -2.0}
nest.Connect(noise_ex, neuron, syn_spec=syn_dict_ex)
nest.Connect(noise_in, neuron, syn_spec=syn_dict_in)

# 创建一个万用表，用来记录膜电压
multimeter = nest.Create("multimeter")
multimeter.set(record_from=["V_m"])

# 创建一个脉冲记录仪，录制由神经元产生的脉冲事件
spikerecorder = nest.Create("spike_recorder")

# 将万用表和神经元关联，将脉冲记录仪和神经元关联
nest.Connect(multimeter, neuron)
nest.Connect(neuron, spikerecorder)

# 设置仿真的时间长度
nest.Simulate(1000.0)

dmm = multimeter.get()
# print("查看下dmm的数据结构: ", dmm)

Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

plt.figure(1)
plt.plot(ts, Vms)


events = spikerecorder.get("events")
senders = events["senders"]
ts = events["times"]
plt.figure(2)
plt.plot(ts, senders, ".")

plt.show()