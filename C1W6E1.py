# Задание по программированию: Сервер для приема метрик
import asyncio


class ClientServerProtocol(asyncio.Protocol):
    """Asynchronous client server protocol"""

    def connection_made(self, transport):
        """Create connection"""
        self.transport = transport
        self.storage = {}

    def data_received(self, data):
        """Called when server recieved data from client"""
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        """Parse and processing data from client. Return response according to protocol"""
        resp = ""
        try:
            data = data.split("\n")
            if len(data) == 2:
                data = data[0].split(" ")
                if data[0] == "put":
                    if data[1] not in self.storage:
                        self.storage[data[1]] = []
                    self.storage[data[1]].append((float(data[2]), int(data[3])))
                    resp = "ok\n\n"
                elif data[0] == "get":
                    if data[1] == "*":
                        resp = f"ok\n{self.storage_print(self.storage)}\n"
                    elif data[1] not in self.storage:
                        resp = "ok\n\n"
                    else:
                        resp = f"ok\n{self.key_print(self.storage, data[1])}\n"
        except:
            resp = "error\nwrong command\n\n"
        return resp

    def key_print(self, storage, key):
        """Prepare values of metric from storage for sending to the client"""
        s = ""
        for n in storage[key]:
            s += key + " " + " ".join(map(str, n)) + "\n"
        return s

    def storage_print(self, storage):
        """Prepare values of all metrics from storage for sending to the client"""
        s = ""
        for key in storage:
            s += self.key_print(storage, key)
        return s


def run_server(host, port):
    """Run server for storage metrics"""
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    run_server("127.0.0.1", 8888)
