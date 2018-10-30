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

        # memoization data structures
        self.routes_le_stops = dict() # (<port-a>, <port-b>, <max-stops> + 1) -> <number-of-routes>
        self.routes_le_days = dict() # (<port-a>, <port-b>, <max-days>) -> <number-of-routes>


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


    # find the number of routes from port_a to port_b with no more stops than max_stops
    # port_a in the beginning and port_b in the end are not counted as stops
    # If port_a and port_b are the same then it counts the route of going nowhere
    def count_routes_le_stops(self, port_a, port_b, max_stops):
        route_limit = max_stops + 1
        direct_distance = lambda a, b: 1
        memoization = self.routes_le_stops
        return self._count_routes(port_a, port_b, route_limit, direct_distance, memoization)

    # find the number of routes from port_a to port_b with exactly a number of stops
    def count_routes_eq_stops(self, port_a, port_b, exact_stops):
        return self.count_routes_le_stops(port_a, port_b, exact_stops) - \
               self.count_routes_le_stops(port_a, port_b, exact_stops-1)

    # find the number of routes from port_a to port_b with exactly a number of days
    def count_routes_le_days(self, port_a, port_b, max_days):
        route_limit = max_days
        direct_distance = lambda a, b: self.shipping_time[(a, b)]
        memoization = self.routes_le_days
        return self._count_routes(port_a, port_b, route_limit, direct_distance, memoization)

    def _count_routes(self, port_a, port_b, route_limit, direct_distance, memoization):
        if route_limit < 0:
            return 0

        if (port_a, port_b, route_limit) in memoization:
            return memoization[(port_a, port_b, route_limit)]
        elif port_a == port_b:
            memoization[(port_a, port_b, route_limit)] = 1
        else:
            memoization[(port_a, port_b, route_limit)] = 0

        if route_limit == 0:
            return memoization[(port_a, port_b, route_limit)]

        if port_a in self.shipping_graph:
            ports_to_go = self.shipping_graph[port_a]
        else:
            ports_to_go = []
        for port in ports_to_go:
            d = direct_distance(port_a, port)
            memoization[(port_a, port_b, route_limit)] += \
            self._count_routes(port, port_b, route_limit - d, direct_distance, memoization)
        return memoization[(port_a, port_b, route_limit)]
