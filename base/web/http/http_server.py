#服务端代码示例
import socket

sock = socket.socket()

sock.bind(("127.0.0.1",9000))

sock.listen(5)

while True:
    conn,addr = sock.accept()

    data=conn.recv(1024)
    print(data.decode("utf8"))
    with open("server_test1.html",encoding="utf8") as f:
        data=f.read()
        conn.send(b"HTTP/1.1 201 OK\r\n\r\n %s" %data.encode("utf8"))

    conn.close()
