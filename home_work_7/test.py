import numpy as np
x = np.random.random((3,3,3))
print(x)
max_value = np.max(x)
min_value = np.min(x)
print('Maximum value of the array is',max_value)
print('Minimum value of the array is',min_value)


# [[[0.81468145 0.37517593 0.50456283]
#   [0.69463295 0.48124015 0.36945437]
#   [0.13646352 0.44760012 0.44313328]]

#  [[0.07739667 0.08836558 0.03966288]
#   [0.42655978 0.24402248 0.37042451]
#   [0.3158586  0.90819089 0.49439457]]

#  [[0.84866459 0.9284673  0.01227487]
#   [0.89057536 0.99190277 0.8695499 ]
#   [0.04518396 0.07873806 0.24564836]]]
# Maximum value of the array is 0.991902770544191
# Minimum value of the array is 0.012274866099942439


import numpy as np
x = np.random.rand(10, 4)
print("Original array: ")
print(x)
y= x[:5, :]
print("First 5 rows of the above array:")
print(y)


# Original array: 
# [[0.04401333 0.1278477  0.21889103 0.2756473 ]
#  [0.26273021 0.88747458 0.25400447 0.14257475]
#  [0.5157038  0.54082752 0.27046972 0.00106136]
#  [0.94987131 0.49931738 0.22073419 0.14876764]
#  [0.96105102 0.53179543 0.75797325 0.37238553]
#  [0.37327006 0.98997703 0.16076955 0.99259885]
#  [0.50532729 0.54556727 0.22667865 0.35690387]
#  [0.15559189 0.86231399 0.23432696 0.48430405]
#  [0.42285281 0.04273016 0.17011897 0.77312481]
#  [0.51524748 0.94087598 0.91206426 0.83397634]]
# First 5 rows of the above array:
# [[0.04401333 0.1278477  0.21889103 0.2756473 ]
#  [0.26273021 0.88747458 0.25400447 0.14257475]
#  [0.5157038  0.54082752 0.27046972 0.00106136]
#  [0.94987131 0.49931738 0.22073419 0.14876764]
#  [0.96105102 0.53179543 0.75797325 0.37238553]]

# ===========================
import pandas as pd
# Read and display the CSV with Pandas
woldcountries_df = pd.read_csv("WorldCountries.csv")
woldcountries_df.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 227 entries, 0 to 226
# Data columns (total 20 columns):
# Country                               227 non-null object
# Region                                227 non-null object
# Population                            227 non-null int64
# Area (sq. mi.)                        227 non-null int64
# Pop. Density (per sq. mi.)            227 non-null object
# Coastline (coast/area ratio)          227 non-null object
# Net migration                         224 non-null object
# Infant mortality (per 1000 births)    224 non-null object
# GDP ($ per capita)                    226 non-null float64
# Literacy (%)                          209 non-null object
# Phones (per 1000)                     223 non-null object
# Arable (%)                            225 non-null object
# Crops (%)                             225 non-null object
# Other (%)                             225 non-null object
# Climate                               205 non-null object
# Birthrate                             224 non-null object
# Deathrate                             223 non-null object
# Agriculture                           212 non-null object
# Industry                              211 non-null object
# Service                               212 non-null object
# dtypes: float64(1), int64(2), object(17)
# memory usage: 35.6+ KB

woldcountries_df.head()
# Country	Region	Population	Area (sq. mi.)	Pop. Density (per sq. mi.)	Coastline (coast/area ratio)	Net migration	Infant mortality (per 1000 births)	GDP ($ per capita)	Literacy (%)	Phones (per 1000)	Arable (%)	Crops (%)	Other (%)	Climate	Birthrate	Deathrate	Agriculture	Industry	Service
# 0	Afghanistan	ASIA (EX. NEAR EAST)	31056997	647500	48,0	0,00	23,06	163,07	700.0	36,0	3,2	12,13	0,22	87,65	1	46,6	20,34	0,38	0,24	0,38
# 1	Albania	EASTERN EUROPE	3581655	28748	124,6	1,26	-4,93	21,52	4500.0	86,5	71,2	21,09	4,42	74,49	3	15,11	5,22	0,232	0,188	0,579
# 2	Algeria	NORTHERN AFRICA	32930091	2381740	13,8	0,04	-0,39	31	6000.0	70,0	78,1	3,22	0,25	96,53	1	17,14	4,61	0,101	0,6	0,298
# 3	American Samoa	OCEANIA	57794	199	290,4	58,29	-20,71	9,27	8000.0	97,0	259,5	10	15	75	2	22,46	3,27	NaN	NaN	NaN
# 4	Andorra	WESTERN EUROPE	71201	468	152,1	0,00	6,6	4,05	19000.0	100,0	497,2	2,22	0	97,78	3	8,71	6,25	NaN	NaN	NaN
woldcountries_df.describe() 
# Population	Area (sq. mi.)	GDP ($ per capita)
# count	2.270000e+02	2.270000e+02	226.000000
# mean	2.874028e+07	5.982270e+05	9689.823009
# std	1.178913e+08	1.790282e+06	10049.138513
# min	7.026000e+03	2.000000e+00	500.000000
# 25%	4.376240e+05	4.647500e+03	1900.000000
# 50%	4.786994e+06	8.660000e+04	5550.000000
# 75%	1.749777e+07	4.418110e+05	15700.000000
# max	1.313974e+09	1.707520e+07	55100.000000