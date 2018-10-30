class ShippingOperator:
    def __init__(self, shipping_network_data):
        # basic data structures
        self.shipping_time = dict() # (<port-a>, <port-b>) -> <number-of-traveling-days>
        self.shipping_graph = dict() # <port-a> -> <port-b>
        for route in shipping_network_data:
            self.shipping_time[route[:2]] = route[2]
            try:
                self.shipping_graph[route[0]].add(route[1])
            except:
                self.shipping_graph[route[0]] = set([route[1]])

    # get the time for direct route of a sequence of ports
    def get_journey_time(self, *journey):
        total_days = 0
        for i in xrange(len(journey)-1):
            try:
                total_days += self.shipping_time[journey[i:i+2]]
            except:
                return "Journey %s is invalid because there is no direct connection from %s to %s" \
                       % (journey, journey[i], journey[i+1])
        return total_days

    # find the time of the shortest journey
    def find_shortest_journey_time(self, port_a, port_b):
        visited = set()
        eventualy_shortest_time = {port_a: 0}
        curr_port = port_a

        while curr_port != port_b:
            visited.add(curr_port)
            curr_time = eventualy_shortest_time[curr_port]
            del eventualy_shortest_time[curr_port]
            if curr_port in self.shipping_graph:
                ports_to_go = self.shipping_graph[curr_port]
            else:
                ports_to_go = []
            for port in ports_to_go:
                if port in visited:
                    continue
                port_time = curr_time + self.shipping_time[(curr_port, port)]
                if port not in eventualy_shortest_time \
                   or eventualy_shortest_time[port] > port_time:
                    eventualy_shortest_time[port] = port_time

            if len(eventualy_shortest_time) == 0:
                return "there is no connection from %s to %s" % (port_a, port_b)
            curr_port = min(eventualy_shortest_time, key = lambda p: eventualy_shortest_time[p])

        return eventualy_shortest_time[port_b]

