from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            width: 60%;
            border-collapse: collapse;
            margin: 20px auto;
            border: 2px solid black;
        }
        th, td {
            border: 2px solid black;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
            font-size: 18px;
        }
        td {
            font-size: 16px;
        }
        h1 {
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>TCP/IP Protocol Suite</h1>
    <table>
        <tr>
            <th>Layer</th>
            <th>Protocols</th>
        </tr>
        <tr><td>Application Layer</td><td>HTTP, FTP, SMTP, DNS, DHCP,Telnet</td></tr>
        <tr><td>Transport Layer</td><td>TCP, UDP</td></tr>
        <tr><td>Internet Layer</td><td>IP, ICMP, ARP</td></tr>
        <tr><td>Network Access Layer</td><td>Ethernet, Wi-Fi, PPP</td></tr>
    </table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',80)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()