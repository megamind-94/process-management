import subprocess
import os
class luigidServ():

    pid = ''

    def start(self):
        print("启动luigid...")
        os.system("luigid")

    def isActive(self):
        self.pid = subprocess.getoutput("pgrep luigid")
        if self.pid == '':
            return False
        else:
            return True

    def close(self):
        if self.isActive():
            subprocess.getoutput('kill {pid}'.format(pid=self.pid))
        print("关闭luigid...")