fitCurves
=========

Python implementation of Philip J. Schneider's "Algorithm for Automatically Fitting Digitized Curves" from the book "Graphics Gems"

Fit one or more cubic Bezier curves to a polyline.

This is a python implementation of Philip J. Schneider's C code. The original C code is available on http://graphicsgems.org/ as well as in https://github.com/erich666/GraphicsGems


Installation
------------

The package should run on python 2 & 3.

To install, run:
```
python setup.py install
```

Numpy is required and will be automatically installed.


Usage
-----

A small demo app is provided using Tkinter. It can be run like this:

```
python -m fitcurves
```

Left click to add points. Right click to remove points. The optimal spline will
be computed on the fly and displayed as with the control points.

![demo](https://github.com/volkerp/fitCurves/raw/master/demo_screenshot.png "demo.py")


Changelog
---------

- (2019) Packaging improvements by Spencer Bliven (https://github.com/sbliven/fitCurves)

- (2014) Port to python by Volker Poplawski (https://github.com/volkerp/fitCurves)

- (1990) Initial C code by Philip Schneider (http://graphicsgems.org/)