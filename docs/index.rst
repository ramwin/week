.. week documentation master file, created by
   sphinx-quickstart on Sun Nov 22 10:48:01 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to week's documentation!
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Installation
============
- install by pip::

    pip install week


Quick Start
===========

- code exapmle::

    import datetime
    from week import Week
    Week.thisweek() == Week.create_from_date(datetime.date.today())
    week = Week.create_from_date(datetime.date(2017, 5, 22)
    week.startdate  # datetime.date(2017, 5, 22)
    week.+1 == week.get_next_week()


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


API Reference
=============

.. autoclass:: week.week.Week

    .. automethod:: create_from_date
    .. autoattribute:: startdate
