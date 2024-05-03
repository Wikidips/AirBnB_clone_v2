#!/usr/bin/python3
"""Generate a .tgz archive from the contents of the web_static directory."""
import os
from datetime import datetime
from fabric.api import local

def do_pack():
    """Create a tar gzipped archive of the web_static directory."""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(now)

    if not os.path.isdir("versions"):
        os.mkdir("versions")

    command = "tar -cvzf {} web_static".format(archive_path)
    if local(command).failed:
        return None
    return archive_path
