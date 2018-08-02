import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import path
import seaborn as sns
#csv = path.expanduser(r"C:\Users\Christian\OneDrive\milletdaniel\lemnatec_pixel_list_2.csv")
csv = path.expanduser(r"C:\Users\Christian\OneDrive\milletdaniel\The List with pixel count daniel.csv")
#print(csv)
#print(path.getsize(csv))


df= pd.read_csv(csv)
#correct raw list
#print(len(df))
#print(df.columns)
#df['Name'] = df['Name'].str.slice(0, -17 )
#df['Date'] = df['Name'].str.slice(4, )
#print(df['Name'])
#df['Name'] = df['Name'].str.slice(0, -11 )

#df.sort_values(by=['Date', "Plant"])


#dataframe separating into plants
Am24989 = df[df['Plant'] == 'Am24989']
CM052 = df[df['Plant'] == 'CM052']
CM291 = df[df['Plant'] == 'CM291']
Control = df[df['Plant'] == 'Control']
PI550473 = df[df['Plant'] == 'PI 550473']
PI315699 = df[df['Plant'] == 'PI315699']
PI462738 = df[df['Plant']== 'PI462738']
PI537070 = df[df['Plant'] == 'PI537070']
PI550558 = df[df['Plant'] == 'PI550558']
PI578073 = df[df['Plant'] == 'PI578073']
PI613116 = df[df['Plant'] == 'PI613116']
PI614815 = df[df['Plant'] == 'PI614815']
R286 = df[df['Plant'] == 'R286']
RedDABI = df[df['Plant'] == 'Red DABI']
Tx623b = df[df['Plant'] == 'Tx623b']
Yugu1 = df[df['Plant'] == 'Yugu1']

#data from to np array for scatter plot

Am249891 = np.array(Am24989)
CM0521 = np.array(CM052)
CM2911 = np.array(CM291)
Control1 = np.array(Control)
PI5504731 = np.array(PI550473)
PI3156991 = np.array(PI315699)
PI4627381 = np.array(PI462738)
PI5370701 = np.array(PI537070)
PI5505581 = np.array(PI550558)
PI5780731 = np.array(PI578073)
PI6131161 = np.array(PI613116)
PI6148151 = np.array(PI614815)
R2861 = np.array(R286)
RedDABI1 = np.array(RedDABI)
Tx623b1 = np.array(Tx623b)
Yugu11 = np.array(Yugu1)


#group each plant by date
Am249892=Am24989.groupby('Date', sort=True).agg('median')
CM052=CM052.groupby('Date', sort=True).agg('median')
CM2912=CM291.groupby('Date', sort=True).agg('median')
Control2=Control.groupby('Date', sort=True).agg('median')
PI5504732=PI550473.groupby('Date', sort=True).agg('median')
PI3156992=PI315699.groupby('Date', sort=True).agg('median')
PI4627382=PI462738.groupby('Date', sort=True).agg('median')
PI5370702=PI537070.groupby('Date', sort=True).agg('median')
PI5505582=PI550558.groupby('Date', sort=True).agg('median')
PI5780732=PI578073.groupby('Date', sort=True).agg('median')
PI6131162=PI613116.groupby('Date', sort=True).agg('median')
PI6148152=PI614815.groupby('Date', sort=True).agg('median')
R2862=R286.groupby('Date', sort=True).agg('median')
RedDABI2=RedDABI.groupby('Date', sort=True).agg('median')
Tx623b2=Tx623b.groupby('Date', sort=True).agg('median')
Yugu12=Yugu1.groupby('Date', sort=True).agg('median')


#########################################################################


#assign each plants x and y cordinates for plant height

xAm249892 = Am249892.index.values
yAm249892 = Am249892["Height (mm)"]
xCM052 = CM052.index.values
yCM052 = CM052["Height (mm)"]
xCM2912 = CM2912.index.values
yCM2912 = CM2912["Height (mm)"]
xControl2 = Control2.index.values
yControl2 = Control2["Height (mm)"]
xPI5504732 = PI5504732.index.values
yPI5504732 = PI5504732["Height (mm)"]
xPI3156992 = PI3156992.index.values
yPI3156992 = PI3156992["Height (mm)"]
xPI4627382 = PI4627382.index.values
yPI4627382 = PI4627382["Height (mm)"]
xPI5370702 = PI5370702.index.values
yPI5370702 = PI5370702["Height (mm)"]
xPI5505582 = PI5505582.index.values
yPI5505582 = PI5505582["Height (mm)"]
xPI5780732 = PI5780732.index.values
yPI5780732 = PI5780732["Height (mm)"]
xPI6131162 = PI6131162.index.values
yPI6131162 = PI6131162["Height (mm)"]
xPI6148152 = PI6148152.index.values
yPI6148152 = PI6148152["Height (mm)"]
xR2862 = R2862.index.values
yR2862 = R2862["Height (mm)"]
xRedDABI2 = RedDABI2.index.values
yRedDABI2 = RedDABI2["Height (mm)"]
xTx623b2 = Tx623b2.index.values
yTx623b2 = Tx623b2["Height (mm)"]
xYugu12 = Yugu12.index.values
yYugu12 = Yugu12["Height (mm)"]



#line chart portion

plt.plot(xAm249892, yAm249892, c="#a6cee3", label="_nolegend_")
plt.plot(xCM052, yCM052, c="#1f78b4", label="_nolegend_")
plt.plot(xCM2912, yCM2912, c="#b2df8a", label="_nolegend_")
#plt.plot(xControl2, yControl2, c="#33a02c", label="_nolegend_")
plt.plot(xPI5504732, yPI5504732, c="#fb9a99", label="_nolegend_")
plt.plot(xPI3156992, yPI3156992, c="#e31a1c", label="_nolegend_")
plt.plot(xPI4627382, yPI4627382, c="#fdbf6f", label="_nolegend_")
plt.plot(xPI5370702, yPI5370702, c="#ff7f00", label="_nolegend_")
plt.plot(xPI5505582, yPI5505582, c="#cab2d6", label="_nolegend_")
plt.plot(xPI5780732, yPI5780732, c="#6a3d9a", label="_nolegend_")
plt.plot(xPI6131162, yPI6131162, c="#ffff99", label="_nolegend_")
plt.plot(xPI6148152, yPI6148152, c="#b15928", label="_nolegend_")
plt.plot(xR2862, yR2862, c="black", label="_nolegend_")
plt.plot(xRedDABI2, yRedDABI2, c="brown", label="_nolegend_")
plt.plot(xTx623b2, yTx623b2, c="tan", label="_nolegend_")
plt.plot(xYugu12, yYugu12, c="gray", label="_nolegend_")


# scatter plot portion for plant height

xAm249891=Am249891[:,4]
yAm249891=Am249891[:, 1]
xCM0521=CM0521[:,4]
yCM0521=CM0521[:, 1]
xCM2911=CM2911[:,4]
yCM2911=CM2911[:, 1]
xControl1=Control1[:,4]
yControl1=Control1[:, 1]
xPI5504731=PI5504731[:,4]
yPI5504731=PI5504731[:, 1]
xPI3156991=PI3156991[:,4]
yPI3156991=PI3156991[:, 1]
xPI4627381=PI4627381[:,4]
yPI4627381=PI4627381[:, 1]
xPI5370701=PI5370701[:,4]
yPI5370701=PI5370701[:, 1]
xPI5505581=PI5505581[:,4]
yPI5505581=PI5505581[:, 1]
xPI5780731=PI5780731[:,4]
yPI5780731=PI5780731[:, 1]
xPI6131161=PI6131161[:,4]
yPI6131161=PI6131161[:, 1]
xPI6148151=PI6148151[:,4]
yPI6148151=PI6148151[:, 1]
xR2861=R2861[:,4]
yR2861=R2861[:, 1]
xRedDABI1=RedDABI1[:,4]
yRedDABI1=RedDABI1[:, 1]
xTx623b1=Tx623b1[:,4]
yTx623b1=Tx623b1[:, 1]
xYugu11=Yugu11[:,4]
yYugu11=Yugu11[:, 1]


#scatter plot

plt.scatter(xAm249891, yAm249891, c="#a6cee3", label="Maize Am24989")
plt.scatter(xCM0521, yCM0521, c="#1f78b4", label="Sorghum CM052")
plt.scatter(xCM2911, yCM2911, c="#b2df8a", label="Sorghum CM291")
#plt.scatter(xControl1, yControl1, c="#33a02c", label="Control")
plt.scatter(xPI5504731, yPI5504731, c="#fb9a99", label="MaizeB73 PI550473")
plt.scatter(xPI3156991, yPI3156991, c="#e31a1c", label="Japanese millet PI315699")
plt.scatter(xPI4627381, yPI4627381, c="#fdbf6f", label="Finger millet PI462738")
plt.scatter(xPI5370701, yPI5370701, c="#ff7f00", label="Pearl millet PI537070")
plt.scatter(xPI5505581, yPI5505581, c="#cab2d6", label="Maize PI550558")
plt.scatter(xPI5780731, yPI5780731, c="#6a3d9a", label="Proso millet PI578073")
plt.scatter(xPI6131161, yPI6131161, c="#ffff99", label="Pearl millet PI613116")
plt.scatter(xPI6148151, yPI6148151, c="#b15928", label="Foxtail millet PI614815")
plt.scatter(xR2861, yR2861, c="black", label="tef R286")
plt.scatter(xRedDABI1, yRedDABI1, c="brown", label="tef Red DABI")
plt.scatter(xTx623b1, yTx623b1, c="tan", label="Sorghum Tx623b")
plt.scatter(xYugu11, yYugu11, c="gray", label="Foxtail millet Yugu1")


#plt.scatter(xcmini, ycmini, c="tan", label="Mini Control Median", alpha=0.5, s=30)
#plt.scatter(xcB73, ycB73, c="magenta", label="B73 Control Median", alpha=0.5, s=30)
plt.ylabel("Height (mm)", fontsize=18)
plt.xlabel("Day #", fontsize=18)
plt.title('Height (mm) vs. Date', fontsize=18)
plt.legend(loc=2, prop={'size': 10}, fontsize=18)
#plt.xticks(rotation=75)
plt.xticks(range(0,116, 5), fontsize=18)
plt.yticks(fontsize=18)

plt.show()


#######################################################################



##assign each plants x and y cordinates for pixel count

xAm249892 = Am249892.index.values
yAm249892 = Am249892["Pixel"]
xCM052 = CM052.index.values
yCM052 = CM052["Pixel"]
xCM2912 = CM2912.index.values
yCM2912 = CM2912["Pixel"]
xControl2 = Control2.index.values
yControl2 = Control2["Pixel"]
xPI5504732 = PI5504732.index.values
yPI5504732 = PI5504732["Pixel"]
xPI3156992 = PI3156992.index.values
yPI3156992 = PI3156992["Pixel"]
xPI4627382 = PI4627382.index.values
yPI4627382 = PI4627382["Pixel"]
xPI5370702 = PI5370702.index.values
yPI5370702 = PI5370702["Pixel"]
xPI5505582 = PI5505582.index.values
yPI5505582 = PI5505582["Pixel"]
xPI5780732 = PI5780732.index.values
yPI5780732 = PI5780732["Pixel"]
xPI6131162 = PI6131162.index.values
yPI6131162 = PI6131162["Pixel"]
xPI6148152 = PI6148152.index.values
yPI6148152 = PI6148152["Pixel"]
xR2862 = R2862.index.values
yR2862 = R2862["Pixel"]
xRedDABI2 = RedDABI2.index.values
yRedDABI2 = RedDABI2["Pixel"]
xTx623b2 = Tx623b2.index.values
yTx623b2 = Tx623b2["Pixel"]
xYugu12 = Yugu12.index.values
yYugu12 = Yugu12["Pixel"]


#line chart portion

plt.plot(xAm249892, yAm249892, c="#a6cee3", label="_nolegend_")
plt.plot(xCM052, yCM052, c="#1f78b4", label="_nolegend_")
plt.plot(xCM2912, yCM2912, c="#b2df8a", label="_nolegend_")
#plt.plot(xControl2, yControl2, c="#33a02c", label="_nolegend_")
plt.plot(xPI5504732, yPI5504732, c="#fb9a99", label="_nolegend_")
plt.plot(xPI3156992, yPI3156992, c="#e31a1c", label="_nolegend_")
plt.plot(xPI4627382, yPI4627382, c="#fdbf6f", label="_nolegend_")
plt.plot(xPI5370702, yPI5370702, c="#ff7f00", label="_nolegend_")
plt.plot(xPI5505582, yPI5505582, c="#cab2d6", label="_nolegend_")
plt.plot(xPI5780732, yPI5780732, c="#6a3d9a", label="_nolegend_")
plt.plot(xPI6131162, yPI6131162, c="#ffff99", label="_nolegend_")
plt.plot(xPI6148152, yPI6148152, c="#b15928", label="_nolegend_")
plt.plot(xR2862, yR2862, c="black", label="_nolegend_")
plt.plot(xRedDABI2, yRedDABI2, c="brown", label="_nolegend_")
plt.plot(xTx623b2, yTx623b2, c="tan", label="_nolegend_")
plt.plot(xYugu12, yYugu12, c="gray", label="_nolegend_")


## scatter plot portion for pixel count


xAm249891=Am249891[:,4]
yAm249891=Am249891[:, 6]
xCM0521=CM0521[:,4]
yCM0521=CM0521[:, 6]
xCM2911=CM2911[:,4]
yCM2911=CM2911[:, 6]
xControl1=Control1[:,4]
yControl1=Control1[:, 6]
xPI5504731=PI5504731[:,4]
yPI5504731=PI5504731[:, 6]
xPI3156991=PI3156991[:,4]
yPI3156991=PI3156991[:, 6]
xPI4627381=PI4627381[:,4]
yPI4627381=PI4627381[:, 6]
xPI5370701=PI5370701[:,4]
yPI5370701=PI5370701[:, 6]
xPI5505581=PI5505581[:,4]
yPI5505581=PI5505581[:, 6]
xPI5780731=PI5780731[:,4]
yPI5780731=PI5780731[:, 6]
xPI6131161=PI6131161[:,4]
yPI6131161=PI6131161[:, 6]
xPI6148151=PI6148151[:,4]
yPI6148151=PI6148151[:, 6]
xR2861=R2861[:,4]
yR2861=R2861[:, 6]
xRedDABI1=RedDABI1[:,4]
yRedDABI1=RedDABI1[:, 6]
xTx623b1=Tx623b1[:,4]
yTx623b1=Tx623b1[:, 6]
xYugu11=Yugu11[:,4]
yYugu11=Yugu11[:, 6]


#scatter plot
plt.scatter(xAm249891, yAm249891, c="#a6cee3", label="Maize Am24989")
plt.scatter(xCM0521, yCM0521, c="#1f78b4", label="Sorghum CM052")
plt.scatter(xCM2911, yCM2911, c="#b2df8a", label="Sorghum CM291")
#plt.scatter(xControl1, yControl1, c="#33a02c", label="Control")
plt.scatter(xPI5504731, yPI5504731, c="#fb9a99", label="MaizeB73 PI550473")
plt.scatter(xPI3156991, yPI3156991, c="#e31a1c", label="Japanese millet PI315699")
plt.scatter(xPI4627381, yPI4627381, c="#fdbf6f", label="Finger millet PI462738")
plt.scatter(xPI5370701, yPI5370701, c="#ff7f00", label="Pearl millet PI537070")
plt.scatter(xPI5505581, yPI5505581, c="#cab2d6", label="Maize PI550558")
plt.scatter(xPI5780731, yPI5780731, c="#6a3d9a", label="Proso millet PI578073")
plt.scatter(xPI6131161, yPI6131161, c="#ffff99", label="Pearl millet PI613116")
plt.scatter(xPI6148151, yPI6148151, c="#b15928", label="Foxtail millet PI614815")
plt.scatter(xR2861, yR2861, c="black", label="tef R286")
plt.scatter(xRedDABI1, yRedDABI1, c="brown", label="tef Red DABI")
plt.scatter(xTx623b1, yTx623b1, c="tan", label="Sorghum Tx623b")
plt.scatter(xYugu11, yYugu11, c="gray", label="Foxtail millet Yugu1")


#plt.scatter(xcmini, ycmini, c="tan", label="Mini Control Median", alpha=0.5, s=30)
#plt.scatter(xcB73, ycB73, c="magenta", label="B73 Control Median", alpha=0.5, s=30)
plt.ylabel("Pixel Count", fontsize=18)
plt.xlabel("Day #", fontsize=18)
plt.title('Pixel Count vs. Date', fontsize=18)
plt.legend(loc=2, prop={'size': 10}, fontsize=18)
plt.yticks(fontsize=18)
#plt.xticks(rotation=75)
plt.xticks(range(0,116, 5), fontsize=18)
plt.show()



###################################################################


##assign each plants x and y cordinates for water data

xAm249892 = Am249892.index.values
yAm249892 = Am249892["Water (ml)"]
xCM052 = CM052.index.values
yCM052 = CM052["Water (ml)"]
xCM2912 = CM2912.index.values
yCM2912 = CM2912["Water (ml)"]
xControl2 = Control2.index.values
yControl2 = Control2["Water (ml)"]
xPI5504732 = PI5504732.index.values
yPI5504732 = PI5504732["Water (ml)"]
xPI3156992 = PI3156992.index.values
yPI3156992 = PI3156992["Water (ml)"]
xPI4627382 = PI4627382.index.values
yPI4627382 = PI4627382["Water (ml)"]
xPI5370702 = PI5370702.index.values
yPI5370702 = PI5370702["Water (ml)"]
xPI5505582 = PI5505582.index.values
yPI5505582 = PI5505582["Water (ml)"]
xPI5780732 = PI5780732.index.values
yPI5780732 = PI5780732["Water (ml)"]
xPI6131162 = PI6131162.index.values
yPI6131162 = PI6131162["Water (ml)"]
xPI6148152 = PI6148152.index.values
yPI6148152 = PI6148152["Water (ml)"]
xR2862 = R2862.index.values
yR2862 = R2862["Water (ml)"]
xRedDABI2 = RedDABI2.index.values
yRedDABI2 = RedDABI2["Water (ml)"]
xTx623b2 = Tx623b2.index.values
yTx623b2 = Tx623b2["Water (ml)"]
xYugu12 = Yugu12.index.values
yYugu12 = Yugu12["Water (ml)"]



#line chart portion

plt.plot(xAm249892, yAm249892, c="#a6cee3", label="_nolegend_")
plt.plot(xCM052, yCM052, c="#1f78b4", label="_nolegend_")
plt.plot(xCM2912, yCM2912, c="#b2df8a", label="_nolegend_")
plt.plot(xControl2, yControl2, c="#33a02c", label="_nolegend_")
plt.plot(xPI5504732, yPI5504732, c="#fb9a99", label="_nolegend_")
plt.plot(xPI3156992, yPI3156992, c="#e31a1c", label="_nolegend_")
plt.plot(xPI4627382, yPI4627382, c="#fdbf6f", label="_nolegend_")
plt.plot(xPI5370702, yPI5370702, c="#ff7f00", label="_nolegend_")
plt.plot(xPI5505582, yPI5505582, c="#cab2d6", label="_nolegend_")
plt.plot(xPI5780732, yPI5780732, c="#6a3d9a", label="_nolegend_")
plt.plot(xPI6131162, yPI6131162, c="#ffff99", label="_nolegend_")
plt.plot(xPI6148152, yPI6148152, c="#b15928", label="_nolegend_")
plt.plot(xR2862, yR2862, c="black", label="_nolegend_")
plt.plot(xRedDABI2, yRedDABI2, c="brown", label="_nolegend_")
plt.plot(xTx623b2, yTx623b2, c="tan", label="_nolegend_")
plt.plot(xYugu12, yYugu12, c="gray", label="_nolegend_")



## scatter plot portion for watering data
xAm249891=Am249891[:,4]
yAm249891=Am249891[:, 3]
xCM0521=CM0521[:,4]
yCM0521=CM0521[:, 3]
xCM2911=CM2911[:,4]
yCM2911=CM2911[:, 3]
xControl1=Control1[:,4]
yControl1=Control1[:, 3]
xPI5504731=PI5504731[:,4]
yPI5504731=PI5504731[:, 3]
xPI3156991=PI3156991[:,4]
yPI3156991=PI3156991[:, 3]
xPI4627381=PI4627381[:,4]
yPI4627381=PI4627381[:, 3]
xPI5370701=PI5370701[:,4]
yPI5370701=PI5370701[:, 3]
xPI5505581=PI5505581[:,4]
yPI5505581=PI5505581[:, 3]
xPI5780731=PI5780731[:,4]
yPI5780731=PI5780731[:, 3]
xPI6131161=PI6131161[:,4]
yPI6131161=PI6131161[:, 3]
xPI6148151=PI6148151[:,4]
yPI6148151=PI6148151[:, 3]
xR2861=R2861[:,4]
yR2861=R2861[:, 3]
xRedDABI1=RedDABI1[:,4]
yRedDABI1=RedDABI1[:, 3]
xTx623b1=Tx623b1[:,4]
yTx623b1=Tx623b1[:, 3]
xYugu11=Yugu11[:,4]
yYugu11=Yugu11[:, 3]


#scatter plot
plt.scatter(xAm249891, yAm249891, c="#a6cee3", label="Maize Am24989")
plt.scatter(xCM0521, yCM0521, c="#1f78b4", label="Sorghum CM052")
plt.scatter(xCM2911, yCM2911, c="#b2df8a", label="Sorghum CM291")
plt.scatter(xControl1, yControl1, c="#33a02c", label="Control")
plt.scatter(xPI5504731, yPI5504731, c="#fb9a99", label="MaizeB73 PI550473")
plt.scatter(xPI3156991, yPI3156991, c="#e31a1c", label="Japanese millet PI315699")
plt.scatter(xPI4627381, yPI4627381, c="#fdbf6f", label="Finger millet PI462738")
plt.scatter(xPI5370701, yPI5370701, c="#ff7f00", label="Pearl millet PI537070")
plt.scatter(xPI5505581, yPI5505581, c="#cab2d6", label="Maize PI550558")
plt.scatter(xPI5780731, yPI5780731, c="#6a3d9a", label="Proso millet PI578073")
plt.scatter(xPI6131161, yPI6131161, c="#ffff99", label="Pearl millet PI613116")
plt.scatter(xPI6148151, yPI6148151, c="#b15928", label="Foxtail millet PI614815")
plt.scatter(xR2861, yR2861, c="black", label="tef R286")
plt.scatter(xRedDABI1, yRedDABI1, c="brown", label="tef Red DABI")
plt.scatter(xTx623b1, yTx623b1, c="tan", label="Sorghum Tx623b")
plt.scatter(xYugu11, yYugu11, c="gray", label="Foxtail millet Yugu1")


#plt.scatter(xcmini, ycmini, c="tan", label="Mini Control Median", alpha=0.5, s=30)
#plt.scatter(xcB73, ycB73, c="magenta", label="B73 Control Median", alpha=0.5, s=30)
plt.ylabel("Water (ml)", fontsize=18)
plt.xlabel("Day #", fontsize=18)
plt.title('Water (ml) vs. Date', fontsize=18)
plt.legend(loc=2, prop={'size': 10}, fontsize=18)
#plt.xticks(rotation=75)
plt.yticks(fontsize=18)
plt.xticks(range(0,116, 5), fontsize=18)
plt.show()
