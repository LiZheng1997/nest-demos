
import nest
import matplotlib.pyplot as plt

neuron = nest.Create("iaf_psc_alpha")

# 获得电流值的常量
current = neuron.get("I_e")
print("当前电流值", current)
neuron.get(["V_reset", "V_th"])

# 设置电流值，必须要对应好类型，NEST对数据类型是敏感的
neuron.set(I_e=376.0)
print("当前电流值", current)

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
print("查看下dmm的数据结构: ", dmm)

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