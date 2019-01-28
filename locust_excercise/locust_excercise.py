from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/gk/controller/AuthenticationServlet",
                         {"gkl": "test",
                        "gkp": "test1",
                        "gkafep": "/pl/home.html?isError=true&gkep=/content/interactive/ilottery/services/session.login.json",
                        "gkep": "/content/interactive/ilottery/services/session.login.json",
                        "gkse": "/pl/home.html?gkse=true",
                        "gkaid": "test",
                        "gkflag": "1",
                        "gksi": "1",
                        "gkst": "gk_GMSDefaultService"
                          })

    @task()
    def home(self):
        self.client.get("/pl/home.html")

    @task()
    def dict(self):
        self.client.get("/libs/cq/i18n/dict.pl.json")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "https://gry.lotto.pl"
    min_wait = 5000
    max_wait = 15000
