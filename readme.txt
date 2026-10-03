========================================================================
         HIGH-PRESSURE VESSEL DESIGN & STRESS ANALYSIS (MECH-001)
========================================================================

STATUS: Completed
CAD: Onshape
PYTHON: Analytical Sizing Script
LICENSE: MIT License

Parametric ASME-compliant CAD model and analytical Python sizing tool 
for aerospace and energy engineering.

------------------------------------------------------------------------
1. PROJECT OVERVIEW
------------------------------------------------------------------------
This package contains the complete design for a carbon steel high-pressure 
vessel featuring hemispherical heads and an integrated top nozzle port. 
The project bridges the gap between 3D parametric modeling and analytical 
stress fundamentals, validating the CAD geometry against thin/thick-wall 
pressure vessel mechanics.

------------------------------------------------------------------------
2. TECHNICAL SPECIFICATIONS
------------------------------------------------------------------------
- Drawing ID        : MECH-001 (Rev 1.0) | Sheet 1 of 1
- Material          : Carbon Steel (Standard structural grade)
- Total Mass        : 72.738 kg (CAD calculated volume)
- Outer Diameter    : 300.0 mm (Cylindrical shell section)
- Cylinder Height   : 500.0 mm (Straight shell body)
- Head Geometry     : Hemispherical (R = 150.0 mm)
- Nozzle Dimensions : 76.2 mm OD / 50.2 mm ID (13.0 mm flange offset)

------------------------------------------------------------------------
3. ENGINEERING & ANALYTICAL BASIS
------------------------------------------------------------------------
The geometry is analytically validated against internal design pressure (P) 
using standard structural mechanics equations.

A. Circumferential (Hoop) Stress:
This is the primary constraint for the cylindrical body's wall thickness.
Formula: Hoop Stress = (P * r) / t

B. Longitudinal (Axial) Stress:
Formula: Axial Stress = (P * r) / (2 * t)

C. Hemispherical Head Stress:
Because the membrane stress on a hemisphere is uniform, the heads require 
less thickness for equivalent pressure containment, optimizing the overall 
72.74 kg mass.
Formula: Head Stress = (P * r) / (2 * t)
