from pipeline_a import AWorkflow as A
from pipeline_b import BWorkflow as B
import luigi

class TaskB(luigi.Task):
    pipeline = None
    b = luigi.Parameter()
    def run(self):
        print("running TaskB outside")
        yield self.pipeline

    def output(self):
        self.pipeline = B(self.b)
        return self.pipeline.output()

class TaskA(luigi.Task):

    pipeline = None
    a = luigi.Parameter()
    b = luigi.Parameter()

    def requires(self):
        return TaskB(self.b)

    def run(self):
        print("running TaskA outside")
        yield self.pipeline

    def output(self):
        self.pipeline = A(self.a)
        return self.pipeline.output()

class workflow(luigi.Task):

    a = luigi.Parameter()
    b = luigi.Parameter()

    def requires(self):
        return TaskA(a=self.a, b=self.b)

    def run(self):
        print("starting...")

if __name__ == "__main__":

    from utils import luigidServ
    serv = luigidServ()

    # serv.start()
    luigi.build([workflow(a=3, b=1)])
    # serv.close()