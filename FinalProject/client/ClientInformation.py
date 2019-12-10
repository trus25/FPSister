class ClientInformation(object):
    def __init__(self):
        self.name = "Your name"
        self.role = ""
        self.address = "127.0.0.1"

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role

    def get_address(self):
        return self.address

    def set_name(self, name: str):
        self.name = name

    def set_role(self, role: str):
        self.role = role

    def set_address(self, address: str):
        self.address = address