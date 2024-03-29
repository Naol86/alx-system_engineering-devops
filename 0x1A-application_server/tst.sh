# server {
#         listen 80 default_server;
#         listen [::]:80 default_server;
#         root /var/www/html;
#         index index.html index.htm index.nginx-debian.html;
#         server_name _;
#         add_header X-Served-By $hostname;
#         location / {
#                 try_files $uri $uri/ =404;
#         }
#         if ($request_filename ~ redirect_me){
#                 rewrite ^ https://youtube.com permanent;
#         }
#         error_page 404 /404.html;
#         location = /404.html {
#                 internal;
#         }
# }

server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name 52.91.146.69

    add_header X-Served-By $hostname;
    
    location = /airbnb/ {
        proxy_pass http://127.0.0.1:5000/airbnb/;
    }

    error_page 404 /404.html;

    location /404.html {
        root /var/www/html;
        internal;
    }
}
