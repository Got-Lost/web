def app(environ, start_response):
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    print(body)
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(body*100)))
    ]
    start_response(status, response_headers)
    return body