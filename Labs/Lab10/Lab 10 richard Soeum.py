import docker

client = docker.from_env()



def show_container_ip(container_name):#from previos code
    container = client.containers.get(container_name)
    networks = container.attrs['NetworkSettings']['Networks']
    
    for net_name, net_data in networks.items():
        print(f"{container_name} in network '{net_name}' has IP: {net_data['IPAddress']}")


#show_container_ip("nginx")
show_container_ip("mysql")
show_container_ip("adminer")






import docker
import time

client = docker.from_env()
containers= client.containers.list(all=True)
container_start_time = {container:time.time() for container in containers}

def relaunchcontainer():
    while True:
        for container_name in containers:
            container = client.containers.get(container_name.name)
            if container.status != 'running':
                print(f"restarting {container_name}")
                container.start()


def maintenance():
