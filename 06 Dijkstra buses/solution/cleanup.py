"""
Extract which bus routes attend which stops
"""
import collections
import pickle

# routes
routes = []
for line in open('../problem/routes.txt'):
    csv = line.split(',')
    route_id = csv[0]
    route_name = csv[3]
    routes.append((route_id, csv[2]+": "+route_name.rstrip()))

print 'Routes loaded. Total: %s| example: %s' % (len(routes), routes[5])

# stops
stops = {}
for line in open('../problem/stops.txt'):
    csv = line.split(',')
    stops[csv[0]] = csv[2]

print 'Stops loaded. Total %s' % (len(stops))

# trips
trips = collections.defaultdict(list)
trip2route = {}
for line in open('../problem/trips.txt'):
    csv = line.split(',')
    trips[csv[0]].append(csv[2]) 
    trip2route[csv[2]] = csv[0]

print '%s trips loaded. For route %s there is %s trips' % (len(trip2route.keys()),routes[5][1], len(trips[routes[5][0]]))

route_stops = collections.defaultdict(set)
distances = {}
for line in open('../problem/stop_times.txt','rb'):
    csv = line.split(',')
    trip_id = csv[0]
    route = trip2route[trip_id]
    stop_id = csv[3]
    route_stops[route].add(stop_id)
    try:
        distance = float(csv[8])  
    except:
        distance = 0.0
    distances[(trip_id,stop_id)] = distance

print 'route stops parsed. | example: for %s we have %s stops: ' % (routes[5][1],len(route_stops[routes[5][0]]))
for route_stop in route_stops[routes[5][0]]:
    print '    * -- %s for %s' % (route_stop,stops[route_stop])

# we can pickle this! 
pickle.dump(routes,open("pickles/routes.pickle","wb"))
pickle.dump(stops,open("pickles/stops.pickle","wb"))
pickle.dump(trips,open("pickles/trips.pickle","wb"))
pickle.dump(trip2route,open("pickles/trip2route.pickle","wb"))
pickle.dump(route_stops,open("pickles/route_stops.pickle","wb"))
pickle.dump(distances,open("pickles/distances.pickle","wb"))



