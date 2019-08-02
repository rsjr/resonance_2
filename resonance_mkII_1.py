import Tkinter
import seaborn
import numpy as np
import scipy
import librosa
import librosa.display, urllib, matplotlib.pyplot as plt, sklearn,pdandas as pd
import csv
import re
import sys
import codecs
from os import listdir
from IPython.display import Audio
from os.path import isfile, join

music_duration=10

window = 1
n_mfcc = 30
scaler = sklearn.preprocessing.StandardScaler()
hop_length = 512
mfcc_window = 43

folder_classical='/home/rogerio/Music/TCC - Music/Classical_3/'
folder_samba='/home/rogerio/Music/TCC - Music/Samba_4/'
folder_rap='/home/rogerio/Music/TCC - Music/Rap_3/'
folder_jazz='/home/rogerio/Music/TCC - Music/Jazz_3/'
folder_rock='/home/rogerio/Music/TCC - Music/Rock_3/'

csv_row_classical=pd.DataFrame()
csv_list_classical=pd.DataFrame()

df_column_classical=pd.DataFrame()
df_row_classical=pd.DataFrame()
df_list_classical=pd.DataFrame()

df_column_samba=pd.DataFrame()
df_row_samba=pd.DataFrame()
df_list_samba=pd.DataFrame()

df_column_rap=pd.DataFrame()
df_row_rap=pd.DataFrame()
df_list_rap=pd.DataFrame()

df_column_jazz=pd.DataFrame()
df_row_jazz=pd.DataFrame()
df_list_jazz=pd.DataFrame()

df_column_rock=pd.DataFrame()
df_row_rock=pd.DataFrame()
df_list_rock=pd.DataFrame()



#----------------------------------------------------------------------------------------------
#CLASSES

#CARREGA ARQUIVOS

class file_loader:
	#filelist = None
	counter = None
	#filelist = None

	def __init__(self, folder):
		self.folder=folder

	def load(self):
		filelist = [f for f in listdir(self.folder) if isfile(join(self.folder, f))]
		file_loader.counter = len(filelist)
		print filelist
		return filelist;

	def get_counter(self):
		print file_loader.counter
		return file_loader.counter;

	#def music_load(self):
		#for i in xrange(counter):
		#x, fs = librosa.load(folder+file_loader.filelist[0], duration=music_duration)
		#print i
		#print x_clas.shape
		#print fs_clas

#----------------------------------------------------------------------------------------------
#instancia objetos

o_classical = file_loader(folder_classical)
filelist_classical=o_classical.load()
counter_classical=o_classical.get_counter()

o_samba = file_loader(folder_samba)
filelist_samba=o_samba.load()
counter_samba=o_samba.get_counter()

o_rap = file_loader(folder_rap)
filelist_rap=o_rap.load()
counter_rap=o_rap.get_counter()

o_jazz = file_loader(folder_jazz)
filelist_jazz=o_jazz.load()
counter_jazz=o_jazz.get_counter()

o_rock = file_loader(folder_rock)
filelist_rock=o_rock.load()
counter_rock=o_rock.get_counter()

#-----------------------------------------------------------------------------------------------------------------
#Extraction Functions


def mfcc_mean(x,sr):

	mfcc = librosa.feature.mfcc(y=x, sr=sr, n_mfcc=n_mfcc)
	mfcc.shape
	mfcc_scaled = scaler.fit_transform(mfcc)

	mfcc_0 = mfcc_scaled[0,0:]
	#print mfcc_0;
	mfcc_1 = mfcc_scaled[1,0:]
	#print mfcc_1;
	mfcc_2 = mfcc_scaled[2,0:]
	#print mfcc_2;
	mfcc_3 = mfcc_scaled[3,0:]
	#print mfcc_3;
	mfcc_4 = mfcc_scaled[4,0:]
	#print mfcc_4;
	mfcc_5 = mfcc_scaled[5,0:]
	#print mfcc_5;
	mfcc_6 = mfcc_scaled[6,0:]
	#print mfcc_6;
	mfcc_7 = mfcc_scaled[7,0:]
	#print mfcc_7;
	mfcc_8 = mfcc_scaled[8,0:]
	#print mfcc_8;
	mfcc_9 = mfcc_scaled[9,0:]
	#print mfcc_9;
	mfcc_10 = mfcc_scaled[10,0:]
	#print mfcc_10;
	mfcc_11 = mfcc_scaled[11,0:]
	#print mfcc_11;
	mfcc_12 = mfcc_scaled[12,0:]
	#print mfcc_12;
	mfcc_13 = mfcc_scaled[13,0:]
	#print mfcc_13;
	mfcc_14 = mfcc_scaled[14,0:]
	#print mfcc_14;
	mfcc_15 = mfcc_scaled[15,0:]
	#print mfcc_15;
	mfcc_16 = mfcc_scaled[16,0:]
	#print mfcc_16;
	mfcc_17 = mfcc_scaled[17,0:]
	#print mfcc_17;
	mfcc_18 = mfcc_scaled[18,0:]
	#print mfcc_18;
	mfcc_19 = mfcc_scaled[19,0:]
	#print mfcc_19;
	mfcc_20 = mfcc_scaled[20,0:]
	#print mfcc_20;
	mfcc_21 = mfcc_scaled[21,0:]
	#print mfcc_21;
	mfcc_22 = mfcc_scaled[22,0:]
	#print mfcc_22;
	mfcc_23 = mfcc_scaled[23,0:]
	#print mfcc_23;
	mfcc_24 = mfcc_scaled[24,0:]
	#print mfcc_24;
	mfcc_25 = mfcc_scaled[25,0:]
	#print mfcc_25;
	mfcc_26 = mfcc_scaled[26,0:]
	#print mfcc_26;
	mfcc_27 = mfcc_scaled[27,0:]
	#print mfcc_27;
	mfcc_28 = mfcc_scaled[28,0:]
	#print mfcc_28;
	mfcc_29 = mfcc_scaled[29,0:]
	#print mfcc_29;

	mfcc_mean_0 = np.mean(mfcc_0)
	mfcc_mean_1 = np.mean(mfcc_1)
	mfcc_mean_2 = np.mean(mfcc_2)
	mfcc_mean_3 = np.mean(mfcc_3)
	mfcc_mean_4 = np.mean(mfcc_4)
	mfcc_mean_5 = np.mean(mfcc_5)
	mfcc_mean_6 = np.mean(mfcc_6)
	mfcc_mean_7 = np.mean(mfcc_7)
	mfcc_mean_8 = np.mean(mfcc_8)
	mfcc_mean_9 = np.mean(mfcc_9)
	mfcc_mean_10 = np.mean(mfcc_10)
	mfcc_mean_11 = np.mean(mfcc_11)
	mfcc_mean_12 = np.mean(mfcc_12)
	mfcc_mean_13 = np.mean(mfcc_13)
	mfcc_mean_14 = np.mean(mfcc_14)
	mfcc_mean_15 = np.mean(mfcc_15)
	mfcc_mean_16 = np.mean(mfcc_16)
	mfcc_mean_17 = np.mean(mfcc_17)
	mfcc_mean_18 = np.mean(mfcc_18)
	mfcc_mean_19 = np.mean(mfcc_19)
	mfcc_mean_20 = np.mean(mfcc_20)
	mfcc_mean_21 = np.mean(mfcc_21)
	mfcc_mean_22 = np.mean(mfcc_22)
	mfcc_mean_23 = np.mean(mfcc_23)
	mfcc_mean_24 = np.mean(mfcc_24)
	mfcc_mean_25 = np.mean(mfcc_25)
	mfcc_mean_26 = np.mean(mfcc_26)
	mfcc_mean_27 = np.mean(mfcc_27)
	mfcc_mean_28 = np.mean(mfcc_28)
	mfcc_mean_29 = np.mean(mfcc_29)

	mfcc_mean_final = [mfcc_mean_0,mfcc_mean_1,mfcc_mean_2,mfcc_mean_3,mfcc_mean_4,mfcc_mean_5,mfcc_mean_6,mfcc_mean_7,mfcc_mean_8,mfcc_mean_9,mfcc_mean_10,
		mfcc_mean_11, mfcc_mean_12,mfcc_mean_13,mfcc_mean_14,mfcc_mean_15,mfcc_mean_16,mfcc_mean_17, mfcc_mean_18, mfcc_mean_19, mfcc_mean_20, 
		mfcc_mean_21, mfcc_mean_22, mfcc_mean_23, mfcc_mean_24, mfcc_mean_25, mfcc_mean_26, mfcc_mean_27, mfcc_mean_28, mfcc_mean_29]

	print "MFCC Mean: ", mfcc_mean_final

	return mfcc_mean_final;

def mfcc_std(x,sr):

	mfcc = librosa.feature.mfcc(y=x, sr=sr, n_mfcc=n_mfcc)
	mfcc.shape

	mfcc_scaled = scaler.fit_transform(mfcc)
	
	mfcc_0 = mfcc_scaled[0,0:]
	#print mfcc_0;
	mfcc_1 = mfcc_scaled[1,0:]
	#print mfcc_1;
	mfcc_2 = mfcc_scaled[2,0:]
	#print mfcc_2;
	mfcc_3 = mfcc_scaled[3,0:]
	#print mfcc_3;
	mfcc_4 = mfcc_scaled[4,0:]
	#print mfcc_4;
	mfcc_5 = mfcc_scaled[5,0:]
	#print mfcc_5;
	mfcc_6 = mfcc_scaled[6,0:]
	#print mfcc_6;
	mfcc_7 = mfcc_scaled[7,0:]
	#print mfcc_7;
	mfcc_8 = mfcc_scaled[8,0:]
	#print mfcc_8;
	mfcc_9 = mfcc_scaled[9,0:]
	#print mfcc_9;
	mfcc_10 = mfcc_scaled[10,0:]
	#print mfcc_10;
	mfcc_11 = mfcc_scaled[11,0:]
	#print mfcc_11;
	mfcc_12 = mfcc_scaled[12,0:]
	#print mfcc_12;
	mfcc_13 = mfcc_scaled[13,0:]
	#print mfcc_13;
	mfcc_14 = mfcc_scaled[14,0:]
	#print mfcc_14;
	mfcc_15 = mfcc_scaled[15,0:]
	#print mfcc_15;
	mfcc_16 = mfcc_scaled[16,0:]
	#print mfcc_16;
	mfcc_17 = mfcc_scaled[17,0:]
	#print mfcc_17;
	mfcc_18 = mfcc_scaled[18,0:]
	#print mfcc_18;
	mfcc_19 = mfcc_scaled[19,0:]
	#print mfcc_19;
	mfcc_20 = mfcc_scaled[20,0:]
	#print mfcc_20;
	mfcc_21 = mfcc_scaled[21,0:]
	#print mfcc_21;
	mfcc_22 = mfcc_scaled[22,0:]
	#print mfcc_22;
	mfcc_23 = mfcc_scaled[23,0:]
	#print mfcc_23;
	mfcc_24 = mfcc_scaled[24,0:]
	#print mfcc_24;
	mfcc_25 = mfcc_scaled[25,0:]
	#print mfcc_25;
	mfcc_26 = mfcc_scaled[26,0:]
	#print mfcc_26;
	mfcc_27 = mfcc_scaled[27,0:]
	#print mfcc_27;
	mfcc_28 = mfcc_scaled[28,0:]
	#print mfcc_28;
	mfcc_29 = mfcc_scaled[29,0:]
	#print mfcc_29;
	
	#print mfcc_29;
	
	mfcc_std_0 = np.std(mfcc_0)
	mfcc_std_1 = np.std(mfcc_1)
	mfcc_std_2 = np.std(mfcc_2)
	mfcc_std_3 = np.std(mfcc_3)
	mfcc_std_4 = np.std(mfcc_4)
	mfcc_std_5 = np.std(mfcc_5)
	mfcc_std_6 = np.std(mfcc_6)
	mfcc_std_7 = np.std(mfcc_7)
	mfcc_std_8 = np.std(mfcc_8)
	mfcc_std_9 = np.std(mfcc_9)
	mfcc_std_10 = np.std(mfcc_10)
	mfcc_std_11 = np.std(mfcc_11)
	mfcc_std_12 = np.std(mfcc_12)
	mfcc_std_13 = np.std(mfcc_13)
	mfcc_std_14 = np.std(mfcc_14)
	mfcc_std_15 = np.std(mfcc_15)
	mfcc_std_16 = np.std(mfcc_16)
	mfcc_std_17 = np.std(mfcc_17)
	mfcc_std_18 = np.std(mfcc_18)
	mfcc_std_19 = np.std(mfcc_19)
	mfcc_std_20 = np.std(mfcc_20)
	mfcc_std_21 = np.std(mfcc_21)
	mfcc_std_22 = np.std(mfcc_22)
	mfcc_std_23 = np.std(mfcc_23)
	mfcc_std_24 = np.std(mfcc_24)
	mfcc_std_25 = np.std(mfcc_25)
	mfcc_std_26 = np.std(mfcc_26)
	mfcc_std_27 = np.std(mfcc_27)
	mfcc_std_28 = np.std(mfcc_28)
	mfcc_std_29 = np.std(mfcc_29)

	mfcc_std_final = [mfcc_std_0,mfcc_std_1,mfcc_std_2,mfcc_std_3,mfcc_std_4,mfcc_std_5,mfcc_std_6,mfcc_std_7,mfcc_std_8,mfcc_std_9,mfcc_std_10,
		mfcc_std_11, mfcc_std_12,mfcc_std_13,mfcc_std_14,mfcc_std_15,mfcc_std_16,mfcc_std_17, mfcc_std_18, mfcc_std_19, mfcc_std_20, 
		mfcc_std_21, mfcc_std_22, mfcc_std_23, mfcc_std_24, mfcc_std_25, mfcc_std_26, mfcc_std_27, mfcc_std_28, mfcc_std_29]

	print "MFCC STD: ", mfcc_std_final

	return mfcc_std_final

def mfcc_max(x,sr):

	mfcc = librosa.feature.mfcc(y=x, sr=sr, n_mfcc=n_mfcc)
	mfcc.shape

	mfcc_scaled = scaler.fit_transform(mfcc)
	
	mfcc_0 = mfcc_scaled[0,0:]
	#print mfcc_0;
	mfcc_1 = mfcc_scaled[1,0:]
	#print mfcc_1;
	mfcc_2 = mfcc_scaled[2,0:]
	#print mfcc_2;
	mfcc_3 = mfcc_scaled[3,0:]
	#print mfcc_3;
	mfcc_4 = mfcc_scaled[4,0:]
	#print mfcc_4;
	mfcc_5 = mfcc_scaled[5,0:]
	#print mfcc_5;
	mfcc_6 = mfcc_scaled[6,0:]
	#print mfcc_6;
	mfcc_7 = mfcc_scaled[7,0:]
	#print mfcc_7;
	mfcc_8 = mfcc_scaled[8,0:]
	#print mfcc_8;
	mfcc_9 = mfcc_scaled[9,0:]
	#print mfcc_9;
	mfcc_10 = mfcc_scaled[10,0:]
	#print mfcc_10;
	mfcc_11 = mfcc_scaled[11,0:]
	#print mfcc_11;
	mfcc_12 = mfcc_scaled[12,0:]
	#print mfcc_12;
	mfcc_13 = mfcc_scaled[13,0:]
	#print mfcc_13;
	mfcc_14 = mfcc_scaled[14,0:]
	#print mfcc_14;
	mfcc_15 = mfcc_scaled[15,0:]
	#print mfcc_15;
	mfcc_16 = mfcc_scaled[16,0:]
	#print mfcc_16;
	mfcc_17 = mfcc_scaled[17,0:]
	#print mfcc_17;
	mfcc_18 = mfcc_scaled[18,0:]
	#print mfcc_18;
	mfcc_19 = mfcc_scaled[19,0:]
	#print mfcc_19;
	mfcc_20 = mfcc_scaled[20,0:]
	#print mfcc_20;
	mfcc_21 = mfcc_scaled[21,0:]
	#print mfcc_21;
	mfcc_22 = mfcc_scaled[22,0:]
	#print mfcc_22;
	mfcc_23 = mfcc_scaled[23,0:]
	#print mfcc_23;
	mfcc_24 = mfcc_scaled[24,0:]
	#print mfcc_24;
	mfcc_25 = mfcc_scaled[25,0:]
	#print mfcc_25;
	mfcc_26 = mfcc_scaled[26,0:]
	#print mfcc_26;
	mfcc_27 = mfcc_scaled[27,0:]
	#print mfcc_27;
	mfcc_28 = mfcc_scaled[28,0:]
	#print mfcc_28;
	mfcc_29 = mfcc_scaled[29,0:]
	#print mfcc_29;

	mfcc_amax_0 = np.amax(mfcc_0)
	mfcc_amax_1 = np.amax(mfcc_1)
	mfcc_amax_2 = np.amax(mfcc_2)
	mfcc_amax_3 = np.amax(mfcc_3)
	mfcc_amax_4 = np.amax(mfcc_4)
	mfcc_amax_5 = np.amax(mfcc_5)
	mfcc_amax_6 = np.amax(mfcc_6)
	mfcc_amax_7 = np.amax(mfcc_7)
	mfcc_amax_8 = np.amax(mfcc_8)
	mfcc_amax_9 = np.amax(mfcc_9)
	mfcc_amax_10 = np.amax(mfcc_10)
	mfcc_amax_11 = np.amax(mfcc_11)
	mfcc_amax_12 = np.amax(mfcc_12)
	mfcc_amax_13 = np.amax(mfcc_13)
	mfcc_amax_14 = np.amax(mfcc_14)
	mfcc_amax_15 = np.amax(mfcc_15)
	mfcc_amax_16 = np.amax(mfcc_16)
	mfcc_amax_17 = np.amax(mfcc_17)
	mfcc_amax_18 = np.amax(mfcc_18)
	mfcc_amax_19 = np.amax(mfcc_19)
	mfcc_amax_20 = np.amax(mfcc_20)
	mfcc_amax_21 = np.amax(mfcc_21)
	mfcc_amax_22 = np.amax(mfcc_22)
	mfcc_amax_23 = np.amax(mfcc_23)
	mfcc_amax_24 = np.amax(mfcc_24)
	mfcc_amax_25 = np.amax(mfcc_25)
	mfcc_amax_26 = np.amax(mfcc_26)
	mfcc_amax_27 = np.amax(mfcc_27)
	mfcc_amax_28 = np.amax(mfcc_28)
	mfcc_amax_29 = np.amax(mfcc_29)

	mfcc_amax_final = [mfcc_amax_0,mfcc_amax_1,mfcc_amax_2,mfcc_amax_3,mfcc_amax_4,mfcc_amax_5,mfcc_amax_6,mfcc_amax_7,mfcc_amax_8,mfcc_amax_9,mfcc_amax_10,
		mfcc_amax_11, mfcc_amax_12,mfcc_amax_13,mfcc_amax_14,mfcc_amax_15,mfcc_amax_16,mfcc_amax_17, mfcc_amax_18, mfcc_amax_19, mfcc_amax_20, 
		mfcc_amax_21, mfcc_amax_22, mfcc_amax_23, mfcc_amax_24, mfcc_amax_25, mfcc_amax_26, mfcc_amax_27, mfcc_amax_28, mfcc_amax_29]

	print "MFCC MAX: ",mfcc_amax_final

	return mfcc_amax_final;

def mfcc_min(x,sr):

	mfcc = librosa.feature.mfcc(y=x, sr=sr, n_mfcc=n_mfcc)
	mfcc.shape

	mfcc_scaled = scaler.fit_transform(mfcc)
	mfcc_0 = mfcc_scaled[0,0:]
	#print mfcc_0;
	mfcc_1 = mfcc_scaled[1,0:]
	#print mfcc_1;
	mfcc_2 = mfcc_scaled[2,0:]
	#print mfcc_2;
	mfcc_3 = mfcc_scaled[3,0:]
	#print mfcc_3;
	mfcc_4 = mfcc_scaled[4,0:]
	#print mfcc_4;
	mfcc_5 = mfcc_scaled[5,0:]
	#print mfcc_5;
	mfcc_6 = mfcc_scaled[6,0:]
	#print mfcc_6;
	mfcc_7 = mfcc_scaled[7,0:]
	#print mfcc_7;
	mfcc_8 = mfcc_scaled[8,0:]
	#print mfcc_8;
	mfcc_9 = mfcc_scaled[9,0:]
	#print mfcc_9;
	mfcc_10 = mfcc_scaled[10,0:]
	#print mfcc_10;
	mfcc_11 = mfcc_scaled[11,0:]
	#print mfcc_11;
	mfcc_12 = mfcc_scaled[12,0:]
	#print mfcc_12;
	mfcc_13 = mfcc_scaled[13,0:]
	#print mfcc_13;
	mfcc_14 = mfcc_scaled[14,0:]
	#print mfcc_14;
	mfcc_15 = mfcc_scaled[15,0:]
	#print mfcc_15;
	mfcc_16 = mfcc_scaled[16,0:]
	#print mfcc_16;
	mfcc_17 = mfcc_scaled[17,0:]
	#print mfcc_17;
	mfcc_18 = mfcc_scaled[18,0:]
	#print mfcc_18;
	mfcc_19 = mfcc_scaled[19,0:]
	#print mfcc_19;
	mfcc_20 = mfcc_scaled[20,0:]
	#print mfcc_20;
	mfcc_21 = mfcc_scaled[21,0:]
	#print mfcc_21;
	mfcc_22 = mfcc_scaled[22,0:]
	#print mfcc_22;
	mfcc_23 = mfcc_scaled[23,0:]
	#print mfcc_23;
	mfcc_24 = mfcc_scaled[24,0:]
	#print mfcc_24;
	mfcc_25 = mfcc_scaled[25,0:]
	#print mfcc_25;
	mfcc_26 = mfcc_scaled[26,0:]
	#print mfcc_26;
	mfcc_27 = mfcc_scaled[27,0:]
	#print mfcc_27;
	mfcc_28 = mfcc_scaled[28,0:]
	#print mfcc_28;
	mfcc_29 = mfcc_scaled[29,0:]
	#print mfcc_29;

	mfcc_amin_0 = np.amin(mfcc_0)
	mfcc_amin_1 = np.amin(mfcc_1)
	mfcc_amin_2 = np.amin(mfcc_2)
	mfcc_amin_3 = np.amin(mfcc_3)
	mfcc_amin_4 = np.amin(mfcc_4)
	mfcc_amin_5 = np.amin(mfcc_5)
	mfcc_amin_6 = np.amin(mfcc_6)
	mfcc_amin_7 = np.amin(mfcc_7)
	mfcc_amin_8 = np.amin(mfcc_8)
	mfcc_amin_9 = np.amin(mfcc_9)
	mfcc_amin_10 = np.amin(mfcc_10)
	mfcc_amin_11 = np.amin(mfcc_11)
	mfcc_amin_12 = np.amin(mfcc_12)
	mfcc_amin_13 = np.amin(mfcc_13)
	mfcc_amin_14 = np.amin(mfcc_14)
	mfcc_amin_15 = np.amin(mfcc_15)
	mfcc_amin_16 = np.amin(mfcc_16)
	mfcc_amin_17 = np.amin(mfcc_17)
	mfcc_amin_18 = np.amin(mfcc_18)
	mfcc_amin_19 = np.amin(mfcc_19)
	mfcc_amin_20 = np.amin(mfcc_20)
	mfcc_amin_21 = np.amin(mfcc_21)
	mfcc_amin_22 = np.amin(mfcc_22)
	mfcc_amin_23 = np.amin(mfcc_23)
	mfcc_amin_24 = np.amin(mfcc_24)
	mfcc_amin_25 = np.amin(mfcc_25)
	mfcc_amin_26 = np.amin(mfcc_26)
	mfcc_amin_27 = np.amin(mfcc_27)
	mfcc_amin_28 = np.amin(mfcc_28)
	mfcc_amin_29 = np.amin(mfcc_29)

	mfcc_amin_final = [mfcc_amin_0,mfcc_amin_1,mfcc_amin_2,mfcc_amin_3,mfcc_amin_4,mfcc_amin_5,mfcc_amin_6,mfcc_amin_7,mfcc_amin_8,mfcc_amin_9,mfcc_amin_10,
		mfcc_amin_11, mfcc_amin_12,mfcc_amin_13,mfcc_amin_14,mfcc_amin_15,mfcc_amin_16,mfcc_amin_17, mfcc_amin_18, mfcc_amin_19, mfcc_amin_20, 
		mfcc_amin_21, mfcc_amin_22, mfcc_amin_23, mfcc_amin_24, mfcc_amin_25, mfcc_amin_26, mfcc_amin_27, mfcc_amin_28, mfcc_amin_29]

	print "MFCC MIN: ",mfcc_amin_final

	return mfcc_amin_final;

def mfcc_var(x,sr):

	mfcc = librosa.feature.mfcc(y=x, sr=sr, n_mfcc=n_mfcc)
	mfcc.shape

	mfcc_scaled = scaler.fit_transform(mfcc)
	
	mfcc_0 = mfcc_scaled[0,0:]
	#print mfcc_0;
	mfcc_1 = mfcc_scaled[1,0:]
	#print mfcc_1;
	mfcc_2 = mfcc_scaled[2,0:]
	#print mfcc_2;
	mfcc_3 = mfcc_scaled[3,0:]
	#print mfcc_3;
	mfcc_4 = mfcc_scaled[4,0:]
	#print mfcc_4;
	mfcc_5 = mfcc_scaled[5,0:]
	#print mfcc_5;
	mfcc_6 = mfcc_scaled[6,0:]
	#print mfcc_6;
	mfcc_7 = mfcc_scaled[7,0:]
	#print mfcc_7;
	mfcc_8 = mfcc_scaled[8,0:]
	#print mfcc_8;
	mfcc_9 = mfcc_scaled[9,0:]
	#print mfcc_9;
	mfcc_10 = mfcc_scaled[10,0:]
	#print mfcc_10;
	mfcc_11 = mfcc_scaled[11,0:]
	#print mfcc_11;
	mfcc_12 = mfcc_scaled[12,0:]
	#print mfcc_12;
	mfcc_13 = mfcc_scaled[13,0:]
	#print mfcc_13;
	mfcc_14 = mfcc_scaled[14,0:]
	#print mfcc_14;
	mfcc_15 = mfcc_scaled[15,0:]
	#print mfcc_15;
	mfcc_16 = mfcc_scaled[16,0:]
	#print mfcc_16;
	mfcc_17 = mfcc_scaled[17,0:]
	#print mfcc_17;
	mfcc_18 = mfcc_scaled[18,0:]
	#print mfcc_18;
	mfcc_19 = mfcc_scaled[19,0:]
	#print mfcc_19;
	mfcc_20 = mfcc_scaled[20,0:]
	#print mfcc_20;
	mfcc_21 = mfcc_scaled[21,0:]
	#print mfcc_21;
	mfcc_22 = mfcc_scaled[22,0:]
	#print mfcc_22;
	mfcc_23 = mfcc_scaled[23,0:]
	#print mfcc_23;
	mfcc_24 = mfcc_scaled[24,0:]
	#print mfcc_24;
	mfcc_25 = mfcc_scaled[25,0:]
	#print mfcc_25;
	mfcc_26 = mfcc_scaled[26,0:]
	#print mfcc_26;
	mfcc_27 = mfcc_scaled[27,0:]
	#print mfcc_27;
	mfcc_28 = mfcc_scaled[28,0:]
	#print mfcc_28;
	mfcc_29 = mfcc_scaled[29,0:]
	#print mfcc_29;

	mfcc_var_0 = np.var(mfcc_0)
	mfcc_var_1 = np.var(mfcc_1)
	mfcc_var_2 = np.var(mfcc_2)
	mfcc_var_3 = np.var(mfcc_3)
	mfcc_var_4 = np.var(mfcc_4)
	mfcc_var_5 = np.var(mfcc_5)
	mfcc_var_6 = np.var(mfcc_6)
	mfcc_var_7 = np.var(mfcc_7)
	mfcc_var_8 = np.var(mfcc_8)
	mfcc_var_9 = np.var(mfcc_9)
	mfcc_var_10 = np.var(mfcc_10)
	mfcc_var_11 = np.var(mfcc_11)
	mfcc_var_12 = np.var(mfcc_12)
	mfcc_var_13 = np.var(mfcc_13)
	mfcc_var_14 = np.var(mfcc_14)
	mfcc_var_15 = np.var(mfcc_15)
	mfcc_var_16 = np.var(mfcc_16)
	mfcc_var_17 = np.var(mfcc_17)
	mfcc_var_18 = np.var(mfcc_18)
	mfcc_var_19 = np.var(mfcc_19)
	mfcc_var_20 = np.var(mfcc_20)
	mfcc_var_21 = np.var(mfcc_21)
	mfcc_var_22 = np.var(mfcc_22)
	mfcc_var_23 = np.var(mfcc_23)
	mfcc_var_24 = np.var(mfcc_24)
	mfcc_var_25 = np.var(mfcc_25)
	mfcc_var_26 = np.var(mfcc_26)
	mfcc_var_27 = np.var(mfcc_27)
	mfcc_var_28 = np.var(mfcc_28)
	mfcc_var_29 = np.var(mfcc_29)

	mfcc_var_final = [mfcc_var_0,mfcc_var_1,mfcc_var_2,mfcc_var_3,mfcc_var_4,mfcc_var_5,mfcc_var_6,mfcc_var_7,mfcc_var_8,mfcc_var_9,mfcc_var_10,
		mfcc_var_11, mfcc_var_12,mfcc_var_13,mfcc_var_14,mfcc_var_15,mfcc_var_16,mfcc_var_17, mfcc_var_18, mfcc_var_19, mfcc_var_20, 
		mfcc_var_21, mfcc_var_22, mfcc_var_23, mfcc_var_24, mfcc_var_25, mfcc_var_26, mfcc_var_27, mfcc_var_28, mfcc_var_29]

	print "MFCC VARIANCE: ",mfcc_var_final

	return mfcc_var_final;


for i in xrange(counter_classical):

	print "For:", i
	print folder_classical+filelist_classical[i]
		
	x_classical_overall, fs_classical = librosa.load(folder_classical+filelist_classical[i], duration=music_duration)
	#x_classical_off, fs_classical_off = librosa.load(folder_classical+filelist_classical[i], offset=60, duration=music_duration)
	#x_classical_overall=np.concatenate((x_classical,x_classical_off),axis=0)

	mfcc_mean_classical = mfcc_mean(x_classical_overall, fs_classical)
	mfcc_std_classical = mfcc_std(x_classical_overall, fs_classical)
	mfcc_max_classical = mfcc_max(x_classical_overall, fs_classical)
	mfcc_min_classical = mfcc_min(x_classical_overall, fs_classical)
	mfcc_var_classical = mfcc_var(x_classical_overall, fs_classical)
	
	mfcc_classical_overall = np.concatenate((mfcc_mean_classical, mfcc_std_classical, mfcc_max_classical,mfcc_min_classical,mfcc_var_classical))

	print mfcc_classical_overall

	df_mfcc_classical = pd.DataFrame(mfcc_classical_overall).T

	df_mfcc_classical.insert(0,'Genre','Classical')
	df_list_classical=pd.DataFrame.append(df_list_classical, df_mfcc_classical)
	df_list_classical.to_csv('mfcc_classical_1.csv')

for i in xrange(counter_samba):

	print "For:", i
	print folder_samba+filelist_samba[i]
		
	x_samba_overall, fs_samba = librosa.load(folder_samba+filelist_samba[i], duration=music_duration)
	#x_samba_off, fs_samba_off = librosa.load(folder_samba+filelist_samba[i], offset=60, duration=music_duration)
	#x_samba_overall=np.concatenate((x_samba,x_samba_off),axis=0)

	mfcc_mean_samba = mfcc_mean(x_samba_overall, fs_samba)
	mfcc_std_samba = mfcc_std(x_samba_overall, fs_samba)
	mfcc_max_samba = mfcc_max(x_samba_overall, fs_samba)
	mfcc_min_samba = mfcc_min(x_samba_overall, fs_samba)
	mfcc_var_samba = mfcc_var(x_samba_overall, fs_samba)
	
	mfcc_samba_overall = np.concatenate((mfcc_mean_samba, mfcc_std_samba, mfcc_max_samba,mfcc_min_samba,mfcc_var_samba))

	print mfcc_samba_overall

	df_mfcc_samba = pd.DataFrame(mfcc_samba_overall).T

	df_mfcc_samba.insert(0,'Genre','Samba')
	df_list_samba=pd.DataFrame.append(df_list_samba, df_mfcc_samba)
	df_list_samba.to_csv('mfcc_samba_1.csv')

for i in xrange(counter_rap):

	print "For:", i
	print folder_rap+filelist_rap[i]
		
	x_rap_overall, fs_rap = librosa.load(folder_rap+filelist_rap[i], duration=music_duration)
	#x_rap_off, fs_rap_off = librosa.load(folder_rap+filelist_rap[i], offset=60, duration=music_duration)
	#x_rap_overall=np.concatenate((x_rap,x_rap_off),axis=0)

	mfcc_mean_rap = mfcc_mean(x_rap_overall, fs_rap)
	mfcc_std_rap = mfcc_std(x_rap_overall, fs_rap)
	mfcc_max_rap = mfcc_max(x_rap_overall, fs_rap)
	mfcc_min_rap = mfcc_min(x_rap_overall, fs_rap)
	mfcc_var_rap = mfcc_var(x_rap_overall, fs_rap)
	
	mfcc_rap_overall = np.concatenate((mfcc_mean_rap, mfcc_std_rap, mfcc_max_rap,mfcc_min_rap,mfcc_var_rap))

	print mfcc_rap_overall

	df_mfcc_rap = pd.DataFrame(mfcc_rap_overall).T

	df_mfcc_rap.insert(0,'Genre','Rap')
	df_list_rap=pd.DataFrame.append(df_list_rap, df_mfcc_rap)
	df_list_rap.to_csv('mfcc_rap_1.csv')


for i in xrange(counter_jazz):

	print "For:", i
	print folder_jazz+filelist_jazz[i]
		
	x_jazz_overall, fs_jazz = librosa.load(folder_jazz+filelist_jazz[i], duration=music_duration)
	#x_jazz_off, fs_jazz_off = librosa.load(folder_jazz+filelist_jazz[i], offset=60, duration=music_duration)
	#x_jazz_overall=np.concatenate((x_jazz,x_jazz_off),axis=0)

	mfcc_mean_jazz = mfcc_mean(x_jazz_overall, fs_jazz)
	mfcc_std_jazz = mfcc_std(x_jazz_overall, fs_jazz)
	mfcc_max_jazz = mfcc_max(x_jazz_overall, fs_jazz)
	mfcc_min_jazz = mfcc_min(x_jazz_overall, fs_jazz)
	mfcc_var_jazz = mfcc_var(x_jazz_overall, fs_jazz)
	
	mfcc_jazz_overall = np.concatenate((mfcc_mean_jazz, mfcc_std_jazz, mfcc_max_jazz,mfcc_min_jazz,mfcc_var_jazz))

	print mfcc_jazz_overall

	df_mfcc_jazz = pd.DataFrame(mfcc_jazz_overall).T

	df_mfcc_jazz.insert(0,'Genre','Jazz')
	df_list_jazz=pd.DataFrame.append(df_list_jazz, df_mfcc_jazz)
	df_list_jazz.to_csv('mfcc_jazz_1.csv')

	#df_column_classical.to_csv("test_overall.csv")


for i in xrange(counter_rock):

	print "For:", i
	print folder_rock+filelist_rock[i]
		
	x_rock_overall, fs_rock = librosa.load(folder_rock+filelist_rock[i], duration=music_duration)
	#x_rock_off, fs_rock_off = librosa.load(folder_rock+filelist_rock[i], offset=60, duration=music_duration)
	#x_rock_overall=np.concatenate((x_rock,x_rock_off),axis=0)

	mfcc_mean_rock = mfcc_mean(x_rock_overall, fs_rock)
	mfcc_std_rock = mfcc_std(x_rock_overall, fs_rock)
	mfcc_max_rock = mfcc_max(x_rock_overall, fs_rock)
	mfcc_min_rock = mfcc_min(x_rock_overall, fs_rock)
	mfcc_var_rock = mfcc_var(x_rock_overall, fs_rock)
	
	mfcc_rock_overall = np.concatenate((mfcc_mean_rock, mfcc_std_rock, mfcc_max_rock,mfcc_min_rock,mfcc_var_rock))

	print mfcc_rock_overall

	df_mfcc_rock = pd.DataFrame(mfcc_rock_overall).T

	df_mfcc_rock.insert(0,'Genre','Rock')
	df_list_rock=pd.DataFrame.append(df_list_rock, df_mfcc_rock)
	df_list_rock.to_csv('mfcc_rock_1.csv')

csv_final=df_list_classical.append([df_list_samba,df_list_rap,df_list_jazz,df_list_rock])
csv_final.to_csv("new_mfcc_final_1.csv")