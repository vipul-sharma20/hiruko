Hiruko
======

Getting inside Python's GIL(Global Interpreter Lock) and Analyzing how it works with threads.

*Note: Work in [Progress](https://trello.com/b/oM4fkHZD/hiruko) (It will take time; I am not good in C :|)*

The Code
--------
***NOTE: Below is what I've done for Python 2.7.14. Will be checking out code for Python 3.6 soon***

* I've included the patch file to log GIL ticks and threads executed
* Or, you can check out my fork of CPython at [hiruko-2.7](https://github.com/vipul-sharma20/cpython/tree/hiruko-2.7) which includes the logging code.

### Questions ###

* How the number of cores affects thread execution and GIL?
* How the number of threads affects their execution and GIL?
* And more ...

(feel free to create a new issue if you have any suggestions)

Credits
-------

Almost entirely adapted from this awesome [talk](https://www.youtube.com/watch?v=Obt-vMVdM8s) by [David Beazley](http://www.dabeaz.com/) and his blog [here](http://www.dabeaz.com/GIL/)

The Name
--------

see: [Hiruko](http://naruto.wikia.com/wiki/Hiruko)

