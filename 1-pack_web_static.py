#!/usr/bin/python3
""" A Fabric script that generates a .tgz archive
from the contents of the web_static folder """

from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """ Function to generate archive of web_static """

    try:
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        if not isdir('versions'):
            local('mkdir versions')
        name_of_archive = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static/".format(name_of_archive))
        return name_of_archive
    except Exception:
        return None
