from bottle.bottle import route, static_file
import os

root_path = os.path.abspath("static")

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=root_path)

