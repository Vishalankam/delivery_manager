from main.models.Delivery import Delivery
from main.utils.logger import log_details, log_exception
from main.models.Eta import Eta


def run():
    try:
        delivery = Delivery()
        output = delivery.pkg_delivery()
    except Exception as e:
        log_exception("", "run", "EXCEPTION :{}".format(e))


run()
