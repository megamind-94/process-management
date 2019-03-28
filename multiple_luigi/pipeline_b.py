import luigi


class Task(luigi.Task):
    i = luigi.Parameter()

    def run(self):
        print("B-Workflow", "task", str(self.i))
        import os
        os.system("echo 'B' >> testB%s.txt" % (str(self.i)))

    def output(self):
        return luigi.LocalTarget("testB%s.txt" % (str(self.i)))


class BWorkflow(luigi.Task):
    b = luigi.Parameter()

    def requires(self):
        print("running TaskA inside")
        return Task(self.b)

    def output(self):
        return self.input()