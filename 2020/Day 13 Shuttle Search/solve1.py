if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        earliest_timestamp = int(lines[0])
        bus_ids = [int(i) for i in lines[1].split(',') if i != 'x']

    next_bus = list(map(lambda x: ((earliest_timestamp // x) + 1) * x, bus_ids))

    earliest_bus = min(next_bus)
    print(bus_ids[next_bus.index(earliest_bus)] * (earliest_bus - earliest_timestamp))
