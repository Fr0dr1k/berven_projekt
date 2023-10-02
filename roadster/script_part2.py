import roadster as r, numpy as np, matplotlib.pyplot as plt


anna = r.load_route("speed_anna.npz")
elsa = r.load_route("speed_elsa.npz")


def script_2a():
    print("Anna time", r.time_to_destination(anna[0][-1],"speed_anna.npz",10000000),"h")
    print("Elsa time", r.time_to_destination(elsa[0][-1], "speed_elsa.npz", 10000000),"h")


def script_2b():
    print("Total consumption Anna", r.total_consumption(anna[0][-1],"speed_anna.npz",100000), "Wh")
    print("Total consumption Elsa", r.total_consumption(elsa[0][-1], "speed_elsa.npz", 100000), "Wh")

def script_2c():
    route = "speed_anna.npz"
    x = r.load_route(route)[0][-1]
    n = 2
    times_to_run = 20
    hvec = np.zeros(times_to_run)  # alla värden på h
    ETvec = np.zeros(times_to_run)  # felet för trapets

    for ind in range(times_to_run):
        Th = r.time_to_destination(x, route, n)
        T2h = r.time_to_destination(x, route, int(n / 2))
        hvec[ind] = (x) / n
        ETvec[ind] = np.abs((Th - T2h) / 3)
        n = 2 * n

    plt.loglog(hvec, ETvec, '-ob',label="fel")
    plt.loglog(hvec, hvec ** 2, '--b', label="O^2")
    plt.loglog(hvec, hvec ** 4, '--r', label="O^4")
    plt.xlabel("x/n")
    plt.legend()


    plt.show()


if __name__ == '__main__':
    script_2a()
    #script_2b()
    #script_2c()
