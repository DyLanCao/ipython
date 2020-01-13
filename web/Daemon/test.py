import os
import sys
import time

from daemon import Daemon

class MyTestDaemon(Daemon):
    def run(self):
        sys.stdout.write('Daemon started with pid {}\n'.format(os.getpid()))
        while True:
            sys.stdout.write('Daemon Alive! {}\n'.format(time.ctime()))
            sys.stdout.flush()

            time.sleep(5)

if __name__ == '__main__':
    PIDFILE = 'python input.py'
    LOG = '/tmp/daemon-example.log'
    daemon = MyTestDaemon(pidfile=PIDFILE, stdout=LOG, stderr=LOG)

    if len(sys.argv) != 2:
        print('Usage: {} [start|stop]'.format(sys.argv[0]), file=sys.stderr)
        raise SystemExit(1)

    if 'start' == sys.argv[1]:
        daemon.start()
    elif 'stop' == sys.argv[1]:
        daemon.stop()
    elif 'restart' == sys.argv[1]:
        daemon.restart()
    else:
        print('Unknown command {!r}'.format(sys.argv[1]), file=sys.stderr)
        raise SystemExit(1)
