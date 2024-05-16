import numpy as np
import matplotlib.pyplot as plt
import pdb

st = pdb.set_trace


import external  # imports external.py
import experiment as ex  #


def my_first_experiment():
    exp = ex.Experiment(lo_freq=5, rx_t=3.125)  # experiment construct
    tx0_times = np.array([50, 130]) # abs times
    tx0_amps = np.array([0.5, 0])   # values of each times

    event_dict = {'tx0': (tx0_times, tx0_amps)}
    exp.add_flodict(event_dict)
    exp.add_flodict({'rx0_en': (np.array([200, 400]), np.array([1, 0]))})   # readout (start at 200us and end at 400us)

    # exp.plot_sequence()
    # plt.show()

    rxd, msgs = exp.run()
    exp.close_server(only_if_sim=True)



if __name__ == "__main__":
    my_first_experiment()
