# coding:utf8
import os,bottle
from bottle import route, run, default_app, error, template, view
from bottle import install 
from bottle_sqlite import SQLitePlugin
from bottle import static_file

install(SQLitePlugin(dbfile='/home/pluto/xiangti/products.db'))


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/home/pluto/xiangti/bootstrap')

@route('/')
@view('content')
def main(main='main'):
    return dict(main=main)

@route('/contact')
def contact():
    return template('contact')

@route('/about')
def contact():
    return template('about')


@route('/links')
def contact():
    return template('links')



@route('/products/:name')
def products(db,name):
    row = db.execute('select name from items ').fetchone()
    return template('product_template', name=row['name'])

@route('/products')
def products(db):
    result = db.execute('select * from baojia ').fetchall()
    return template('products_template', rows=result)
    #result = db.execute('select * from items ').fetchall()
    #return template('products_template', rows=result)


@error(404)
def error404(error):
    return template('error')

class StripPathMiddleware(object):
  def __init__(self, app):
    self.app = app
  def __call__(self, e, h):
    e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
    return self.app(e,h)

if __name__ == "__main__":
    # Interactive mode
    run(app=myapp)
    
else:
    # Mod WSGI launch
    bottle.debug(True)
    os.chdir(os.path.dirname(__file__))
    application = StripPathMiddleware(default_app())

