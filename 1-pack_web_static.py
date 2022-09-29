#!/usr/bin/python3
""" A Fabric script that generates a .tgz archive
from the contents of the web_static folder """

from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """ Function to generate archive of web_static """

    local('mkdir -p versions/')
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    name_of_archive = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static/".format(name_of_archive))
    if isdir(name_of_archive) is False:
        return None
    return name_of_archive
