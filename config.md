<uwsgi>
  <limit-as>128</limit-as>
  <processes>4</processes>
  <memory-report/>
  <vhost/>
  <no-site/>
<pythonpath>/usr/local/lib/python2.7/dist-packages</pythonpath>
<pythonpath>/home/pluto/xiangti</pythonpath>
</uwsgi>




    server{
            listen 80;
            server_name xiangti.co www.xiangti.co;
    location / {
                include uwsgi_params;
                uwsgi_pass unix:///tmp/uwsgi.sock;
                uwsgi_param WSGI_PYHOME /home/pluto/xiangti;
                uwsgi_param UWSGI_CHDIR /home/pluto/xiangti;
                uwsgi_param UWSGI_SCRIPT hi;
        }
    }

