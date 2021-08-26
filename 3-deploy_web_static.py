#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
import os.path
from fabric.api import put, run, env
from datetime import datetime
from fabric.api import local

env.hosts = ['35.196.239.113', '3.94.160.0']

def do_pack():
    """Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "versions/web_static_{}.tgz".format(date)
        if not os.path.exists("versions"):
            local("mkdir versions")
        local("tar -cvzf {} web_static".format(file))
        return file
    except:
        return None

def do_deploy(archive_path):
    """
    Deply funtion that Deploy archive!
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        file_old = archive_path.split("/")[-1]
        file_new = file_old.split(".")
        put(archive_path, "/tmp/".format(file_old))
        run('mkdir -p /data/web_static/releases/{}/'.format(file_new[0]))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file_old, file_new[0]))
        run('rm /tmp/{}'.format(file_old))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(file_new[0], file_new[0]))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_new[0]))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
             .format(file_new[0]))
        return True
    except:
        return False

def deploy():
    """ Fabric script (based on the file 2-do_deploy_web_static.py)
    that creates and distributes an archive to your web servers,
    using the function deploy:
    """
    file = do_pack()
    if os.path.isfile(file) is False:
        return False
    do_deploy(file)
    return file
