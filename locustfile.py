from locust import HttpUser, task, between
class ApiLoader(HttpUser):
    @task
    def noop(self):
        self.client.get("/noop")

    # @task
    # def cpu(self):
    #     self.client.get("/cpu/1")

    # @task
    # def acpu(self):
    #     self.client.get("/acpu/1")

    # @task
    # def wait(self):
    #     self.client.get("/wait/1")

    # @task
    # def await(self):
    #     self.client.get("/await/1")

    # @task
    # def cpu(self):
    #     self.client.get("/mem/10/1")
