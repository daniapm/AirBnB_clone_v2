#!/usr/bin/python3
"""Fabfile to generates a .tgz archive from the contents of web_static.
"""
import os.path
from fabric.api import put, run, env

env.hosts = ['35.196.239.113', '3.94.160.0']

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
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(file_old, file_new[0]))
        run('rm /tmp/{}'.format(file_old))
        run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(file_new[0], file_new[0]))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(file_new[0]))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(file_new[0]))
        return True
    except:
        return False
