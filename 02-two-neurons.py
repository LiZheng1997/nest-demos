
import nest
import matplotlib.pyplot as plt

neuron = nest.Create("iaf_psc_alpha")
# 创建一个相同的神经元
neuron2 = nest.Create("iaf_psc_alpha")
neuron2.set({"I_e": 370.0})

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
nest.Connect(multimeter, neuron2)
nest.Connect(neuron, spikerecorder)

# 设置仿真的时间长度
nest.Simulate(1000.0)

dmm = multimeter.get()
print("查看下dmm的数据结构: ", dmm)

# 错误的方法，当一个万用表测量两个神经元的时候
Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]
plt.figure(1)
plt.plot(ts, Vms)


# 正确的方法，将数据进行切片
plt.figure(2)
Vms1 = dmm["events"]["V_m"][::2] # start at index 0: till the end: each second entry
ts1 = dmm["events"]["times"][::2]
plt.plot(ts1, Vms1)
Vms2 = dmm["events"]["V_m"][1::2] # start at index 1: till the end: each second entry
ts2 = dmm["events"]["times"][1::2]
plt.plot(ts2, Vms2)

plt.show()