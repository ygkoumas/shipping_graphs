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
