# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start

# Add a custom HTTP header with Puppet

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update'
}

exec {'upgrade':
  provider  => shell,
  command   => 'sudo apt-get -y upgrade'
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx'
}

exec {'create dirs':
  provider  => shell,
  command   => sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
}

exec {'write':
  provider    => shell,
  command     => 'echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html'
}

exec {'create soft link':
  provider  => shell,
  command   => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current'
}

exec {'change ownership':
  provider  => shell,
  command   => 'sudo chown -hR ubuntu:ubuntu /data/'
}

exec {'config':
  provider  => shell,
  command   => 'sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default'
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
