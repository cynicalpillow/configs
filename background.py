import signal
import time
from subprocess import call
import fcntl

pid_file = 'program.pid'
fp = open(pid_file, 'w')
try:
    fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOError:
    # another instance is running
    sys.exit(1)

stopped = False

def stop(sig, frame):
    global stopped
    stopped = True

signal.signal(signal.SIGTERM, stop)

while not stopped:
    call(["wal", "-i", "/home/rui/Pictures/Backgrounds/", "-q"])
    time.sleep(600)