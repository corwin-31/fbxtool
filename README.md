fbxtools
========

Here you'll find some tools built to manage Freebox. They are using fbxapitool package, available here: https://github.com/corwin-31/fbxapitool.git
It was developed with Python 3 with Delta S box, and tested under Linux (Debian & Ubuntu). I think it can be used under macOS, not yet tested on my side. I've no idea of the effort required to used it on Windows 10, and I'll not do it. Last but not least, it'll only work with last version of the API in end of 2020, which mean version 8.

Install
-------

If you have the fbxapitool, just download tools you want. Don't forget to configure parameters to use your freebox, the default may not work... Moreover, you'll to grant rights to the "fbxapitool" using Freebox OS web app.

Available tools
---------------
fbx-cmd.py:	a command line tool to manage your Freebox
fbx-dump.py:	dumps Freebox config using fbx-cmd.py calls to restore

Resources
---------
Freebox OS API documentation : http://dev.freebox.fr/sdk/os/ or http://mafreebox.freebox.fr/doc/index.html#
Freebox API package : https://github.com/corwin-31/fbxapitool.git

