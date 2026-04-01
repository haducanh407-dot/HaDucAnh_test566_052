import socket

def handle_request(client_socket, request_data):
    # Kiểm tra đường dẫn yêu cầu
    if "GET /admin" in request_data:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nWelcome to the admin page!"
    else:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, this is a simple web server!"
    
    # Gửi phản hồi về client
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def main():
    # Khởi tạo socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Gán địa chỉ IP và cổng (port)
    server_socket.bind(('127.0.0.1', 8080))
    # Bắt đầu lắng nghe kết nối (tối đa 5 kết nối trong hàng đợi)
    server_socket.listen(5)

    print("Server đang lắng nghe tại cổng 8080...")

    while True:
        # Chấp nhận kết nối từ client
        client_socket, client_address = server_socket.accept()
        print(f"Kết nối từ {client_address}")
        
        # Nhận dữ liệu từ client
        request_data = client_socket.recv(1024).decode('utf-8')
        
        # Xử lý yêu cầu và gửi phản hồi
        handle_request(client_socket, request_data)

if __name__ == '__main__':
    main()