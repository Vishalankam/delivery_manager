from . import *

"""Eta class calculates the estimated time arrival for the package"""


class Eta():

    def __init__(self, pkg_details, no_of_vehicles,
                 wt_limit, speed_of_vehicle) -> None:
        self.pkg_details = pkg_details
        self.no_of_vehicles = no_of_vehicles
        self.wt_limit = wt_limit
        self.speed_of_vehicle = speed_of_vehicle

        super().__init__()

    def get_sort_key(self, obj):
        return obj[KEY_FOR_SORTING_ETA]

    def calculate_eta_of_vehicle_and_pkg(self, pkg_count, vehicle_away_for, eta_of_vehicle):
        self.pkg_details[pkg_count][ETA_OF_PKG] = float("{:.2}".format(
            self.pkg_details[pkg_count][DISTANCE] / self.speed_of_vehicle))
        self.pkg_details[pkg_count][ETA_OF_PKG] = self.pkg_details[pkg_count][ETA_OF_PKG] + \
            vehicle_away_for[0]
        eta_of_vehicle = eta_of_vehicle + \
            self.pkg_details[pkg_count][ETA_OF_PKG]
        return eta_of_vehicle

    def get_eta_for_pkg(self):
        # sort it based on the weight, so that we can load as many packages as possible
        # if the single pkg weight exceeds the vehicle limit then throw an error

        self.pkg_details.sort(key=self.get_sort_key)
        pkg_remained = self.pkg_details.__len__()
        pkg_count = 0
        available_vehicles = self.no_of_vehicles
        vehicle_away_for = []
        while(pkg_count < pkg_remained):
            if available_vehicles:
                vehicle_away_for.append(0)
                available_vehicles = available_vehicles-1

            vehicle_away_for.sort()
            weights = 0
            no_of_pkg_to_load = 0
            eta_of_vehicle = 0

            while (weights <= self.wt_limit):
                if self.pkg_details[pkg_count][PKG_WEIGHT] > self.wt_limit:
                    log_details(self.__class__.__name__, "get_eta_for_pkg", WEIGHT_EXCEEDED_ERROR.format(
                        self.pkg_details[pkg_count][PKG_ID]))
                    self.pkg_details[pkg_count][ERROR] = WEIGHT_EXCEEDED_ERROR.format(
                        self.pkg_details[pkg_count][PKG_ID])
                    pkg_count = pkg_count+1
                    if not pkg_count < pkg_remained:
                        break

                temp = weights + self.pkg_details[pkg_count][PKG_WEIGHT]

                if temp < self.wt_limit:
                    # can load more pkgs
                    weights = temp
                    no_of_pkg_to_load = no_of_pkg_to_load + 1
                    eta_of_vehicle = self.calculate_eta_of_vehicle_and_pkg(
                        pkg_count, vehicle_away_for, eta_of_vehicle)
                    pkg_count = pkg_count+1
                    if not pkg_count < pkg_remained:
                        break
                else:
                    # cant carry any more pkg
                    vehicle_away_for[0] = vehicle_away_for[0] + eta_of_vehicle
                    break

            log_details(self.__class__.__name__, "get_eta_for_pkg",
                        VEHICLE_LOADING_MESSAGE.format(no_of_pkg_to_load))

        return self.pkg_details
