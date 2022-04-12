from main import offers
from . import *


""" Discount class calculates the discount and total price of delivery """


class Discount():

    def get_the_delivery_cost(self, base_delivery_cost, wt, dist):
        return (base_delivery_cost + (wt * 10) + (dist * 5))

    # move it to another class
    def get_discount(self, total_cost, pkg_weight, distance, offer_code):
        # Note:  what if the package is valid for the 2 offers  - we'll just apply the max offer
        # currently assuming the offers are in descending order

        for ofr in offers:
            if ofr[OFFER_CODE] == offer_code:
                log_details(self.__class__.__name__, "get_discount",
                            OFFER_CODE_MATCHED_MESSAGE)
                if ofr[VALID_DISTANCE][MIN] <= distance and ofr[VALID_DISTANCE][MAX] >= distance\
                        and ofr[VALID_WEIGHT][MIN] <= pkg_weight and ofr[VALID_WEIGHT][MAX] >= pkg_weight:
                    log_details(self.__class__.__name__, "get_discount",
                                OFFER_VALID_MESSAGE)
                    discount_percent = ofr[DISCOUNT_IN_PERCENTAGE]
                    discounted_cost = (total_cost * discount_percent / 100)
                    return discounted_cost
        log_details(self.__class__.__name__, "get_discount",
                    INVALID_OFFER_MESSAGE)
        return 0
