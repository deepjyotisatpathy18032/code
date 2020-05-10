{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import matplotlib.pyplot as plt\
import numpy as np\
\
\
c= 3*10**8\
\
time, redshift1, redshift2 = np.loadtxt('Binary_data 2.csv', delimiter = ',', unpack = True)\
\
\
plt.figure(figsize=(15,3))\
plt.plot(time,c*redshift1, 'b')\
plt.plot(time,c*redshift2, 'r')\
plt.xlabel('Time(y)')\
plt.ylabel('radial velocity') # Normalized Strain is not strain\
plt.grid()\
plt.show()}