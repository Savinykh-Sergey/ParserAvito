class ProxyManager:
    def __init__(self, list_proxy: list[str], login: str, password: str) -> None:
        self.list_proxy = list_proxy
        self.login = login
        self.password = password

    def change_proxy(self, current_proxy: str) -> dict[str, dict[str, str]]:
        proxy = self.list_proxy[current_proxy]
        self.proxy_options = {
            'proxy' : {
                'https' : f'http://{self.login}:{self.password}@{proxy}'
            }
        }
        return self.proxy_options