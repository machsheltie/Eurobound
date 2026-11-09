"""Mural sheet constants (facade metres, Blender frame); shared by e5_mural.py (plain Python) and e5_build.py."""
SHEET_X0, SHEET_X1, SHEET_Z0, SHEET_Z1 = -4.9, 3.0, 2.4, 12.4
PPM = 4096 / (SHEET_Z1 - SHEET_Z0)
# peel-zones mask extent (whole frontage)
ZONE_X0, ZONE_X1, ZONE_Z0, ZONE_Z1 = -7.0, 3.4, 0.0, 13.3
