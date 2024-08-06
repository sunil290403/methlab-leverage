from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    host = "https://www.methlab.xyz"

    @task
    def leverage_page(self):
        # Define the URL
        url = "/leverage"

        # Perform the GET request using Locust's built-in HTTP client
        self.client.get(url)


if __name__ == "__main__":
    import os

    os.system("locust -f locustfile.py")
