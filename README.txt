Cheeserater
-----------

:Author: Jacob Kaplan-Moss

The is the source code to cheeserater.com, a demo site used in my Django
tutorials. You can read `the tutorial online`__, and the latest
source can always be found `in a GitHub repository`__

__ http://toys.jacobian.org/presentations/2008/oscon/tutorial/
__ http://github.com/jacobian/cheeserater/tree

The code is released under a BSD license which basically means you can do
whatever you want with it. The media, however, is *NOT* open source, and may not
be used without permission.

Usage
-----

To get this up and running, you'll need:

    * A recent trunk checkout of Django -- revision 7000+. 
    
    * `django-voting`__ SVN revision 61 or later.
    
    * `docutils__ 0.4 or later.`
    
__ http://code.google.com/p/django-voting/
__ http://docutils.sourceforge.net/

Then you'll want to create a settings.py file in this directory containing::

    from settings_template import *
    
    # Override any settings you like here.
    
Bugs/additions
--------------

Please feel free to send pull requests, or patches to <jacob@jacobian.org>