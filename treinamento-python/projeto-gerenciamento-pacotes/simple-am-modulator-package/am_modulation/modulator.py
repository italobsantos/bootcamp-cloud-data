import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0,1,1000)

message_amplitude = 10
message_frequency = 1000
message = message_amplitude * np.cos((2*np.pi)*message_frequency*x)


carrier_frequency = 100000
carrier = np.cos(2*np.pi*carrier_frequency*x)

tx_signal = ((1+message)*carrier)

plt.subplot(3,1,1)
plt.title('AM Modulation')
plt.plot(message,'b')
plt.xlabel('Message')

plt.subplot(3,1,2)
plt.plot(carrier, 'r')
plt.xlabel('Carrier')


plt.subplot(3,1,3)
plt.plot(tx_signal, 'g')
plt.xlabel('Modulated Signal')

plt.subplots_adjust(hspace=1)
fig = plt.gcf()
fig.set_size_inches(16, 9)

