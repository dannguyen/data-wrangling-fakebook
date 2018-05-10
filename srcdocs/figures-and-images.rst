******************
Figures and Images
******************

http://www.sphinx-doc.org/en/stable/rest.html#images

Images
======

Standard embed
--------------

.. code-block:: rst

    .. image:: files/images/nyc-midtown.jpg

.. image:: files/images/nyc-midtown.jpg


Changing attributes
-------------------

Adds a class of ``align-center``

.. image:: files/images/nyc-midtown.jpg
    :align: center
    :alt: Alternative text


Figures
=======


Like an image, but with a caption:

.. code-block:: rst

    .. figure:: files/images/nyc-midtown.jpg

        This is a caption. Which can `include HTML <https://unsplash.com/@dancow>`_

.. figure:: files/images/nyc-midtown.jpg

    This is a caption. Which can `include HTML <https://unsplash.com/@dancow>`_
