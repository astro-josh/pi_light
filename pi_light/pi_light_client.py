import yaml


def get_known_servers_list(path: str):
    with open(path, "r") as server_list_file:
        g = yaml.load(server_list_file)
        print(g)


if __name__ == '__main__':
    get_known_servers_list("servers.yaml")