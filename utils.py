# utils.py
import logging
from termcolor import colored
#from pprint import pp
import pprint

logger = logging.getLogger(__name__)

def handle_error(e, func, message, errors, key):
    logger.error(f"{func} {message}")
    logger.error(f"{func} Error message: {str(e)}")
    logger.debug(f"{func} Error type: {type(e)}")
    errors[key] = str(e) # Store the error message in the dictionary

def output_errors(errors, calling_func=None):
        if len(errors) == 0:
            print(f"[main-{calling_func}]: complete")
            print(colored("ERRORS:", "green"))
            print("None")
            return
        print(f"[main-{calling_func}]: complete - errors reported")
        print(colored("ERRORS:", "red"))
        pprint.pprint(errors)
    
def output_output(output):
    if len(output) == 0:
        print(colored("OUTPUT:", "blue"))
        print("None")
        return
    print(colored("OUTPUT:", "blue"))
    pprint.pprint(output)

