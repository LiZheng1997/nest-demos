
import nest
import matplotlib.pyplot as plt

neuron1 = nest.Create("iaf_psc_alpha")
neuron1.set(I_e=376.0)
neuron2 = nest.Create("iaf_psc_alpha")
multimeter = nest.Create("multimeter")
multimeter.set(record_from=["V_m"])

nest.Connect(neuron1, neuron2, syn_spec={"weight":20.0, "delay":1.0})
# nest.Connect(neuron1, neuron2, syn_spec = {"weight":20.0})
nest.Connect(multimeter, neuron2)

# 设置仿真的时间长度
nest.Simulate(1000.0)


dmm = multimeter.get()
print("查看下dmm的数据结构: ", dmm)

Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

plt.figure(1)
plt.plot(ts, Vms)

plt.show()