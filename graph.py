import numpy as np
import matplotlib.pyplot as plt


deltax_cpu = 3.5/1000
a_cpu = deltax_cpu*(3/100)*(3/100)
k_cpu = 310
r_cpu = deltax_cpu/(a_cpu*k_cpu)

deltax_copper = 60/1000
a_copper = deltax_copper*(6/100)*(6/100) #?
k_copper = 400
r_copper = deltax_copper/(a_copper*k_copper)

deltax_tp = 0.1/1000
rad_tp = 4.5/100
k_tp = 7
a_tp = np.pi*rad_tp**2
r_tp = deltax_tp/(a_tp*0.95*k_tp)

h_air = 2.3
r_air = 1/(a_copper*h_air)

t_max = 38
t_air = 20




x_tp = []
y_tp = []

for _ in range(31):
    t_max += 2
    t_out = t_air + t_max*0.4
    x_tp.append(t_max)
    Q = (t_max-t_out)/(r_cpu+r_tp+r_copper+r_air)
    power = (Q/(t_out-t_air))**3
    y_tp.append(power)
    
t_max = 38

k_lm = 73
r_lm = deltax_tp/(a_tp*0.95*k_lm)

x_lm = []
y_lm = []

for _ in range(31):
    t_max += 2
    t_out = t_air + t_max*0.4
    x_lm.append(t_max)
    Q = (t_max-t_out)/(r_cpu+r_lm+r_copper+r_air)
    power = (Q/(t_out-t_air))**3
    y_lm.append(power)

# plt.plot(x_tp,y_tp, 'r-o',x_lm,y_lm,'b-o')
# essentially identical lines, so show 2 subplots
fig, (ax_tp, ax_lm) = plt.subplots(2, sharex=True)
ax_tp.plot(x_tp,y_tp, 'r-o')
ax_lm.plot(x_lm,y_lm,'b-o')
fig.legend([r'Conductivity of thermal paste, $k_{thermal paste}$ / $\frac{W}{m•K}$', r'Conductivity of liquid metal, $k_{liquid metal}$ / $\frac{W}{m•K}$'])
fig.text(0.5, 0.04, 'Temperature of CPU, $T_{max} / °C $', ha='center', va='center')
fig.text(0.06, 0.5, 'Relative power required for cooling, P', ha='center', va='center', rotation='vertical')
plt.show()

# I am going to plot Q with varying ambient temperatures and see how much it affects it