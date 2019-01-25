from shipping_network_data import shipping_network_data
from shipping_operator import ShippingOperator

def test(test_cases, code, msg):
    for i, case in enumerate(test_cases):
        if code(*case[0]) != case[1]:
            print "Failed: " + msg + ", case %s" % i
            return
    print "Passed: " + msg


so = ShippingOperator(shipping_network_data)

# test time calculation of the direct routes
get_journey_time_test_cases = [
    [("buenos-aires", "new-york", "liverpool"), 10],
    [("buenos-aires", "casablanca", "liverpool"), 8],
    [("buenos-aires", "cape-town", "new-york", "liverpool", "casablanca"), 19],
    [("buenos-aires", "cape-town", "casablanca"), "Journey ('buenos-aires', 'cape-town', 'casablanca') is invalid because there is no direct connection from cape-town to casablanca"]
]
get_journey_time_code = so.get_journey_time
get_journey_time_msg = "get_journey_time_test_cases"
test(get_journey_time_test_cases, get_journey_time_code, get_journey_time_msg)


# test finding the time of the shortest journey
find_shortest_journey_time_test_cases = [
    [("buenos-aires", "liverpool"), 8],
    [("new-york", "new-york"), 0]
]
find_shortest_journey_time_code = so.find_shortest_journey_time
find_shortest_journey_time_msg = "find_shortest_journey_time_test_cases"
test(find_shortest_journey_time_test_cases, find_shortest_journey_time_code, find_shortest_journey_time_msg)


# test count of number of routes with maximum number of stops
count_routes_le_stops_test_cases = [
    [("liverpool", "liverpool", 3), 5]
]
count_routes_le_stops_code = so.count_routes_le_stops
count_routes_le_stops_msg = "count_routes_le_stops_test_cases"
test(count_routes_le_stops_test_cases, count_routes_le_stops_code, count_routes_le_stops_msg)


# test count of number of routes with exact number of stops
count_routes_eq_stops_test_cases = [
    [("buenos-aires", "liverpool", 4), 3]
]
count_routes_eq_stops_code = so.count_routes_eq_stops
count_routes_eq_stops_msg = "count_routes_eq_stops_test_cases"
test(count_routes_eq_stops_test_cases, count_routes_eq_stops_code, count_routes_eq_stops_msg)


# test count of number of routes with maximum number of days
count_routes_le_days_test_cases = [
    [("liverpool", "liverpool", 25), 9]
]
count_routes_le_days_code = so.count_routes_le_days
count_routes_le_days_msg = "count_routes_le_days_test_cases"
test(count_routes_le_days_test_cases, count_routes_le_days_code, count_routes_le_days_msg)
