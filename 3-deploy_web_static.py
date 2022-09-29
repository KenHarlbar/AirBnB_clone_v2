#!/usr/bin/python3
""" Full deployment """

from fabric.api import local, run, put, env
from datetime import datetime
from os.path import isdir, exists

env.hosts = ['3.239.59.25', '3.235.170.47']


def do_pack():
    """ Function to generate archive of web_static """

    local('mkdir -p versions/')
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    name_of_archive = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static/".format(name_of_archive))
    if isdir(name_of_archive) is False:
        return None
    return name_of_archive


def do_deploy(archive_path):
    """ Function to distribute an archive to web servers """

    if not exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """ function to create and distribute an archive to your web servers """

    if not do_pack():
        return False

    return do_deploy('versions/web_static_20220929202050.tgz')
