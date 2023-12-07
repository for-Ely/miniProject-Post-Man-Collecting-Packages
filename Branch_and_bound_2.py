from random import choice
from time import time

#   get data
from Get_data import getData
Data = getData("1000_20.txt")
N = Data[0]
K = Data[1]
Distance_matrix = Data[2]                # distain matrix
Routes = [[0] for _ in range(K)]         # route for K postman
Available = [x for x in range(1, N+1)]  # index of points, when a point is chosed, pop it out
max_len = 0
length = [0 for _ in range(K)]
#   code
'''
def length(route):
    length = 0
    if len(route) == 1:
        return length
    for i in range(len(route)-1):
        length += Distance_matrix[route[i]][route[i+1]]
    return length
'''
def PCP():
    global max_len
    while Available:
        point, position, route_belong, diff = find_min_increase_routes()
        Routes[route_belong].insert(position, point)
        Available.remove(point)
        length[route_belong] += Distance_matrix[Routes[route_belong][position-1]][point]
        print(len(Available))
        if diff > 0:
            max_len = max_len + diff        
def find_min_increase_routes():
    diff = 1e10
    global max_len
    for i in range(len(Routes)):
        point, position = find_min_increase_route(Routes[i], i)
        expected_len = length_after_insert(i, position, point)
        dif = expected_len - max_len
        if dif == diff:
            next_step.append([point, position, i, diff])
        if dif < diff:
            diff = dif
            next_step = []
            next_step.append([point, position,  i, diff])
    return choice(next_step)
# Given a Route and Available points, return a Point and its Position to insert to Route so that the increase Length is smallest
def find_min_increase_route(route, number_of_route):
    lowest_increase = 1e10
    position = int
    for i in range(1, len(route)+1):
        point = min(Available, key=lambda x:length_after_insert(number_of_route, i, x)-length[number_of_route])
        increase = length_after_insert(number_of_route, i, point)-length[number_of_route]
        if increase < lowest_increase:
            lowest_increase = increase
            position = i
    return point, position
def length_after_insert(number_of_route, position, point):
    if len(Routes[number_of_route]) == position:
        return length[number_of_route] + Distance_matrix[Routes[number_of_route][position-1]][point]
    else:
        result = length[number_of_route] - Distance_matrix[Routes[number_of_route][position-1]][Routes[number_of_route][position]] + Distance_matrix[Routes[number_of_route][position-1]][point] + Distance_matrix[point][Routes[number_of_route][position]]
    return result
    
#   run
if __name__ == '__main__':
    print('____________________________________________________')
    time_begin = time()
    PCP()
    print(K)
    for route in Routes:
        print(len(route))
        print(*route)
    print(min(length))
    time_end = time()
    print(time_end-time_begin)
    