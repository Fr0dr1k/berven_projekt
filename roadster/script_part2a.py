import roadster as r

if __name__ == '__main__':
    anna = r.load_route("speed_anna.npz")
    print(r.time_to_destination(anna[0][-1],"speed_anna.npz",10000000))