from main import KEY_FOR_SORTING_ETA
from main.utils.logger import log_details, log_exception

class Eta():
    
    def __init__(self, pkg_details) -> None:
        self.pkg_details = pkg_details
        super().__init__()
    
    
    def get_sort_key(self, obj):
      return obj[KEY_FOR_SORTING_ETA]
            
    def get_eta_for_pkg(self):
        # sort it based on the weight, so that we can load as many packages as possible 
        # if the single pkg weight exceeds the vehicle limit then throw an error 
        
        # self.pkg_details  = [{'pkg_id': 'pk1', 'pkg_weight': 50,'distance': 30, 'discount': 0, 'total_cost': 1000},
        #                 {'pkg_id': 'pk2', 'pkg_weight': 75,'distance': 125, 'discount': 0, 'total_cost': 1000},
        #                 {'pkg_id': 'pk3', 'pkg_weight': 175,'distance': 100, 'discount': 0, 'total_cost': 1000},
        #                 {'pkg_id': 'pk4', 'pkg_weight': 155,'distance': 95, 'discount': 0, 'total_cost': 1000},
        #                  {'pkg_id': 'pk5', 'pkg_weight': 110,'distance': 60, 'discount': 0, 'total_cost': 1000}]
        self.pkg_details.sort(key=self.get_sort_key)
        try:
            no_of_vehicles = int(input("Enter the number of vehicles available for the delivery: "))
            if not no_of_vehicles:
                log_details("Eta", "get_eta_for_pkg", "Can't deliver with no vehicles..!")
                
            wt_limit = int(input("Enter the weight limit that can be carried out a vehicle: "))
            speed_of_vehicle  = int(input("Enter the speed of the vehicle: "))
        except Exception as e:
            raise  Exception({error_code: "Error while taking the input", message: "".format(e)})
        
        pkg_remained = self.pkg_details.__len__()
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
                if self.pkg_details[i]['pkg_weight'] > wt_limit:
                    log_details("Eta", "get_eta_for_pkg", "Error Weight Exceeded, can't deliver this package {}".format(self.pkg_details[i]['pkg_id']))
                    self.pkg_details[i]['error'] = "Weight Exceeded, can't deliver package"
                    i = i+1    
                    if not i < pkg_remained:
                        break
                    
                temp = weights + self.pkg_details[i]['pkg_weight']
                
                if temp < wt_limit:
                    weights = temp
                    no_of_pkg_to_load = no_of_pkg_to_load + 1
                    self.pkg_details[i]['eta_of_pkg'] = float("{:.2}".format(self.pkg_details[i]['distance'] / speed_of_vehicle))
                    self.pkg_details[i]['eta_of_pkg'] = self.pkg_details[i]['eta_of_pkg'] + vehicle_away_for[0]
                    eta_of_vehicle = eta_of_vehicle + self.pkg_details[i]['eta_of_pkg']
                    i = i+1    
                    if not i < pkg_remained:
                        break
                else: 
                    vehicle_away_for[0] = vehicle_away_for[0] + eta_of_vehicle 
                    break
                
            log_details("Eta", "get_eta_for_pkg", "vehicle is carring no_of_pkgs {}".format(no_of_pkg_to_load))
                    
        return self.pkg_details 