# latest_tutorials.py
import threading
from timer import Timer
from reader import feed

def main():
    """Print the 10 latest tutorials from Real Python"""
    t = Timer("download", logger=None)
    for tutorial_num in range(10):
        t.start()
        tutorial = feed.get_article(tutorial_num)
        t.stop()
        print(tutorial)

    download_time = Timer.timers["download"]
    print(f"Downloaded 10 tutorials in {download_time:0.2f} seconds")

if __name__ == "__main__":
    main()
