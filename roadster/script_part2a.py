import roadster as r

if __name__ == '__main__':
    anna = r.load_route("speed_anna.npz")
    elsa = r.load_route("speed_elsa.npz")
    print("Anna time",r.time_to_destination(anna[0][-1],"speed_anna.npz",10000000))
    print("Elsa time", r.time_to_destination(elsa[0][-1], "speed_elsa.npz", 10000000))
