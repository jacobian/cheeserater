Cheeserater
-----------

:Author: Jacob Kaplan-Moss

The is the source code to cheeserater.com, a demo site used in my Django
tutorials. The latest version of this tutorial can be found at
http://toys.jacobian.org/presentations/2008/pycon/tutorial/, and the latest
source can always be found in a Mercurial repository at
http://toys.jacobian.org/hg/cheeserater.

The code is released under a BSD license which basically means you can do
whatever you want with it. The media, however, is *NOT* open source, and may not
be used without permission.

To get this up and running, you'll need a recent trunk checkout of Django --
revision 7000+. You'll also need to install docutils (http://docutils.sf.net/).
Then you'll want to create a settings.py file in this directory containing::

    from settings_template import *
    
    # Override any settings you like here.
    
Good luck!