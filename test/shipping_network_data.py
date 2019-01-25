# shiping network data of all posible one way routes from port-a to port-b:
# (<port-a>, <port-b>, <number-of-traveling-days>)
shipping_network_data = [
    ("buenos-aires", "new-york", 6),
    ("buenos-aires", "casablanca", 5),
    ("buenos-aires", "cape-town", 4),
    ("new-york", "liverpool", 4),
    ("liverpool", "casablanca", 3),
    ("liverpool", "cape-town", 6),
    ("casablanca", "liverpool", 3),
    ("casablanca", "cape-town", 6),
    ("cape-town", "new-york", 8),
]
