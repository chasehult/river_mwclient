from .auth_credentials import AuthCredentials
from .site import Site


class SessionManager(object):
    """Manages instances of WikiClient
    """
    existing_wikis = {}
    
    def get_client(self, url: str = None, path: str = None, credentials: AuthCredentials = None, **kwargs):
        if url in self.existing_wikis:
            return self.existing_wikis[url]['client']
        client = Site(url, path=path, **kwargs)
        if credentials:
            client.login(username=credentials.username, password=credentials.password)
        self.existing_wikis[url] = {'client': client}
        return client


session_manager = SessionManager()
