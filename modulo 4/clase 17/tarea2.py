 #Segunda asignación 

 #Correr este código (se trata de un módulo(http) que se importa para crear un servidor local mostrando algo visualmente estético, totalmente con Python, para verlo deben primero correr el programa y luego en su navegador ir a este enlace http://localhost:8000/


from http.server import BaseHTTPRequestHandler, HTTPServer
from http.cookies import SimpleCookie

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configurar las cookies
        cookie = SimpleCookie(self.headers.get('Cookie'))
        username = cookie.get('username')

        if username:
            greeting = f"¡Hola, {username.value}!"
        else:
            greeting = "¡Bienvenidos, estudiantes del curso IPC! No les parece esto interesante?"

        # Enviar encabezados HTTP
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Set-Cookie", "username=EstudianteIPC; path=/")
        self.end_headers()

        # HTML mejorado con CSS
        html = f"""
        <html>
        <head>
            <title>Bienvenida al Curso IPC</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                .container {{
                    text-align: center;
                    background-color: #fff;
                    padding: 50px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    font-size: 2.5em;
                    color: #4CAF50;
                    margin-bottom: 20px;
                }}
                p {{
                    font-size: 1.2em;
                    color: #555;
                }}
                a {{
                    text-decoration: none;
                    color: #4CAF50;
                    font-weight: bold;
                }}
                a:hover {{
                    color: #333;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{greeting}</h1>
                <p>Es fascinante aprender como funciona un servidor HTTP en Python</p>
                <p>Este servidor esta funcionando en el puerto 8000 y es parte del curso IPC.</p>
                <p>Haga clic <a href="/">aqui</a> para recargar la pagina y explorar mas.</p>
            </div>
        </body>
        </html>
        """
        # Enviar el contenido HTML
        self.wfile.write(html.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando el servidor en el puerto {port}...")
    httpd.serve_forever()

if __name__ == "_main_":
    run()