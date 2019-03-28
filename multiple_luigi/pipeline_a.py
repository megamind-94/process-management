import luigi
import crash_on_ipy

class Task(luigi.Task):

    i = luigi.Parameter()

    def run(self):
        print("A-Workflow", "task", str(self.i))
        import os
        os.system("echo 'A' >> testA%s.txt" % (str(self.i)))

    def output(self):
        return luigi.LocalTarget("testA%s.txt" % (str(self.i)))

class AWorkflow(luigi.Task):

    a = luigi.Parameter()

    def requires(self):
        print("running TaskA inside")
        return [Task(i=_) for _ in range(int(self.a))]

    def output(self):
        return self.input()