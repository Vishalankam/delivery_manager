from main.Discount import Discount
from main.utils.logger import log_details, log_exception

def run():
    try:
        dis = Discount()
        output_pkg_details = dis.pkg_delivery()
        log_details("", "run", output_pkg_details)
    except Exception as e:
        log_exception("", "run", "Exception: {}".format(e))
run()