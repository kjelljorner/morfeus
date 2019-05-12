"""Data dictionaries. Data taken from the Mendeleev package.

Attributes:
    atomic_symbols (dict): Dictionary of atomic symbols.
    atomic_numbers (dict): Dictionary of atomic numbers.
    bondi_radii (dict): Dictionary of Bondi vdW radii.
    crc_radii (dict): Dictionary of CRC vdW radii.
    jmol_colors (dict): Dictionary of jmol colors.
"""

atomic_symbols = {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N',
8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P',
16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca', 21: 'Sc', 22: 'Ti', 23: 'V',
24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn', 31: 'Ga',
32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr', 37: 'Rb', 38: 'Sr', 39: 'Y',
40: 'Zr', 41: 'Nb', 42: 'Mo', 43: 'Tc', 44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag',
48: 'Cd', 49: 'In', 50: 'Sn', 51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe', 55: 'Cs',
56: 'Ba', 57: 'La', 58: 'Ce', 59: 'Pr', 60: 'Nd', 61: 'Pm', 62: 'Sm', 63: 'Eu',
64: 'Gd', 65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70: 'Yb', 71: 'Lu',
72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir', 78: 'Pt', 79: 'Au',
80: 'Hg', 81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At', 86: 'Rn', 87: 'Fr',
88: 'Ra', 89: 'Ac', 90: 'Th', 91: 'Pa', 92: 'U', 93: 'Np', 94: 'Pu', 95: 'Am',
96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es', 100: 'Fm', 101: 'Md', 102: 'No',
103: 'Lr', 104: 'Rf', 105: 'Db', 106: 'Sg', 107: 'Bh', 108: 'Hs', 109:
'Mt', 110: 'Ds', 111: 'Rg', 112: 'Cn', 113: 'Nh', 114: 'Fl', 115: 'Mc',
116: 'Lv', 117: 'Ts', 118: 'Og'}
"""dict: Atomic numbers as keys and symbols as values."""

atomic_numbers = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7,
'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15,
'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20, 'Sc': 21, 'Ti': 22,'V': 23,
'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27, 'Ni': 28, 'Cu': 29, 'Zn': 30, 'Ga': 31,
'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35, 'Kr': 36, 'Rb': 37, 'Sr': 38, 'Y': 39,
'Zr': 40, 'Nb': 41, 'Mo': 42, 'Tc': 43, 'Ru': 44, 'Rh': 45, 'Pd': 46, 'Ag': 47,
'Cd': 48, 'In': 49, 'Sn': 50, 'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54, 'Cs': 55,
'Ba': 56, 'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60, 'Pm': 61, 'Sm': 62, 'Eu': 63,
'Gd': 64, 'Tb': 65, 'Dy': 66, 'Ho': 67, 'Er': 68, 'Tm': 69, 'Yb': 70, 'Lu': 71,
'Hf': 72, 'Ta': 73, 'W': 74, 'Re': 75, 'Os': 76, 'Ir': 77, 'Pt': 78, 'Au': 79,
'Hg': 80, 'Tl': 81, 'Pb': 82, 'Bi': 83, 'Po': 84, 'At': 85, 'Rn': 86, 'Fr': 87,
'Ra': 88, 'Ac': 89, 'Th': 90, 'Pa': 91, 'U': 92, 'Np': 93, 'Pu': 94, 'Am': 95,
'Cm': 96, 'Bk': 97, 'Cf': 98, 'Es': 99, 'Fm': 100, 'Md': 101, 'No': 102,
'Lr': 103, 'Rf': 104, 'Db': 105, 'Sg': 106, 'Bh': 107, 'Hs': 108, 'Mt': 109,
'Ds': 110, 'Rg': 111, 'Cn': 112, 'Nh': 113, 'Fl': 114, 'Mc': 115, 'Lv': 116,
'Ts': 117, 'Og': 118}
"""dict: Atomic symbols as keys and numbers as values."""

# William M Haynes. CRC Handbook of Chemistry and Physics. 100 Key Points. 
# CRC Press, London, 95th edition, 2014. ISBN 9781482208689. 
crc_radii = {1: 1.1, 2: 1.4, 3: 1.82, 4: 1.53, 5: 1.92, 6: 1.7, 7: 1.55,
8: 1.52, 9: 1.47, 10: 1.54, 11: 2.27, 12: 1.73, 13: 1.84, 14: 2.1, 15: 1.8,
16: 1.8, 17: 1.75, 18: 1.88, 19: 2.75, 20: 2.31, 21: 2.15, 22: 2.11, 23: 2.07,
24: 2.06, 25: 2.05, 26: 2.04, 27: 2.0, 28: 1.97, 29: 1.96, 30: 2.01, 31: 1.87,
32: 2.11, 33: 1.85, 34: 1.9, 35: 1.85, 36: 2.02, 37: 3.03, 38: 2.49, 39: 2.32,
40: 2.23, 41: 2.18, 42: 2.17, 43: 2.16, 44: 2.13, 45: 2.1, 46: 2.1, 47: 2.11,
48: 2.18, 49: 1.93, 50: 2.17, 51: 2.06, 52: 2.06, 53: 1.98, 54: 2.16, 55: 3.43,
56: 2.68, 57: 2.43, 58: 2.42, 59: 2.4, 60: 2.39, 61: 2.38, 62: 2.36, 63: 2.35,
64: 2.34, 65: 2.33, 66: 2.31, 67: 2.3, 68: 2.29, 69: 2.27, 70: 2.26, 71: 2.24,
72: 2.23, 73: 2.22, 74: 2.18, 75: 2.16, 76: 2.16, 77: 2.13, 78: 2.13, 79: 2.14,
80: 2.23, 81: 1.96, 82: 2.02, 83: 2.07, 84: 1.97, 85: 2.02, 86: 2.2, 87: 3.48,
88: 2.83, 89: 2.47, 90: 2.45, 91: 2.43, 92: 2.41, 93: 2.39, 94: 2.43, 95: 2.44,
96: 2.45, 97: 2.44, 98: 2.45, 99: 2.45, 100: 2.45, 101: 2.46, 102: 2.46,
103: 2.46}
"""dict: Atomic numbers as keys and CRC vdW radii as values."""


# A Bondi. van der Waals Volumes and Radii. The Journal of Physical Chemistry,
# 68(3):441–451, 1964. URL: http://pubs.acs.org/doi/abs/10.1021/j100785a001,
# doi:10.1021/j100785a001.
bondi_radii = {1: 1.2, 2: 1.4, 3: 1.81, 6: 1.7, 7: 1.55, 8: 1.52, 9: 1.47,
10: 1.54, 11: 2.27, 12: 1.73, 14: 2.1, 15: 1.8, 16: 1.8, 17: 1.75, 18: 1.88,
19: 2.75, 31: 1.87, 33: 1.85, 34: 1.9, 35: 1.83, 36: 2.02, 49: 1.93, 50: 2.17,
52: 2.06, 53: 1.98, 54: 2.16, 81: 1.96, 82: 2.02}
"""dict: Atomic numbers as keys and Bondi vdW radii as values."""

jmol_colors = {1: '#ffffff', 2: '#ffc0cb', 3: '#b22222', 4: '#ff1493',
5: '#00ff00', 6: '#c8c8c8', 7: '#8f8fff', 8: '#f00000', 9: '#daa520',
10: '#ff1493', 11: '#0000ff', 12: '#228b22', 13: '#808090', 14: '#daa520',
15: '#ffa500', 16: '#ffc832', 17: '#00ff00', 18: '#ff1493', 19: '#ff1493',
20: '#808090', 21: '#ff1493', 22: '#808090', 23: '#ff1493', 24: '#808090',
25: '#808090', 26: '#ffa500', 27: '#ff1493', 28: '#a52a2a', 29: '#a52a2a',
30: '#a52a2a', 31: '#ff1493', 32: '#ff1493', 33: '#ff1493', 34: '#ff1493',
35: '#a52a2a', 36: '#ff1493', 37: '#ff1493', 38: '#ff1493', 39: '#ff1493',
40: '#ff1493', 41: '#ff1493', 42: '#ff1493', 43: '#ff1493', 44: '#ff1493',
45: '#ff1493', 46: '#ff1493', 47: '#808090', 48: '#ff1493', 49: '#ff1493',
50: '#ff1493', 51: '#ff1493', 52: '#ff1493', 53: '#a020f0', 54: '#ff1493',
55: '#ff1493', 56: '#ffa500', 57: '#ff1493', 58: '#ff1493', 59: '#ff1493',
60: '#ff1493', 61: '#ff1493', 62: '#ff1493', 63: '#ff1493', 64: '#ff1493',
65: '#ff1493', 66: '#ff1493', 67: '#ff1493', 68: '#ff1493', 69: '#ff1493',
70: '#ff1493', 71: '#ff1493', 72: '#ff1493', 73: '#ff1493', 74: '#ff1493',
75: '#ff1493', 76: '#ff1493', 77: '#ff1493', 78: '#ff1493', 79: '#daa520',
80: '#ff1493', 81: '#ff1493', 82: '#ff1493', 83: '#ff1493', 84: '#ff1493',
85: '#ff1493', 86: '#ffffff', 87: '#ffffff', 88: '#ffffff', 89: '#ffffff',
90: '#ff1493', 91: '#ffffff', 92: '#ff1493', 93: '#ffffff', 94: '#ffffff',
95: '#ffffff', 96: '#ffffff', 97: '#ffffff', 98: '#ffffff', 99: '#ffffff',
100: '#ffffff', 101: '#ffffff', 102: '#ffffff', 103: '#ffffff', 104: None,
105: None, 106: None, 107: None, 108: None, 109: None, 110: None, 111: None,
112: None, 113: None, 114: None, 115: None, 116: None, 117: None, 118: None}
"""dict: Atomic numbers as keys and jmol hexadecimal colors as values."""