# Задание по программированию: Клиент для отправки метрик
import socket
import time


class ClientError(Exception):
    """Special Client Error Exception"""

    pass


class Client:
    """
    Class for create new client and initialization connection with server

    ...

    Methods
    -------
    put(metric, value, timestamp)
        Send value and timestamp of the metric into the server
    get(metric)
        Recieve value and timestamp of the metric from the server
    close()
        Close connection with the server
    """

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError("Create connection error: ", err)

    def put(self, metric, value, timestamp=int(time.time())):
        """Send value and timestamp of the metric into the server"""
        try:
            self.connection.sendall(
                f"put {metric} {value} {timestamp}\n".encode("utf8")
            )
            data = self.connection.recv(1024).decode("utf8")
        except socket.error as err:
            raise ClientError("Send data error: ", err)

        if data == "error\nwrong command\n\n":
            raise ClientError(data)

    def get(self, metric):
        """Recieve value and timestamp of the metric from the server"""
        try:
            self.connection.sendall(f"get {metric}\n".encode("utf8"))
            data = self.connection.recv(1024).decode("utf8")
        except socket.error as err:
            raise ClientError("Get data error: ", err)
        status, data = data.split("\n", 1)
        if status == "error":
            raise ClientError(data)
        get_data = {}
        for row in data.split("\n")[:-2]:
            key, value, timestamp = row.split()
            if key not in get_data:
                get_data[key] = []
            get_data[key].append((int(timestamp), float(value)))
        return get_data

    def close(self):
        """Close connection with the server"""
        try:
            self.connection.close()
        except socket.error as err:
            raise ClientError("Close connection error", err)


if __name__ == "__main__":
    client = Client("127.0.0.1", 10001, timeout=15)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)
    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)
    print(client.get("*"))
    print(client.get("palm.cpu"))