import socketserver
import subprocess
import os
import fcntl
import time
import shlex

def recvall(sock):
    buf = b""
    while True:
        temp = sock.recv(1024, os.O_NONBLOCK)
        buf += temp
        if len(temp) < 1024:
            break
    return buf


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        proc = subprocess.Popen(["/bin/bash"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, env={"PATH":""})
        fcntl.fcntl(proc.stdout.fileno(), fcntl.F_SETFL, fcntl.fcntl(proc.stdout.fileno(), fcntl.F_GETFL)|os.O_NONBLOCK)
        while True:
            self.request.send(b">>> ")
            req = self.request.recv(5).decode().strip().replace("'", '')
            cmd = f"eval '{req}'\n"
            proc.stdin.write(cmd.encode())
            proc.stdin.flush()
            time.sleep(0.01)

            buf = proc.stdout.read()
            buf = buf or b""
            self.request.send(buf + b"\n")


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", 1337), TCPHandler) as server:
        server.serve_forever()
