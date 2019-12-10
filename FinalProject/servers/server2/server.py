from FinalProject.servers.grid import Grid
import Pyro4


def start_server(host_address):
    # name server harus di start dulu dengan  pyro4-ns -n localhost -p 7777
    # untuk mengecek service apa yang ada di ns, gunakan pyro4-nsc -n localhost -p 7777 list

    daemon = Pyro4.Daemon(host=host_address)
    name_server = Pyro4.locateNS(host_address, 7777)
    server = Pyro4.expose(Grid)
    server_uri = daemon.register(server)
    print("server URI: ", server_uri)
    name_server.register("game_server", server_uri)
    daemon.requestLoop()


if __name__ == "__main__":
    input_ip = input(">> Input server's IP address(or just enter if testing on local): ")

    if input_ip == "":
        address = "localhost"
    else:
        address = input_ip

    start_server(address)
