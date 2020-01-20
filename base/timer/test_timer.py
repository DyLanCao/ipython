
from timer import Timer
import logging
import time

def main():
    """Print the latest tutorial from Real Python"""
    t = Timer()
    t.start()
    logging.debug("test")
    time.sleep(2)
    t.stop()


if __name__ == "__main__":
    main()
