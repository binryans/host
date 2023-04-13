from flask import Flask, request, jsonify

import socket

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hostname and IP address</title>
        </head>
        <body>
            <h1>Thông tin máy tính</h1>
            <p>Tên máy tính: <span id="hostname"></span></p>
            <p>Địa chỉ IP: <span id="ip"></span></p>

            <script>
                fetch('/info')
                    .then(response => response.json())
                    .then(data => {
                        document.querySelector('#hostname').textContent = data.hostname;
                        document.querySelector('#ip').textContent = data.ip_address;
                    })
                    .catch(error => console.error(error));
            </script>
        </body>
        </html>
    '''

@app.route('/info')
def info():
    # lấy thông tin tên máy tính và địa chỉ IP của máy đang truy cập
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # trả về dữ liệu dưới dạng JSON
    return jsonify({'hostname': hostname, 'ip_address': ip_address})

if __name__ == '__main__':
    app.run(debug=True)
