from http.server import HTTPServer,BaseHTTPRequestHandler

class MyServerHandeler(BaseHTTPRequestHandler):

    def  do_GET(self):
        path=self.path

        if path=="/":
            type='text/html'
            f=open('D://Study//python//HTTPServer//index.html','rb')
        elif path=='/Styles/index.css':
            type= 'text/css'
            f = open('D://Study//python//HTTPServer//Styles//index.css','rb')
        elif '/images' in path:
            type='image/*'
            imgName=str(path).split('/')[2]
            f=open("D://Study//python//HTTPServer//images//"+imgName,'rb')
        elif path =="/scripts/index.js":
            type= "application/javascript"
            f=open('D://Study//python//HTTPServer//scripts//index.js','rb')
        else:
            print("Error")
            f=open("D://Study//python//HTTPServer//error.html",'rb')


       
        self.send_response(200)
        self.send_header( 'Content-type',type)
        self.end_headers()
        self.wfile.write(f.read())

server=HTTPServer(('localhost',8080),MyServerHandeler)
print("server is running")
server.serve_forever()
server.server_close()