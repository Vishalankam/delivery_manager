from main.utils.logger import log_exception, log_details


def input_pkg_details():

    try:

        pkg_id = input("Enter the package_id: ")
        pkg_weight = int(input("Enter the package weight: "))
        distance = int(input("Enter the delivery distance: "))
        offer_code = input("Enter the offer_code: ")
        return pkg_id, pkg_weight, distance, offer_code

    except Exception as e:
        log_exception("helpers", "input_pkg_details",
                      "EXCEPTION: {}".format(e))


def input_vehicle_details():
    try:
        no_of_vehicles = int(
            input("Enter the number of vehicles available for the delivery: "))
        if not no_of_vehicles:
            log_details("Eta", "get_eta_for_pkg",
                        "Can't deliver with no vehicles..!")
        wt_limit = int(
            input("Enter the weight limit that can be carried out a vehicle: "))
        speed_of_vehicle = int(input("Enter the speed of the vehicle: "))
        return no_of_vehicles, wt_limit, speed_of_vehicle

    except Exception as e:
        log_exception("helpers", "input_vehicle_details",
                      "EXCEPTION: {}".format(e))


def input_delivery_info():
    try:
        base_delivery_cost = int(input("Please enter Base delivery cost: "))
        no_of_pkgs = int(input("Please enter number of packages: "))
        return base_delivery_cost, no_of_pkgs

    except Exception as e:
        log_exception("helpers", "input_delivery_info",
                      "EXCEPTION: {}".format(e))
