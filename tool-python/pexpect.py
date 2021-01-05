import os
import pexpect
import sys

print('hello world')

child = pexpect.spawn('ssh vim@180.201.3.195')
child.logfile = sys.stdout

child.expect('password:')
child.sendline('vim617')
child.expect('vim.*')
child.sendline('ls')

os.system('pause')