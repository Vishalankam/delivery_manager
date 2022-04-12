from . import offers
from main.utils.helper import input_pkg_details, input_delivery_info, input_vehicle_details
from . import *
from main.Discount import Discount
from main.Eta import Eta

""" Delivery """


class Delivery():

    def pkg_delivery(self):

        base_delivery_cost, no_of_pkgs = input_delivery_info()
        dis = Discount()
        delivery_cost_details = []

        for i in range(no_of_pkgs):
            log_details(self.__class__.__name__, "pkg_delivery",
                        ENTER_THE_PKG_DETAILS_MESSAGE.format(i+1))
            pkg_id, pkg_weight, distance, offer_code = input_pkg_details()
            total_cost = dis.get_the_delivery_cost(
                base_delivery_cost, pkg_weight, distance)

            discount = dis.get_discount(
                total_cost, pkg_weight, distance, offer_code)

            delivery_cost_details.append({PKG_ID: pkg_id, PKG_WEIGHT: pkg_weight,
                                         DISTANCE: distance, DISCOUNT: discount, TOTAL_COST: total_cost-discount})

        no_of_vehicles, wt_limit, speed_of_vehicle = input_vehicle_details()
        eta = Eta(delivery_cost_details, no_of_vehicles,
                  wt_limit, speed_of_vehicle)
        output_pkg_details = eta.get_eta_for_pkg()

        log_details(self.__class__.__name__,
                    "pkg_delivery", output_pkg_details)
        return delivery_cost_details
