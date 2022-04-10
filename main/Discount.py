from main import offers
from main.Eta import Eta
from main.utils.logger import log_details, log_exception

class Discount():  
            
    def get_the_delivery_cost(self, base_delivery_cost, wt, dist): 
        return  base_delivery_cost + (wt * 10) + (dist* 5) 
    
    def get_discount(self, total_cost, pkg_weight, distance, offer_code): 
        #Note:  what if the package is valid for the 2 offers  - we'll just apply the max offer 
        # currently assuming the offers are in descending order
        for i in offers:
            if i['offer_code'] == offer_code:
                log_details("Discount", "get_discount", "Offer_code_matched...!!!!")
                if i['valid_distance']['min'] <= distance and i['valid_distance']['max'] >= distance\
                and i['valid_weight']['min'] <= pkg_weight and i['valid_weight']['max'] >= pkg_weight:
                    log_details("Discount", "get_discount", "Offer valid...!!!!")
                    discount_percent = i['discount_in_percentage']
                    discounted_cost = total_cost - (total_cost * discount_percent / 100)
                    return discounted_cost
        log_details("Discount", "get_discount", "Offer not valid or invalid offer code...!")
        return 0 
        
    def pkg_delivery(self):
        try:
            base_delivery_cost = int(input("Please enter Base delivery cost: "))
            no_of_pkgs = int(input("Please enter number of packages: "))
        except Exception as e:  
            log_exception("Discount", "pkg_delivery", "Error while getting the input",e)

        delivery_cost_details = []

        for i in range(no_of_pkgs):
            log_details("Discount", "pkg_delivery","Enter the package {} details :".format(i+1))
            pkg_id = input("Enter the package_id: ")
            
            pkg_weight =  int(input("Enter the package weight: "))
            distance =  int(input("Enter the delivery distance: "))
            offer_code = input("Enter the offer_code: ")
            
            total_cost = self.get_the_delivery_cost(base_delivery_cost, pkg_weight, distance)
            discount = self.get_discount(total_cost, pkg_weight, distance, offer_code)
            delivery_cost_details.append({'pkg_id': pkg_id, 'pkg_weight': pkg_weight, 'distance': distance, 'discount': discount, 'total_cost': total_cost-discount})
        
        eta = Eta(delivery_cost_details)
        output_pkg_details = eta.get_eta_for_pkg()
        return output_pkg_details