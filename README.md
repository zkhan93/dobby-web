# dobby-web
web interface for Dobby

#### Gunicorn deamon
*location*: /etc/systemd/system/dobby-web.service
```
[Unit]
Description=Unicorn Daemon for Dobby
After=network.target

[Service]
User=pi
Group=www-data
WorkingDirectory=/home/pi/dobby-web
ExecStart=/home/pi/dobby-web/venv/bin/gunicorn --workers 2 --bind unix:/home/pi/dobby-web/web.sock run:app

ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID


[Install]
WantedBy=multi-user.target
```
#### Nginx config
location: /etc/nginx/sites-enabled/dobby.conf
```
server { 
        listen 8080;

        # path for static files
	root /home/pi/dobby-web/app/static;

	location / {
		try_files $uri /html/$uri.html /404;
	}

	location = / {
		index /html/index.html;
	}

        location /api { 
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto $scheme;
	        proxy_set_header Host $http_host;
	        # we don't want nginx trying to do something clever with
		# redirects, we set the Host: header above already.
	        proxy_redirect off;
	        # include proxy_params; original parameters
                proxy_pass http://unix:/home/pi/dobby-web/web.sock;
        }

	error_page 500 502 503 504 /500;
	error_page 404 /404;
}
```

#### Worker deamon service
*location*: /etc/systemd/system/dobby-worker.service
```
[Unit]
Description=Worker Daemon for Dobby
After=dobby-web.service

[Service]
User=pi
Group=www-data
WorkingDirectory=/home/pi/dobby-web
ExecStart=/home/pi/dobby-web/venv/bin/python worker.py
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID

[Install]
WantedBy=multi-user.target
```
