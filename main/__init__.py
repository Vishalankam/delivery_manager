from main.utils.logger import log_details, log_exception
from main.utils.constants import *


offers = [
    {'offer_code': 'OFR001',
     'valid_distance': {'min': 0, 'max': 200},
     'valid_weight': {'min': 70, 'max': 200},
     'discount_in_percentage': 10
     },
    {'offer_code': 'OFR002',
     'valid_distance': {'min': 50, 'max': 150},
     'valid_weight': {'min': 100, 'max': 250},
     'discount_in_percentage': 7

     },
    {'offer_code': 'OFR003',
     'valid_distance': {'min': 50, 'max': 250},
     'valid_weight': {'min': 10, 'max': 150},
     'discount_in_percentage': 5
     },
]

KEY_FOR_SORTING_ETA = 'pkg_weight'
