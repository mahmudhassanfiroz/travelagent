
from TravelAgent import TravelAgent

def main():
    # print("Main Function is executing")
    travel_agent = TravelAgent("Go Jaan")
    trip_info1 = travel_agent.set_trip_one_city_one_way('DAC', 'PRA', '05-07-2023')
    # print('aircraft', trip_info1[0])
    # print('price', trip_info1[1])
    # print('Aircraft', trip_info1.aricraft)
    # print('Price', trip_info1.price)

    trip_cities = ['DUB', 'LHR', 'SYD', 'JFK']
    trip_info2 = travel_agent.set_trip_multi_city_flexible_route(trip_cities, '05-11-2023')

    print('Price', trip_info2[1])
    for trip in trip_info2[0]:
        print(trip)

if __name__ == '__main__':
    main()

