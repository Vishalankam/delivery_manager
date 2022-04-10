

offers = [
    {'offer_code': 'OFR001', 
     'valid_distance': {'min': 0, 'max': 200}, 
     'valid_weight':{'min':70, 'max':200} ,
     'discount_in_percentage': 10
     },
     {'offer_code': 'OFR002', 
     'valid_distance': {'min': 50, 'max': 150}, 
     'valid_weight':{'min':100, 'max':250},
     'discount_in_percentage': 7

     },
     {'offer_code': 'OFR003', 
     'valid_distance': {'min': 50, 'max': 250}, 
     'valid_weight':{'min':10, 'max':150} ,
     'discount_in_percentage': 5
     },
]


def get_the_delivery_cost(base_delivery_cost, wt, dist):
    
   cost  =  base_delivery_cost + (wt * 10) + (dist* 5) 
   return cost


def get_discount(total_cost, pkg_weight, distance, offer_code): 
    #Note:  what if the package is valid for the 2 offers  - we'll just apply the max offer 
    # currently assuming the offers are in descending order
    for i in offers:
        if i['offer_code'] == offer_code:
            print("Offer_code_matched...!!!!")
            if i['valid_distance']['min'] <= distance and i['valid_distance']['max'] >= distance\
            and i['valid_weight']['min'] <= pkg_weight and i['valid_weight']['max'] >= pkg_weight:
                print("Offer valid...!!!!")
                discount_percent = i['discount_in_percentage']
                discounted_cost = total_cost - (total_cost * discount_percent / 100)
                return discounted_cost
   
    print("Offer not valid or invalid offer code...!")
    return 0 

def get_sort_key(obj):
  return obj['pkg_weight']
            
def get_eta_for_pkg(pkg_details):
    # sort it based on the weight, so that we can load as many packages as possible 
    # if the single pkg weight exceeds the vehicle limit then throw an error 
    # pkg_details  = [{'pkg_id': 'pk1', 'pkg_weight': 50,'distance': 30, 'discount': 0, 'total_cost': 1000},
    #                 {'pkg_id': 'pk2', 'pkg_weight': 75,'distance': 125, 'discount': 0, 'total_cost': 1000},
    #                 {'pkg_id': 'pk3', 'pkg_weight': 175,'distance': 100, 'discount': 0, 'total_cost': 1000},
    #                 {'pkg_id': 'pk4', 'pkg_weight': 155,'distance': 95, 'discount': 0, 'total_cost': 1000},
    #                  {'pkg_id': 'pk5', 'pkg_weight': 110,'distance': 60, 'discount': 0, 'total_cost': 1000}]
    pkg_details.sort(key=get_sort_key)
    no_of_vehicles = int(input("Enter the number of vehicles available for the delivery: "))
    if not no_of_vehicles:
        print("Can't deliver with no vehicles..!")
        
    wt_limit = int(input("Enter the weight limit that can be carried out a vehicle: "))
    speed_of_vehicle  = int(input("Enter the speed of the vehicle: "))
    
    pkg_remained = pkg_details.__len__()
    i = 0
    available_vehicles = no_of_vehicles
    vehicle_away_for = []
    while(i < pkg_remained):
        if available_vehicles:
            vehicle_away_for.append(0)
            available_vehicles = available_vehicles-1
               
        vehicle_away_for.sort()
        weights = 0
        no_of_pkg_to_load = 0
        eta_of_vehicle = 0
        
        while (weights <= wt_limit):            
            if pkg_details[i]['pkg_weight'] > wt_limit:
                print("Error Weight Exceeded, can't deliver this package {}".format(pkg_details[i]['pkg_id']))
            
            temp = weights + pkg_details[i]['pkg_weight']
            
            if temp < wt_limit:
                weights = temp
                no_of_pkg_to_load = no_of_pkg_to_load + 1
                pkg_details[i]['eta_of_pkg'] = float("{:.2}".format(pkg_details[i]['distance'] / speed_of_vehicle))
                pkg_details[i]['eta_of_pkg'] = pkg_details[i]['eta_of_pkg'] + vehicle_away_for[0]
                eta_of_vehicle = eta_of_vehicle + pkg_details[i]['eta_of_pkg']
                i = i+1    
                if not i < pkg_remained:
                    break
            else: 
                vehicle_away_for[0] = vehicle_away_for[0] + eta_of_vehicle 
                break
            
        print("vehicle is carring no_of_pkgs {}".format(no_of_pkg_to_load))
                
    return  pkg_details 
        
def pkg_delivery():
    try:
        base_delivery_cost = int(input("Please enter Base delivery cost: "))
        no_of_pkgs = int(input("Please enter number of packages: "))
    except Exception as e:  
        print("Error while getting the input",e)
    
    delivery_cost_details = []
    
    for i in range(no_of_pkgs):
        print("Enter the package {} details :".format(i+1))
        pkg_id = input("Enter the package_id: ")
        pkg_weight =  int(input("Enter the package weight: "))
        distance =  int(input("Enter the delivery distance: "))
        offer_code = input("Enter the offer_code: ")
        total_cost = get_the_delivery_cost(base_delivery_cost, pkg_weight, distance)
        print("🚀 ~ file: app.py ~ line 60 ~ total_cost", total_cost)
        discount = get_discount(total_cost, pkg_weight, distance, offer_code)
        print("🚀 ~ file: app.py ~ line 62 ~ discount", discount)
        delivery_cost_details.append({'pkg_id': pkg_id, 'pkg_weight': pkg_weight,'distance': distance, 'discount': discount, 'total_cost': total_cost-discount})
    
    eta = get_eta_for_pkg(delivery_cost_details)
    return delivery_cost_details
   
        
print(pkg_delivery()[0]['pkg_id'])
# eta = get_eta_for_pkg()
# print(eta)
