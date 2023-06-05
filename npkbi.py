from tkinter import *
import time
import threading
from tkinter.ttk import Progressbar
from tkinter import ttk
import socket
import re
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import subprocess
import PIL
from PIL import Image,ImageTk
import signal
import subprocess
import time
#import threading
import serial
import requests
import json
import uuid
from datetime import date
from timeit import Timer

try:
    from Tkinter import Frame, Label, Message, StringVar, Canvas
    from ttk import Scrollbar
    from Tkconstants import *
except ImportError:
    from tkinter import Frame, Label, Message, StringVar, Canvas
    from tkinter.ttk import Scrollbar
    from tkinter.constants import *

import platform
import sys,os
import picamera
import base64
import array as arr
import numpy as np
import urllib.request
import random 
import pathlib
from uuid import UUID
from geopy.geocoders import Nominatim
import textwrap

import logging

from tkinter import messagebox

############################################################################
import datetime
import queue
import logging
import signal
import time
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk, VERTICAL, HORIZONTAL, N, S, E, W
import pathlib
import json
import logging.config

############################################################################

#os.system("export DISPLAY=:0")
#os.system("xhost +")

OS = platform.system()

#logging.basicConfig(format='%(asctime)s %(message)s')
#logging.basicConfig('%(asctime)s - %(levelname)s - %(message)s')

logging.config.fileConfig("logging.conf")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
kt = logging.StreamHandler()
kt.setLevel(logging.DEBUG)

logpath = "/home/pi/kt/"

kt_hdlr = logging.FileHandler(logpath + 'myapp.log')
# create formatter
kt_hdlr.kt_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
kt.setFormatter(kt_hdlr.kt_formatter)
logger.addHandler(kt)

class Application(object):
	def __init__(self, parent):
		try:
			self.logpath = "/home/pi/kt/"
			kt_file_size = os.path.getsize("/home/pi/kt/log")
			logging.info ("kt_file_size ==> %s",kt_file_size)
			log_file = pathlib.Path(self.logpath + "log")
			if log_file.exists ():					
				readlogfile = open(self.logpath + "log","r+")

			self.parent = parent 
			self.canvas =  Canvas(self.parent, bg='white', width = 780, height = 320)
			self.mainFrame = Frame(self.canvas)
			self.scroll = Scrollbar(self.parent, orient = VERTICAL, command=self.canvas.yview)
			self.scroll.pack(side='right', fill='y')
			
			a = readlogfile.read()

			readlogfile.flush()
			readlogfile.close()

			text = Text(self.parent, height=27, width=107, wrap=WORD, yscrollcommand=self.scroll.set)
			text.insert(INSERT, a)	
			text.place(x=5,y=5)#.pack()	
			del a
			self.scroll.config(command=text.yview)		
		except Exception as e:
			errorstring = "/E-Application-init()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 				

class PotassiumPixelCounter(object):
	def __init__(self, imageName,pic_number):
		try:
			self.select_image_coordinates_potassium = "/home/pi/kt/npk-device-addon/"
			
			with open(self.select_image_coordinates_potassium+"kipcs.json") as equation_contents:
				pixel_data = json.load(equation_contents)		
				
			c1p1_left_pstart = pixel_data["1"]["topx"]
			c1p1_top_pstart = pixel_data["1"]["topy"]
			c1p1_right_pstart = pixel_data["1"]["botx"]
			c1p1_bottom_pstart = pixel_data["1"]["boty"]

			c1p2_left_pstart = pixel_data["2"]["topx"]
			c1p2_top_pstart = pixel_data["2"]["topy"]
			c1p2_right_pstart = pixel_data["2"]["botx"]
			c1p2_bottom_pstart = pixel_data["2"]["boty"]

			c1p3_left_pstart = pixel_data["3"]["topx"]
			c1p3_top_pstart = pixel_data["3"]["topy"]
			c1p3_right_pstart = pixel_data["3"]["botx"]
			c1p3_bottom_pstart = pixel_data["3"]["boty"]

			c1p4_left_pstart = pixel_data["4"]["topx"]
			c1p4_top_pstart = pixel_data["4"]["topy"]
			c1p4_right_pstart = pixel_data["4"]["botx"]
			c1p4_bottom_pstart = pixel_data["4"]["boty"]

			c1p5_left_pstart = pixel_data["5"]["topx"]
			c1p5_top_pstart = pixel_data["5"]["topy"]
			c1p5_right_pstart = pixel_data["5"]["botx"]
			c1p5_bottom_pstart = pixel_data["5"]["boty"]
    		
    		######################### 
    		
			c2p1_left_pstart = c1p1_left_pstart 
			c2p1_top_pstart = c1p1_top_pstart 
			c2p1_right_pstart = c1p1_right_pstart
			c2p1_bottom_pstart = c1p1_bottom_pstart

			c2p2_left_pstart = c1p2_left_pstart
			c2p2_top_pstart = c1p2_top_pstart
			c2p2_right_pstart = c1p2_right_pstart
			c2p2_bottom_pstart = c1p2_bottom_pstart

			c2p3_left_pstart = c1p3_left_pstart
			c2p3_top_pstart = c1p3_top_pstart
			c2p3_right_pstart = c1p3_right_pstart
			c2p3_bottom_pstart = c1p3_bottom_pstart

			c2p4_left_pstart = c1p4_left_pstart
			c2p4_top_pstart = c1p4_top_pstart
			c2p4_right_pstart = c1p4_right_pstart
			c2p4_bottom_pstart = c1p4_bottom_pstart

			c2p5_left_pstart = c1p5_left_pstart
			c2p5_top_pstart = c1p5_top_pstart
			c2p5_right_pstart = c1p5_right_pstart
			c2p5_bottom_pstart = c1p5_bottom_pstart    

			##########################

			c3p1_left_pstart = c1p1_left_pstart
			c3p1_top_pstart = c1p1_top_pstart
			c3p1_right_pstart = c1p1_right_pstart
			c3p1_bottom_pstart = c1p1_bottom_pstart

			c3p2_left_pstart = c1p2_left_pstart
			c3p2_top_pstart = c1p2_top_pstart
			c3p2_right_pstart = c1p2_right_pstart
			c3p2_bottom_pstart = c1p2_bottom_pstart

			c3p3_left_pstart = c1p3_left_pstart
			c3p3_top_pstart = c1p3_top_pstart
			c3p3_right_pstart = c1p3_right_pstart
			c3p3_bottom_pstart = c1p3_bottom_pstart

			c3p4_left_pstart = c1p4_left_pstart
			c3p4_top_pstart = c1p4_top_pstart
			c3p4_right_pstart = c1p4_right_pstart
			c3p4_bottom_pstart = c1p4_bottom_pstart

			c3p5_left_pstart = c1p5_left_pstart
			c3p5_top_pstart = c1p5_top_pstart
			c3p5_right_pstart = c1p5_right_pstart
			c3p5_bottom_pstart = c1p5_bottom_pstart  

			########################

			c4p1_left_pstart = c1p1_left_pstart
			c4p1_top_pstart = c1p1_top_pstart
			c4p1_right_pstart = c1p1_right_pstart
			c4p1_bottom_pstart = c1p1_bottom_pstart

			c4p2_left_pstart = c1p2_left_pstart
			c4p2_top_pstart = c1p2_top_pstart
			c4p2_right_pstart = c1p2_right_pstart
			c4p2_bottom_pstart = c1p2_bottom_pstart

			c4p3_left_pstart = c1p3_left_pstart
			c4p3_top_pstart = c1p3_top_pstart
			c4p3_right_pstart = c1p3_right_pstart
			c4p3_bottom_pstart = c1p3_bottom_pstart

			c4p4_left_pstart = c1p4_left_pstart
			c4p4_top_pstart = c1p4_top_pstart
			c4p4_right_pstart = c1p4_right_pstart
			c4p4_bottom_pstart = c1p4_bottom_pstart

			c4p5_left_pstart = c1p5_left_pstart
			c4p5_top_pstart = c1p5_top_pstart
			c4p5_right_pstart = c1p5_right_pstart
			c4p5_bottom_pstart = c1p5_bottom_pstart  

			######################## 

			c5p1_left_pstart = c1p1_left_pstart
			c5p1_top_pstart = c1p1_top_pstart
			c5p1_right_pstart = c1p1_right_pstart
			c5p1_bottom_pstart = c1p1_bottom_pstart

			c5p2_left_pstart = c1p2_left_pstart
			c5p2_top_pstart = c1p2_top_pstart
			c5p2_right_pstart = c1p2_right_pstart
			c5p2_bottom_pstart = c1p2_bottom_pstart

			c5p3_left_pstart = c1p3_left_pstart
			c5p3_top_pstart = c1p3_top_pstart
			c5p3_right_pstart = c1p3_right_pstart
			c5p3_bottom_pstart = c1p3_bottom_pstart

			c5p4_left_pstart = c1p4_left_pstart
			c5p4_top_pstart = c1p4_top_pstart
			c5p4_right_pstart = c1p4_right_pstart
			c5p4_bottom_pstart = c1p4_bottom_pstart

			c5p5_left_pstart = c1p5_left_pstart
			c5p5_top_pstart = c1p5_top_pstart
			c5p5_right_pstart = c1p5_right_pstart
			c5p5_bottom_pstart = c1p5_bottom_pstart         		      		      		     		      		        		        		

			self.c1p1left,self.c1p1top,self.c1p1right,self.c1p1bottom = c1p1_left_pstart,c1p1_top_pstart,c1p1_right_pstart,c1p1_bottom_pstart
			self.c1p2left,self.c1p2top,self.c1p2right,self.c1p2bottom = c1p2_left_pstart,c1p2_top_pstart,c1p2_right_pstart,c1p2_bottom_pstart
			self.c1p3left,self.c1p3top,self.c1p3right,self.c1p3bottom = c1p3_left_pstart,c1p3_top_pstart,c1p3_right_pstart,c1p3_bottom_pstart
			self.c1p4left,self.c1p4top,self.c1p4right,self.c1p4bottom = c1p4_left_pstart,c1p4_top_pstart,c1p4_right_pstart,c1p4_bottom_pstart
			self.c1p5left,self.c1p5top,self.c1p5right,self.c1p5bottom = c1p5_left_pstart,c1p5_top_pstart,c1p5_right_pstart,c1p5_bottom_pstart

			self.c2p1left,self.c2p1top,self.c2p1right,self.c2p1bottom = c2p1_left_pstart,c2p1_top_pstart,c2p1_right_pstart,c2p1_bottom_pstart
			self.c2p2left,self.c2p2top,self.c2p2right,self.c2p2bottom = c2p2_left_pstart,c2p2_top_pstart,c2p2_right_pstart,c2p2_bottom_pstart
			self.c2p3left,self.c2p3top,self.c2p3right,self.c2p3bottom = c2p3_left_pstart,c2p3_top_pstart,c2p3_right_pstart,c2p3_bottom_pstart
			self.c2p4left,self.c2p4top,self.c2p4right,self.c2p4bottom = c2p4_left_pstart,c2p4_top_pstart,c2p4_right_pstart,c2p4_bottom_pstart
			self.c2p5left,self.c2p5top,self.c2p5right,self.c2p5bottom = c2p5_left_pstart,c2p5_top_pstart,c2p5_right_pstart,c2p5_bottom_pstart

			self.c3p1left,self.c3p1top,self.c3p1right,self.c3p1bottom = c3p1_left_pstart,c3p1_top_pstart,c3p1_right_pstart,c3p1_bottom_pstart
			self.c3p2left,self.c3p2top,self.c3p2right,self.c3p2bottom = c3p2_left_pstart,c3p2_top_pstart,c3p2_right_pstart,c3p2_bottom_pstart
			self.c3p3left,self.c3p3top,self.c3p3right,self.c3p3bottom = c3p3_left_pstart,c3p3_top_pstart,c3p3_right_pstart,c3p3_bottom_pstart
			self.c3p4left,self.c3p4top,self.c3p4right,self.c3p4bottom = c3p4_left_pstart,c3p4_top_pstart,c3p4_right_pstart,c3p4_bottom_pstart
			self.c3p5left,self.c3p5top,self.c3p5right,self.c3p5bottom = c3p5_left_pstart,c3p5_top_pstart,c3p5_right_pstart,c3p5_bottom_pstart

			self.c4p1left,self.c4p1top,self.c4p1right,self.c4p1bottom = c4p1_left_pstart,c4p1_top_pstart,c4p1_right_pstart,c4p1_bottom_pstart
			self.c4p2left,self.c4p2top,self.c4p2right,self.c4p2bottom = c4p2_left_pstart,c4p2_top_pstart,c4p2_right_pstart,c4p2_bottom_pstart
			self.c4p3left,self.c4p3top,self.c4p3right,self.c4p3bottom = c4p3_left_pstart,c4p3_top_pstart,c4p3_right_pstart,c4p3_bottom_pstart
			self.c4p4left,self.c4p4top,self.c4p4right,self.c4p4bottom = c4p4_left_pstart,c4p4_top_pstart,c4p4_right_pstart,c4p4_bottom_pstart
			self.c4p5left,self.c4p5top,self.c4p5right,self.c4p5bottom = c4p5_left_pstart,c4p5_top_pstart,c4p5_right_pstart,c4p5_bottom_pstart

			self.c5p1left,self.c5p1top,self.c5p1right,self.c5p1bottom = c5p1_left_pstart,c5p1_top_pstart,c5p1_right_pstart,c5p1_bottom_pstart
			self.c5p2left,self.c5p2top,self.c5p2right,self.c5p2bottom = c5p2_left_pstart,c5p2_top_pstart,c5p2_right_pstart,c5p2_bottom_pstart
			self.c5p3left,self.c5p3top,self.c5p3right,self.c5p3bottom = c5p3_left_pstart,c5p3_top_pstart,c5p3_right_pstart,c5p3_bottom_pstart
			self.c5p4left,self.c5p4top,self.c5p4right,self.c5p4bottom = c5p4_left_pstart,c5p4_top_pstart,c5p4_right_pstart,c5p4_bottom_pstart
			self.c5p5left,self.c5p5top,self.c5p5right,self.c5p5bottom = c5p5_left_pstart,c5p5_top_pstart,c5p5_right_pstart,c5p5_bottom_pstart
    
			if pic_number == 1:
					self.pic1 = Image.open(imageName)
					self.width1, self.height1 = self.pic1.size   # Get dimensions

					self.left = self.width1/4
					self.top = self.height1/4
					self.right = 3 * self.width1/4
					self.bottom = 3 * self.height1/4

					self.pcroppedpic1_1 = self.pic1.crop((self.c1p1left,self.c1p1top,self.c1p1right,self.c1p1bottom))
					self.imgData1_1 = self.pcroppedpic1_1.load()

					self.pcroppedpic1_2 = self.pic1.crop((self.c1p2left,self.c1p2top,self.c1p2right,self.c1p2bottom))
					self.imgData1_2 = self.pcroppedpic1_2.load()  
							 
					self.pcroppedpic1_3 = self.pic1.crop((self.c1p3left,self.c1p3top,self.c1p3right,self.c1p3bottom))
					self.imgData1_3 = self.pcroppedpic1_3.load()
							 
					self.pcroppedpic1_4 = self.pic1.crop((self.c1p4left,self.c1p4top,self.c1p4right,self.c1p4bottom))
					self.imgData1_4 = self.pcroppedpic1_4.load()
							 
					self.pcroppedpic1_5 = self.pic1.crop((self.c1p5left,self.c1p5top,self.c1p5right,self.c1p5bottom))
					self.imgData1_5 = self.pcroppedpic1_5.load()                                  

			if pic_number == 2:
					self.pic2 = Image.open(imageName)
					self.width2, self.height2 = self.pic2.size   # Get dimensions

					self.left = self.width2/4
					self.top = self.height2/4
					self.right = 3 * self.width2/4
					self.bottom = 3 * self.height2/4

					self.croppedpic2_1 = self.pic2.crop((self.c2p1left,self.c2p1top,self.c2p1right,self.c2p1bottom))
					self.imgData2_1 = self.croppedpic2_1.load()

					self.croppedpic2_2 = self.pic2.crop((self.c2p2left,self.c2p2top,self.c2p2right,self.c2p2bottom ))
					self.imgData2_2 = self.croppedpic2_2.load()  

					self.croppedpic2_3 = self.pic2.crop((self.c2p3left,self.c2p3top,self.c2p3right,self.c2p3bottom ))
					self.imgData2_3 = self.croppedpic2_3.load()

					self.croppedpic2_4 = self.pic2.crop((self.c2p4left,self.c2p4top,self.c2p4right,self.c2p4bottom ))
					self.imgData2_4 = self.croppedpic2_4.load()

					self.croppedpic2_5 = self.pic2.crop((self.c2p5left,self.c2p5top,self.c2p5right,self.c2p5bottom ))
					self.imgData2_5 = self.croppedpic2_5.load()

			if pic_number == 3:
					self.pic3 = Image.open(imageName)
					self.width3, self.height3 = self.pic3.size   # Get dimensions

					self.left = self.width3/4
					self.top = self.height3/4
					self.right = 3 * self.width3/4
					self.bottom = 3 * self.height3/4

					self.croppedpic3_1 = self.pic3.crop((self.c3p1left,self.c3p1top,self.c3p1right,self.c3p1bottom ))
					self.imgData3_1 = self.croppedpic3_1.load()

					self.croppedpic3_2 = self.pic3.crop((self.c3p2left,self.c3p2top,self.c3p2right,self.c3p2bottom ))
					self.imgData3_2 = self.croppedpic3_2.load()  

					self.croppedpic3_3 = self.pic3.crop((self.c3p3left,self.c3p3top,self.c3p3right,self.c3p3bottom ))
					self.imgData3_3 = self.croppedpic3_3.load()

					self.croppedpic3_4 = self.pic3.crop((self.c3p4left,self.c3p4top,self.c3p4right,self.c3p4bottom ))
					self.imgData3_4 = self.croppedpic3_4.load()

					self.croppedpic3_5 = self.pic3.crop((self.c3p5left,self.c3p5top,self.c3p5right,self.c3p5bottom ))
					self.imgData3_5 = self.croppedpic3_5.load()

			if pic_number == 4:
					self.pic4 = Image.open(imageName)
					self.width4, self.height4 = self.pic4.size   # Get dimensions

					self.left = self.width4/4
					self.top = self.height4/4
					self.right = 3 * self.width4/4
					self.bottom = 3 * self.height4/4

					self.croppedpic4_1 = self.pic4.crop((self.c4p1left,self.c4p1top,self.c4p1right,self.c4p1bottom))
					self.imgData4_1 = self.croppedpic4_1.load()

					self.croppedpic4_2 = self.pic4.crop((self.c4p2left,self.c4p2top,self.c4p2right,self.c4p2bottom))
					self.imgData4_2 = self.croppedpic4_2.load()  

					self.croppedpic4_3 = self.pic4.crop((self.c4p3left,self.c4p3top,self.c4p3right,self.c4p3bottom))
					self.imgData4_3 = self.croppedpic4_3.load()

					self.croppedpic4_4 = self.pic4.crop((self.c4p4left,self.c4p4top,self.c4p4right,self.c4p4bottom))
					self.imgData4_4 = self.croppedpic4_4.load()

					self.croppedpic4_5 = self.pic4.crop((self.c4p5left,self.c4p5top,self.c4p5right,self.c4p5bottom))
					self.imgData4_5 = self.croppedpic4_5.load()

			if pic_number == 5:
					self.pic5 = Image.open(imageName)
					self.width5, self.height5 = self.pic5.size   # Get dimensions

					self.left = self.width5/4
					self.top = self.height5/4
					self.right = 3 * self.width5/4
					self.bottom = 3 * self.height5/4

					self.croppedpic5_1 = self.pic5.crop((self.c5p1left,self.c5p1top,self.c5p1right,self.c5p1bottom))
					self.imgData5_1 = self.croppedpic5_1.load()

					self.croppedpic5_2 = self.pic5.crop((self.c5p2left,self.c5p2top,self.c5p2right,self.c5p2bottom))
					self.imgData5_2 = self.croppedpic5_2.load()  

					self.croppedpic5_3 = self.pic5.crop((self.c5p3left,self.c5p3top,self.c5p3right,self.c5p3bottom))
					self.imgData5_3 = self.croppedpic5_3.load()

					self.croppedpic5_4 = self.pic5.crop((self.c5p4left,self.c5p4top,self.c5p4right,self.c5p4bottom))
					self.imgData5_4 = self.croppedpic5_4.load()

					self.croppedpic5_5 = self.pic5.crop((self.c5p5left,self.c5p5top,self.c5p5right,self.c5p5bottom))
					self.imgData5_5 = self.croppedpic5_5.load()
		except Exception as e:
			errorstring = "/E-PotassiumPixelCounter-init()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 
			
	def paveragePixels1(self):
		try:
			r, g, b = 0, 0, 0  
			r1_1, g1_1, b1_1 = 0, 0, 0
			r1_2, g1_2, b1_2 = 0, 0, 0
			r1_3, g1_3, b1_3 = 0, 0, 0
			r1_4, g1_4, b1_4 = 0, 0, 0
			r1_5, g1_5, b1_5 = 0, 0, 0
			count = 0
			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			count5 = 0
			for x in range(self.pcroppedpic1_1.size[0]):
			  for y in range(self.pcroppedpic1_1.size[1]):
			      tempr1,tempg1,tempb1,dummy = self.imgData1_1[x,y]
			      r1_1 += tempr1
			      g1_1 += tempg1
			      b1_1 += tempb1
			      count1 += 1
			      
			for x in range(self.pcroppedpic1_2.size[0]):
			  for y in range(self.pcroppedpic1_2.size[1]):
			      tempr2,tempg2,tempb2,dummy = self.imgData1_2[x,y]
			      r1_2 += tempr2
			      g1_2 += tempg2
			      b1_2 += tempb2
			      count2 += 1
			      
			for x in range(self.pcroppedpic1_3.size[0]):
			  for y in range(self.pcroppedpic1_3.size[1]):
			      tempr3,tempg3,tempb3,dummy = self.imgData1_3[x,y]
			      r1_3 += tempr3
			      g1_3 += tempg3
			      b1_3 += tempb3
			      count3 += 1
			      
			for x in range(self.pcroppedpic1_4.size[0]):
			  for y in range(self.pcroppedpic1_4.size[1]):
			      tempr4,tempg4,tempb4,dummy = self.imgData1_4[x,y]
			      r1_4 += tempr4
			      g1_4 += tempg4
			      b1_4 += tempb4
			      count4 += 1
			      
			for x in range(self.pcroppedpic1_5.size[0]):
			  for y in range(self.pcroppedpic1_5.size[1]):
			      tempr5,tempg5,tempb5,dummy = self.imgData1_5[x,y]
			      r1_5 += tempr5
			      g1_5 += tempg5
			      b1_5 += tempb5
			      count5 += 1                                 
			                             
			r = (r1_1 + r1_2 + r1_3 + r1_4 + r1_5) / 5
			g = (g1_1 + g1_2 + g1_3 + g1_4 + g1_5) / 5
			b = (b1_1 + b1_2 + b1_3 + b1_4 + b1_5) / 5
			count = (count1 + count2 + count3 + count4 + count5) / 5

			# calculate averages
			return (r/count), (g/count), (b/count), count
		except Exception as e:
			errorstring = "/E-PotassiumPixelCounter-averagePixels1()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 				

	def paveragePixels2(self):
		try:
			r, g, b = 0, 0, 0
			r2_1, g2_1, b2_1 = 0, 0, 0
			r2_2, g2_2, b2_2 = 0, 0, 0
			r2_3, g2_3, b2_3 = 0, 0, 0
			r2_4, g2_4, b2_4 = 0, 0, 0
			r2_5, g2_5, b2_5 = 0, 0, 0
			count = 0
			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			count5 = 0      

			for x in range(self.croppedpic2_1.size[0]):
			  for y in range(self.croppedpic2_1.size[1]):
			      tempr1,tempg1,tempb1,dummy = self.imgData2_1[x,y]
			      r2_1 += tempr1
			      g2_1 += tempg1
			      b2_1 += tempb1
			      count1 += 1
			      
			for x in range(self.croppedpic2_2.size[0]):
			  for y in range(self.croppedpic2_2.size[1]):
			      tempr2,tempg2,tempb2,dummy = self.imgData2_2[x,y]
			      r2_2 += tempr2
			      g2_2 += tempg2
			      b2_2 += tempb2
			      count2 += 1
			      
			for x in range(self.croppedpic2_3.size[0]):
			  for y in range(self.croppedpic2_3.size[1]):
			      tempr3,tempg3,tempb3,dummy = self.imgData2_3[x,y]
			      r2_3 += tempr3
			      g2_3 += tempg3
			      b2_3 += tempb3
			      count3 += 1
			      
			for x in range(self.croppedpic2_4.size[0]):
			  for y in range(self.croppedpic2_4.size[1]):
			      tempr4,tempg4,tempb4,dummy = self.imgData2_4[x,y]
			      r2_4 += tempr4
			      g2_4 += tempg4
			      b2_4 += tempb4
			      count4 += 1
			      
			for x in range(self.croppedpic2_5.size[0]):
			  for y in range(self.croppedpic2_5.size[1]):
			      tempr5,tempg5,tempb5,dummy = self.imgData2_5[x,y]
			      r2_5 += tempr5
			      g2_5 += tempg5
			      b2_5 += tempb5
			      count5 += 1                                 
			                             
			r = (r2_1 + r2_2 + r2_3 + r2_4 + r2_5) / 5
			g = (g2_1 + g2_2 + g2_3 + g2_4 + g2_5) / 5              
			b = (b2_1 + b2_2 + b2_3 + b2_4 + b2_5) / 5
			count = (count1 + count2 + count3 + count4 + count5) / 5
			      
			# calculate averages
			return (r/count), (g/count), (b/count), count
		except Exception as e:
			errorstring = "/E-PotassiumPixelCounter-averagePixels2()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 				

	def paveragePixels3(self):
		try:
			r, g, b = 0, 0, 0
			r3_1, g3_1, b3_1 = 0, 0, 0
			r3_2, g3_2, b3_2 = 0, 0, 0
			r3_3, g3_3, b3_3 = 0, 0, 0
			r3_4, g3_4, b3_4 = 0, 0, 0
			r3_5, g3_5, b3_5 = 0, 0, 0
			count = 0
			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			count5 = 0      

			for x in range(self.croppedpic3_1.size[0]):
			  for y in range(self.croppedpic3_1.size[1]):
			      tempr1,tempg1,tempb1,dummy = self.imgData3_1[x,y]
			      r3_1 += tempr1
			      g3_1 += tempg1
			      b3_1 += tempb1
			      count1 += 1
			      
			for x in range(self.croppedpic3_2.size[0]):
			  for y in range(self.croppedpic3_2.size[1]):
			      tempr2,tempg2,tempb2,dummy = self.imgData3_2[x,y]
			      r3_2 += tempr2
			      g3_2 += tempg2
			      b3_2 += tempb2
			      count2 += 1
			      
			for x in range(self.croppedpic3_3.size[0]):
			  for y in range(self.croppedpic3_3.size[1]):
			      tempr3,tempg3,tempb3,dummy = self.imgData3_3[x,y]
			      r3_3 += tempr3
			      g3_3 += tempg3
			      b3_3 += tempb3
			      count3 += 1
			      
			for x in range(self.croppedpic3_4.size[0]):
			  for y in range(self.croppedpic3_4.size[1]):
			      tempr4,tempg4,tempb4,dummy = self.imgData3_4[x,y]
			      r3_4 += tempr4
			      g3_4 += tempg4
			      b3_4 += tempb4
			      count4 += 1
			      
			for x in range(self.croppedpic3_5.size[0]):
			  for y in range(self.croppedpic3_5.size[1]):
			      tempr5,tempg5,tempb5,dummy = self.imgData3_5[x,y]
			      r3_5 += tempr5
			      g3_5 += tempg5
			      b3_5 += tempb5
			      count5 += 1                                 
			                             
			r = (r3_1 + r3_2 + r3_3 + r3_4 + r3_5) / 5
			g = (g3_1 + g3_2 + g3_3 + g3_4 + g3_5) / 5              
			b = (b3_1 + b3_2 + b3_3 + b3_4 + b3_5) / 5
			count = (count1 + count2 + count3 + count4 + count5) / 5
			      
			# calculate averages
			return (r/count), (g/count), (b/count), count
		except Exception as e:
			errorstring = "/E-PotassiumPixelCounter-averagePixels3()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 				

	def paveragePixels4(self):
		try:
			r, g, b = 0, 0, 0
			r4_1, g4_1, b4_1 = 0, 0, 0
			r4_2, g4_2, b4_2 = 0, 0, 0
			r4_3, g4_3, b4_3 = 0, 0, 0
			r4_4, g4_4, b4_4 = 0, 0, 0
			r4_5, g4_5, b4_5 = 0, 0, 0
			count = 0
			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			count5 = 0      

			for x in range(self.croppedpic4_1.size[0]):
			  for y in range(self.croppedpic4_1.size[1]):
			      tempr1,tempg1,tempb1,dummy = self.imgData4_1[x,y]
			      r4_1 += tempr1
			      g4_1 += tempg1
			      b4_1 += tempb1
			      count1 += 1
			      
			for x in range(self.croppedpic4_2.size[0]):
			  for y in range(self.croppedpic4_2.size[1]):
			      tempr2,tempg2,tempb2,dummy = self.imgData4_2[x,y]
			      r4_2 += tempr2
			      g4_2 += tempg2
			      b4_2 += tempb2
			      count2 += 1
			      
			for x in range(self.croppedpic4_3.size[0]):
			  for y in range(self.croppedpic4_3.size[1]):
			      tempr3,tempg3,tempb3,dummy = self.imgData4_3[x,y]
			      r4_3 += tempr3
			      g4_3 += tempg3
			      b4_3 += tempb3
			      count3 += 1
			      
			for x in range(self.croppedpic4_4.size[0]):
			  for y in range(self.croppedpic4_4.size[1]):
			      tempr4,tempg4,tempb4,dummy = self.imgData4_4[x,y]
			      r4_4 += tempr4
			      g4_4 += tempg4
			      b4_4 += tempb4
			      count4 += 1
			      
			for x in range(self.croppedpic4_5.size[0]):
			  for y in range(self.croppedpic4_5.size[1]):
			      tempr5,tempg5,tempb5,dummy = self.imgData4_5[x,y]
			      r4_5 += tempr5
			      g4_5 += tempg5
			      b4_5 += tempb5
			      count5 += 1                                 
			                             
			r = (r4_1 + r4_2 + r4_3 + r4_4 + r4_5) / 5
			g = (g4_1 + g4_2 + g4_3 + g4_4 + g4_5) / 5              
			b = (b4_1 + b4_2 + b4_3 + b4_4 + b4_5) / 5
			count = (count1 + count2 + count3 + count4 + count5) / 5
			            
			# calculate averages
			return (r/count), (g/count), (b/count), count
		except Exception as e:
			errorstring = "/E-PotassiumPixelCounter-averagePixels4()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 				

	def paveragePixels5(self):
		try:
			r, g, b = 0, 0, 0
			r5_1, g5_1, b5_1 = 0, 0, 0
			r5_2, g5_2, b5_2 = 0, 0, 0
			r5_3, g5_3, b5_3 = 0, 0, 0
			r5_4, g5_4, b5_4 = 0, 0, 0
			r5_5, g5_5, b5_5 = 0, 0, 0
			count = 0
			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			count5 = 0        

			for x in range(self.croppedpic5_1.size[0]):
			  for y in range(self.croppedpic5_1.size[1]):
			      tempr1,tempg1,tempb1,dummy = self.imgData5_1[x,y]
			      r5_1 += tempr1
			      g5_1 += tempg1
			      b5_1 += tempb1
			      count1 += 1
			      
			for x in range(self.croppedpic5_2.size[0]):
			  for y in range(self.croppedpic5_2.size[1]):
			      tempr2,tempg2,tempb2,dummy = self.imgData5_2[x,y]
			      r5_2 += tempr2
			      g5_2 += tempg2
			      b5_2 += tempb2
			      count2 += 1
			      
			for x in range(self.croppedpic5_3.size[0]):
			  for y in range(self.croppedpic5_3.size[1]):
			      tempr3,tempg3,tempb3,dummy = self.imgData5_3[x,y]
			      r5_3 += tempr3
			      g5_3 += tempg3
			      b5_3 += tempb3
			      count3 += 1
			      
			for x in range(self.croppedpic5_4.size[0]):
			  for y in range(self.croppedpic5_4.size[1]):
			      tempr4,tempg4,tempb4,dummy = self.imgData5_4[x,y]
			      r5_4 += tempr4
			      g5_4 += tempg4
			      b5_4 += tempb4
			      count4 += 1
			      
			for x in range(self.croppedpic5_5.size[0]):
			  for y in range(self.croppedpic5_5.size[1]):
			      tempr5,tempg5,tempb5,dummy = self.imgData5_5[x,y]
			      r5_5 += tempr5
			      g5_5 += tempg5
			      b5_5 += tempb5
			      count5 += 1                                 
			                             
			r = (r5_1 + r5_2 + r5_3 + r5_4 + r5_5) / 5
			g = (g5_1 + g5_2 + g5_3 + g5_4 + g5_5) / 5              
			b = (b5_1 + b5_2 + b5_3 + b5_4 + b5_5) / 5
			count = (count1 + count2 + count3 + count4 + count5) / 5
			            
			# calculate averages
			return (r/count), (g/count), (b/count), count
		except Exception as e:
			errorstring = "/E-PotassiumPixelCounter-averagePixels5()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 									

class PixelCounter(object):
	def __init__(self, imageName,pic_number):
		try:
			self.select_image_coordinates = "/home/pi/kt/npk-device-addon/"
			
			with open(self.select_image_coordinates+"ipcs.json") as equation_contents:
				pixel_data = json.load(equation_contents)		
				
			c1p1_left_pstart = pixel_data["1"]["topx"]
			c1p1_top_pstart = pixel_data["1"]["topy"]
			c1p1_right_pstart = pixel_data["1"]["botx"]
			c1p1_bottom_pstart = pixel_data["1"]["boty"]

			c1p2_left_pstart = pixel_data["2"]["topx"]
			c1p2_top_pstart = pixel_data["2"]["topy"]
			c1p2_right_pstart = pixel_data["2"]["botx"]
			c1p2_bottom_pstart = pixel_data["2"]["boty"]

			c1p3_left_pstart = pixel_data["3"]["topx"]
			c1p3_top_pstart = pixel_data["3"]["topy"]
			c1p3_right_pstart = pixel_data["3"]["botx"]
			c1p3_bottom_pstart = pixel_data["3"]["boty"]

			c1p4_left_pstart = pixel_data["4"]["topx"]
			c1p4_top_pstart = pixel_data["4"]["topy"]
			c1p4_right_pstart = pixel_data["4"]["botx"]
			c1p4_bottom_pstart = pixel_data["4"]["boty"]

			c1p5_left_pstart = pixel_data["5"]["topx"]
			c1p5_top_pstart = pixel_data["5"]["topy"]
			c1p5_right_pstart = pixel_data["5"]["botx"]
			c1p5_bottom_pstart = pixel_data["5"]["boty"]
    		
    		######################### 
    		
			c2p1_left_pstart = c1p1_left_pstart 
			c2p1_top_pstart = c1p1_top_pstart 
			c2p1_right_pstart = c1p1_right_pstart
			c2p1_bottom_pstart = c1p1_bottom_pstart

			c2p2_left_pstart = c1p2_left_pstart
			c2p2_top_pstart = c1p2_top_pstart
			c2p2_right_pstart = c1p2_right_pstart
			c2p2_bottom_pstart = c1p2_bottom_pstart

			c2p3_left_pstart = c1p3_left_pstart
			c2p3_top_pstart = c1p3_top_pstart
			c2p3_right_pstart = c1p3_right_pstart
			c2p3_bottom_pstart = c1p3_bottom_pstart

			c2p4_left_pstart = c1p4_left_pstart
			c2p4_top_pstart = c1p4_top_pstart
			c2p4_right_pstart = c1p4_right_pstart
			c2p4_bottom_pstart = c1p4_bottom_pstart

			c2p5_left_pstart = c1p5_left_pstart
			c2p5_top_pstart = c1p5_top_pstart
			c2p5_right_pstart = c1p5_right_pstart
			c2p5_bottom_pstart = c1p5_bottom_pstart    

			##########################

			c3p1_left_pstart = c1p1_left_pstart
			c3p1_top_pstart = c1p1_top_pstart
			c3p1_right_pstart = c1p1_right_pstart
			c3p1_bottom_pstart = c1p1_bottom_pstart

			c3p2_left_pstart = c1p2_left_pstart
			c3p2_top_pstart = c1p2_top_pstart
			c3p2_right_pstart = c1p2_right_pstart
			c3p2_bottom_pstart = c1p2_bottom_pstart

			c3p3_left_pstart = c1p3_left_pstart
			c3p3_top_pstart = c1p3_top_pstart
			c3p3_right_pstart = c1p3_right_pstart
			c3p3_bottom_pstart = c1p3_bottom_pstart

			c3p4_left_pstart = c1p4_left_pstart
			c3p4_top_pstart = c1p4_top_pstart
			c3p4_right_pstart = c1p4_right_pstart
			c3p4_bottom_pstart = c1p4_bottom_pstart

			c3p5_left_pstart = c1p5_left_pstart
			c3p5_top_pstart = c1p5_top_pstart
			c3p5_right_pstart = c1p5_right_pstart
			c3p5_bottom_pstart = c1p5_bottom_pstart  

			########################

			c4p1_left_pstart = c1p1_left_pstart
			c4p1_top_pstart = c1p1_top_pstart
			c4p1_right_pstart = c1p1_right_pstart
			c4p1_bottom_pstart = c1p1_bottom_pstart

			c4p2_left_pstart = c1p2_left_pstart
			c4p2_top_pstart = c1p2_top_pstart
			c4p2_right_pstart = c1p2_right_pstart
			c4p2_bottom_pstart = c1p2_bottom_pstart

			c4p3_left_pstart = c1p3_left_pstart
			c4p3_top_pstart = c1p3_top_pstart
			c4p3_right_pstart = c1p3_right_pstart
			c4p3_bottom_pstart = c1p3_bottom_pstart

			c4p4_left_pstart = c1p4_left_pstart
			c4p4_top_pstart = c1p4_top_pstart
			c4p4_right_pstart = c1p4_right_pstart
			c4p4_bottom_pstart = c1p4_bottom_pstart

			c4p5_left_pstart = c1p5_left_pstart
			c4p5_top_pstart = c1p5_top_pstart
			c4p5_right_pstart = c1p5_right_pstart
			c4p5_bottom_pstart = c1p5_bottom_pstart  

			######################## 

			c5p1_left_pstart = c1p1_left_pstart
			c5p1_top_pstart = c1p1_top_pstart
			c5p1_right_pstart = c1p1_right_pstart
			c5p1_bottom_pstart = c1p1_bottom_pstart

			c5p2_left_pstart = c1p2_left_pstart
			c5p2_top_pstart = c1p2_top_pstart
			c5p2_right_pstart = c1p2_right_pstart
			c5p2_bottom_pstart = c1p2_bottom_pstart

			c5p3_left_pstart = c1p3_left_pstart
			c5p3_top_pstart = c1p3_top_pstart
			c5p3_right_pstart = c1p3_right_pstart
			c5p3_bottom_pstart = c1p3_bottom_pstart

			c5p4_left_pstart = c1p4_left_pstart
			c5p4_top_pstart = c1p4_top_pstart
			c5p4_right_pstart = c1p4_right_pstart
			c5p4_bottom_pstart = c1p4_bottom_pstart

			c5p5_left_pstart = c1p5_left_pstart
			c5p5_top_pstart = c1p5_top_pstart
			c5p5_right_pstart = c1p5_right_pstart
			c5p5_bottom_pstart = c1p5_bottom_pstart         		      		      		     		      		        		        		

			self.c1p1left,self.c1p1top,self.c1p1right,self.c1p1bottom = c1p1_left_pstart,c1p1_top_pstart,c1p1_right_pstart,c1p1_bottom_pstart
			self.c1p2left,self.c1p2top,self.c1p2right,self.c1p2bottom = c1p2_left_pstart,c1p2_top_pstart,c1p2_right_pstart,c1p2_bottom_pstart
			self.c1p3left,self.c1p3top,self.c1p3right,self.c1p3bottom = c1p3_left_pstart,c1p3_top_pstart,c1p3_right_pstart,c1p3_bottom_pstart
			self.c1p4left,self.c1p4top,self.c1p4right,self.c1p4bottom = c1p4_left_pstart,c1p4_top_pstart,c1p4_right_pstart,c1p4_bottom_pstart
			self.c1p5left,self.c1p5top,self.c1p5right,self.c1p5bottom = c1p5_left_pstart,c1p5_top_pstart,c1p5_right_pstart,c1p5_bottom_pstart

			self.c2p1left,self.c2p1top,self.c2p1right,self.c2p1bottom = c2p1_left_pstart,c2p1_top_pstart,c2p1_right_pstart,c2p1_bottom_pstart
			self.c2p2left,self.c2p2top,self.c2p2right,self.c2p2bottom = c2p2_left_pstart,c2p2_top_pstart,c2p2_right_pstart,c2p2_bottom_pstart
			self.c2p3left,self.c2p3top,self.c2p3right,self.c2p3bottom = c2p3_left_pstart,c2p3_top_pstart,c2p3_right_pstart,c2p3_bottom_pstart
			self.c2p4left,self.c2p4top,self.c2p4right,self.c2p4bottom = c2p4_left_pstart,c2p4_top_pstart,c2p4_right_pstart,c2p4_bottom_pstart
			self.c2p5left,self.c2p5top,self.c2p5right,self.c2p5bottom = c2p5_left_pstart,c2p5_top_pstart,c2p5_right_pstart,c2p5_bottom_pstart

			self.c3p1left,self.c3p1top,self.c3p1right,self.c3p1bottom = c3p1_left_pstart,c3p1_top_pstart,c3p1_right_pstart,c3p1_bottom_pstart
			self.c3p2left,self.c3p2top,self.c3p2right,self.c3p2bottom = c3p2_left_pstart,c3p2_top_pstart,c3p2_right_pstart,c3p2_bottom_pstart
			self.c3p3left,self.c3p3top,self.c3p3right,self.c3p3bottom = c3p3_left_pstart,c3p3_top_pstart,c3p3_right_pstart,c3p3_bottom_pstart
			self.c3p4left,self.c3p4top,self.c3p4right,self.c3p4bottom = c3p4_left_pstart,c3p4_top_pstart,c3p4_right_pstart,c3p4_bottom_pstart
			self.c3p5left,self.c3p5top,self.c3p5right,self.c3p5bottom = c3p5_left_pstart,c3p5_top_pstart,c3p5_right_pstart,c3p5_bottom_pstart

			self.c4p1left,self.c4p1top,self.c4p1right,self.c4p1bottom = c4p1_left_pstart,c4p1_top_pstart,c4p1_right_pstart,c4p1_bottom_pstart
			self.c4p2left,self.c4p2top,self.c4p2right,self.c4p2bottom = c4p2_left_pstart,c4p2_top_pstart,c4p2_right_pstart,c4p2_bottom_pstart
			self.c4p3left,self.c4p3top,self.c4p3right,self.c4p3bottom = c4p3_left_pstart,c4p3_top_pstart,c4p3_right_pstart,c4p3_bottom_pstart
			self.c4p4left,self.c4p4top,self.c4p4right,self.c4p4bottom = c4p4_left_pstart,c4p4_top_pstart,c4p4_right_pstart,c4p4_bottom_pstart
			self.c4p5left,self.c4p5top,self.c4p5right,self.c4p5bottom = c4p5_left_pstart,c4p5_top_pstart,c4p5_right_pstart,c4p5_bottom_pstart

			self.c5p1left,self.c5p1top,self.c5p1right,self.c5p1bottom = c5p1_left_pstart,c5p1_top_pstart,c5p1_right_pstart,c5p1_bottom_pstart
			self.c5p2left,self.c5p2top,self.c5p2right,self.c5p2bottom = c5p2_left_pstart,c5p2_top_pstart,c5p2_right_pstart,c5p2_bottom_pstart
			self.c5p3left,self.c5p3top,self.c5p3right,self.c5p3bottom = c5p3_left_pstart,c5p3_top_pstart,c5p3_right_pstart,c5p3_bottom_pstart
			self.c5p4left,self.c5p4top,self.c5p4right,self.c5p4bottom = c5p4_left_pstart,c5p4_top_pstart,c5p4_right_pstart,c5p4_bottom_pstart
			self.c5p5left,self.c5p5top,self.c5p5right,self.c5p5bottom = c5p5_left_pstart,c5p5_top_pstart,c5p5_right_pstart,c5p5_bottom_pstart
    
			if pic_number == 1:
					self.pic1 = Image.open(imageName)
					self.width1, self.height1 = self.pic1.size   # Get dimensions

					self.left = self.width1/4
					self.top = self.height1/4
					self.right = 3 * self.width1/4
					self.bottom = 3 * self.height1/4

					self.croppedpic1_1 = self.pic1.crop((self.c1p1left,self.c1p1top,self.c1p1right,self.c1p1bottom))
					self.imgData1_1 = self.croppedpic1_1.load()

					self.croppedpic1_2 = self.pic1.crop((self.c1p2left,self.c1p2top,self.c1p2right,self.c1p2bottom))
					self.imgData1_2 = self.croppedpic1_2.load()  
							 
					self.croppedpic1_3 = self.pic1.crop((self.c1p3left,self.c1p3top,self.c1p3right,self.c1p3bottom))
					self.imgData1_3 = self.croppedpic1_3.load()
							 
					self.croppedpic1_4 = self.pic1.crop((self.c1p4left,self.c1p4top,self.c1p4right,self.c1p4bottom))
					self.imgData1_4 = self.croppedpic1_4.load()
							 
					self.croppedpic1_5 = self.pic1.crop((self.c1p5left,self.c1p5top,self.c1p5right,self.c1p5bottom))
					self.imgData1_5 = self.croppedpic1_5.load()                                  

			if pic_number == 2:
					self.pic2 = Image.open(imageName)
					self.width2, self.height2 = self.pic2.size   # Get dimensions
					self.left = self.width2/4
					self.top = self.height2/4
					self.right = 3 * self.width2/4
					self.bottom = 3 * self.height2/4

					self.croppedpic2_1 = self.pic2.crop((self.c2p1left,self.c2p1top,self.c2p1right,self.c2p1bottom))
					self.imgData2_1 = self.croppedpic2_1.load()

					self.croppedpic2_2 = self.pic2.crop((self.c2p2left,self.c2p2top,self.c2p2right,self.c2p2bottom ))
					self.imgData2_2 = self.croppedpic2_2.load()  

					self.croppedpic2_3 = self.pic2.crop((self.c2p3left,self.c2p3top,self.c2p3right,self.c2p3bottom ))
					self.imgData2_3 = self.croppedpic2_3.load()

					self.croppedpic2_4 = self.pic2.crop((self.c2p4left,self.c2p4top,self.c2p4right,self.c2p4bottom ))
					self.imgData2_4 = self.croppedpic2_4.load()

					self.croppedpic2_5 = self.pic2.crop((self.c2p5left,self.c2p5top,self.c2p5right,self.c2p5bottom ))
					self.imgData2_5 = self.croppedpic2_5.load()

			if pic_number == 3:
					self.pic3 = Image.open(imageName)
					self.width3, self.height3 = self.pic3.size   # Get dimensions

					self.left = self.width3/4
					self.top = self.height3/4
					self.right = 3 * self.width3/4
					self.bottom = 3 * self.height3/4

					self.croppedpic3_1 = self.pic3.crop((self.c3p1left,self.c3p1top,self.c3p1right,self.c3p1bottom ))
					self.imgData3_1 = self.croppedpic3_1.load()

					self.croppedpic3_2 = self.pic3.crop((self.c3p2left,self.c3p2top,self.c3p2right,self.c3p2bottom ))
					self.imgData3_2 = self.croppedpic3_2.load()  

					self.croppedpic3_3 = self.pic3.crop((self.c3p3left,self.c3p3top,self.c3p3right,self.c3p3bottom ))
					self.imgData3_3 = self.croppedpic3_3.load()

					self.croppedpic3_4 = self.pic3.crop((self.c3p4left,self.c3p4top,self.c3p4right,self.c3p4bottom ))
					self.imgData3_4 = self.croppedpic3_4.load()

					self.croppedpic3_5 = self.pic3.crop((self.c3p5left,self.c3p5top,self.c3p5right,self.c3p5bottom ))
					self.imgData3_5 = self.croppedpic3_5.load()

			if pic_number == 4:
					self.pic4 = Image.open(imageName)
					self.width4, self.height4 = self.pic4.size   # Get dimensions

					self.left = self.width4/4
					self.top = self.height4/4
					self.right = 3 * self.width4/4
					self.bottom = 3 * self.height4/4

					self.croppedpic4_1 = self.pic4.crop((self.c4p1left,self.c4p1top,self.c4p1right,self.c4p1bottom))
					self.imgData4_1 = self.croppedpic4_1.load()

					self.croppedpic4_2 = self.pic4.crop((self.c4p2left,self.c4p2top,self.c4p2right,self.c4p2bottom))
					self.imgData4_2 = self.croppedpic4_2.load()  

					self.croppedpic4_3 = self.pic4.crop((self.c4p3left,self.c4p3top,self.c4p3right,self.c4p3bottom))
					self.imgData4_3 = self.croppedpic4_3.load()

					self.croppedpic4_4 = self.pic4.crop((self.c4p4left,self.c4p4top,self.c4p4right,self.c4p4bottom))
					self.imgData4_4 = self.croppedpic4_4.load()

					self.croppedpic4_5 = self.pic4.crop((self.c4p5left,self.c4p5top,self.c4p5right,self.c4p5bottom))
					self.imgData4_5 = self.croppedpic4_5.load()

			if pic_number == 5:
					self.pic5 = Image.open(imageName)
					self.width5, self.height5 = self.pic5.size   # Get dimensions

					self.left = self.width5/4
					self.top = self.height5/4
					self.right = 3 * self.width5/4
					self.bottom = 3 * self.height5/4

					self.croppedpic5_1 = self.pic5.crop((self.c5p1left,self.c5p1top,self.c5p1right,self.c5p1bottom))
					self.imgData5_1 = self.croppedpic5_1.load()

					self.croppedpic5_2 = self.pic5.crop((self.c5p2left,self.c5p2top,self.c5p2right,self.c5p2bottom))
					self.imgData5_2 = self.croppedpic5_2.load()  

					self.croppedpic5_3 = self.pic5.crop((self.c5p3left,self.c5p3top,self.c5p3right,self.c5p3bottom))
					self.imgData5_3 = self.croppedpic5_3.load()

					self.croppedpic5_4 = self.pic5.crop((self.c5p4left,self.c5p4top,self.c5p4right,self.c5p4bottom))
					self.imgData5_4 = self.croppedpic5_4.load()

					self.croppedpic5_5 = self.pic5.crop((self.c5p5left,self.c5p5top,self.c5p5right,self.c5p5bottom))
					self.imgData5_5 = self.croppedpic5_5.load()
		except Exception as e:
			errorstring = "/E-PixelCounter-init()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 						

	def averagePixels1(self):
		try:
			r, g, b = 0, 0, 0  
			r1_1, g1_1, b1_1 = 0, 0, 0
			r1_2, g1_2, b1_2 = 0, 0, 0
			r1_3, g1_3, b1_3 = 0, 0, 0
			r1_4, g1_4, b1_4 = 0, 0, 0
			r1_5, g1_5, b1_5 = 0, 0, 0
			count = 0
			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			count5 = 0
			for x in range(self.croppedpic1_1.size[0]):
				for y in range(self.croppedpic1_1.size[1]):
					tempr1,tempg1,tempb1,dummy = self.imgData1_1[x,y]
					r1_1 += tempr1
					g1_1 += tempg1
					b1_1 += tempb1
					count1 += 1
				  
			for x in range(self.croppedpic1_2.size[0]):
				for y in range(self.croppedpic1_2.size[1]):
					tempr2,tempg2,tempb2,dummy = self.imgData1_2[x,y]
					r1_2 += tempr2
					g1_2 += tempg2
					b1_2 += tempb2
					count2 += 1
				  
			for x in range(self.croppedpic1_3.size[0]):
				for y in range(self.croppedpic1_3.size[1]):
					tempr3,tempg3,tempb3,dummy = self.imgData1_3[x,y]
					r1_3 += tempr3
					g1_3 += tempg3
					b1_3 += tempb3
					count3 += 1
				  
			for x in range(self.croppedpic1_4.size[0]):
				for y in range(self.croppedpic1_4.size[1]):
					tempr4,tempg4,tempb4,dummy = self.imgData1_4[x,y]
					r1_4 += tempr4
					g1_4 += tempg4
					b1_4 += tempb4
					count4 += 1
				  
			for x in range(self.croppedpic1_5.size[0]):
				for y in range(self.croppedpic1_5.size[1]):
					tempr5,tempg5,tempb5,dummy = self.imgData1_5[x,y]
					r1_5 += tempr5
					g1_5 += tempg5
					b1_5 += tempb5
					count5 += 1                                 
								         
			r = (r1_1 + r1_2 + r1_3 + r1_4 + r1_5) / 5
			g = (g1_1 + g1_2 + g1_3 + g1_4 + g1_5) / 5
			b = (b1_1 + b1_2 + b1_3 + b1_4 + b1_5) / 5
			count = (count1 + count2 + count3 + count4 + count5) / 5

			# calculate averages
			return (r/count), (g/count), (b/count), count
		except Exception as e:
			errorstring = "/E-PixelCounter-averagePixels1()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 				

	def averagePixels2(self):
		try:
			r, g, b = 0, 0, 0
			r2_1, g2_1, b2_1 = 0, 0, 0
			r2_2, g2_2, b2_2 = 0, 0, 0
			r2_3, g2_3, b2_3 = 0, 0, 0
			r2_4, g2_4, b2_4 = 0, 0, 0
			r2_5, g2_5, b2_5 = 0, 0, 0
			count = 0
			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			count5 = 0      

			for x in range(self.croppedpic2_1.size[0]):
				for y in range(self.croppedpic2_1.size[1]):
					tempr1,tempg1,tempb1,dummy = self.imgData2_1[x,y]
					r2_1 += tempr1
					g2_1 += tempg1
					b2_1 += tempb1
					count1 += 1
				  
			for x in range(self.croppedpic2_2.size[0]):
				for y in range(self.croppedpic2_2.size[1]):
					tempr2,tempg2,tempb2,dummy = self.imgData2_2[x,y]
					r2_2 += tempr2
					g2_2 += tempg2
					b2_2 += tempb2
					count2 += 1
				  
			for x in range(self.croppedpic2_3.size[0]):
				for y in range(self.croppedpic2_3.size[1]):
					tempr3,tempg3,tempb3,dummy = self.imgData2_3[x,y]
					r2_3 += tempr3
					g2_3 += tempg3
					b2_3 += tempb3
					count3 += 1
				  
			for x in range(self.croppedpic2_4.size[0]):
				for y in range(self.croppedpic2_4.size[1]):
					tempr4,tempg4,tempb4,dummy = self.imgData2_4[x,y]
					r2_4 += tempr4
					g2_4 += tempg4
					b2_4 += tempb4
					count4 += 1
				  
			for x in range(self.croppedpic2_5.size[0]):
				for y in range(self.croppedpic2_5.size[1]):
					tempr5,tempg5,tempb5,dummy = self.imgData2_5[x,y]
					r2_5 += tempr5
					g2_5 += tempg5
					b2_5 += tempb5
					count5 += 1                                 
									     
			r = (r2_1 + r2_2 + r2_3 + r2_4 + r2_5) / 5
			g = (g2_1 + g2_2 + g2_3 + g2_4 + g2_5) / 5              
			b = (b2_1 + b2_2 + b2_3 + b2_4 + b2_5) / 5
			count = (count1 + count2 + count3 + count4 + count5) / 5
				  
			# calculate averages
			return (r/count), (g/count), (b/count), count
		except Exception as e:
			errorstring = "/E-PixelCounter-averagePixels2()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 				

	def averagePixels3(self):
		try:
			r, g, b = 0, 0, 0
			r3_1, g3_1, b3_1 = 0, 0, 0
			r3_2, g3_2, b3_2 = 0, 0, 0
			r3_3, g3_3, b3_3 = 0, 0, 0
			r3_4, g3_4, b3_4 = 0, 0, 0
			r3_5, g3_5, b3_5 = 0, 0, 0
			count = 0
			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			count5 = 0      

			for x in range(self.croppedpic3_1.size[0]):
			  for y in range(self.croppedpic3_1.size[1]):
			      tempr1,tempg1,tempb1,dummy = self.imgData3_1[x,y]
			      r3_1 += tempr1
			      g3_1 += tempg1
			      b3_1 += tempb1
			      count1 += 1
			      
			for x in range(self.croppedpic3_2.size[0]):
			  for y in range(self.croppedpic3_2.size[1]):
			      tempr2,tempg2,tempb2,dummy = self.imgData3_2[x,y]
			      r3_2 += tempr2
			      g3_2 += tempg2
			      b3_2 += tempb2
			      count2 += 1
			      
			for x in range(self.croppedpic3_3.size[0]):
			  for y in range(self.croppedpic3_3.size[1]):
			      tempr3,tempg3,tempb3,dummy = self.imgData3_3[x,y]
			      r3_3 += tempr3
			      g3_3 += tempg3
			      b3_3 += tempb3
			      count3 += 1
			      
			for x in range(self.croppedpic3_4.size[0]):
			  for y in range(self.croppedpic3_4.size[1]):
			      tempr4,tempg4,tempb4,dummy = self.imgData3_4[x,y]
			      r3_4 += tempr4
			      g3_4 += tempg4
			      b3_4 += tempb4
			      count4 += 1
			      
			for x in range(self.croppedpic3_5.size[0]):
			  for y in range(self.croppedpic3_5.size[1]):
			      tempr5,tempg5,tempb5,dummy = self.imgData3_5[x,y]
			      r3_5 += tempr5
			      g3_5 += tempg5
			      b3_5 += tempb5
			      count5 += 1                                 
			                             
			r = (r3_1 + r3_2 + r3_3 + r3_4 + r3_5) / 5
			g = (g3_1 + g3_2 + g3_3 + g3_4 + g3_5) / 5              
			b = (b3_1 + b3_2 + b3_3 + b3_4 + b3_5) / 5
			count = (count1 + count2 + count3 + count4 + count5) / 5
			      
			# calculate averages
			return (r/count), (g/count), (b/count), count
		except Exception as e:
			errorstring = "/E-PixelCounter-averagePixels3()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 				

	def averagePixels4(self):
		try:
			r, g, b = 0, 0, 0
			r4_1, g4_1, b4_1 = 0, 0, 0
			r4_2, g4_2, b4_2 = 0, 0, 0
			r4_3, g4_3, b4_3 = 0, 0, 0
			r4_4, g4_4, b4_4 = 0, 0, 0
			r4_5, g4_5, b4_5 = 0, 0, 0
			count = 0
			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			count5 = 0      

			for x in range(self.croppedpic4_1.size[0]):
			  for y in range(self.croppedpic4_1.size[1]):
			      tempr1,tempg1,tempb1,dummy = self.imgData4_1[x,y]
			      r4_1 += tempr1
			      g4_1 += tempg1
			      b4_1 += tempb1
			      count1 += 1
			      
			for x in range(self.croppedpic4_2.size[0]):
			  for y in range(self.croppedpic4_2.size[1]):
			      tempr2,tempg2,tempb2,dummy = self.imgData4_2[x,y]
			      r4_2 += tempr2
			      g4_2 += tempg2
			      b4_2 += tempb2
			      count2 += 1
			      
			for x in range(self.croppedpic4_3.size[0]):
			  for y in range(self.croppedpic4_3.size[1]):
			      tempr3,tempg3,tempb3,dummy = self.imgData4_3[x,y]
			      r4_3 += tempr3
			      g4_3 += tempg3
			      b4_3 += tempb3
			      count3 += 1
			      
			for x in range(self.croppedpic4_4.size[0]):
			  for y in range(self.croppedpic4_4.size[1]):
			      tempr4,tempg4,tempb4,dummy = self.imgData4_4[x,y]
			      r4_4 += tempr4
			      g4_4 += tempg4
			      b4_4 += tempb4
			      count4 += 1
			      
			for x in range(self.croppedpic4_5.size[0]):
			  for y in range(self.croppedpic4_5.size[1]):
			      tempr5,tempg5,tempb5,dummy = self.imgData4_5[x,y]
			      r4_5 += tempr5
			      g4_5 += tempg5
			      b4_5 += tempb5
			      count5 += 1                                 
			                             
			r = (r4_1 + r4_2 + r4_3 + r4_4 + r4_5) / 5
			g = (g4_1 + g4_2 + g4_3 + g4_4 + g4_5) / 5              
			b = (b4_1 + b4_2 + b4_3 + b4_4 + b4_5) / 5
			count = (count1 + count2 + count3 + count4 + count5) / 5
			            
			# calculate averages
			return (r/count), (g/count), (b/count), count
		except Exception as e:
			errorstring = "/E-PixelCounter-averagePixels4()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 				

	def averagePixels5(self):
		try:
			r, g, b = 0, 0, 0
			r5_1, g5_1, b5_1 = 0, 0, 0
			r5_2, g5_2, b5_2 = 0, 0, 0
			r5_3, g5_3, b5_3 = 0, 0, 0
			r5_4, g5_4, b5_4 = 0, 0, 0
			r5_5, g5_5, b5_5 = 0, 0, 0
			count = 0
			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			count5 = 0        

			for x in range(self.croppedpic5_1.size[0]):
			  for y in range(self.croppedpic5_1.size[1]):
			      tempr1,tempg1,tempb1,dummy = self.imgData5_1[x,y]
			      r5_1 += tempr1
			      g5_1 += tempg1
			      b5_1 += tempb1
			      count1 += 1
			      
			for x in range(self.croppedpic5_2.size[0]):
			  for y in range(self.croppedpic5_2.size[1]):
			      tempr2,tempg2,tempb2,dummy = self.imgData5_2[x,y]
			      r5_2 += tempr2
			      g5_2 += tempg2
			      b5_2 += tempb2
			      count2 += 1
			      
			for x in range(self.croppedpic5_3.size[0]):
			  for y in range(self.croppedpic5_3.size[1]):
			      tempr3,tempg3,tempb3,dummy = self.imgData5_3[x,y]
			      r5_3 += tempr3
			      g5_3 += tempg3
			      b5_3 += tempb3
			      count3 += 1
			      
			for x in range(self.croppedpic5_4.size[0]):
			  for y in range(self.croppedpic5_4.size[1]):
			      tempr4,tempg4,tempb4,dummy = self.imgData5_4[x,y]
			      r5_4 += tempr4
			      g5_4 += tempg4
			      b5_4 += tempb4
			      count4 += 1
			      
			for x in range(self.croppedpic5_5.size[0]):
			  for y in range(self.croppedpic5_5.size[1]):
			      tempr5,tempg5,tempb5,dummy = self.imgData5_5[x,y]
			      r5_5 += tempr5
			      g5_5 += tempg5
			      b5_5 += tempb5
			      count5 += 1                                 
			                             
			r = (r5_1 + r5_2 + r5_3 + r5_4 + r5_5) / 5
			g = (g5_1 + g5_2 + g5_3 + g5_4 + g5_5) / 5              
			b = (b5_1 + b5_2 + b5_3 + b5_4 + b5_5) / 5
			count = (count1 + count2 + count3 + count4 + count5) / 5
			            
			# calculate averages
			return (r/count), (g/count), (b/count), count
		except Exception as e:
			errorstring = "/E-PixelCounter-averagePixels5()"
			logging.warning("%s", errorstring)
			logging.exception("Exception occurred")
		finally:
			pass 				

class Mousewheel_Support(object):    
    # implemetation of singleton pattern
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, root, horizontal_factor = 2, vertical_factor=2):
        
        self._active_area = None
        
        if isinstance(horizontal_factor, int):
            self.horizontal_factor = horizontal_factor
        else:
            raise Exception("Vertical factor must be an integer.")

        if isinstance(vertical_factor, int):
            self.vertical_factor = vertical_factor
        else:
            raise Exception("Horizontal factor must be an integer.")

        if OS == "Linux" :
            root.bind_all('<4>', self._on_mousewheel,  add='+')
            root.bind_all('<5>', self._on_mousewheel,  add='+')
        else:
            # Windows and MacOS
            root.bind_all("<MouseWheel>", self._on_mousewheel,  add='+')

    def _on_mousewheel(self,event):
        if self._active_area:
            self._active_area.onMouseWheel(event)

    def _mousewheel_bind(self, widget):
        self._active_area = widget

    def _mousewheel_unbind(self):
        self._active_area = None

    def add_support_to(self, widget=None, xscrollbar=None, yscrollbar=None, what="units", horizontal_factor=None, vertical_factor=None):
        if xscrollbar is None and yscrollbar is None:
            return

        if xscrollbar is not None:
            horizontal_factor = horizontal_factor or self.horizontal_factor

            xscrollbar.onMouseWheel = self._make_mouse_wheel_handler(widget,'x', self.horizontal_factor, what)
            xscrollbar.bind('<Enter>', lambda event, scrollbar=xscrollbar: self._mousewheel_bind(scrollbar) )
            xscrollbar.bind('<Leave>', lambda event: self._mousewheel_unbind())

        if yscrollbar is not None:
            vertical_factor = vertical_factor or self.vertical_factor

            yscrollbar.onMouseWheel = self._make_mouse_wheel_handler(widget,'y', self.vertical_factor, what)
            yscrollbar.bind('<Enter>', lambda event, scrollbar=yscrollbar: self._mousewheel_bind(scrollbar) )
            yscrollbar.bind('<Leave>', lambda event: self._mousewheel_unbind())

        main_scrollbar = yscrollbar if yscrollbar is not None else xscrollbar
        
        if widget is not None:
            if isinstance(widget, list) or isinstance(widget, tuple):
                list_of_widgets = widget
                for widget in list_of_widgets:
                    widget.bind('<Enter>',lambda event: self._mousewheel_bind(widget))
                    widget.bind('<Leave>', lambda event: self._mousewheel_unbind())

                    widget.onMouseWheel = main_scrollbar.onMouseWheel
            else:
                widget.bind('<Enter>',lambda event: self._mousewheel_bind(widget))
                widget.bind('<Leave>', lambda event: self._mousewheel_unbind())

                widget.onMouseWheel = main_scrollbar.onMouseWheel

    @staticmethod
    def _make_mouse_wheel_handler(widget, orient, factor = 1, what="units"):
        view_command = getattr(widget, orient+'view')
        
        if OS == 'Linux':
            def onMouseWheel(event):
                if event.num == 4:
                    view_command("scroll",(-1)*factor, what)
                elif event.num == 5:
                    view_command("scroll",factor, what) 
                
        elif OS == 'Windows':
            def onMouseWheel(event):        
                view_command("scroll",(-1)*int((event.delta/120)*factor), what) 
        
        elif OS == 'Darwin':
            def onMouseWheel(event):        
                view_command("scroll",event.delta, what)
        
        return onMouseWheel

class Scrolling_Area(Frame, object):

    def __init__(self, master, width=None, anchor=N, height=None, mousewheel_speed = 2, scroll_horizontally=True, xscrollbar=None, scroll_vertically=True, yscrollbar=None, outer_background=None, inner_frame=Frame, **kw):
        Frame.__init__(self, master, class_=self.__class__)

        if outer_background:
            self.configure(background=outer_background)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self._width = width
        self._height = height

        self.canvas = Canvas(self, background=outer_background, highlightthickness=0, width=width, height=height)
        self.canvas.grid(row=0, column=0, sticky=N+E+W+S)

        if scroll_vertically:
            if yscrollbar is not None:
                self.yscrollbar = yscrollbar
            else:
                self.yscrollbar = Scrollbar(self, orient=VERTICAL)
                self.yscrollbar.grid(row=0, column=1,sticky=N+S)
        
            self.canvas.configure(yscrollcommand=self.yscrollbar.set)
            self.yscrollbar['command']=self.canvas.yview
        else:
            self.yscrollbar = None

        if scroll_horizontally:
            if xscrollbar is not None:
                self.xscrollbar = xscrollbar
            else:
                self.xscrollbar = Scrollbar(self, orient=HORIZONTAL)
                self.xscrollbar.grid(row=1, column=0, sticky=E+W)
            
            self.canvas.configure(xscrollcommand=self.xscrollbar.set)
            self.xscrollbar['command']=self.canvas.xview
        else:
            self.xscrollbar = None

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.innerframe = inner_frame(self.canvas, **kw)
        self.innerframe.pack(anchor=anchor)
        
        self.canvas.create_window(0, 0, window=self.innerframe, anchor='nw', tags="inner_frame")

        self.canvas.bind('<Configure>', self._on_canvas_configure)

        Mousewheel_Support(self).add_support_to(self.canvas, xscrollbar=self.xscrollbar, yscrollbar=self.yscrollbar)

    @property
    def width(self):
        return self.canvas.winfo_width()

    @width.setter
    def width(self, width):
        self.canvas.configure(width= width)

    @property
    def height(self):
        return self.canvas.winfo_height()
        
    @height.setter
    def height(self, height):
        self.canvas.configure(height = height)
        
    def set_size(self, width, height):
        self.canvas.configure(width=width, height = height)

    def _on_canvas_configure(self, event):
        width = max(self.innerframe.winfo_reqwidth(), event.width)
        height = max(self.innerframe.winfo_reqheight(), event.height)

        self.canvas.configure(scrollregion="0 0 %s %s" % (width, height))
        self.canvas.itemconfigure("inner_frame", width=width, height=height)

    def update_viewport(self):
        self.update()

        window_width = self.innerframe.winfo_reqwidth()
        window_height = self.innerframe.winfo_reqheight()
        
        if self._width is None:
            canvas_width = window_width
        else:
            canvas_width = min(self._width, window_width)
            
        if self._height is None:
            canvas_height = window_height
        else:
            canvas_height = min(self._height, window_height)

        self.canvas.configure(scrollregion="0 0 %s %s" % (window_width, window_height), width=canvas_width, height=canvas_height)
        self.canvas.itemconfigure("inner_frame", width=window_width, height=window_height)

class Cell(Frame):
    """Base class for cells"""

class Data_Cell(Cell):
    def __init__(self, master, variable, anchor=W, bordercolor=None, borderwidth=1, padx=0, pady=0, background=None, foreground=None, font=None):
        Cell.__init__(self, master, background=background, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=borderwidth, bd= 0)

        self._message_widget = Message(self, textvariable=variable, font=font, background=background, foreground=foreground)
        self._message_widget.pack(expand=True, padx=padx, pady=pady, anchor=anchor)
        self.bind("<Configure>", self._on_configure)

    def _on_configure(self, event):
        self._message_widget.configure(width=event.width)


class Header_Cell(Cell):
    def __init__(self, master, text, bordercolor=None, borderwidth=1, padx=0, pady=0, background=None, foreground=None, font=None, anchor=CENTER, separator=True):
        Cell.__init__(self, master, background=background, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=borderwidth, bd= 0)
        self.pack_propagate(False)

        self._header_label = Label(self, text=text, background=background, foreground=foreground, font=font)
        self._header_label.pack(padx=padx, pady=pady, expand=True)

        if separator and bordercolor is not None:
            separator = Frame(self, height=2, background=bordercolor, bd=0, highlightthickness=0, class_="Separator")
            separator.pack(fill=X, anchor=anchor)

        self.update()
        height = self._header_label.winfo_reqheight() + 2*padx
        width = self._header_label.winfo_reqwidth() + 2*pady

        self.configure(height=height, width=width)
        
class Table(Frame):
    def __init__(self, master, columns, column_weights=None, column_minwidths=None, height=500, minwidth=20, minheight=20, padx=0, pady=0, cell_font=None, cell_foreground="black", cell_background="white", cell_anchor=W, header_font=None, header_background="white", header_foreground="black", header_anchor=CENTER, bordercolor = "#999999", innerborder=True, outerborder=True, stripped_rows=("#EEEEEE", "white"), on_change_data=None, mousewheel_speed = 2, scroll_horizontally=False, scroll_vertically=True):
        outerborder_width = 1 if outerborder else 0

        Frame.__init__(self,master, bd= 0)

        self._cell_background = cell_background
        self._cell_foreground = cell_foreground
        self._cell_font = cell_font
        self._cell_anchor = cell_anchor
        
        self._stripped_rows = stripped_rows

        self._padx = padx
        self._pady = pady
        
        self._bordercolor = bordercolor
        self._innerborder_width = 1 if innerborder else 0

        self._data_vars = []

        self._columns = columns
        
        self._number_of_rows = 0
        self._number_of_columns = len(columns)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self._head = Frame(self, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=outerborder_width, bd= 0)
        self._head.grid(row=0, column=0, sticky=E+W)

        header_separator = False if outerborder else True

        for j in range(len(columns)):
            column_name = columns[j]

            header_cell = Header_Cell(self._head, text=column_name, borderwidth=self._innerborder_width, font=header_font, background=header_background, foreground=header_foreground, padx=padx, pady=pady, bordercolor=bordercolor, anchor=header_anchor, separator=header_separator)
            header_cell.grid(row=0, column=j, sticky=N+E+W+S)

        add_scrollbars = scroll_horizontally or scroll_vertically
        if add_scrollbars:
            if scroll_horizontally:
                xscrollbar = Scrollbar(self, orient=HORIZONTAL)
                xscrollbar.grid(row=2, column=0, sticky=E+W)
            else:
                xscrollbar = None

            if scroll_vertically:
                yscrollbar = Scrollbar(self, orient=VERTICAL)
                yscrollbar.grid(row=1, column=1, sticky=N+S)
            else:
                yscrollbar = None

            scrolling_area = Scrolling_Area(self, width=self._head.winfo_reqwidth(), height=height, scroll_horizontally=scroll_horizontally, xscrollbar=xscrollbar, scroll_vertically=scroll_vertically, yscrollbar=yscrollbar)
            scrolling_area.grid(row=1, column=0, sticky=E+W)

            self._body = Frame(scrolling_area.innerframe, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=outerborder_width, bd= 0)
            self._body.pack()
            
            def on_change_data():
                scrolling_area.update_viewport()

        else:
            self._body = Frame(self, height=height, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=outerborder_width, bd= 0)
            self._body.grid(row=1, column=0, sticky=N+E+W+S)

        if column_weights is None:
            for j in range(len(columns)):
                self._body.grid_columnconfigure(j, weight=1)
        else:
            for j, weight in enumerate(column_weights):
                self._body.grid_columnconfigure(j, weight=weight)

        if column_minwidths is not None:
            for j, minwidth in enumerate(column_minwidths):
                if minwidth is None:
                    header_cell = self._head.grid_slaves(row=0, column=j)[0]
                    minwidth = header_cell.winfo_reqwidth()

                self._body.grid_columnconfigure(j, minsize=minwidth)
        else:
            for j in range(len(columns)):
                header_cell = self._head.grid_slaves(row=0, column=j)[0]
                minwidth = header_cell.winfo_reqwidth()

                self._body.grid_columnconfigure(j, minsize=minwidth)

        self._on_change_data = on_change_data

    def _append_n_rows(self, n):
        number_of_rows = self._number_of_rows
        number_of_columns = self._number_of_columns

        for i in range(number_of_rows, number_of_rows+n):
            list_of_vars = []
            for j in range(number_of_columns):
                var = StringVar()
                list_of_vars.append(var)

                if self._stripped_rows:
                    cell = Data_Cell(self._body, borderwidth=self._innerborder_width, variable=var, bordercolor=self._bordercolor, padx=self._padx, pady=self._pady, background=self._stripped_rows[i%2], foreground=self._cell_foreground, font=self._cell_font, anchor=self._cell_anchor)
                else:
                    cell = Data_Cell(self._body, borderwidth=self._innerborder_width, variable=var, bordercolor=self._bordercolor, padx=self._padx, pady=self._pady, background=self._cell_background, foreground=self._cell_foreground, font=self._cell_font, anchor=self._cell_anchor)

                cell.grid(row=i, column=j, sticky=N+E+W+S)

            self._data_vars.append(list_of_vars)
            
        if number_of_rows == 0:
            for j in range(self.number_of_columns):
                header_cell = self._head.grid_slaves(row=0, column=j)[0]
                data_cell = self._body.grid_slaves(row=0, column=j)[0]
                data_cell.bind("<Configure>", lambda event, header_cell=header_cell: header_cell.configure(width=event.width), add="+")

        self._number_of_rows += n

    def _pop_n_rows(self, n):
        number_of_rows = self._number_of_rows
        number_of_columns = self._number_of_columns
        
        for i in range(number_of_rows-n, number_of_rows):
            for j in range(number_of_columns):
                self._body.grid_slaves(row=i, column=j)[0].destroy()
            
            self._data_vars.pop()
    
        self._number_of_rows -= n

    def set_data(self, data):
        n = len(data)
        m = len(data[0])

        number_of_rows = self._number_of_rows

        if number_of_rows > n:
            self._pop_n_rows(number_of_rows-n)
        elif number_of_rows < n:
            self._append_n_rows(n-number_of_rows)

        for i in range(n):
            for j in range(m):
                self._data_vars[i][j].set(data[i][j])

        if self._on_change_data is not None: self._on_change_data()

    def get_data(self):
        number_of_rows = self._number_of_rows
        number_of_columns = self.number_of_columns
        
        data = []
        for i in range(number_of_rows):
            row = []
            row_of_vars = self._data_vars[i]
            for j in range(number_of_columns):
                cell_data = row_of_vars[j].get()
                row.append(cell_data)
            
            data.append(row)
        return data

    @property
    def number_of_rows(self):
        return self._number_of_rows

    @property
    def number_of_columns(self):
        return self._number_of_columns

    def row(self, index, data=None):
        if data is None:
            row = []
            row_of_vars = self._data_vars[index]

            for j in range(self.number_of_columns):
                row.append(row_of_vars[j].get())
                
            return row
        else:
            number_of_columns = self.number_of_columns
            
            if len(data) != number_of_columns:
                raise ValueError("data has no %d elements: %s"%(number_of_columns, data))

            row_of_vars = self._data_vars[index]
            for j in range(number_of_columns):
                row_of_vars[index][j].set(data[j])
                
            if self._on_change_data is not None: self._on_change_data()

    def column(self, index, data=None):
        number_of_rows = self._number_of_rows

        if data is None:
            column= []

            for i in range(number_of_rows):
                column.append(self._data_vars[i][index].get())
                
            return column
        else:            
            if len(data) != number_of_rows:
                raise ValueError("data has no %d elements: %s"%(number_of_rows, data))

            for i in range(number_of_columns):
                self._data_vars[i][index].set(data[i])

            if self._on_change_data is not None: self._on_change_data()

    def clear(self):
        number_of_rows = self._number_of_rows
        number_of_columns = self._number_of_columns

        for i in range(number_of_rows):
            for j in range(number_of_columns):
                self._data_vars[i][j].set("")

        if self._on_change_data is not None: self._on_change_data()

    def delete_row(self, index):
        i = index
        while i < self._number_of_rows:
            row_of_vars_1 = self._data_vars[i]
            row_of_vars_2 = self._data_vars[i+1]

            j = 0
            while j <self.number_of_columns:
                row_of_vars_1[j].set(row_of_vars_2[j])

            i += 1

        self._pop_n_rows(1)

        if self._on_change_data is not None: self._on_change_data()

    def insert_row(self, data, index=END):
        self._append_n_rows(1)

        if index == END:
            index = self._number_of_rows - 1
        
        i = self._number_of_rows-1
        while i > index:
            row_of_vars_1 = self._data_vars[i-1]
            row_of_vars_2 = self._data_vars[i]

            j = 0
            while j < self.number_of_columns:
                row_of_vars_2[j].set(row_of_vars_1[j])
                j += 1
            i -= 1

        list_of_cell_vars = self._data_vars[index]
        for cell_var, cell_data in zip(list_of_cell_vars, data):
            cell_var.set(cell_data)

        if self._on_change_data is not None: self._on_change_data()

    def cell(self, row, column, data=None):
        """Get the value of a table cell"""
        if data is None:
            return self._data_vars[row][column].get()
        else:
            self._data_vars[row][column].set(data)
            if self._on_change_data is not None: self._on_change_data()

    def __getitem__(self, index):
        if isinstance(index, tuple):
            row, column = index
            return self.cell(row, column)
        else:
            raise Exception("Row and column indices are required")
        
    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            row, column = index
            self.cell(row, column, value)
        else:
            raise Exception("Row and column indices are required")

    def on_change_data(self, callback):
        self._on_change_data = callback
        def __init__(self, master, columns, column_weights=None, column_minwidths=None, height=500, minwidth=20, minheight=20, padx=0, pady=0, cell_font=None, cell_foreground="black", cell_background="white", cell_anchor=W, header_font=None, header_background="white", header_foreground="black", header_anchor=CENTER, bordercolor = "#999999", innerborder=True, outerborder=True, stripped_rows=("#EEEEEE", "white"), on_change_data=None, mousewheel_speed = 2, scroll_horizontally=False, scroll_vertically=True):
                outerborder_width = 1 if outerborder else 0

                Frame.__init__(self,master, bd= 0)

                self._cell_background = cell_background
                self._cell_foreground = cell_foreground
                self._cell_font = cell_font
                self._cell_anchor = cell_anchor

                self._stripped_rows = stripped_rows

                self._padx = padx
                self._pady = pady

                self._bordercolor = bordercolor
                self._innerborder_width = 1 if innerborder else 0

                self._data_vars = []

                self._columns = columns

                self._number_of_rows = 0
                self._number_of_columns = len(columns)

                self.grid_columnconfigure(0, weight=1)
                self.grid_rowconfigure(1, weight=1)

                self._head = Frame(self, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=outerborder_width, bd= 0)
                self._head.grid(row=0, column=0, sticky=E+W)

                header_separator = False if outerborder else True

                for j in range(len(columns)):
                    column_name = columns[j]

                    header_cell = Header_Cell(self._head, text=column_name, borderwidth=self._innerborder_width, font=header_font, background=header_background, foreground=header_foreground, padx=padx, pady=pady, bordercolor=bordercolor, anchor=header_anchor, separator=header_separator)
                    header_cell.grid(row=0, column=j, sticky=N+E+W+S)

                add_scrollbars = scroll_horizontally or scroll_vertically
                if add_scrollbars:
                        if scroll_horizontally:
                                xscrollbar = Scrollbar(self, orient=HORIZONTAL)
                                xscrollbar.grid(row=2, column=0, sticky=E+W)
                        else:
                                xscrollbar = None

                        if scroll_vertically:
                                yscrollbar = Scrollbar(self, orient=VERTICAL)
                                yscrollbar.grid(row=1, column=1, sticky=N+S)
                        else:
                                yscrollbar = None

                        scrolling_area = Scrolling_Area(self, width=self._head.winfo_reqwidth(), height=height, scroll_horizontally=scroll_horizontally, xscrollbar=xscrollbar, scroll_vertically=scroll_vertically, yscrollbar=yscrollbar)
                        scrolling_area.grid(row=1, column=0, sticky=E+W)

                        self._body = Frame(scrolling_area.innerframe, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=outerborder_width, bd= 0)
                        self._body.pack()
    
                        def on_change_data():
                                scrolling_area.update_viewport()

                else:
                        self._body = Frame(self, height=height, highlightbackground=bordercolor, highlightcolor=bordercolor, highlightthickness=outerborder_width, bd= 0)
                        self._body.grid(row=1, column=0, sticky=N+E+W+S)

                if column_weights is None:
                        for j in range(len(columns)):
                                self._body.grid_columnconfigure(j, weight=1)
                else:
                        for j, weight in enumerate(column_weights):
                                self._body.grid_columnconfigure(j, weight=weight)

                        if column_minwidths is not None:
                                for j, minwidth in enumerate(column_minwidths):
                                        if minwidth is None:
                                                header_cell = self._head.grid_slaves(row=0, column=j)[0]
                                                minwidth = header_cell.winfo_reqwidth()

                                        self._body.grid_columnconfigure(j, minsize=minwidth)
                        else:
                                for j in range(len(columns)):
                                        header_cell = self._head.grid_slaves(row=0, column=j)[0]
                                        minwidth = header_cell.winfo_reqwidth()

                                        self._body.grid_columnconfigure(j, minsize=minwidth)

                        self._on_change_data = on_change_data

        def _append_n_rows(self, n):
                number_of_rows = self._number_of_rows
                number_of_columns = self._number_of_columns

                for i in range(number_of_rows, number_of_rows+n):
                        list_of_vars = []
                        for j in range(number_of_columns):
                                var = StringVar()
                                list_of_vars.append(var)

                                if self._stripped_rows:
                                        cell = Data_Cell(self._body, borderwidth=self._innerborder_width, variable=var, bordercolor=self._bordercolor, padx=self._padx, pady=self._pady, background=self._stripped_rows[i%2], foreground=self._cell_foreground, font=self._cell_font, anchor=self._cell_anchor)
                                else:
                                        cell = Data_Cell(self._body, borderwidth=self._innerborder_width, variable=var, bordercolor=self._bordercolor, padx=self._padx, pady=self._pady, background=self._cell_background, foreground=self._cell_foreground, font=self._cell_font, anchor=self._cell_anchor)

                                cell.grid(row=i, column=j, sticky=N+E+W+S)

                        self._data_vars.append(list_of_vars)
                    
                        if number_of_rows == 0:
                            for j in range(self.number_of_columns):
                                header_cell = self._head.grid_slaves(row=0, column=j)[0]
                                data_cell = self._body.grid_slaves(row=0, column=j)[0]
                                data_cell.bind("<Configure>", lambda event, header_cell=header_cell: header_cell.configure(width=event.width), add="+")

                        self._number_of_rows += n

        def _pop_n_rows(self, n):
                number_of_rows = self._number_of_rows
                number_of_columns = self._number_of_columns

                for i in range(number_of_rows-n, number_of_rows):
                    for j in range(number_of_columns):
                        self._body.grid_slaves(row=i, column=j)[0].destroy()
                    
                    self._data_vars.pop()

                self._number_of_rows -= n

        def set_data(self, data):
                n = len(data)
                m = len(data[0])

                number_of_rows = self._number_of_rows

                if number_of_rows > n:
                        self._pop_n_rows(number_of_rows-n)
                elif number_of_rows < n:
                        self._append_n_rows(n-number_of_rows)

                for i in range(n):
                        for j in range(m):
                            self._data_vars[i][j].set(data[i][j])

                if self._on_change_data is not None: self._on_change_data()

        def get_data(self):
                number_of_rows = self._number_of_rows
                number_of_columns = self.number_of_columns

                data = []
                for i in range(number_of_rows):
                        row = []
                        row_of_vars = self._data_vars[i]
                        for j in range(number_of_columns):
                                cell_data = row_of_vars[j].get()
                                row.append(cell_data)
                    
                        data.append(row)
                return data

        @property
        def number_of_rows(self):
                return self._number_of_rows

        @property
        def number_of_columns(self):
                return self._number_of_columns

        def row(self, index, data=None):
                if data is None:
                    row = []
                    row_of_vars = self._data_vars[index]

                    for j in range(self.number_of_columns):
                        row.append(row_of_vars[j].get())
                        
                    return row
                else:
                    number_of_columns = self.number_of_columns
                    
                    if len(data) != number_of_columns:
                        raise ValueError("data has no %d elements: %s"%(number_of_columns, data))

                    row_of_vars = self._data_vars[index]
                    for j in range(number_of_columns):
                        row_of_vars[index][j].set(data[j])
                        
                    if self._on_change_data is not None: self._on_change_data()

        def column(self, index, data=None):
                number_of_rows = self._number_of_rows

                if data is None:
                    column= []

                    for i in range(number_of_rows):
                        column.append(self._data_vars[i][index].get())
                        
                    return column
                else:            
                    if len(data) != number_of_rows:
                        raise ValueError("data has no %d elements: %s"%(number_of_rows, data))

                    for i in range(number_of_columns):
                        self._data_vars[i][index].set(data[i])

                    if self._on_change_data is not None: self._on_change_data()

        def clear(self):
                number_of_rows = self._number_of_rows
                number_of_columns = self._number_of_columns

                for i in range(number_of_rows):
                    for j in range(number_of_columns):
                        self._data_vars[i][j].set("")

                if self._on_change_data is not None: self._on_change_data()

        def delete_row(self, index):
                i = index
                while i < self._number_of_rows:
                    row_of_vars_1 = self._data_vars[i]
                    row_of_vars_2 = self._data_vars[i+1]

                    j = 0
                    while j <self.number_of_columns:
                        row_of_vars_1[j].set(row_of_vars_2[j])

                    i += 1

                self._pop_n_rows(1)

                if self._on_change_data is not None: self._on_change_data()

        def insert_row(self, data, index=END):
                self._append_n_rows(1)

                if index == END:
                    index = self._number_of_rows - 1

                i = self._number_of_rows-1
                while i > index:
                    row_of_vars_1 = self._data_vars[i-1]
                    row_of_vars_2 = self._data_vars[i]

                    j = 0
                    while j < self.number_of_columns:
                        row_of_vars_2[j].set(row_of_vars_1[j])
                        j += 1
                    i -= 1

                list_of_cell_vars = self._data_vars[index]
                for cell_var, cell_data in zip(list_of_cell_vars, data):
                    cell_var.set(cell_data)

                if self._on_change_data is not None: self._on_change_data()

        def cell(self, row, column, data=None):
                """Get the value of a table cell"""
                if data is None:
                    return self._data_vars[row][column].get()
                else:
                    self._data_vars[row][column].set(data)
                    if self._on_change_data is not None: self._on_change_data()

        def __getitem__(self, index):
                if isinstance(index, tuple):
                    row, column = index
                    return self.cell(row, column)
                else:
                    raise Exception("Row and column indices are required")

        def __setitem__(self, index, value):
                if isinstance(index, tuple):
                    row, column = index
                    self.cell(row, column, value)
                else:
                    raise Exception("Row and column indices are required")

        def on_change_data(self, callback):
                self._on_change_data = callback        

URL="https://soil.krishitantra.com/api/"
token=""
Name=""
device_id=""
fr_name=""
fr_username=""
fr_contact=""
fr_email=""
fr_address=""
fr_state=""
fr_country=""
fr_lang=""
fr_geolat=""
fr_geolong=""
fr_fieldname=""
fr_fieldarea=""
fr_croptype=""
fr_soiltype=""
fr_farmlong=""
fr_farmlat=""
fr_farmsurveyno=""
fr_uuid=""
farmuuid=""
fr_soilden=""
fr_farmuuid=""

class MainPAGE:
		def is_connected(self):
			try:
				# connect to the host -- tells us if the host is actually
				# reachable
				socket.setdefaulttimeout(30)
				socket.create_connection(("www.google.com", 80))
				return True
			except OSError:
				pass
			return False
				
		def check_internet_connection(self): 
			try:       
				status = "retry"
				internet_connection = self.is_connected()
				while (internet_connection == False and status == "retry"):
					MsgBox = messagebox.askquestion ('Internet Connection','Press yes to retry for the connection / press no to redirect to home screen ',icon = 'warning')
					if MsgBox == 'yes':
						internet_connection = self.is_connected()
						if internet_connection == False:
							pass
					else:
						#self.front_page()
						return 0
				return 1
			except Exception as e:
				errorstring = "/E-check_internet_connection()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 				
			
		def check_internet_connection_continuous(self):
			try:        
				status = "retry"
				internet_connection = self.is_connected()
				if internet_connection == True:
					self.internet_conn_label.configure(text = "Connected to Internet")				
				while (internet_connection == False and status == "retry"):
					self.internet_conn_label.configure(text = "")
					MsgBox = messagebox.askretrycancel('No Internet','Lost internet connection')
					if MsgBox == True:
						internet_connection = self.is_connected()
						if internet_connection == False:
							pass
					else:
						return 0
				return 1
			except Exception as e:
				errorstring = "/E-check_internet_connection_continuous()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 							

		def n_cal_imagecapture(self,nsample):
			try:
				# assumes you have a test.jpg in the working directory! 
				self.machine_status_label.configure(text = "")
				pic_number = 1
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(2)
				camera.capture(self.image_path+"nc1_"+nsample+"_fulltest.png")
				pc1 = PixelCounter(self.image_path+"nc1_"+nsample+"_fulltest.png",pic_number)
				one_r,one_g,one_b,one_count = pc1.averagePixels1()
				time.sleep(2)  

				pic_number = 2
				camera.capture(self.image_path+"nc2_"+nsample+"_fulltest.png")
				pc2 = PixelCounter(self.image_path+"nc2_"+nsample+"_fulltest.png",pic_number)
				two_r,two_g,two_b,two_count = pc2.averagePixels2()
				time.sleep(2)

				pic_number = 3
				camera.capture(self.image_path+"nc3_"+nsample+"_fulltest.png")
				pc3 = PixelCounter(self.image_path+"nc3_"+nsample+"_fulltest.png",pic_number)
				three_r,three_g,three_b,three_count = pc3.averagePixels3()
				time.sleep(2)

				pic_number = 4
				camera.capture(self.image_path+"nc4_"+nsample+"_fulltest.png")
				pc4 = PixelCounter(self.image_path+"nc4_"+nsample+"_fulltest.png",pic_number)
				four_r,four_g,four_b,four_count = pc4.averagePixels4()
				time.sleep(2)

				pic_number = 5
				camera.capture(self.image_path+"nc5_"+nsample+"_fulltest.png")
				pc5 = PixelCounter(self.image_path+"nc5_"+nsample+"_fulltest.png",pic_number)
				five_r,five_g,five_b,five_count = pc5.averagePixels5()

				avg_r = (two_r + three_r +four_r + five_r) / 4
				avg_g = (two_g + three_g +four_g + five_g) / 4
				avg_b = (two_b + three_b +four_b + five_b) / 4
				
				avg_r = int(avg_r)
				avg_g = int(avg_g)
				avg_b = int(avg_b)
				
			except Exception as e:
				errorstring = "/E-N_cal_imagecapture()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				camera.close()
				return avg_r, avg_g, avg_b                        

		def p_cal_imagecapture(self,psample):
			try:
				# assumes you have a test.jpg in the working directory! 
				self.machine_status_label.configure(text = "")
				pic_number = 1
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(2)
				camera.capture(self.image_path+"pc1_"+psample+"_fulltest.png")
				pc1 = PixelCounter(self.image_path+"pc1_"+psample+"_fulltest.png",pic_number)
				one_r,one_g,one_b,one_count = pc1.averagePixels1()
				time.sleep(2)  

				pic_number = 2
				camera.capture(self.image_path+"pc2_"+psample+"_fulltest.png")
				pc2 = PixelCounter(self.image_path+"pc2_"+psample+"_fulltest.png",pic_number)
				two_r,two_g,two_b,two_count = pc2.averagePixels2()
				time.sleep(2)

				pic_number = 3
				camera.capture(self.image_path+"pc3_"+psample+"_fulltest.png")
				pc3 = PixelCounter(self.image_path+"pc3_"+psample+"_fulltest.png",pic_number)
				three_r,three_g,three_b,three_count = pc3.averagePixels3()
				time.sleep(2)

				pic_number = 4
				camera.capture(self.image_path+"pc4_"+psample+"_fulltest.png")
				pc4 = PixelCounter(self.image_path+"pc4_"+psample+"_fulltest.png",pic_number)
				four_r,four_g,four_b,four_count = pc4.averagePixels4()
				time.sleep(2)

				pic_number = 5
				camera.capture(self.image_path+"pc5_"+psample+"_fulltest.png")
				pc5 = PixelCounter(self.image_path+"pc5_"+psample+"_fulltest.png",pic_number)
				five_r,five_g,five_b,five_count = pc5.averagePixels5()

				avg_r = (two_r + three_r +four_r + five_r) / 4
				avg_g = (two_g + three_g +four_g + five_g) / 4
				avg_b = (two_b + three_b +four_b + five_b) / 4
				
				avg_r = int(avg_r)
				avg_g = int(avg_g)
				avg_b = int(avg_b)					

			except (KeyError, ZeroDivisionError, serial.SerialException, ValueError) as e:
				errorstring = "/E-P_cal_imagecapture()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")			        
			finally:
				camera.close()
				return avg_r, avg_g, avg_b                        
				        
		def k_cal_imagecapture(self,ksample):
			try:
				# assumes you have a test.jpg in the working directory! 
				self.machine_status_label.configure(text = "")
				pic_number = 1
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(2)
				camera.capture(self.image_path+"kc1_"+ksample+"_fulltest.png")
				pc1 = PotassiumPixelCounter(self.image_path+"kc1_"+ksample+"_fulltest.png",pic_number)
				one_r,one_g,one_b,one_count = pc1.paveragePixels1()
				time.sleep(2)  

				pic_number = 2
				camera.capture(self.image_path+"kc2_"+ksample+"_fulltest.png")
				pc2 = PotassiumPixelCounter(self.image_path+"kc2_"+ksample+"_fulltest.png",pic_number)
				two_r,two_g,two_b,two_count = pc2.paveragePixels2()
				time.sleep(2)

				pic_number = 3
				camera.capture(self.image_path+"kc3_"+ksample+"_fulltest.png")
				pc3 = PotassiumPixelCounter(self.image_path+"kc3_"+ksample+"_fulltest.png",pic_number)
				three_r,three_g,three_b,three_count = pc3.paveragePixels3()
				time.sleep(2)

				pic_number = 4
				camera.capture(self.image_path+"kc4_"+ksample+"_fulltest.png")
				pc4 = PotassiumPixelCounter(self.image_path+"kc4_"+ksample+"_fulltest.png",pic_number)
				four_r,four_g,four_b,four_count = pc4.paveragePixels4()
				time.sleep(2)

				pic_number = 5
				camera.capture(self.image_path+"kc5_"+ksample+"_fulltest.png")
				pc5 = PotassiumPixelCounter(self.image_path+"kc5_"+ksample+"_fulltest.png",pic_number)
				five_r,five_g,five_b,five_count = pc5.paveragePixels5()

				avg_r = (two_r + three_r +four_r + five_r) / 4
				avg_g = (two_g + three_g +four_g + five_g) / 4
				avg_b = (two_b + three_b +four_b + five_b) / 4
				
				avg_r = int(avg_r)
				avg_g = int(avg_g)
				avg_b = int(avg_b)					

			except (KeyError, ZeroDivisionError, serial.SerialException, ValueError) as e:
				errorstring = "/E-K_cal_imagecapture()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				camera.close()
				return avg_r, avg_g, avg_b 
				
		def b_cal_imagecapture(self,bsample):
			try:
				# assumes you have a test.jpg in the working directory! 
				self.machine_status_label.configure(text = "")
				pic_number = 1
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(2)
				camera.capture(self.image_path+"bc1_"+bsample+"_fulltest.png")
				pc1 = PixelCounter(self.image_path+"bc1_"+bsample+"_fulltest.png",pic_number)
				one_r,one_g,one_b,one_count = pc1.averagePixels1()
				time.sleep(2)  

				pic_number = 2
				camera.capture(self.image_path+"bc2_"+bsample+"_fulltest.png")
				pc2 = PixelCounter(self.image_path+"bc2_"+bsample+"_fulltest.png",pic_number)
				two_r,two_g,two_b,two_count = pc2.averagePixels2()
				time.sleep(2)

				pic_number = 3
				camera.capture(self.image_path+"bc3_"+bsample+"_fulltest.png")
				pc3 = PixelCounter(self.image_path+"bc3_"+bsample+"_fulltest.png",pic_number)
				three_r,three_g,three_b,three_count = pc3.averagePixels3()
				time.sleep(2)

				pic_number = 4
				camera.capture(self.image_path+"bc4_"+bsample+"_fulltest.png")
				pc4 = PixelCounter(self.image_path+"bc4_"+bsample+"_fulltest.png",pic_number)
				four_r,four_g,four_b,four_count = pc4.averagePixels4()
				time.sleep(2)

				pic_number = 5
				camera.capture(self.image_path+"bc5_"+bsample+"_fulltest.png")
				pc5 = PixelCounter(self.image_path+"bc5_"+bsample+"_fulltest.png",pic_number)
				five_r,five_g,five_b,five_count = pc5.averagePixels5()

				avg_r = (two_r + three_r +four_r + five_r) / 4
				avg_g = (two_g + three_g +four_g + five_g) / 4
				avg_b = (two_b + three_b +four_b + five_b) / 4
				
				avg_r = int(avg_r)
				avg_g = int(avg_g)
				avg_b = int(avg_b)					

			except (KeyError, ZeroDivisionError, serial.SerialException, ValueError) as e:
				errorstring = "/E-B_cal_imagecapture()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")			        
			finally:
				camera.close()
				return avg_r, avg_g, avg_b     
				
		def i_cal_imagecapture(self,isample):
			try:
				# assumes you have a test.jpg in the working directory! 
				self.machine_status_label.configure(text = "")
				pic_number = 1
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(2)
				camera.capture(self.image_path+"ic1_"+isample+"_fulltest.png")
				pc1 = PixelCounter(self.image_path+"ic1_"+isample+"_fulltest.png",pic_number)
				one_r,one_g,one_b,one_count = pc1.averagePixels1()
				time.sleep(2)  

				pic_number = 2
				camera.capture(self.image_path+"ic2_"+isample+"_fulltest.png")
				pc2 = PixelCounter(self.image_path+"ic2_"+isample+"_fulltest.png",pic_number)
				two_r,two_g,two_b,two_count = pc2.averagePixels2()
				time.sleep(2)

				pic_number = 3
				camera.capture(self.image_path+"ic3_"+isample+"_fulltest.png")
				pc3 = PixelCounter(self.image_path+"ic3_"+isample+"_fulltest.png",pic_number)
				three_r,three_g,three_b,three_count = pc3.averagePixels3()
				time.sleep(2)

				pic_number = 4
				camera.capture(self.image_path+"ic4_"+isample+"_fulltest.png")
				pc4 = PixelCounter(self.image_path+"ic4_"+isample+"_fulltest.png",pic_number)
				four_r,four_g,four_b,four_count = pc4.averagePixels4()
				time.sleep(2)

				pic_number = 5
				camera.capture(self.image_path+"ic5_"+isample+"_fulltest.png")
				pc5 = PixelCounter(self.image_path+"ic5_"+isample+"_fulltest.png",pic_number)
				five_r,five_g,five_b,five_count = pc5.averagePixels5()

				avg_r = (two_r + three_r +four_r + five_r) / 4
				avg_g = (two_g + three_g +four_g + five_g) / 4
				avg_b = (two_b + three_b +four_b + five_b) / 4
				
				avg_r = int(avg_r)
				avg_g = int(avg_g)
				avg_b = int(avg_b)					

			except (KeyError, ZeroDivisionError, serial.SerialException, ValueError) as e:
				errorstring = "/E-I_cal_imagecapture()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")			        
			finally:
				camera.close()
				return avg_r, avg_g, avg_b                        
				                   

		def oc_cal_imagecapture(self,isample):
			try:
				# assumes you have a test.jpg in the working directory! 
				self.machine_status_label.configure(text = "")
				pic_number = 1
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(2)
				camera.capture(self.image_path+"occ1_"+isample+"_fulltest.png")
				pc1 = PixelCounter(self.image_path+"occ1_"+isample+"_fulltest.png",pic_number)
				one_r,one_g,one_b,one_count = pc1.averagePixels1()
				time.sleep(2)  

				pic_number = 2
				camera.capture(self.image_path+"occ2_"+isample+"_fulltest.png")
				pc2 = PixelCounter(self.image_path+"occ2_"+isample+"_fulltest.png",pic_number)
				two_r,two_g,two_b,two_count = pc2.averagePixels2()
				time.sleep(2)

				pic_number = 3
				camera.capture(self.image_path+"occ3_"+isample+"_fulltest.png")
				pc3 = PixelCounter(self.image_path+"occ3_"+isample+"_fulltest.png",pic_number)
				three_r,three_g,three_b,three_count = pc3.averagePixels3()
				time.sleep(2)

				pic_number = 4
				camera.capture(self.image_path+"occ4_"+isample+"_fulltest.png")
				pc4 = PixelCounter(self.image_path+"occ4_"+isample+"_fulltest.png",pic_number)
				four_r,four_g,four_b,four_count = pc4.averagePixels4()
				time.sleep(2)

				pic_number = 5
				camera.capture(self.image_path+"occ5_"+isample+"_fulltest.png")
				pc5 = PixelCounter(self.image_path+"occ5_"+isample+"_fulltest.png",pic_number)
				five_r,five_g,five_b,five_count = pc5.averagePixels5()

				avg_r = (two_r + three_r +four_r + five_r) / 4
				avg_g = (two_g + three_g +four_g + five_g) / 4
				avg_b = (two_b + three_b +four_b + five_b) / 4
				
				avg_r = int(avg_r)
				avg_g = int(avg_g)
				avg_b = int(avg_b)					

			except (KeyError, ZeroDivisionError, serial.SerialException, ValueError) as e:
				errorstring = "/E-OC_cal_imagecapture()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")			        
			finally:
				camera.close()
				return avg_r, avg_g, avg_b                        

		def n_imagecapture(self):
			try:
				n_run_status = 0
				result = 0			
				# assumes you have a test.jpg in the working directory! 
				self.machine_status_label.configure(text = "")
				pic_number = 1
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(2)
				camera.capture(self.image_path+"N1_fulltest.png")
				pc1 = PixelCounter(self.image_path+"N1_fulltest.png",pic_number)
				one_r,one_g,one_b,one_count = pc1.averagePixels1()
				time.sleep(2)  

				pic_number = 2
				camera.capture(self.image_path+"N2_fulltest.png")
				pc2 = PixelCounter(self.image_path+"N2_fulltest.png",pic_number)
				two_r,two_g,two_b,two_count = pc2.averagePixels2()
				time.sleep(2)

				pic_number = 3
				camera.capture(self.image_path+"N3_fulltest.png")
				pc3 = PixelCounter(self.image_path+"N3_fulltest.png",pic_number)
				three_r,three_g,three_b,three_count = pc3.averagePixels3()
				time.sleep(2)

				pic_number = 4
				camera.capture(self.image_path+"N4_fulltest.png")
				pc4 = PixelCounter(self.image_path+"N4_fulltest.png",pic_number)
				four_r,four_g,four_b,four_count = pc4.averagePixels4()
				time.sleep(2)

				pic_number = 5
				camera.capture(self.image_path+"N5_fulltest.png")
				pc5 = PixelCounter(self.image_path+"N5_fulltest.png",pic_number)
				five_r,five_g,five_b,five_count = pc5.averagePixels5()

				avg_r = (two_r + three_r +four_r + five_r) / 4
				avg_g = (two_g + three_g +four_g + five_g) / 4
				avg_b = (two_b + three_b +four_b + five_b) / 4
				
				avg_r = int (avg_r)
				avg_g = int (avg_g)
				avg_b = int (avg_b)
				
#########################################################################################################################################
		
				with open(self.image_path+"rgb_result.json","r+") as e:
					a=json.load(e)	
				a["n_rgb"]["result_n_r"] = avg_r
				a["n_rgb"]["result_n_g"] = avg_g				
				a["n_rgb"]["result_n_b"] = avg_b				

				obj=a

				with open(self.image_path+"rgb_result.json","w")as e:
					json.dump(obj,e)
				with open(self.image_path+"rgb_result.json","r+") as e:
					a=json.load(e)

#########################################################################################################################################				

				w,h = 100, 100
				data = np.zeros((h,w,3), dtype= np.uint8)

				for i in range(w):
						for j in range(h):
								data[i][j] = [avg_r,avg_g,avg_b]
				img = Image.fromarray(data, 'RGB')
				img.save(self.image_path+"Ntest.png")
				time.sleep(2)
				with open(self.image_path+"Ntest.png","rb") as imageFile:
						test_image = base64.b64encode(imageFile.read())

				fopn = open(self.image_path+"testid", "r")
				read_testid_count = fopn.read()
				fopn.close()
				split_test_id = read_testid_count.split('_')
				read_testid_count_int = int(split_test_id[1]) + 1
				userid = uuid.uuid4()
				fopnwrite = open(self.image_path+"testid","w")
				fopnwrite.write(str(userid) +"_"+ str(read_testid_count_int))
				fopnwrite.close()
				fopnread = open(self.image_path+"testid","r")
				test_id = fopnread.read()
				#test_id = int(test_id) 

				test_image = str(test_image.decode())
				#test_id = "K0006"
				#test_id = str(xyz)

				with open(self.npk_calibration_values_path) as json_file:
					n_calib_data_from_json_file = json.load(json_file)	

				n0r = n_calib_data_from_json_file["calibration"]["N"]["0"]["r"]
				n5r = n_calib_data_from_json_file["calibration"]["N"]["5"]["r"]
				n10r = n_calib_data_from_json_file["calibration"]["N"]["10"]["r"]
				n20r = n_calib_data_from_json_file["calibration"]["N"]["20"]["r"]	
				n30r = n_calib_data_from_json_file["calibration"]["N"]["30"]["r"]	
				n40r = n_calib_data_from_json_file["calibration"]["N"]["40"]["r"]	

				n0g = n_calib_data_from_json_file["calibration"]["N"]["0"]["g"]
				n5g = n_calib_data_from_json_file["calibration"]["N"]["5"]["g"]
				n10g = n_calib_data_from_json_file["calibration"]["N"]["10"]["g"]
				n20g = n_calib_data_from_json_file["calibration"]["N"]["20"]["g"]	
				n30g = n_calib_data_from_json_file["calibration"]["N"]["30"]["g"]	
				n40g = n_calib_data_from_json_file["calibration"]["N"]["40"]["g"]		

				n0b = n_calib_data_from_json_file["calibration"]["N"]["0"]["b"]
				n5b = n_calib_data_from_json_file["calibration"]["N"]["5"]["b"]
				n10b = n_calib_data_from_json_file["calibration"]["N"]["10"]["b"]
				n20b = n_calib_data_from_json_file["calibration"]["N"]["20"]["b"]	
				n30b = n_calib_data_from_json_file["calibration"]["N"]["30"]["b"]	
				n40b = n_calib_data_from_json_file["calibration"]["N"]["40"]["b"]	
				
				x = {
				"id": test_id,
				"testId":"ddd64497-43e0-4289-a84f-6890ff80cf20",
				"dilution": 1,
				"calibration": [
				{
				"value": 0,
				"rgb": [n0r,n0g,n0b]
				},
				{
				"value": 5,
				"rgb": [n5r,n5g,n5b]
				},
				{
				"value": 10,
				"rgb": [n10r,n10g,n10b]
				},
				{
				"value": 20,
				"rgb": [n20r,n20g,n20b]
				},
				{
				"value": 30,
				"rgb": [n30r,n30g,n30b]
				},
				{
				"value": 40,
				"rgb": [n40r,n40g,n40b]
				}
				],
				"device": [
				{
				"model": "Krishitantra V1.0",
				"cameraMegaPixel": 8
				}
				],
				"image": test_image
				}
				
				for i_request in range(0,5):
					try:
						r = requests.post('https://flhszwy9k7.execute-api.us-west-1.amazonaws.com/alpha/calculate', json=x)
						return_request_value = r.json()
						result_str = json.dumps(return_request_value)
						result_dict = eval(result_str)
						result = result_dict["result"]["value"]
						n_run_status = 1
						break
					except Exception as e:
						self.machine_status_label.configure(text = "No internet Connection.. Please connect to internet within 30 Secs.. ")
						logging.warning("%s",e)	
						logging.exception("Exception occurred")		        
						n_run_status = 2
					time.sleep(12)
			except Exception as e:
				errorstring = "/E-N_imagecapture()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				if n_run_status == 2:
					self.internet_conn_label.configure(text = "")
					self.machine_status_label.configure(text = "Nitrogen test failed due to Poor or No internet")
				camera.close()
				return result   
				        
		def p_imagecapture(self):
			try:
				p_run_status = 0			
				result = 0
				# assumes you have a test.jpg in the working directory! 
				self.machine_status_label.configure(text = "")
				pic_number = 1
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(2)
				camera.capture(self.image_path+"P1_fulltest.png")
				pc1 = PixelCounter(self.image_path+"P1_fulltest.png",pic_number)
				one_r,one_g,one_b,one_count = pc1.averagePixels1()
				time.sleep(2)  

				pic_number = 2
				camera.capture(self.image_path+"P2_fulltest.png")
				pc2 = PixelCounter(self.image_path+"P2_fulltest.png",pic_number)
				two_r,two_g,two_b,two_count = pc2.averagePixels2()
				time.sleep(2)

				pic_number = 3
				camera.capture(self.image_path+"P3_fulltest.png")
				pc3 = PixelCounter(self.image_path+"P3_fulltest.png",pic_number)
				three_r,three_g,three_b,three_count = pc3.averagePixels3()
				time.sleep(2)

				pic_number = 4
				camera.capture(self.image_path+"P4_fulltest.png")
				pc4 = PixelCounter(self.image_path+"P4_fulltest.png",pic_number)
				four_r,four_g,four_b,four_count = pc4.averagePixels4()
				time.sleep(2)

				pic_number = 5
				camera.capture(self.image_path+"P5_fulltest.png")
				pc5 = PixelCounter(self.image_path+"P5_fulltest.png",pic_number)
				five_r,five_g,five_b,five_count = pc5.averagePixels5()

				avg_r = (two_r + three_r +four_r + five_r) / 4
				avg_g = (two_g + three_g +four_g + five_g) / 4
				avg_b = (two_b + three_b +four_b + five_b) / 4
				
				avg_r = int (avg_r)
				avg_g = int (avg_g)
				avg_b = int (avg_b)	
				
				with open(self.image_path+"rgb_result.json","r+") as e:
					a=json.load(e)	
				a["p_rgb"]["result_p_r"] = avg_r
				a["p_rgb"]["result_p_g"] = avg_g				
				a["p_rgb"]["result_p_b"] = avg_b				

				obj=a

				with open(self.image_path+"rgb_result.json","w")as e:
					json.dump(obj,e)
				with open(self.image_path+"rgb_result.json","r+") as e:
					a=json.load(e)

				w,h = 100, 100
				data = np.zeros((h,w,3), dtype= np.uint8)

				for i in range(w):
						for j in range(h):
								data[i][j] = [avg_r,avg_g,avg_b]
				img = Image.fromarray(data, 'RGB')
				img.save(self.image_path+"Ptest.png")
				time.sleep(2)
				with open(self.image_path+"Ptest.png","rb") as imageFile:
						test_image = base64.b64encode(imageFile.read())

				fopn = open(self.image_path+"testid", "r")
				read_testid_count = fopn.read()
				fopn.close()
				split_test_id = read_testid_count.split('_')
				read_testid_count_int = int(split_test_id[1]) + 1
				userid = uuid.uuid4()
				fopnwrite = open(self.image_path+"testid","w")
				fopnwrite.write(str(userid) +"_"+ str(read_testid_count_int))
				fopnwrite.close()
				fopnread = open(self.image_path+"testid","r")
				test_id = fopnread.read()
				#test_id = int(test_id) 

				test_image = str(test_image.decode())

				with open(self.npk_calibration_values_path) as json_file:
					p_calib_data_from_json_file = json.load(json_file)					        

				p0r = p_calib_data_from_json_file["calibration"]["P"]["0"]["r"]
				p5r = p_calib_data_from_json_file["calibration"]["P"]["5"]["r"]
				p10r = p_calib_data_from_json_file["calibration"]["P"]["10"]["r"]
				p15r = p_calib_data_from_json_file["calibration"]["P"]["15"]["r"]	
				p20r = p_calib_data_from_json_file["calibration"]["P"]["20"]["r"]	
				p25r = p_calib_data_from_json_file["calibration"]["P"]["25"]["r"]	

				p0g = p_calib_data_from_json_file["calibration"]["P"]["0"]["g"]
				p5g = p_calib_data_from_json_file["calibration"]["P"]["5"]["g"]
				p10g = p_calib_data_from_json_file["calibration"]["P"]["10"]["g"]
				p15g = p_calib_data_from_json_file["calibration"]["P"]["15"]["g"]	
				p20g = p_calib_data_from_json_file["calibration"]["P"]["20"]["g"]	
				p25g = p_calib_data_from_json_file["calibration"]["P"]["25"]["g"]		

				p0b = p_calib_data_from_json_file["calibration"]["P"]["0"]["b"]
				p5b = p_calib_data_from_json_file["calibration"]["P"]["5"]["b"]
				p10b = p_calib_data_from_json_file["calibration"]["P"]["10"]["b"]
				p15b = p_calib_data_from_json_file["calibration"]["P"]["15"]["b"]	
				p20b = p_calib_data_from_json_file["calibration"]["P"]["20"]["b"]	
				p25b = p_calib_data_from_json_file["calibration"]["P"]["25"]["b"]					        

				x = {
				"id": test_id,
				"testId":"ddd64497-43e0-4289-a84f-6890ff80cf20",
				"dilution": 1,
				"calibration": [
				{
				"value": 0,
				"rgb": [p0r,p0g,p0b]
				},
				{
				"value": 5,
				"rgb": [p5r,p5g,p5b]
				},
				{
				"value": 10,
				"rgb": [p10r,p10g,p10b]
				},
				{
				"value": 15,
				"rgb": [p15r,p15g,p15b]
				},
				{
				"value": 20,
				"rgb": [p20r,p20g,p20b]
				},
				{
				"value": 25,
				"rgb": [p25r,p25g,p25b]
				}
				],
				"device": [
				{
				"model": "Krishitantra V1.0",
				"cameraMegaPixel": 8
				}
				],
				"image": test_image
				}
				
				for i_request in range(0,5):
					try:
						r = requests.post('https://flhszwy9k7.execute-api.us-west-1.amazonaws.com/alpha/calculate', json=x)
						return_request_value = r.json()
						result_str = json.dumps(return_request_value)
						result_dict = eval(result_str)
						result = result_dict["result"]["value"]
						p_run_status = 1
						break
					except Exception as e:
						p_run_status = 2
						logging.warning ("%s",e)
						logging.exception("Exception occurred")
					time.sleep(2)

			except Exception as e:
				errorstring = "/E-P_imagecapture()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				if p_run_status == 2:
					self.internet_conn_label.configure(text = "")
					self.machine_status_label.configure(text = "Phosphorus test failed due to Poor or No internet")
				camera.close()
				return result                        
				        
		def k_imagecapture(self):
			try:
				k_run_status = 0			
				result = 0
				self.machine_status_label.configure(text = "")
				pic_number = 1
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(2)
				camera.capture(self.image_path+"K1_fulltest.png")
				pc1 = PotassiumPixelCounter(self.image_path+"K1_fulltest.png",pic_number)
				one_r,one_g,one_b,one_count = pc1.paveragePixels1()
				time.sleep(2)  

				pic_number = 2
				camera.capture(self.image_path+"K2_fulltest.png")
				pc2 = PotassiumPixelCounter(self.image_path+"K2_fulltest.png",pic_number)
				two_r,two_g,two_b,two_count = pc2.paveragePixels2()
				time.sleep(2)

				pic_number = 3
				camera.capture(self.image_path+"K3_fulltest.png")
				pc3 = PotassiumPixelCounter(self.image_path+"K3_fulltest.png",pic_number)
				three_r,three_g,three_b,three_count = pc3.paveragePixels3()
				time.sleep(2)

				pic_number = 4
				camera.capture(self.image_path+"K4_fulltest.png")
				pc4 = PotassiumPixelCounter(self.image_path+"K4_fulltest.png",pic_number)
				four_r,four_g,four_b,four_count = pc4.paveragePixels4()
				time.sleep(2)

				pic_number = 5
				camera.capture(self.image_path+"K5_fulltest.png")
				pc5 = PotassiumPixelCounter(self.image_path+"K5_fulltest.png",pic_number)
				five_r,five_g,five_b,five_count = pc5.paveragePixels5()

				avg_r = (two_r + three_r +four_r + five_r) / 4
				avg_g = (two_g + three_g +four_g + five_g) / 4
				avg_b = (two_b + three_b +four_b + five_b) / 4
				
				avg_r = int (avg_r)
				avg_g = int (avg_g)
				avg_b = int (avg_b)	
				
				with open(self.image_path+"rgb_result.json","r+") as e:
					a=json.load(e)	
				a["k_rgb"]["result_k_r"] = avg_r
				a["k_rgb"]["result_k_g"] = avg_g				
				a["k_rgb"]["result_k_b"] = avg_b				

				obj=a

				with open(self.image_path+"rgb_result.json","w")as e:
					json.dump(obj,e)
				with open(self.image_path+"rgb_result.json","r+") as e:
					a=json.load(e)

				w,h = 100, 100
				data = np.zeros((h,w,3), dtype= np.uint8)

				for i in range(w):
						for j in range(h):
								data[i][j] = [avg_r,avg_g,avg_b]
				img = Image.fromarray(data, 'RGB')
				img.save(self.image_path+"Ktest.png")
				time.sleep(2)
				with open(self.image_path+"Ktest.png","rb") as imageFile:
						test_image = base64.b64encode(imageFile.read())

				fopn = open(self.image_path+"testid", "r")
				read_testid_count = fopn.read()
				fopn.close()
				split_test_id = read_testid_count.split('_')
				read_testid_count_int = int(split_test_id[1]) + 1
				userid = uuid.uuid4()
				fopnwrite = open(self.image_path+"testid","w")
				fopnwrite.write(str(userid) +"_"+ str(read_testid_count_int))
				fopnwrite.close()
				fopnread = open(self.image_path+"testid","r")
				test_id = fopnread.read()
				#test_id = int(test_id) 

				test_image = str(test_image.decode())
				#test_id = "K0006"
				#test_id = str(xyz)

				with open(self.npk_calibration_values_path) as json_file:
					k_calib_data_from_json_file = json.load(json_file)					        

				k0r = k_calib_data_from_json_file["calibration"]["K"]["0"]["r"]
				k10r = k_calib_data_from_json_file["calibration"]["K"]["10"]["r"]
				k20r = k_calib_data_from_json_file["calibration"]["K"]["20"]["r"]	
				k40r = k_calib_data_from_json_file["calibration"]["K"]["40"]["r"]	

				k0g = k_calib_data_from_json_file["calibration"]["K"]["0"]["g"]
				k10g = k_calib_data_from_json_file["calibration"]["K"]["10"]["g"]
				k20g = k_calib_data_from_json_file["calibration"]["K"]["20"]["g"]	
				k40g = k_calib_data_from_json_file["calibration"]["K"]["40"]["g"]		

				k0b = k_calib_data_from_json_file["calibration"]["K"]["0"]["b"]
				k10b = k_calib_data_from_json_file["calibration"]["K"]["10"]["b"]
				k20b = k_calib_data_from_json_file["calibration"]["K"]["20"]["b"]	
				k40b = k_calib_data_from_json_file["calibration"]["K"]["40"]["b"]					        

				x = {
				"id": test_id,
				"testId":"ddd64497-43e0-4289-a84f-6890ff80cf20",
				"dilution": 1,
				"calibration": [
				{
				"value": 0,
				"rgb": [k0r,k0g,k0b]
				},
				{
				"value": 10,
				"rgb": [k10r,k10g,k10b]
				},
				{
				"value": 20,
				"rgb": [k20r,k20g,k20b]
				},
				{
				"value": 40,
				"rgb": [k40r,k40g,k40b]
				}],
				"device": [
				{
				"model": "Krishitantra V1.0",
				"cameraMegaPixel": 8
				}
				],
				"image": test_image
				}
				
				for i_request in range(0,5):
					try:
						r = requests.post('https://flhszwy9k7.execute-api.us-west-1.amazonaws.com/alpha/calculate', json=x)
						return_request_value = r.json()
						result_str = json.dumps(return_request_value)
						result_dict = eval(result_str)
						result = result_dict["result"]["value"]
						k_run_status = 1
						break
					except Exception as e:
						k_run_status = 2
						logging.info ("%s",e)
					time.sleep(2)

			except Exception as e:
				errorstring = "/E-K_imagecapture()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				if k_run_status == 2:
					self.internet_conn_label.configure(text = "")
					self.machine_status_label.configure(text = "Potassium test failed due to Poor or No internet")
				camera.close()
				return result 
				
		def i_imagecapture(self):
			try:
				i_run_status = 0			
				result = 0
				# assumes you have a test.jpg in the working directory! 
				self.machine_status_label.configure(text = "")
				pic_number = 1
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(2)
				camera.capture(self.image_path+"I1_fulltest.png")
				pc1 = PixelCounter(self.image_path+"I1_fulltest.png",pic_number)
				one_r,one_g,one_b,one_count = pc1.averagePixels1()
				time.sleep(2)  

				pic_number = 2
				camera.capture(self.image_path+"I2_fulltest.png")
				pc2 = PixelCounter(self.image_path+"I2_fulltest.png",pic_number)
				two_r,two_g,two_b,two_count = pc2.averagePixels2()
				time.sleep(2)

				pic_number = 3
				camera.capture(self.image_path+"I3_fulltest.png")
				pc3 = PixelCounter(self.image_path+"I3_fulltest.png",pic_number)
				three_r,three_g,three_b,three_count = pc3.averagePixels3()
				time.sleep(2)

				pic_number = 4
				camera.capture(self.image_path+"I4_fulltest.png")
				pc4 = PixelCounter(self.image_path+"I4_fulltest.png",pic_number)
				four_r,four_g,four_b,four_count = pc4.averagePixels4()
				time.sleep(2)

				pic_number = 5
				camera.capture(self.image_path+"I5_fulltest.png")
				pc5 = PixelCounter(self.image_path+"I5_fulltest.png",pic_number)
				five_r,five_g,five_b,five_count = pc5.averagePixels5()

				avg_r = (two_r + three_r +four_r + five_r) / 4
				avg_g = (two_g + three_g +four_g + five_g) / 4
				avg_b = (two_b + three_b +four_b + five_b) / 4
				
				avg_r = int (avg_r)
				avg_g = int (avg_g)
				avg_b = int (avg_b)	
				
				with open(self.image_path+"rgb_result.json","r+") as e:
					a=json.load(e)	
				a["i_rgb"]["result_i_r"] = avg_r
				a["i_rgb"]["result_i_g"] = avg_g				
				a["i_rgb"]["result_i_b"] = avg_b				

				obj=a

				with open(self.image_path+"rgb_result.json","w")as e:
					json.dump(obj,e)
				with open(self.image_path+"rgb_result.json","r+") as e:
					a=json.load(e)

				w,h = 100, 100
				data = np.zeros((h,w,3), dtype= np.uint8)

				for i in range(w):
						for j in range(h):
								data[i][j] = [avg_r,avg_g,avg_b]
				img = Image.fromarray(data, 'RGB')
				img.save(self.image_path+"Itest.png")
				time.sleep(2)
				with open(self.image_path+"Itest.png","rb") as imageFile:
						test_image = base64.b64encode(imageFile.read())

				fopn = open(self.image_path+"testid", "r")
				read_testid_count = fopn.read()
				fopn.close()
				split_test_id = read_testid_count.split('_')
				read_testid_count_int = int(split_test_id[1]) + 1
				userid = uuid.uuid4()
				fopnwrite = open(self.image_path+"testid","w")
				fopnwrite.write(str(userid) +"_"+ str(read_testid_count_int))
				fopnwrite.close()
				fopnread = open(self.image_path+"testid","r")
				test_id = fopnread.read()
				#test_id = int(test_id) 

				test_image = str(test_image.decode())

				with open(self.npk_calibration_values_path) as json_file:
					i_calib_data_from_json_file = json.load(json_file)					        

				i00r = i_calib_data_from_json_file["calibration"]["I"]["0.0"]["r"]
				i05r = i_calib_data_from_json_file["calibration"]["I"]["0.5"]["r"]
				i10r = i_calib_data_from_json_file["calibration"]["I"]["1.0"]["r"]
				i15r = i_calib_data_from_json_file["calibration"]["I"]["1.5"]["r"]	
				i20r = i_calib_data_from_json_file["calibration"]["I"]["2.0"]["r"]	
				
				i00g = i_calib_data_from_json_file["calibration"]["I"]["0.0"]["g"]
				i05g = i_calib_data_from_json_file["calibration"]["I"]["0.5"]["g"]
				i10g = i_calib_data_from_json_file["calibration"]["I"]["1.0"]["g"]
				i15g = i_calib_data_from_json_file["calibration"]["I"]["1.5"]["g"]	
				i20g = i_calib_data_from_json_file["calibration"]["I"]["2.0"]["g"]	
				
				i00b = i_calib_data_from_json_file["calibration"]["I"]["0.0"]["b"]
				i05b = i_calib_data_from_json_file["calibration"]["I"]["0.5"]["b"]
				i10b = i_calib_data_from_json_file["calibration"]["I"]["1.0"]["b"]
				i15b = i_calib_data_from_json_file["calibration"]["I"]["1.5"]["b"]	
				i20b = i_calib_data_from_json_file["calibration"]["I"]["2.0"]["b"]	
				

				x = {
				"id": test_id,
				"testId":"ddd64497-43e0-4289-a84f-6890ff80cf20",
				"dilution": 1,
				"calibration": [
				{
				"value": 0,
				"rgb": [i00r,i00g,i00b]
				},
				{
				"value": 0.5,
				"rgb": [i05r,i05g,i05b]
				},
				{
				"value": 1.0,
				"rgb": [i10r,i10g,i10b]
				},
				{
				"value": 1.5,
				"rgb": [i15r,i15g,i15b]
				},
				{
				"value": 2.0,
				"rgb": [i20r,i20g,i20b]
				}
				],
				"device": [
				{
				"model": "Krishitantra V1.0",
				"cameraMegaPixel": 8
				}
				],
				"image": test_image
				}
				
				for i_request in range(0,5):
					try:
						r = requests.post('https://flhszwy9k7.execute-api.us-west-1.amazonaws.com/alpha/calculate', json=x)
						return_request_value = r.json()
						result_str = json.dumps(return_request_value)
						result_dict = eval(result_str)
						result = result_dict["result"]["value"]
						i_run_status = 1
						break
					except Exception as e:
						i_run_status = 2
						logging.warning ("%s",e)
						logging.exception("Exception occurred")
					time.sleep(2)

			except Exception as e:
				errorstring = "/E-P_imagecapture()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				if i_run_status == 2:
					self.internet_conn_label.configure(text = "")
					self.machine_status_label.configure(text = "Iron test failed due to Poor or No internet")
				camera.close()
				return result                        

		def b_imagecapture(self):
			try:
				b_run_status = 0			
				result = 0
				# assumes you have a test.jpg in the working directory! 
				self.machine_status_label.configure(text = "")
				pic_number = 1
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(2)
				camera.capture(self.image_path+"B1_fulltest.png")
				pc1 = PixelCounter(self.image_path+"B1_fulltest.png",pic_number)
				one_r,one_g,one_b,one_count = pc1.averagePixels1()
				time.sleep(2)  

				pic_number = 2
				camera.capture(self.image_path+"B2_fulltest.png")
				pc2 = PixelCounter(self.image_path+"B2_fulltest.png",pic_number)
				two_r,two_g,two_b,two_count = pc2.averagePixels2()
				time.sleep(2)

				pic_number = 3
				camera.capture(self.image_path+"B3_fulltest.png")
				pc3 = PixelCounter(self.image_path+"B3_fulltest.png",pic_number)
				three_r,three_g,three_b,three_count = pc3.averagePixels3()
				time.sleep(2)

				pic_number = 4
				camera.capture(self.image_path+"B4_fulltest.png")
				pc4 = PixelCounter(self.image_path+"B4_fulltest.png",pic_number)
				four_r,four_g,four_b,four_count = pc4.averagePixels4()
				time.sleep(2)

				pic_number = 5
				camera.capture(self.image_path+"B5_fulltest.png")
				pc5 = PixelCounter(self.image_path+"B5_fulltest.png",pic_number)
				five_r,five_g,five_b,five_count = pc5.averagePixels5()

				avg_r = (two_r + three_r +four_r + five_r) / 4
				avg_g = (two_g + three_g +four_g + five_g) / 4
				avg_b = (two_b + three_b +four_b + five_b) / 4
				
				avg_r = int (avg_r)
				avg_g = int (avg_g)
				avg_b = int (avg_b)	
				
				with open(self.image_path+"rgb_result.json","r+") as e:
					a=json.load(e)	
				a["b_rgb"]["result_b_r"] = avg_r
				a["b_rgb"]["result_b_g"] = avg_g				
				a["b_rgb"]["result_b_b"] = avg_b				

				obj=a

				with open(self.image_path+"rgb_result.json","w")as e:
					json.dump(obj,e)
				with open(self.image_path+"rgb_result.json","r+") as e:
					a=json.load(e)

				w,h = 100, 100
				data = np.zeros((h,w,3), dtype= np.uint8)

				for i in range(w):
						for j in range(h):
								data[i][j] = [avg_r,avg_g,avg_b]
				img = Image.fromarray(data, 'RGB')
				img.save(self.image_path+"Btest.png")
				time.sleep(2)
				with open(self.image_path+"Btest.png","rb") as imageFile:
						test_image = base64.b64encode(imageFile.read())

				fopn = open(self.image_path+"testid", "r")
				read_testid_count = fopn.read()
				fopn.close()
				split_test_id = read_testid_count.split('_')
				read_testid_count_int = int(split_test_id[1]) + 1
				userid = uuid.uuid4()
				fopnwrite = open(self.image_path+"testid","w")
				fopnwrite.write(str(userid) +"_"+ str(read_testid_count_int))
				fopnwrite.close()
				fopnread = open(self.image_path+"testid","r")
				test_id = fopnread.read()
				#test_id = int(test_id) 

				test_image = str(test_image.decode())

				with open(self.npk_calibration_values_path) as json_file:
					b_calib_data_from_json_file = json.load(json_file)					        

				b00r = b_calib_data_from_json_file["calibration"]["B"]["0.0"]["r"]
				b025r = b_calib_data_from_json_file["calibration"]["B"]["0.25"]["r"]
				b05r = b_calib_data_from_json_file["calibration"]["B"]["0.5"]["r"]
				b10r = b_calib_data_from_json_file["calibration"]["B"]["1.0"]["r"]
				b15r = b_calib_data_from_json_file["calibration"]["B"]["1.5"]["r"]	
				b20r = b_calib_data_from_json_file["calibration"]["B"]["2.0"]["r"]	
				
				b00g = b_calib_data_from_json_file["calibration"]["B"]["0.0"]["g"]
				b025g = b_calib_data_from_json_file["calibration"]["B"]["0.25"]["g"]
				b05g = b_calib_data_from_json_file["calibration"]["B"]["0.5"]["g"]
				b10g = b_calib_data_from_json_file["calibration"]["B"]["1.0"]["g"]
				b15g = b_calib_data_from_json_file["calibration"]["B"]["1.5"]["g"]	
				b20g = b_calib_data_from_json_file["calibration"]["B"]["2.0"]["g"]	
				
				b00b = b_calib_data_from_json_file["calibration"]["B"]["0.0"]["b"]
				b025b = b_calib_data_from_json_file["calibration"]["B"]["0.25"]["b"]
				b05b = b_calib_data_from_json_file["calibration"]["B"]["0.5"]["b"]
				b10b = b_calib_data_from_json_file["calibration"]["B"]["1.0"]["b"]
				b15b = b_calib_data_from_json_file["calibration"]["B"]["1.5"]["b"]	
				b20b = b_calib_data_from_json_file["calibration"]["B"]["2.0"]["b"]	
				

				x = {
				"id": test_id,
				"testId":"ddd64497-43e0-4289-a84f-6890ff80cf20",
				"dilution": 1,
				"calibration": [
				{
				"value": 0,
				"rgb": [b00r,b00g,b00b]
				},
				{
				"value": 0.25,
				"rgb": [b025r,b025g,b025b]
				},				
				{
				"value": 0.5,
				"rgb": [b05r,b05g,b05b]
				},
				{
				"value": 1.0,
				"rgb": [b10r,b10g,b10b]
				},
				{
				"value": 1.5,
				"rgb": [b15r,b15g,b15b]
				},
				{
				"value": 2.0,
				"rgb": [b20r,b20g,b20b]
				}
				],
				"device": [
				{
				"model": "Krishitantra V1.0",
				"cameraMegaPixel": 8
				}
				],
				"image": test_image
				}
				
				for i_request in range(0,5):
					try:
						r = requests.post('https://flhszwy9k7.execute-api.us-west-1.amazonaws.com/alpha/calculate', json=x)
						return_request_value = r.json()
						result_str = json.dumps(return_request_value)
						result_dict = eval(result_str)
						result = result_dict["result"]["value"]
						b_run_status = 1
						break
					except Exception as e:
						b_run_status = 2
						logging.warning ("%s",e)
						logging.exception("Exception occurred")
					time.sleep(2)

			except Exception as e:
				errorstring = "/E-P_imagecapture()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				if b_run_status == 2:
					self.internet_conn_label.configure(text = "")
					self.machine_status_label.configure(text = "Boron test failed due to Poor or No internet")
				camera.close()
				return result  	
				
		def oc_imagecapture(self):
			try:
				oc_run_status = 0			
				result = 0
				# assumes you have a test.jpg in the working directory! 
				self.machine_status_label.configure(text = "")
				pic_number = 1
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(2)
				camera.capture(self.image_path+"OC1_fulltest.png")
				pc1 = PixelCounter(self.image_path+"OC1_fulltest.png",pic_number)
				one_r,one_g,one_b,one_count = pc1.averagePixels1()
				time.sleep(2)  

				pic_number = 2
				camera.capture(self.image_path+"OC2_fulltest.png")
				pc2 = PixelCounter(self.image_path+"OC2_fulltest.png",pic_number)
				two_r,two_g,two_b,two_count = pc2.averagePixels2()
				time.sleep(2)

				pic_number = 3
				camera.capture(self.image_path+"OC3_fulltest.png")
				pc3 = PixelCounter(self.image_path+"OC3_fulltest.png",pic_number)
				three_r,three_g,three_b,three_count = pc3.averagePixels3()
				time.sleep(2)

				pic_number = 4
				camera.capture(self.image_path+"OC4_fulltest.png")
				pc4 = PixelCounter(self.image_path+"OC4_fulltest.png",pic_number)
				four_r,four_g,four_b,four_count = pc4.averagePixels4()
				time.sleep(2)

				pic_number = 5
				camera.capture(self.image_path+"OC5_fulltest.png")
				pc5 = PixelCounter(self.image_path+"OC5_fulltest.png",pic_number)
				five_r,five_g,five_b,five_count = pc5.averagePixels5()

				avg_r = (two_r + three_r +four_r + five_r) / 4
				avg_g = (two_g + three_g +four_g + five_g) / 4
				avg_b = (two_b + three_b +four_b + five_b) / 4
				
				avg_r = int (avg_r)
				avg_g = int (avg_g)
				avg_b = int (avg_b)	
				
				with open(self.image_path+"rgb_result.json","r+") as e:
					a=json.load(e)	
				a["oc_rgb"]["result_oc_r"] = avg_r
				a["oc_rgb"]["result_oc_g"] = avg_g				
				a["oc_rgb"]["result_oc_b"] = avg_b				

				obj=a

				with open(self.image_path+"rgb_result.json","w")as e:
					json.dump(obj,e)
				with open(self.image_path+"rgb_result.json","r+") as e:
					a=json.load(e)

				w,h = 100, 100
				data = np.zeros((h,w,3), dtype= np.uint8)

				for i in range(w):
						for j in range(h):
								data[i][j] = [avg_r,avg_g,avg_b]
				img = Image.fromarray(data, 'RGB')
				img.save(self.image_path+"OCtest.png")
				time.sleep(2)
				with open(self.image_path+"OCtest.png","rb") as imageFile:
						test_image = base64.b64encode(imageFile.read())

				fopn = open(self.image_path+"testid", "r")
				read_testid_count = fopn.read()
				fopn.close()
				split_test_id = read_testid_count.split('_')
				read_testid_count_int = int(split_test_id[1]) + 1
				userid = uuid.uuid4()
				fopnwrite = open(self.image_path+"testid","w")
				fopnwrite.write(str(userid) +"_"+ str(read_testid_count_int))
				fopnwrite.close()
				fopnread = open(self.image_path+"testid","r")
				test_id = fopnread.read()
				#test_id = int(test_id) 

				test_image = str(test_image.decode())

				with open(self.npk_calibration_values_path) as json_file:
					oc_calib_data_from_json_file = json.load(json_file)					        

				oc00r = oc_calib_data_from_json_file["calibration"]["OC"]["0.0"]["r"]
				oc025r = oc_calib_data_from_json_file["calibration"]["OC"]["0.25"]["r"]
				oc05r = oc_calib_data_from_json_file["calibration"]["OC"]["0.5"]["r"]
				oc075r = oc_calib_data_from_json_file["calibration"]["OC"]["0.75"]["r"]	
				oc10r = oc_calib_data_from_json_file["calibration"]["OC"]["1.0"]["r"]	
				
				oc00g = oc_calib_data_from_json_file["calibration"]["OC"]["0.0"]["g"]
				oc025g = oc_calib_data_from_json_file["calibration"]["OC"]["0.25"]["g"]
				oc05g = oc_calib_data_from_json_file["calibration"]["OC"]["0.5"]["g"]
				oc075g = oc_calib_data_from_json_file["calibration"]["OC"]["0.75"]["g"]	
				oc10g = oc_calib_data_from_json_file["calibration"]["OC"]["1.0"]["g"]	
				
				oc00b = oc_calib_data_from_json_file["calibration"]["OC"]["0.0"]["b"]
				oc025b = oc_calib_data_from_json_file["calibration"]["OC"]["0.25"]["b"]
				oc05b = oc_calib_data_from_json_file["calibration"]["OC"]["0.5"]["b"]
				oc075b = oc_calib_data_from_json_file["calibration"]["OC"]["0.75"]["b"]	
				oc10b = oc_calib_data_from_json_file["calibration"]["OC"]["1.0"]["b"]	
				

				x = {
				"id": test_id,
				"testId":"ddd64497-43e0-4289-a84f-6890ff80cf20",
				"dilution": 1,
				"calibration": [
				{
				"value": 0,
				"rgb": [oc00r,oc00g,oc00b]
				},
				{
				"value": 0.25,
				"rgb": [oc025r,oc025g,oc025b]
				},
				{
				"value": 0.5,
				"rgb": [oc05r,oc05g,oc05b]
				},
				{
				"value": 0.75,
				"rgb": [oc075r,oc075g,oc075b]
				},
				{
				"value": 1.0,
				"rgb": [oc10r,oc10g,oc10b]
				}
				],
				"device": [
				{
				"model": "Krishitantra V1.0",
				"cameraMegaPixel": 8
				}
				],
				"image": test_image
				}
				
				for i_request in range(0,5):
					try:
						r = requests.post('https://flhszwy9k7.execute-api.us-west-1.amazonaws.com/alpha/calculate', json=x)
						return_request_value = r.json()
						result_str = json.dumps(return_request_value)
						result_dict = eval(result_str)
						result = result_dict["result"]["value"]
						oc_run_status = 1
						break
					except Exception as e:
						oc_run_status = 2
						logging.warning ("%s",e)
						logging.exception("Exception occurred")
					time.sleep(2)

			except Exception as e:
				errorstring = "/E-OC_imagecapture()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				if oc_run_status == 2:
					self.internet_conn_label.configure(text = "")
					self.machine_status_label.configure(text = "Organic Carbon test failed due to Poor or No internet")
				camera.close()
				return result                        
									               

		def focus_out(self):
			try:
				if self.keyboard_process is not None:
					self.keyboard_process.terminate()
					self.keyboard_process=None
			except Exception as e:
				errorstring = "/E-focus_out()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				self.bfocus_in['state']=ACTIVE
				pass                            

		def bfocus_out(self,event):
			try:
				if self.keyboard_process is not None:
					self.keyboard_process.terminate()
					self.keyboard_process=None
			except Exception as e:
				errorstring = "/E-bfocus_out()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass                            

		def focus_in(self):
			try:
				self.bfocus_in['state']=DISABLED 
				self.keyboard_process=subprocess.Popen("matchbox-keyboard")
			except Exception as e:
				errorstring = "/E-focus_in()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass   

		def baacklogin_page(self):
			try:
				self.forget_FRame.destroy()
				self.front_page()
			except Exception as e:
				errorstring = "/E-baacklogin_page()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 				
		
		def forget_check(self):
			try:
				#forgot_username=self.eforgetuser_name.get()
				forgot_email=self.eforget_email.get()

				#communicate to forget passsword page
				global URL
				url= URL+"password/email"

				payload={'email':forgot_email}

				headers={'content-type': 'application/json'}
				r=requests.post(url,data=json.dumps(payload),headers=headers)

				if(r.status_code == 200):
					messagebox.showinfo("Forget Password", "Reset Mail is sent to valid email ID...")
					self.forget_FRame.destroy()
					self.front_page()
			except Exception as e:
				errorstring = "/E-forget check()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass  					
    
		def forget_page(self):
			try:
				self.login_FRame.destroy()
				self.forget_FRame= Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)
				self.welcomemsg=Label(self.forget_FRame,text="Forget Password",bg="#F5F4EB",fg="#254E58",font="BOLD  18 ")
				Bback=Button(self.forget_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre 10",command=self.baacklogin_page)
		
				canvas=Canvas(self.forget_FRame,bg="#F5F4EB")
				canvas.create_rectangle(10, 10, 540, 240,outline="#fb0",fill="#F5F4EB")
				canvas.place(x=60,y=80,width=550,height=250)
		
				lforget_mail=Label(self.forget_FRame,text="Email",bg="#F5F4EB",fg="#254E58",font="BOLD  14 ")
				self.eforget_email=Entry(self.forget_FRame,bg="#F5F4EB",font=("Calibri",14),justify="left")
				bfarmer_register=Button(self.forget_FRame,text="Next",bg="#3e8ddc",fg="#fffdfd",font="centre 10",command=self.forget_check)
		
				self.forget_FRame.place(x=10,y=40,width=780,height=390)
				self.welcomemsg.place(x=60,y=30,height=30)
				lforget_mail.place(x=120,y=185,height=25)
				self.eforget_email.place(x=200,y=185,width=350)
				Bback.place(x=650,y=30,height=30,width=60)
				bfarmer_register.place(x=650,y=340,height=30,width=60)                  
				self.bfocus_in.place(x=60,y=5,width=40,height=20)    
				self.bfocus_out.place(x=120,y=15,width=40,height=20) 
			except Exception as e:
				errorstring = "/E-forget_page()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass				
    
		def fpo_logout(self):
			try:
				global URL
				global token
				url= URL +"logout"
				headers={'Authorization': "Bearer "+token}
				r=requests.post(url,headers=headers)       
				if(r.status_code == 200):
					self.Fpodashboard_FRame.destroy()
					self.front_page()
				else:
					pass
			except Exception as e:
				errorstring = "/E-fpo_logout()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 		            

		def bachfbodash(self):
			try:
				self.farmerLOGIN_FRame.destroy()
				self.fpo_dashboard()
			except Exception as e:
				errorstring = "/E-bachfbodash()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass		    
    
		def update_xdetails(self):
			try:    
				self.farmerxmangement_FRame.destroy()
				self.xfarmer_register()
			except Exception as e:
				errorstring = "/E-update_xdetails()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass			    

		def backfarmer_management(self):
			try:
				self.farmerxmangement_FRame.destroy()
				self.farm_dashboard()
			except Exception as e:
				errorstring = "/E-backfarmer_management()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass			    

		def backfpo_dash(self):
			try:
				self.testregi_FRame.destroy()
				self.fpo_dashboard()
			except Exception as e:
				errorstring = "/E-backfpo_dash()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass		    
###########################################################################
#################### check again ##########################################
###########################################################################

		def calculate(self,x,y):
			try:
				r=((y-x)/y)*100
				return r
			except Exception as e:
				errorstring = "/E-Calculate()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass	
						    
		'''
			def countdown(self,a):
				self.progress.start()
				self.timetext.configure(text="30")
				p = 0.00
				t = time.time()
				n = a
				# Loop while the number of seconds is less than the integer defined in "p"
				while p - t < n: 
				    p = time.time()
				    i=round((t+n) - p)
				    if p == round(t + n):
				        self.timetext.configure(text="Time's up!")
				    else:
				        
				        self.timetext.configure(text=i)
				        print(i,n)
				        unit=self.calculate(i,n)
				        print(unit)
				        if(unit==100):
				            self.progress.stop()
				            
				        else:    
				            self.progress['value']=unit

			def readdy(self):
				#self.c1.itemconfigure(self.r,fill="#FFA500")

				self.countdown(10)
		'''

		def countdown(self,a):
			try:
				self.timetext.configure(text="30")
				p = 0.00
				t = time.time()
				n = a
				msgbox_time_to_add = 0
				time_before_msgbox = 0
				es_n_time_before_msgbox = 0
				time_after_msgbox = 0
				es_n_time_after_msgbox = 0
				# Loop while the number of seconds is less than the integer defined in "p"
				while p - t < n + msgbox_time_to_add:
					self.msg_nitro.acquire()
					temp_flag = self.tablet_dispense 
					self.msg_nitro.release()
					
					self.es_nitro_selection.acquire()
					es_n_temp_flag = self.es_ph_ec_msg_flag
					self.es_nitro_selection.release()
									
					p = time.time()
					if p == t + n:
						#self.machine_status_label.configure(text = "Please wait for Next button to appear")
						self.timetext.configure(text="0")
						self.timetext_min.configure(text="0")
					elif self.tablet_dispense == 1:
						time_before_msgbox = time.time()
						while temp_flag == 1:
							self.msg_nitro.acquire()
							temp_flag = self.tablet_dispense
							self.msg_nitro.release()
							time.sleep(0.5)
						time_after_msgbox = time.time()
						msgbox_time_to_add = msgbox_time_to_add + round (time_after_msgbox - time_before_msgbox)
						self.tablet_dispense = 0	
					elif self.es_ph_ec_msg_flag == 1:
						es_n_time_before_msgbox = time.time()
						while es_n_temp_flag == 1:
							self.es_nitro_selection.acquire()
							es_n_temp_flag = self.es_ph_ec_msg_flag
							self.es_nitro_selection.release()
							time.sleep(0.5)
						es_n_time_after_msgboxtime_after_msgbox = time.time()
						msgbox_time_to_add = msgbox_time_to_add + round (es_n_time_after_msgboxtime_after_msgbox - es_n_time_before_msgbox)
						self.es_ph_ec_msg_flag = 0						
					else:    
						time_value = round((t+n+msgbox_time_to_add) - p) 
						min_value = int(time_value / 60)
						sec_value = time_value % 60
						self.timetext.configure(text=min_value)
						self.timetext_min.configure(text=sec_value)
					time.sleep(0.5)
			except Exception as e:
				errorstring = "/E-Countdown()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass      

		
		def readdy(self):
			try:
				ph_timer = 0
				ec_timer = 0
				n_timer = 0
				p_timer = 0
				k_timer = 0
				b_timer = 0
				i_timer = 0
				oc_timer = 0
					
				wash_nitro = 0
				wash_potash = 0
				wash_phos = 0
				wash_boron = 0
				wash_iron = 0
				wash_oc = 0
				flush_oc = 0			
				
				lst_values = [self.listboxx.get(idx) for idx in self.listboxx.curselection()]				
					
				if "pH" in lst_values:
					ph_timer = 70#65
				if "EC" in lst_values:
					ec_timer = 15#12
				if "Nitrogen" in lst_values:
					n_timer = 519#414#985
					wash_nitro = 45
					wash_potash = 0
					wash_phos = 0
					wash_boron = 0
					wash_iron = 0
					wash_oc = 0					
					flush_oc = 0
				if "Potassium" in lst_values:
					p_timer = 747#708#745
					wash_nitro = 0
					wash_potash = 45
					wash_phos = 0
					wash_boron = 0
					wash_iron = 0
					wash_oc = 0					
					flush_oc = 0
				if "Phosphorus" in lst_values:
					k_timer = 395#366#405
					wash_nitro = 0
					wash_potash = 0
					wash_phos = 45
					wash_boron = 0
					wash_iron = 0
					wash_oc = 0
					flush_oc = 0
				if "Boron" in lst_values:
					b_timer = 703#673
					wash_nitro = 0
					wash_potash = 0
					wash_phos = 0
					wash_boron = 45
					wash_iron = 0
					wash_oc = 0
					flush_oc = 0
				if "Iron" in lst_values:
					i_timer = 703#670
					wash_nitro = 0
					wash_potash = 0
					wash_phos = 0
					wash_boron = 0
					wash_iron = 45
					wash_oc = 0	
					flush_oc = 0														
				if "Organic Carbon" in lst_values:
					oc_timer = 94
					wash_nitro = 0
					wash_potash = 0
					wash_phos = 0
					wash_boron = 0
					wash_iron = 0
					wash_oc = 45
					flush_oc = 360

				timer_value_to_send = int(ph_timer) + int(ec_timer) + int(n_timer) + int(p_timer) + int(k_timer) + int(b_timer) + int(i_timer)+ int(oc_timer)
				timer_value_to_send = timer_value_to_send+ wash_nitro + wash_potash + wash_phos + wash_boron + wash_iron + wash_oc + flush_oc
				logging.info (timer_value_to_send)
				self.countdown(timer_value_to_send) 
				
			except Exception as e:
				errorstring = "/E-readdy()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass  
    	
    	
		def flush_end(self):
			try:
				self.bgohome['state']=DISABLED				
				with open(self.chemical_firmware_version) as equation_contents:
					equation_status_data = json.load(equation_contents)				        

				WashTestTube_DeviceFlush1 = equation_status_data["WashTestTube-DeviceFlush1"]
				WashTestTube_DeviceFlush2 = equation_status_data["WashTestTube-DeviceFlush2"]
				WashTestTube_DeviceFlush3 = equation_status_data["WashTestTube-DeviceFlush3"]
			
				WashCuvette_DeviceWash = equation_status_data["WashCuvette-DeviceWash"]		
				
				flush_success = 0
				DeviceFlush1 = "KT+PR:"+WashTestTube_DeviceFlush1+"\r\n"
				flush_ret_val = self.kt_sendcommand(DeviceFlush1,103,10)
				DeviceFlush2 = "KT+PR:"+WashTestTube_DeviceFlush2+"\r\n"
				flush_ret_val = self.kt_sendcommand(DeviceFlush2,160,10)	
				DeviceFlush3 = "KT+PR:"+WashTestTube_DeviceFlush3+"\r\n"
				flush_ret_val = self.kt_sendcommand(DeviceFlush3,80,10)						
				if flush_ret_val == "SUCCESS":
					self.bgohome['state']=NORMAL
					flush_success = 1
				else:
					flush_success = 0
			except Exception as e:
				errorstring = "/E-flush_end()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
				flush_success = 0
			finally:
				pass  		
		
		def goback_home(self):
			try:
				self.fpo_dashboard()
			except Exception as e:
				errorstring = "/E-goback_home()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass   		    
				    
		def goback_home_from_servicetest(self):
			try:
				texttosend = "KT+ABORT\r\n"
				read_abort_ret_val = self.kt_sendcommand(texttosend,0,10)			
				texttosend = "KT+EXTABORT\r\n"			
				ext_abort_ret_val = self.kt_send_external_abort_command(texttosend,0,10)			
			
				self.farmer_dashboard()
			except Exception as e:
				errorstring = "/E-goback_home_from_servicetest()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass  
				    
		def goback_cal_home_from_calibration(self):
			try:
				texttosend = "KT+ABORT\r\n"
				read_abort_ret_val = self.kt_sendcommand(texttosend,0,10)			
				texttosend = "KT+EXTABORT\r\n"			
				ext_abort_ret_val = self.kt_send_external_abort_command(texttosend,0,10)			
			
				self.calibration()
			except Exception as e:
				errorstring = "/E-goback_cal_home_from_calib()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 	
				    
		def goback_dashboard_from_calibration(self):
			try:
				texttosend = "KT+ABORT\r\n"
				read_abort_ret_val = self.kt_sendcommand(texttosend,2,10)			
				texttosend = "KT+EXTABORT\r\n"			
				ext_abort_ret_val = self.kt_send_external_abort_command(texttosend,0,10)			
			
				self.fpo_dashboard()
			except Exception as e:
				errorstring = "/E-goback_dashboard_from_calib()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				    
		def goback_service_from_softwareupdate(self):
			try:
				self.servicetest()
			except Exception as e:
				errorstring = "/E-goback_service_from_sw_update()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 	
				
		def goback_service_from_log(self):
			try:
				self.systemlog_FRame.destroy()
				del self.ret_app			
				self.servicetest()
			except Exception as e:
				errorstring = "/E-goback_service_from_log()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass				
				    
		def goback_home_from_settings(self):
			try:
				self.fpo_dashboard()
			except Exception as e:
				errorstring = "/E-goback-home_from_settings()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass  	
				    
		def valid_result_test(self,result,parameter):
			try:
				a=0
				if result.startswith(">"):
					a = result[1:]
					if "-1." in a:
						if parameter == "N":
							a = "210"
						if parameter == "A":
							a = "25"
						if parameter == "P":
							a = "125"
						if parameter == "K":
							a = "150"
						if parameter == "B":
							a = "125"
						if parameter == "I":
							a = "150"							
					else:
						a = float(a)		
				else:
					a = result[0:]
					if "-1." in a:
						if parameter == "N":
							a = "210"
						if parameter == "A":
							a = "25"
						if parameter == "P":
							a = "125"
						if parameter == "K":
							a = "150"
						if parameter == "B":
							a = "125"
						if parameter == "I":
							a = "150"							
					else:
						a = float(a)
				#return a
			except Exception as e:
				errorstring = "/E-valid_result_test()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				return a
				pass			
							    
		def show_report(self):
			try:
				self.machine_status_label.configure(text = "")
				global device_id
				global fr_name
				global Name
				
				nitro_value = 0
				phosphorus_value = 0
				potash_value = 0
				ph = 0
				ec = 0	
				boron_value = 0
				iron_value = 0
				oc_value = 0
				
				nitro_value_local_report = 0	
				phosphorus_value_local_report = 0
				potash_value_local_report = 0	
				boron_value_local_report = 0	
				iron_value_local_report = 0	
				oc_value_local_report = 0					
				
				phrange = "---"
				ecrange = "---"
				nrange = "---"
				prange = "---"
				krange = "---"
				brange = "---"
				irange = "---"
				ocrange = "---"				
				
				self.Timm_FRame.destroy()
				test_date=date.today()
				analysisdate=date.today()
				report_no="DEMO-123"
				self.report_FRame= Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)
				self.bgohome=Button(self.report_FRame,text="Home",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.goback_home)	
				sr_lst_values = [self.listboxx.get(idx) for idx in self.listboxx.curselection()]
				
				if "Nitrogen" in sr_lst_values or "Potassium" in sr_lst_values or "Phosphorus" in sr_lst_values or "Boron" in sr_lst_values or "Iron" in sr_lst_values or "Organic Carbon" in sr_lst_values:
					self.machine_status_label.configure(text = "System Rinsing... Please wait (approx 6 mins...)")				
					timerflushend = threading.Timer(0.1, self.flush_end)
					timerflushend.start()
				else:
					self.bgohome['state']=ACTIVE				
				
				im=Image.open(self.image_path+"krishitantralogo.png")
				photo=ImageTk.PhotoImage(im)  
				cv = Canvas(self.report_FRame)  
				cv.place(x=10,y=10,width=159,height=43)
				cv.create_image(0, 0, image=photo, anchor='nw')  
				com_address=Label(self.report_FRame,text="Address:\t\t2-53(1) Opp Janardhana Temple",bg="#F5F4EB",font="BOLD 8")
				com_address2=Label(self.report_FRame,text="\t\tPangala Udupi - 576122",bg="#F5F4EB",font="BOLD 8")
				com_email=Label(self.report_FRame,text="Phone Number:\t+91 6362380978",bg="#F5F4EB",font="BOLD 8")
				com_website=Label(self.report_FRame,text="Website:\t\tkrishitantra.com",bg="#F5F4EB",font="BOLD 8")
				lline=Label(self.report_FRame,text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg="#F5F4EB")
				ltest_result=Label(self.report_FRame,text="TEST RESULTS",bg="#F5F4EB",fg="#254E58",font="BOLD  9")    
				canvas=Canvas(self.report_FRame,bg="#F5F4EB")
				canvas.create_rectangle(10, 10, 370, 215,outline="#fb0",fill="#F5F4EB")
				com_farmername=Label(self.report_FRame,text="Farmer Name:",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
				com_farmername2=Label(self.report_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD 12")
				com_Testdate=Label(self.report_FRame,text="Test Date:",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
				com_Testdate2=Label(self.report_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD 12")
				com_organisationname=Label(self.report_FRame,text="Organization:",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
				com_organisationname2=Label(self.report_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD 12")
				com_analysis=Label(self.report_FRame,text="Analysis Date:",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
				com_analysis2=Label(self.report_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD 12")
				com_Deviceid=Label(self.report_FRame,text="Device ID:",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
				
				wrapper = textwrap.TextWrapper(width=50) 
				disp_device_id = wrapper.fill(text=device_id) 			
				com_Deviceid2=Label(self.report_FRame,text=disp_device_id,bg="#F5F4EB",fg="#254E58",font="BOLD 8")
				
			
				with open(self.result_path,"r+") as e:
					result_data=json.load(e)
				
				logging.info ("Show report ==> %s",result_data)	
				
				if "pH" in sr_lst_values:
					ph = result_data["pH"]	
					ph_float = float("{0:0.2f}".format(ph))
					if ph_float > 9.0:
						phrange = "Alkaline"
					elif ph_float > 8.6 or ph_float < 9.0:
						phrange = "Normal to Saline"
					elif ph_float > 6.0 or ph_float < 8.5:
						phrange = "Normal to Saline"
					elif ph_float < 6.0:
						phrange = "Acids"
				else:
					ph = "-"					  
				if "EC" in sr_lst_values:
					ec = result_data["EC"]
					ec_float = float("{0:0.2f}".format(ec))
					if ec_float < 1.0:
						ecrange = "Normal"
					elif ec_float > 1.0 or ec_float < 2.0:
						ecrange = "Critical for Germination"
					elif ec_float > 2.0 or ec_float < 4.0:
						ecrange = "Critical for Growth of the Sensitive Crops"
					elif ec_float > 4.0:
						ecrange = "Injurious to most crops"					
				else:
					ec = "-"
				if "Nitrogen" in sr_lst_values:
					nitrate_value = result_data["N"]
					valid_n_test_result = self.valid_result_test(nitrate_value,"N")
					temp_test_res = float (valid_n_test_result) * 2
					nitro_value = temp_test_res * 2.25
					nitro_value = float("{0:0.2f}".format(nitro_value))

					nitro_value_float = nitro_value
					if nitro_value_float < 240:
						nrange = "LOW"
					elif nitro_value_float >= 240 or nitro_value_float < 480:
						nrange = "MEDIUM"
					elif nitro_value_float > 480:
						nrange = "HIGH"
					
					nitro_value = str(nitro_value)
					if nitrate_value.startswith(">"):
						nitro_value_local_report = ">" + nitro_value
					elif nitrate_value.startswith("-1"):
						nitro_value_local_report = ">" + nitro_value
					else:
						nitro_value_local_report = nitro_value
				else:
					nitro_value = "-"
					nitro_value_local_report = "-"

				if "Phosphorus" in sr_lst_values:
					p_value = 	result_data["P"]
					valid_p_test_result = self.valid_result_test(p_value,"P")
					phosphorus_value = float (valid_p_test_result) * 2.25
					phosphorus_value = float("{0:0.2f}".format(phosphorus_value))	
					
					phosphorus_value_float = phosphorus_value
					if phosphorus_value_float < 11:
						prange = "LOW"
					elif phosphorus_value_float >= 11 or phosphorus_value_float < 22:
						prange = "MEDIUM"
					elif phosphorus_value_float > 22:
						prange = "HIGH"

					phosphorus_value = str(phosphorus_value)
					if p_value.startswith(">") or p_value.startswith("-1"):
						phosphorus_value_local_report = ">" + phosphorus_value
					else:
						phosphorus_value_local_report = phosphorus_value
				else:
					phosphorus_value = "-"
					phosphorus_value_local_report = "-"
											
				if "Potassium" in sr_lst_values:
					k_value = result_data["K"]  
					valid_k_test_result = self.valid_result_test(k_value,"K")
					potash_value = float (valid_k_test_result) * 2.25
					potash_value = float("{0:0.2f}".format(potash_value))
					
					potash_value_float = potash_value
					if potash_value_float < 110:
						krange = "LOW"
					elif potash_value_float >= 110 or potash_value_float < 280:
						krange = "MEDIUM"
					elif potash_value_float > 280:
						krange = "HIGH"
											
					potash_value = str(potash_value)	
					if k_value.startswith(">") or k_value.startswith("-1"):
						potash_value_local_report = ">" + potash_value
					else:
						potash_value_local_report = potash_value
				else:
					potash_value = "-"		
					potash_value_local_report = "-"		
					
				if "Boron" in sr_lst_values:
					b_value = result_data["B"]  
					valid_b_test_result = self.valid_result_test(b_value,"B")
					binc_value = float (valid_b_test_result) * 2.25
					binc_value = float("{0:0.2f}".format(binc_value))
					
					binc_value_float = binc_value
					if binc_value_float < 110:
						brange = "LOW"
					elif binc_value_float >= 110 or binc_value_float < 280:
						brange = "MEDIUM"
					elif binc_value_float > 280:
						brange = "HIGH"
											
					binc_value = str(binc_value)	
					if b_value.startswith(">") or b_value.startswith("-1"):
						boron_value_local_report = ">" + binc_value
					else:
						boron_value_local_report = binc_value
				else:
					binc_value = "-"		
					boron_value_local_report = "-"	
					
				if "Iron" in sr_lst_values:
					i_value = result_data["I"]  
					valid_i_test_result = self.valid_result_test(i_value,"I")
					iron_value = float (valid_i_test_result) * 2.25
					iron_value = float("{0:0.2f}".format(iron_value))
					
					iron_value_float = iron_value
					if iron_value_float < 110:
						irange = "LOW"
					elif iron_value_float >= 110 or iron_value_float < 280:
						irange = "MEDIUM"
					elif iron_value_float > 280:
						irange = "HIGH"
											
					iron_value = str(iron_value)	
					if i_value.startswith(">") or i_value.startswith("-1"):
						iron_value_local_report = ">" + iron_value
					else:
						iron_value_local_report = iron_value
				else:
					iron_value = "-"		
					iron_value_local_report = "-"	
					
				if "Organic Carbon" in sr_lst_values:
					oc_value = result_data["OC"]  
					valid_oc_test_result = self.valid_result_test(oc_value,"OC")
					orgcarbon_value = float (valid_oc_test_result) * 2.25
					orgcarbon_value = float("{0:0.2f}".format(orgcarbon_value))
					
					orgcarbon_value_float = orgcarbon_value
					if orgcarbon_value_float < 110:
						ocrange = "LOW"
					elif orgcarbon_value_float >= 110 or orgcarbon_value_float < 280:
						ocrange = "MEDIUM"
					elif orgcarbon_value_float > 280:
						ocrange = "HIGH"
											
					orgcarbon_value = str(orgcarbon_value)	
					if oc_value.startswith(">") or oc_value.startswith("-1"):
						orgcarbon_value_local_report = ">" + orgcarbon_value
					else:
						orgcarbon_value_local_report = orgcarbon_value
				else:
					orgcarbon_value = "-"		
					orgcarbon_value_local_report = "-"										
														
				disp_company_code = result_data["Company_code"]				
				
				'''			
				global URL
				global token
				global fr_uuid
				global fr_farmuuid

				url= URL +"farmers/"+fr_uuid+"/areas/"+fr_farmuuid+"/reports"
				payload={"n": nitro_value,"p": phosphorus_value,"k":potash_value,"ec":ec,"pH":ph,"a":"0","device":device_id, "Company_code": disp_company_code}
				headers={'Authorization': "Bearer "+token,'content-type': 'application/json'}
				r=requests.post(url,data=json.dumps(payload),headers=headers)       
				if(r.status_code == 200):
					logging.info ("Sent values to cloud")   
				else:
					logging.info (r.content)
					pass				
				'''
				
				str_desclaimer = "*Desclaimer:  Our report is not to be reproduced wholly or in part and cannot be used as an evidence in the court of law and should not be used in any advertising media without our prior written approval"
				wrapper_desclaimer = textwrap.TextWrapper(width=102) 
				disp_desclaimer = wrapper_desclaimer.fill(text=str_desclaimer) 
				#disp_desclaimer = textwrap.dedent(disp_desclaimer)			
					
				table = Table(self.report_FRame, ["Sl No", "Parameter", "Unit", "Range", "Results"], column_minwidths=[40, 120, 30, 60, 80])#[40, 180, 40, 80])
				table.place(x=390,y=150,width=380,height=138)
				table.set_data([([1,"pH","-",phrange,ph]),[2,"EC","mS/cm",ecrange,ec],[3,"Nitrate Nitrogen","kg/ha",nrange,nitro_value_local_report],[4,"Phosphorus","kg/ha",prange,phosphorus_value_local_report],[5,"Potassium","kg/ha", krange, potash_value_local_report],[6,"Boron","kg/ha", brange, boron_value_local_report],[7,"Iron","kg/ha", irange, iron_value_local_report]])  
				com_disclamier=Label(self.report_FRame,text=disp_desclaimer,bg="#F5F4EB",fg="#ff0000",font="BOLD  7")
				#com_disclamier2=Label(self.report_FRame,text="evidence in the court of law and should not be used in any advertising media without our",bg="#F5F4EB",fg="#ff0000",font="BOLD  7")
				#com_disclamier3=Label(self.report_FRame,text="prior written approval",bg="#F5F4EB",fg="#ff0000",font="BOLD  7")
				com_farmername2['text']=fr_name
				com_Testdate2['text']=test_date
				com_organisationname2['text']=Name
				com_analysis2['text']=analysisdate
				com_Deviceid2['text']=device_id
				self.report_FRame.place(x=10,y=40,width=780,height=390)
				com_address.place(x=480,y=5)
				com_address2.place(x=480,y=20)
				com_email.place(x=480,y=35)
				com_website.place(x=480,y=50)
				lline.place(x=0,y=65)
				ltest_result.place(x=420,y=100,width=300)
				canvas.place(x=10,y=100,width=380,height=225)
				com_farmername.place(x=30,y=120)
				com_farmername2.place(x=150,y=120)
				com_Testdate.place(x=30,y=150)
				com_Testdate2.place(x=150,y=150)
				com_organisationname.place(x=30,y=180)
				com_organisationname2.place(x=150,y=180)
				com_analysis.place(x=30,y=210)
				com_analysis2.place(x=150,y=210)
				com_Deviceid.place(x=30,y=240)
				com_Deviceid2.place(x=120,y=240)
				com_disclamier.place(x=20,y=340)
				#com_disclamier2.place(x=20,y=350)
				#com_disclamier3.place(x=20,y=360)
				self.bgohome.place(x=690,y=340)
				self.root.mainloop()
			except Exception as e:
				errorstring = "/E-show_report()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				    pass  					
		
		def compute_test(self):
			try:
				self.machine_status_label.configure(text = "")
				
				lst_values = [self.listboxx.get(idx) for idx in self.listboxx.curselection()] 
				self.Timm_FRame=Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)				    
				    
				if "pH" in lst_values:		
					self.machine_status_label.configure(text = "")		
					Mainlabel=Label(self.Timm_FRame,text="Test Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")							
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.sublabel=Label(self.Timm_FRame,text="pH",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=100,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)
					
					self.min_label=Label(self.Timm_FRame,text="Min",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.min_label.place(x=520,y=170)
					self.sec_label=Label(self.Timm_FRame,text="Sec",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.sec_label.place(x=620,y=170)
					
						#a=nameff
   
					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)
						
				if "EC" in lst_values:	
					self.machine_status_label.configure(text = "")				
					Mainlabel=Label(self.Timm_FRame,text="Test Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")							
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.sublabel=Label(self.Timm_FRame,text="EC",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=100,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)
					
					self.min_label=Label(self.Timm_FRame,text="Min",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.min_label.place(x=520,y=170)
					self.sec_label=Label(self.Timm_FRame,text="Sec",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.sec_label.place(x=620,y=170)					

					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)

				if "Nitrogen" in lst_values:	
					self.machine_status_label.configure(text = "")				
					Mainlabel=Label(self.Timm_FRame,text="Test Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")							
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.sublabel=Label(self.Timm_FRame,text="Nitrogen",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=100,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)
					
					self.min_label=Label(self.Timm_FRame,text="Min",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.min_label.place(x=520,y=170)
					self.sec_label=Label(self.Timm_FRame,text="Sec",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.sec_label.place(x=620,y=170)					
					
					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)

				if "Potassium" in lst_values:	
					self.machine_status_label.configure(text = "")				
					Mainlabel=Label(self.Timm_FRame,text="Test Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")							
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.sublabel=Label(self.Timm_FRame,text="Potassium",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=100,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)
					
					self.min_label=Label(self.Timm_FRame,text="Min",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.min_label.place(x=520,y=170)
					self.sec_label=Label(self.Timm_FRame,text="Sec",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.sec_label.place(x=620,y=170)					
					
					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)
									            
				if "Phosphorus" in lst_values:	
					self.machine_status_label.configure(text = "")				
					Mainlabel=Label(self.Timm_FRame,text="Test Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")							
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.sublabel=Label(self.Timm_FRame,text="Phosphorus",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=100,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)
					
					self.min_label=Label(self.Timm_FRame,text="Min",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.min_label.place(x=520,y=170)
					self.sec_label=Label(self.Timm_FRame,text="Sec",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.sec_label.place(x=620,y=170)					
					
					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)
					
				if "Boron" in lst_values:	
					self.machine_status_label.configure(text = "")				
					Mainlabel=Label(self.Timm_FRame,text="Test Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")							
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.sublabel=Label(self.Timm_FRame,text="Boron",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=100,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)
					
					self.min_label=Label(self.Timm_FRame,text="Min",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.min_label.place(x=520,y=170)
					self.sec_label=Label(self.Timm_FRame,text="Sec",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.sec_label.place(x=620,y=170)					
					
					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)
					
				if "Iron" in lst_values:	
					self.machine_status_label.configure(text = "")				
					Mainlabel=Label(self.Timm_FRame,text="Test Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")							
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.sublabel=Label(self.Timm_FRame,text="Iron",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=100,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)
					
					self.min_label=Label(self.Timm_FRame,text="Min",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.min_label.place(x=520,y=170)
					self.sec_label=Label(self.Timm_FRame,text="Sec",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.sec_label.place(x=620,y=170)					
					
					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)
					
				if "Organic Carbon" in lst_values:	
					self.machine_status_label.configure(text = "")				
					Mainlabel=Label(self.Timm_FRame,text="Test Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")							
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.sublabel=Label(self.Timm_FRame,text="Organic Carbon",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=100,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)
					
					self.min_label=Label(self.Timm_FRame,text="Min",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.min_label.place(x=520,y=170)
					self.sec_label=Label(self.Timm_FRame,text="Sec",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					self.sec_label.place(x=620,y=170)					
					
					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)
																				
				self.timer=threading.Timer(0.2,self.readdy)
				self.timer.start()
				self.timer3 = threading.Timer(0.1, self.samplesolution)
				self.timer3.start()

			except Exception as e:
				errorstring = "/E-compute_test()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 	
				
		def samplesolution(self):
			try:
				self.machine_status_label.configure(text = "")
				self.c1.itemconfigure(self.r,fill="#FFA500")
				with open(self.chemical_firmware_version) as equation_contents:
					equation_status_data = json.load(equation_contents)
				
				d1n1_to_send = equation_status_data["D1N1"]
				d1n2_to_send = equation_status_data["D1N2"]
				d1n3_to_send = equation_status_data["D1N3"]
				
				d1p1_to_send = equation_status_data["D1P1"]
				d1p2_to_send = equation_status_data["D1P2"]
				d1p3_to_send = equation_status_data["D1P3"]					
				
				d1k1_to_send = equation_status_data["D1K1"]
				d1k2_to_send = equation_status_data["D1K2"]
				d1k3_to_send = equation_status_data["D1K3"]		

				d1b1_to_send = equation_status_data["D1B1"]
				d1b2_to_send = equation_status_data["D1B2"]
				d1b3_to_send = equation_status_data["D1B3"]
				
				d1i1_to_send = equation_status_data["D1I1"]
				d1i2_to_send = equation_status_data["D1I2"]
				d1i3_to_send = equation_status_data["D1I3"]							

				d1oc1_to_send = equation_status_data["D1OC1"]
				d1oc2_to_send = equation_status_data["D1OC2"]
				d1oc3_to_send = equation_status_data["D1OC3"]							
				
				WashTestTube_DeviceFlush1 = equation_status_data["WashTestTube-DeviceFlush1"]
				WashTestTube_DeviceFlush2 = equation_status_data["WashTestTube-DeviceFlush2"]
				WashTestTube_DeviceFlush3 = equation_status_data["WashTestTube-DeviceFlush3"]					
				
				WashCuvette_DeviceWash = equation_status_data["WashCuvette-DeviceWash"]		
			
				lst_values = [self.listboxx.get(idx) for idx in self.listboxx.curselection()]

				self.nnitro = 0
				self.pphosphorus = 0
				self.kpotash = 0
				self.pph = 0
				self.eec = 0
				self.bboron = 0
				self.iiron = 0
				self.ooc = 0				

				read_ph_val = 0
				read_ph_temp_val = 0
				read_ec_val = 0
				read_ec_temp_val = 0

				if "pH" in lst_values:	
					self.machine_status_label.configure(text = "")
					
					self.sublabel.configure(text="pH")									
					
					texttosend = "KT+STARTPH\r\n"
					startph_ret_val = self.kt_sendcommand(texttosend,60,10)		
					if 	startph_ret_val == "SUCCESS":					
						time.sleep(2)
						texttosend = "KT+READPH\r\n"
						readph_ret_val = self.kt_sendcommand(texttosend,5,10)	
						if readph_ret_val.startswith("KT+"):
								read_ph_n_temp_val = readph_ret_val.split('+')
								read_ph_val = read_ph_n_temp_val[1]
								read_ph_temp_val = read_ph_n_temp_val[2]
								
#####################################################################################################################################
					with open(self.image_path+"pump_servo_constants.json","r+") as e:
						a=json.load(e)	

					'''
					ph4temp = a["PH4"]["T"]
					ph7temp = a["PH7"]["T"]
					ph4const = a["PH4"]["PHCONST"]
					ph7const = a["PH7"]["PHCONST"]
					ph4v = a["PH4"]["V"]
					ph7v = a["PH7"]["V"]
					
					avg_temp = (ph4temp + ph7temp) / 2
					m = (ph4v - ph7v) / (ph7const - ph4const)
					m = m / (avg_temp + 273.15)

					a["CONSTANB"]["B"] = m
					a["CONSTANB"]["A"] = ph7v
					'''
					
					constanta = float(a["CONSTANB"]["A"])
					constantb = float(a["CONSTANB"]["B"])
					read_ph_val = float (read_ph_val)
					read_ph_temp_val = float(read_ph_temp_val)
						
					ph_meas=(7.0 +((constanta-read_ph_val)/(constantb*(read_ph_temp_val+273.15))));
					
					ph_meas = float("{0:0.2f}".format(ph_meas))
					
					'''
					obj=a

					with open(self.image_path+"pump_servo_constants.json","w")as e:
						json.dump(obj,e)
					with open(self.image_path+"pump_servo_constants.json","r+") as e:
						a=json.load(e)
					print(a)
					'''

					with open(self.result_path,"r+") as e:
						a=json.load(e)					    		
					#a.update({'pH':ph_meas})
					a["pH"] = ph_meas
					obj=a

					with open(self.result_path,"w")as e:
						json.dump(obj,e)
								
				if "EC" in lst_values:	
					self.machine_status_label.configure(text = "")			

					self.sublabel.configure(text="EC")
										
					texttosend = "KT+STARTEC\r\n"
					startph_ret_val = self.kt_sendcommand(texttosend,10,10)		
					if 	startph_ret_val == "SUCCESS":					
						time.sleep(2)
						texttosend = "KT+READEC\r\n"
						readec_ret_val = self.kt_sendcommand(texttosend,5,10)	
						if readec_ret_val.startswith("KT+"):
								read_ec_n_temp_val = readec_ret_val.split('+')
								read_ec_val = read_ec_n_temp_val[1]
								read_ec_temp_val = read_ec_n_temp_val[2]	
					
					with open(self.image_path+"pump_servo_constants.json","r+") as e:
						a=json.load(e)	

					k_constant = a["EC"]["K"] 
					
					Rwater = float(read_ec_val)
					K = float(k_constant)
					TemperatureCoef = 0.019
					Temperature = float(read_ec_temp_val)
					
					EC = 1000.0/(Rwater*K);
					EC25  =  EC/ (1+ TemperatureCoef*(Temperature-25.0));
					measured_ec_EC25=EC25;
					measured_ec_ppm=EC25*500;
					
					measured_ec_EC25 = float("{0:0.2f}".format(measured_ec_EC25))					
					
					with open(self.result_path,"r+") as e:
						a=json.load(e)	
					a["EC"] = measured_ec_EC25				    		
					#a.update({'EC':measured_ec_EC25})
					obj=a

					with open(self.result_path,"w")as e:
						json.dump(obj,e)
								
				if "Nitrogen" in lst_values:
					self.bsample_solution['state']=DISABLED
					#self.bocsample_solution['state']=DISABLED 
					self.bdistilled_water['state']=DISABLED
					self.bdistilled_water_ec['state']=DISABLED 					
					self.machine_status_label.configure(text = "")				
					self.sublabel.configure(text="Nitrogen")
											
					d1n1_cmd_to_send = "KT+PR:"+d1n1_to_send+"\r\n"
					#n1_ret_val = self.kt_sendcommand(d1n1_cmd_to_send,38,10)
					n1_ret_val = self.kt_sendcommand(d1n1_cmd_to_send,33,10)
					
					self.es_nitro_selection.acquire()
					self.es_ph_ec_msg_flag = 1
					self.es_nitro_selection.release()
					
					while self.es_or_nitrogen_flag == 1:
						self.machine_status_label.configure(text = "Please wait for Extraction Solution / Distilled Water to get dispensed")
						time.sleep(1)
						self.machine_status_label.configure(text = "")
						time.sleep(1)
						
					self.es_nitro_selection.acquire()
					self.es_ph_ec_msg_flag = 0
					self.es_nitro_selection.release()
					
					self.machine_status_label.configure(text = "")
					self.bsample_solution['state']=DISABLED
					#self.bocsample_solution['state']=DISABLED  
					self.bdistilled_water['state']=DISABLED
					self.bdistilled_water_ec['state']=DISABLED 					
					
					self.msg_nitro.acquire()
					self.tablet_dispense = 1						
					self.msg_nitro.release()
					messagebox.showinfo("Nitrogen Sample Preparation", "Place the testtube under Distilled water dipenser")
					self.msg_nitro.acquire()
					self.tablet_dispense = 0
					self.msg_nitro.release()
					
					texttosend = "KT+EXTDISPENSEM:10+05\r\n"
					n_ext_disp_ret_val = self.kt_send_external_command(texttosend,10,10)	
					
					#self.bocsample_solution['state']=ACTIVE
					self.bsample_solution['state']=ACTIVE 	
					self.bdistilled_water['state']=ACTIVE
					self.bdistilled_water_ec['state']=ACTIVE 									
			
					time.sleep(60)
			
					self.msg_nitro.acquire()
					self.tablet_dispense = 1						
					self.msg_nitro.release()
					messagebox.showinfo("Nitrogen Sample Preparation", "Pour the solution onto N-Funnel")
					self.msg_nitro.acquire()
					self.tablet_dispense = 0
					self.msg_nitro.release()
					
					d1n2_cmd_to_send = "KT+PR:"+d1n2_to_send+"\r\n"
					n2_ret_val = self.kt_sendcommand(d1n2_cmd_to_send,140,10)		
			
					d1n3_cmd_to_send = "KT+PR:"+d1n3_to_send+"\r\n"
					n3_ret_val = self.kt_sendcommand(d1n3_cmd_to_send,241,10)										
			
					ledon_cmd_to_send = "KT+LEDON\r\n" 
					ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)
			
					#net_connection_status = self.check_internet_connection()

					self.nnitro = self.n_imagecapture()
		
					with open(self.result_path,"r+") as e:
						a=json.load(e)					    		
					a["N"] = self.nnitro
					#a.update({'N':self.nnitro})
					obj=a

					with open(self.result_path,"w")as e:
						json.dump(obj,e)
		
					ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
					ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)
	
					texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
					wash_ret_val = self.kt_sendcommand(texttosend,45,10)
					
				if "Phosphorus" in lst_values:	
					self.machine_status_label.configure(text = "")
							
					self.sublabel.configure(text="Phosphorus")
											
					d1p1_cmd_to_send = "KT+PR:"+d1p1_to_send+"\r\n"
					#p1_ret_val = self.kt_sendcommand(d1p1_cmd_to_send,43,10)
					p1_ret_val = self.kt_sendcommand(d1p1_cmd_to_send,45,10)
					
					d1p2_cmd_to_send = "KT+PR:"+d1p2_to_send+"\r\n"
					p2_ret_val = self.kt_sendcommand(d1p2_cmd_to_send,321,10)	
					
					d1p3_cmd_to_send = "KT+PR:"+d1p3_to_send+"\r\n"
					p3_ret_val = self.kt_sendcommand(d1p3_cmd_to_send,1,10)												
					
					ledon_cmd_to_send = "KT+LEDON\r\n" 
					ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)
					
					#net_connection_status = self.check_internet_connection()
				
					self.pphosphorus = self.p_imagecapture()
					
					with open(self.result_path,"r+") as e:
						a=json.load(e)
					
					a["P"] = self.pphosphorus					    		
					#a.update({'P':self.pphosphorus})
					obj=a

					with open(self.result_path,"w")as e:
						json.dump(obj,e)
					
					ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
					ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)
				
					texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
					wash_ret_val = self.kt_sendcommand(texttosend,45,10)	
											                    
				if "Potassium" in lst_values:
					self.machine_status_label.configure(text = "")			
					
					self.sublabel.configure(text="Potassium")
											
					d1k1_cmd_to_send = "KT+PR:"+d1k1_to_send+"\r\n"
					#k1_ret_val = self.kt_sendcommand(d1k1_cmd_to_send,44,10)
					k1_ret_val = self.kt_sendcommand(d1k1_cmd_to_send,46,10)
					
					d1k2_cmd_to_send = "KT+PR:"+d1k2_to_send+"\r\n"
					k2_ret_val = self.kt_sendcommand(d1k2_cmd_to_send,661,10)	
					
					d1k3_cmd_to_send = "KT+PR:"+d1k3_to_send+"\r\n"
					k3_ret_val = self.kt_sendcommand(d1k3_cmd_to_send,1,10)											
					
					ledon_cmd_to_send = "KT+LEDON\r\n" 
					ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)    
					
					#net_connection_status = self.check_internet_connection()
				
					self.kpotash = self.k_imagecapture()
					
					with open(self.result_path,"r+") as e:
						a=json.load(e)
						
					a["K"] = self.kpotash					    		
					
					#a.update({'K':self.kpotash})
					obj=a

					with open(self.result_path,"w")as e:
						json.dump(obj,e)
					
					ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
					ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)
				
					texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
					wash_ret_val = self.kt_sendcommand(texttosend,45,10)
					
				if "Boron" in lst_values:	
					self.machine_status_label.configure(text = "")
							
					self.sublabel.configure(text="Boron")
											
					d1b1_cmd_to_send = "KT+PR:"+d1b1_to_send+"\r\n"
					b1_ret_val = self.kt_sendcommand(d1b1_cmd_to_send,52,10)
					
					d1b2_cmd_to_send = "KT+PR:"+d1b2_to_send+"\r\n"
					b2_ret_val = self.kt_sendcommand(d1b2_cmd_to_send,621,10)	
					
					d1b3_cmd_to_send = "KT+PR:"+d1b3_to_send+"\r\n"
					b3_ret_val = self.kt_sendcommand(d1b3_cmd_to_send,1,10)												
					
					ledon_cmd_to_send = "KT+LEDON\r\n" 
					ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)
					
					#net_connection_status = self.check_internet_connection()
				
					self.bboron = self.b_imagecapture()
					
					with open(self.result_path,"r+") as e:
						a=json.load(e)
					
					a["B"] = self.bboron					    		
					obj=a

					with open(self.result_path,"w")as e:
						json.dump(obj,e)
					with open(self.result_path,"r+") as e:
						a=json.load(e)
					print(a)   
					
					ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
					ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)
				
					texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
					wash_ret_val = self.kt_sendcommand(texttosend,45,10)	


				if "Iron" in lst_values:	
					self.machine_status_label.configure(text = "")
							
					self.sublabel.configure(text="Iron")
											
					d1i1_cmd_to_send = "KT+PR:"+d1i1_to_send+"\r\n"
					i1_ret_val = self.kt_sendcommand(d1i1_cmd_to_send,39,10)
					
					d1i2_cmd_to_send = "KT+PR:"+d1i2_to_send+"\r\n"
					i2_ret_val = self.kt_sendcommand(d1i2_cmd_to_send,631,10)	
					
					d1i3_cmd_to_send = "KT+PR:"+d1i3_to_send+"\r\n"
					i3_ret_val = self.kt_sendcommand(d1i3_cmd_to_send,1,10)												
					
					ledon_cmd_to_send = "KT+LEDON\r\n" 
					ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)
					
					#net_connection_status = self.check_internet_connection()
				
					self.iiron = self.i_imagecapture()
					
					with open(self.result_path,"r+") as e:
						a=json.load(e)
					
					a["I"] = self.iiron					    		

					obj=a

					with open(self.result_path,"w")as e:
						json.dump(obj,e)
					with open(self.result_path,"r+") as e:
						a=json.load(e)
					print(a)   
					
					ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
					ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)
				
					texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
					wash_ret_val = self.kt_sendcommand(texttosend,45,10)	
					
				if "Organic Carbon" in lst_values:
					self.machine_status_label.configure(text = "")
							
					self.sublabel.configure(text="Organic Carbon")
										
					with open(self.chemical_firmware_version) as equation_contents:
						equation_status_data = json.load(equation_contents)				        

					WashTestTube_DeviceFlush1 = equation_status_data["WashTestTube-DeviceFlush1"]
					WashTestTube_DeviceFlush2 = equation_status_data["WashTestTube-DeviceFlush2"]
					WashTestTube_DeviceFlush3 = equation_status_data["WashTestTube-DeviceFlush3"]
			
					DeviceFlush1 = "KT+PR:"+WashTestTube_DeviceFlush1+"\r\n"
					flush_ret_val = self.kt_sendcommand(DeviceFlush1,103,10)
					DeviceFlush2 = "KT+PR:"+WashTestTube_DeviceFlush2+"\r\n"
					flush_ret_val = self.kt_sendcommand(DeviceFlush2,160,10)	
					DeviceFlush3 = "KT+PR:"+WashTestTube_DeviceFlush3+"\r\n"
					flush_ret_val = self.kt_sendcommand(DeviceFlush3,80,10)	
					
					self.msg_nitro.acquire()
					self.tablet_dispense = 1						
					self.msg_nitro.release()
					messagebox.showinfo("Organinc Carbon Sample Preparation", "Pour the solution onto Sample Solution Dispenser")
					self.msg_nitro.acquire()
					self.tablet_dispense = 0
					self.msg_nitro.release()									
											
					d1oc1_cmd_to_send = "KT+PR:"+d1oc1_to_send+"\r\n"
					oc1_ret_val = self.kt_sendcommand(d1oc1_cmd_to_send,39,10)
					
					d1oc2_cmd_to_send = "KT+PR:"+d1oc2_to_send+"\r\n"
					oc2_ret_val = self.kt_sendcommand(d1oc2_cmd_to_send,61,10)	
					
					ledon_cmd_to_send = "KT+LEDON\r\n" 
					ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)
					
					#net_connection_status = self.check_internet_connection()
				
					self.ooc = self.oc_imagecapture()
					
					with open(self.result_path,"r+") as e:
						a=json.load(e)
					
					a["OC"] = self.ooc					    		

					obj=a

					with open(self.result_path,"w")as e:
						json.dump(obj,e)
					with open(self.result_path,"r+") as e:
						a=json.load(e)
					print(a)   
					
					ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
					ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)
				
					texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
					wash_ret_val = self.kt_sendcommand(texttosend,45,10)				

				self.breportt=Button(self.Timm_FRame,text="Next",bg="blue",font="centre",fg="white",command=self.show_report)
				self.breportt.place(x=650,y=340,height=30)					
				
				self.c1.itemconfigure(self.r,fill="#1f1")

			except Exception as e:
				self.c1.itemconfigure(self.r,fill="#f11")
				errorstring = "/E-sample_solution()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")

			finally:
				pass                         
				
		def pss_message(self):
			try:
				self.machine_status_label.configure(text = "")
				self.Timm_FRame_pss_message=Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)

				Mainlabel=Label(self.Timm_FRame_pss_message,text="Instructions",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
				canvas=Canvas(self.Timm_FRame_pss_message,bg="#F5F4EB")
				canvas.create_rectangle(30, 10, 650, 180,outline="#fb0",fill="#F5F4EB")

				lst_values = [self.listboxx.get(idx) for idx in self.listboxx.curselection()] 
			    
				if "pH" in lst_values:
					self.machine_status_label.configure(text = "")
					messagebox.showinfo("Start", "Dip pH probe in the Soil Water Suspension")
					sublabel3=Label(self.Timm_FRame_pss_message,text="Press Next to Initiate pH Testing ",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3.place(x=100,y=110)  
					self.breporttt=Button(self.Timm_FRame_pss_message,text="Next",bg="blue",font="centre",fg="white",command=self.compute_test)
					self.breporttt.place(x=650,y=340,height=30)
					self.breporttt['state']=ACTIVE						
		        
				if "EC" in lst_values:
					self.machine_status_label.configure(text = "")
					messagebox.showinfo("Start", "Dip EC probe in the Soil Water Suspension")					
					sublabel3=Label(self.Timm_FRame_pss_message,text="Press Next to Initiate EC Testing",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3.place(x=100,y=130)  
					self.breporttt=Button(self.Timm_FRame_pss_message,text="Next",bg="blue",font="centre",fg="white",command=self.compute_test)
					self.breporttt.place(x=650,y=340,height=30)
					self.breporttt['state']=ACTIVE			
				
				if "Nitrogen" in lst_values or "Potassium" in lst_values or "Phosphorus" in lst_values or "Boron" in lst_values or "Iron" in lst_values or "Organic Carbon" in lst_values:	
					self.machine_status_label.configure(text = "")
					messagebox.showinfo("Extraction Solution", "Pour the extracted clear soil solution sample into the inlet")			
					sublabel3=Label(self.Timm_FRame_pss_message,text="Preparing system for Testing",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3.place(x=100,y=150)
					
					
					self.breporttt=Button(self.Timm_FRame_pss_message,text="Next",bg="blue",font="centre",fg="white",command=self.compute_test)
					self.breporttt.place(x=650,y=340,height=30)
					self.breporttt['state']=ACTIVE
					
				self.Timm_FRame_pss_message.place(x=10,y=40,width=780,height=390)
				canvas.place(x=10,y=80,width=700,height=200)
				Mainlabel.place(x=20,y=20)						
			except Exception as e:
				errorstring = "/E-pss_solution()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				
		def onselect_testpage(self,event):
			try:
				if self.listboxx.curselection():
					self.bconfirm_test['state'] = ACTIVE
				else:
					self.bconfirm_test['state'] = DISABLED				
			except Exception as e:
				errorstring = "/E-onselect_testpage()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 	
	
		def test_page(self):
			try:
				self.machine_status_label.configure(text = "")
				ser_status_ret_val = self.kt_sendcommand("KT+STATUS\r\n",1,10)

				self.testregi_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				mainlabel=Label(self.testregi_FRame,text="Register Your Test Here",bg="#F5F4EB",fg="#254E58",font="BOLD  14 ")    
				line=Label(self.testregi_FRame,text="  #############################################################################################################")
				
				self.bconfirm_test=Button(self.testregi_FRame,text="Next",bg="blue",font="centre",fg="white",command=self.pss_message)
				
				self.bconfirm_test['state'] = DISABLED	
				self.testregi_FRame.place(x=10,y=40,width=780,height=390)			

				if ser_status_ret_val == "KT+07\r\n":	
					MsgBox = messagebox.askquestion ('Washing required or not ?','Click "yes" to test ALL. "No" to test only EC and pH ',icon = 'warning')
					if MsgBox == 'yes':
						self.listboxx=Listbox(self.testregi_FRame,selectmode=MULTIPLE,width=30,height=5,font=("Calibri",17))
						self.listboxx.insert(0,"pH")
						self.listboxx.insert(1,"EC")
						self.listboxx.insert(2,"Nitrogen")
						self.listboxx.insert(3,"Phosphorus")
						self.listboxx.insert(4,"Potassium")
						self.listboxx.insert(5,"Boron")
						self.listboxx.insert(6,"Iron")
						self.listboxx.selection_set(0)

						self.listboxx.bind('<<ListboxSelect>>',self.onselect_testpage)	
						self.listboxx.config(state=DISABLED)
					
						timer5 = threading.Timer(0.1, self.washaprtus)
						timer5.start()
						
						self.machine_status_label.configure(text = "Preparing for testing... Please wait (approx 6 mins...)")
						logging.info ("self.listboxx.get(self.listboxx.curselection()) => %s",self.listboxx.get(self.listboxx.curselection()))
					else:
						self.listboxx=Listbox(self.testregi_FRame,selectmode=MULTIPLE,width=30,height=5,font=("Calibri",17))
						self.listboxx.insert(0,"pH")
						self.listboxx.insert(1,"EC")
						self.listboxx.selection_set(0)

						self.listboxx.bind('<<ListboxSelect>>',self.onselect_testpage)	
						#self.listboxx.config(state=DISABLED)
					
						self.bconfirm_test['state'] = ACTIVE						
						
					mainlabel.place(x=270,y=5)
					line.place(x=0,y=30)
					self.listboxx.place(x=200,y=110)
					self.bconfirm_test.place(x=600,y=350,width=50,height=30)
					self.keypad_label.place_forget()
					self.bfocus_in.place_forget()
					self.bfocus_out.place_forget()				        
					#messagebox.showinfo("System Preparation", "Preparing System - Press Ok to continue")
				else:
					self.machine_status_label.configure(text = "Error in serial Connection !!!")
					#time.sleep(1)
					#self.machine_status_label.configure(text = "")
					pass
			except Exception as e:
				errorstring = "/E-test_select()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass                         
	
		def xnext_test(self):
			try:
				global fr_fieldname
				global fr_fieldarea
				global fr_croptype
				global fr_soiltype
				global fr_farmlong
				global fr_farmlat
				global fr_farmsurveyno
				global fr_density
				global fr_soilden
				global URL
				global token
				global Name
				global fr_uuid
				fr_fieldname=self.efield_name.get()
				fr_fieldarea=self.efarmmer_area.get()
				#fr_croptype=self.efarmer_crop.get()
				fr_croptype=self.tkvarr2.get()
				fr_soiltype=self.tkvarr.get()
				fr_farmlong=self.efarmer_long.get()
				fr_farmlat=self.efarmer_lat.get()
				fr_farmsurveyno=self.efarmer_surveyno.get()
				fr_soilden=1.3#self.esoil_density.get()
				if(fr_fieldname=='' or fr_fieldarea=='' or fr_croptype=='' or fr_soiltype=='' or fr_farmlong=='' or fr_farmlat=='' or fr_farmsurveyno==''):
					messagebox.showerror("Error","Fill all the fields")
				else:
					a=re.match("^[0-9]",fr_fieldarea)
					#b=re.match("^[0-9]",fr_farmlong)
					#c=re.match("^[0-9]",fr_farmlat)
					d=re.match("^[0-9]",fr_farmsurveyno)
					if(not a):
						messagebox.showerror("Value Error","Field area should be a number")
					#elif(not b):
					#	messagebox.showerror("Value Error","Longitude should be a number")
					#elif(not c):
					#	messagebox.showerror("Value Error","Latitude should be a number")
					elif(not d):
						messagebox.showerror("Value Error","Survey Number should be a number")
					else:
						url= URL +"farmers/"+fr_uuid+"/areas/"
						payload={'name':fr_fieldname,'latitude':fr_farmlat,'longitude':fr_farmlong,'soil_density':fr_soilden,'crop':[fr_croptype],'soil_type':fr_soiltype,'survey_no':fr_farmsurveyno,'area_size':fr_fieldarea}
						headers={'Authorization': "Bearer "+token,'content-type': 'application/json'}
						r=requests.post(url,data=json.dumps(payload),headers=headers)   
						data=r.json()
						logger.info ("post ret value ==>%s",r)
						logger.info ("Status code ==>%s",r.status_code)
						logger.info ("Data ==>%s",data)
						if(r.status_code == 200):
							self.farmerxmangement_FRame.destroy()
							self.farm_dashboard()
						else:
							if('name' in data['errors']):
								messagebox.showerror("Value Error","Name should be of minimum length\n (minimum length=3)")
			except Exception as e:
				errorstring = "/E-xnext_test()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 		        

		def farmer_xmanagement(self):
			try:
				farmer_uuid="4f34a3aa-200c-4a18-be5e-96cbdb9b5dea"
				url=URL+"farmers/"+farmer_uuid 
				headers={'Authorization': "Bearer "+token}
				r=requests.get(url,headers=headers)
				data=r.json()
				if(r.status_code == 200):
					location_longitude = data['longitude']
					location_latitude =  data['latitude']
				else:
					messagebox.showerror("Search Result","Invalid Phone Number")
			
				self.effarmmer_getlong=StringVar()
				self.effarmmer_getlati=StringVar()
				
				self.keyboard_process = None
				self.farmerxmangement_FRame = Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1,)
				managementmsg=Label(self.farmerxmangement_FRame,text="Create Field",bg="#F5F4EB",fg="#254E58",font="BOLD  16 ")
				Bback=Button(self.farmerxmangement_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre 10",command=self.backfarmer_management)
				#Bupdatefarmer=Button(self.farmerxmangement_FRame,text="Basic\nDetails",bg="#A79B94",fg="#2C2C2C",font="centre",command=self.update_xdetails)
				canvas=Canvas(self.farmerxmangement_FRame)#,bg="#F5F4EB")
				canvas.create_rectangle(5, 5, 505, 330,outline="#fb0",fill="#F5F4EB")
				canvas.place(x=170,y=50,width=510,height=335)
				bfarmer_register=Button(self.farmerxmangement_FRame,text="Next",bg="#3e8ddc",fg="#fffdfd",font="centre 10",command=self.xnext_test)
				#lpreviousEntry=Label(self.farmerxmangement_FRame,text="Previous Entry\t\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  13 ")
				#self.tkvariable=StringVar(self.farmerxmangement_FRame)
				#self.previous_choice={'None'}
				#self.epreviousEntry= OptionMenu(self.farmerxmangement_FRame, self.tkvariable, *self.previous_choice)
				lfield_name=Label(self.farmerxmangement_FRame,text="Field Name\t\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  12 ")
				self.efield_name=Entry(self.farmerxmangement_FRame,bg="#F5F4EB",font=("Calibri",12),justify="left")
				#self.efield_name.bind("<FocusIn>",self.focus_in)
				#self.efield_name.bind("<FocusOut>",self.focus_out)
				lfamrmer_area=Label(self.farmerxmangement_FRame,text="Field Area (acres)\t\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  12 ")
				self.efarmmer_area=Entry(self.farmerxmangement_FRame,bg="#F5F4EB",font=("Calibri",12),justify="left")
				#self.efarmmer_area.bind("<FocusIn>",self.focus_in)
				#self.efarmmer_area.bind("<FocusOut>",self.focus_out)
				lfarmer_crop=Label(self.farmerxmangement_FRame,text="Crop Type\t\t",bg="#F5F4EB",fg="#254E58",font="BOLD  12 ")
				self.tkvarr2=StringVar(self.farmerxmangement_FRame)
				choice2={'Turmeric','Local cultivar','Cabbage','Rice','Wheat','Bajra','Barley','Maize','Mothbean','Guar','Castor','Sunflower','Oat','Sorghum','Soyabean','Pearlmillet','Chickpea','Pigeonpea'}
				self.tkvarr2.set('Turmeric')
				self.efarmer_crop=OptionMenu(self.farmerxmangement_FRame, self.tkvarr2, *choice2)
				#self.efarmer_crop=Entry(self.farmerxmangement_FRame,bg="#F5F4EB",font=("Calibri",14),justify="left")
				#self.efarmer_crop.bind("<FocusIn>",self.focus_in)
				#self.efarmer_crop.bind("<FocusOut>",self.focus_out)
				lfarmer_soil=Label(self.farmerxmangement_FRame,text="Soil Type\t\t",bg="#F5F4EB",fg="#254E58",font="BOLD  12 ")
				self.tkvarr=StringVar(self.farmerxmangement_FRame)
				choice={'Alfisol','Alfisol(Sandy Loam)','Alluvial','Alluvial Soil','Black Soil','Black soil (Vertisols)','Chalka Soils','Inceptisol','Inceptisols (Sandy loam)','Inceptisols(Sandy Clay Loam)','Red Loam Soil','Sandy Clay Loam','Seirozem(Inceptisols/Entisols)','Sierozem','Sierozem (Inceptisols/Verisols)','Typic Haplustept(Alluvial)','Vertisol'}
				self.tkvarr.set('Alfisol')
				self.esample_type= OptionMenu(self.farmerxmangement_FRame, self.tkvarr, *choice)
				lfarmer_long=Label(self.farmerxmangement_FRame,text="Geographical Longitude\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  12 ")
				self.efarmer_long=Entry(self.farmerxmangement_FRame,textvariable=self.effarmmer_getlong,bg="#F5F4EB",font=("Calibri",12),justify="left")
				#self.efarmer_long.bind("<FocusIn>",self.focus_in)
				#self.efarmer_long.bind("<FocusOut>",self.focus_out)
				lfarmer_lat=Label(self.farmerxmangement_FRame,text="Geographical Latitude\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  12 ")
				self.efarmer_lat=Entry(self.farmerxmangement_FRame,textvariable=self.effarmmer_getlati,bg="#F5F4EB",font=("Calibri",12),justify="left")
				#self.efarmer_lat.bind("<FocusIn>",self.focus_in)
				#self.efarmer_lat.bind("<FocusOut>",self.focus_out)
				lfarmer_surveyno=Label(self.farmerxmangement_FRame,text="Survey Number\t\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  12 ")
				self.efarmer_surveyno=Entry(self.farmerxmangement_FRame,bg="#F5F4EB",font=("Calibri",12),justify="left")
				
				lsoil_density=Label(self.farmerxmangement_FRame,text="Soil Density\t\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  12 ")
				self.esoil_density=Entry(self.farmerxmangement_FRame,bg="#F5F4EB",font=("Calibri",12),justify="left")
				self.esoil_density['state']=DISABLED
				
	
				text_msg_long_and_lat = "*Farmers Location (longitude and Latitude) is fetched from server. Please fill the exact field location (farm) by searching the internet"
				wrapper = textwrap.TextWrapper(width=25) 
				disp_lat_long = wrapper.fill(text=text_msg_long_and_lat) 			
				label_text_msg_long_and_lat=Label(self.farmerxmangement_FRame,text=disp_lat_long,bg="#F5F4EB",fg="red",font="BOLD  8 ")
				label_text_msg_long_and_lat.place(x=5,y=210)	
								
				self.effarmmer_getlong.set(location_longitude)
				self.effarmmer_getlati.set(location_latitude)
								
				#self.efarmer_surveyno.bind("<FocusIn>",self.focus_in)
				#self.efarmer_surveyno.bind("<FocusOut>",self.focus_out)
				self.farmerxmangement_FRame.place(x=10,y=40,width=780,height=390)
				managementmsg.place(x=5,y=10,height=34)
				Bback.place(x=690,y=15,height=30,width=60)
				#Bupdatefarmer.place(x=680,y=230,width=80,height=80)
				bfarmer_register.place(x=690,y=340,height=30,width=60)    
				#lpreviousEntry.place(x=190,y=65,height=25)        
				#self.epreviousEntry.place(x=420,y=65,width=230,height=25)
				lfield_name.place(x=190,y=60,height=25)  
				self.efield_name.place(x=420,y=60,width=230,height=25)
				lfamrmer_area.place(x=190,y=100,height=25)  
				self.efarmmer_area.place(x=420,y=100,width=230,height=25)
				lfarmer_crop.place(x=190,y=140,height=25)  
				self.efarmer_crop.place(x=420,y=140,width=230,height=25)
				lfarmer_soil.place(x=190,y=180,height=25)  
				self.esample_type.place(x=420,y=180,width=230,height=25)
				lfarmer_long.place(x=190,y=220,height=25)  
				self.efarmer_long.place(x=420,y=220,width=230,height=25)
				lfarmer_lat.place(x=190,y=260,height=25)  
				self.efarmer_lat.place(x=420,y=260,width=230,height=25)
				lfarmer_surveyno.place(x=190,y=300,height=25)  
				self.efarmer_surveyno.place(x=420,y=300,width=230,height=25)
				self.esoil_density.place(x=420,y=340,width=230,height=25)
				lsoil_density.place(x=190,y=340,height=25)  
				self.keypad_label.place(x=18,y=15,width=40,height=20)                        
				self.bfocus_in.place(x=60,y=15,width=40,height=20)    
				self.bfocus_out.place(x=120,y=15,width=40,height=20)
								
			except Exception as e:
				errorstring = "/E-farmer_xmanagement()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 			    

		def nextexistingfarmermanagement(self):
			try:
				global fr_name
				global fr_uuid
				fr_username=self.eloginfarmer_username.get()

				url= URL +"farmers?username="+fr_username    
				headers={'Authorization': "Bearer "+token}
				r=requests.get(url,headers=headers)
				data=r.json()

				if(len(data['data'])==0):
					messagebox.showerror("Error","Ivalid User")
				else:
					if(r.status_code == 200):
						fr_name=data['data'][0]['name'].upper()
						fr_uuid=data['data'][0]['uuid']
						
						fr_uuid = str(fr_uuid)
				
						with open(self.result_path,"r+") as e:
							a=json.load(e)
						a["fr_uuid"] = fr_uuid					    		
						#a.update({'fr_uuid':fr_uuid})
						obj=a

						with open(self.result_path,"w")as e:
							json.dump(obj,e)

						self.farmerLOGIN_FRame.destroy()
						self.farm_dashboard()
			except Exception as e:
				errorstring = "/E-next_existing_farmer_management()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 		        
        

		def existingfarmer_login(self):
			try:
				self.Fpodashboard_FRame.destroy()
				self.farmerLOGIN_FRame= Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)
				self.welcomemsg=Label(self.farmerLOGIN_FRame,text="Farmer Login",bg="#F5F4EB",fg="#254E58",font="BOLD  16 ")
				Bback=Button(self.farmerLOGIN_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre 10",command=self.bachfbodash)
				canvas=Canvas(self.farmerLOGIN_FRame,bg="#F5F4EB")
				canvas.create_rectangle(10, 10, 540, 240,outline="#fb0",fill="#F5F4EB")
				canvas.place(x=60,y=80,width=550,height=250)
				lusername=Label(self.farmerLOGIN_FRame,text="User Name\t",bg="#F5F4EB",fg="#254E58",font="BOLD  14 ")
				self.eloginfarmer_username=Entry(self.farmerLOGIN_FRame,bg="#F5F4EB",font=("Calibri",14),justify="left")
				
				#self.eloginfarmer_username.bind("<FocusIn>")#,self.focus_in)
				#self.eloginfarmer_username.bind("<FocusOut>")#,self.focus_out)
				#lfarmer_phoneNo=Label(self.farmerLOGIN_FRame,text="Phone Number\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  14 ")
				#self.efarmerlogin_phone=Entry(self.farmerLOGIN_FRame,bg="#F5F4EB",font=("Calibri",14),justify="left")
				#self.efarmerlogin_phone.bind("<FocusIn>")#,self.focus_in)
				#self.efarmerlogin_phone.bind("<FocusOut>")#,self.focus_out)
				
				bfarmer_register=Button(self.farmerLOGIN_FRame,text="Next",bg="#3e8ddc",fg="#fffdfd",font="centre 10",command=self.nextexistingfarmermanagement)
				#bfarmer_register.bind("<FocusIn>")#,self.bfocus_out)
				self.welcomemsg.place(x=5,y=20,height=40)
				self.farmerLOGIN_FRame.place(x=10,y=40,width=780,height=390)
				lusername.place(x=80,y=190,height=25)
				self.eloginfarmer_username.place(x=280,y=190,width=300)
				#lfarmer_phoneNo.place(x=80,y=225,height=25)
				#self.efarmerlogin_phone.place(x=280,y=225,width=300)
				Bback.place(x=650,y=40,height=30,width=60)
				bfarmer_register.place(x=650,y=340,height=30,width=60)  
				self.keypad_label.place(x=18,y=15,width=40,height=20)                        
				self.bfocus_in.place(x=60,y=15,width=40,height=20)    
				self.bfocus_out.place(x=120,y=15,width=40,height=20) 				
			except Exception as e:
				errorstring = "/E-existing_farmer_login()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 		    

		def backfpo_pagereg(self):
			try:
				self.farmer_FRame.destroy()
				self.fpo_dashboard()
			except Exception as e:
				errorstring = "/E-backfpo_pagereg()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 		    

		def xbackfpo_pagereg(self):
			try:
				self.xfarmer_FRame.destroy()
				self.fpo_dashboard()
			except Exception as e:
				errorstring = "/E-xbackfpo_pagereg()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 		    

		def nextxfamerregister_farmermanagement(self):
			#take values later on
			try:
				global fr_name
				global fr_username
				global fr_contact
				global fr_email
				global fr_address
				global fr_state
				global fr_country
				global fr_lang
				fr_name=self.efarmer_name.get()
				fr_username=self.efarmer_userName.get()
				fr_contact=self.efarmer_contact.get()
				fr_email=self.efarmer_email.get()
				fr_address=self.efarmer_address.get()
				#fr_state=self.efarmer_state.get()
				#fr_country=self.efarmer_country.get()
				fr_lang=self.efarmerlanguage.get()
			
				self.xfarmer_FRame.destroy()
				self.farmer_xmanagement()
			except Exception as e:
				errorstring = "/E-nextfarmerregister_farmermanagement()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass		    


		def nextfamerregister_farmermanagement(self):
			try:
				global fr_name
				global fr_username
				global fr_contact
				global fr_email
				global fr_address
				global fr_state
				global fr_country
				global fr_lang
				global fr_geolong
				global fr_geolat
				global URL
				global token
				global Name
				fr_name=self.efarmer_name.get()
				fr_username=self.efarmer_userName.get()
				fr_contact=self.efarmer_contact.get()
				fr_email=self.efarmer_email.get()
				fr_address=self.efarmer_address.get()
				fr_geolong=self.efarmer_geolong.get()
				fr_geolat=self.efarmer_geolati.get()
				fr_lang=self.efarmerlanguage.get()
				if(fr_name=='' or fr_username=='' or fr_contact=='' or fr_address=='' or fr_geolong=='' or fr_geolat=='' or fr_lang==''):
					messagebox.showerror("Input Error","Enter all values")
				elif fr_email == "":
					url= URL +"farmer/register"
					payload={ "username":fr_username,"password":"abcd@1234","confirm-password":"abcd@1234","address":fr_address,"contact_no":fr_contact,"longitude":fr_geolong,"latitude":fr_geolat,"name":fr_name}
					headers={'content-type': 'application/json'}
					r=requests.post(url,data=json.dumps(payload),headers=headers)   
					data=r.json()    
					if(r.status_code == 200):
						self.farmer_FRame.destroy()
						self.fpo_dashboard()
					else:
						if('username' in data['errors']):
							messagebox.showerror("Input Value Error","Already in use Or User Name should be Alphanumeric")
						elif('name' in data['errors']):
							messagebox.showerror("Input Value Error","Name Must Have minimum length 3")
						#elif('email' in data['errors']):
						#	messagebox.showerror("Input Value Error","Enter Valid email ")
						elif('contact_no' in data['errors']):
							messagebox.showerror("Input Value Error","Must provide a valid Indian phone number")
				else:
					url= URL +"farmer/register"
					payload={ "username":fr_username,"password":"abcd@1234","confirm-password":"abcd@1234","email":fr_email,"address":fr_address,"contact_no":fr_contact,"longitude":fr_geolong,"latitude":fr_geolat,"name":fr_name}
					headers={'content-type': 'application/json'}
					r=requests.post(url,data=json.dumps(payload),headers=headers)   
					data=r.json()    

					if(r.status_code == 200):
						self.farmer_FRame.destroy()
						self.fpo_dashboard()
					else:
						if('username' in data['errors']):
							messagebox.showerror("Input Value Error","Already in use Or User Name should be Alphanumeric")
						elif('name' in data['errors']):
							messagebox.showerror("Input Value Error","Name Must Have minimum length 3")
						#elif('email' in data['errors']):
						#	messagebox.showerror("Input Value Error","Enter Valid email ")
						elif('contact_no' in data['errors']):
							messagebox.showerror("Input Value Error","Must provide a valid Indian phone number")
			except Exception as e:
				errorstring = "/E-nextfarmer_register_farmer_management()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass		        

		def xfarmer_register(self):
			try:
				self.Fpodashboard_FRame.destroy()
				self.xfarmer_FRame= Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)
				Main_Label1=Label(self.xfarmer_FRame,text="Farmer Personal Details",bg="#F5F4EB",fg="#254E58",font="BOLD  14 ")
				
				#sub_label1=Label(self.xfarmer_FRame,text="Enter the details with full accuracy",bg="#F5F4EB",fg="#ff0000",font="BOLD 8")
				
				Bback=Button(self.xfarmer_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.xbackfpo_pagereg)
				lfarmer_name=Label(self.xfarmer_FRame,text="Name",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_name=Entry(self.xfarmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")
				#self.efarmer_name.bind("<FocusIn>",self.focus_in)
				#self.efarmer_name.bind("<FocusOut>",self.focus_out)
				lfarmer_userName=Label(self.xfarmer_FRame,text="User Name",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_userName=Entry(self.xfarmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")
				#self.efarmer_userName.bind("<FocusIn>",self.focus_in)
				#self.efarmer_userName.bind("<FocusOut>",self.focus_out)
				lfarmer_contact=Label(self.xfarmer_FRame,text="Contact Number",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_contact=Entry(self.xfarmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")
				#self.efarmer_contact.bind("<FocusIn>",self.focus_in)
				#self.efarmer_contact.bind("<FocusOut>",self.focus_out)
				lfarmer_email=Label(self.xfarmer_FRame,text="Email",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_email=Entry(self.xfarmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")
				#self.efarmer_email.bind("<FocusIn>",self.focus_in)
				#self.efarmer_email.bind("<FocusOut>",self.focus_out)
				lfarmer_address=Label(self.xfarmer_FRame,text="Address",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_address=Entry(self.xfarmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")
				#self.efarmer_address.bind("<FocusIn>",self.focus_in)
				#self.efarmer_address.bind("<FocusOut>",self.focus_out)
				lfarmer_state=Label(self.xfarmer_FRame,text="Longitude",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_geolong=Entry(self.xfarmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")
				#self.efarmer_state.bind("<FocusIn>",self.focus_in)
				#self.efarmer_state.bind("<FocusOut>",self.focus_out)
				lfarmer_country=Label(self.xfarmer_FRame,text="Latitude",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_geolati=Entry(self.xfarmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")
				#self.efarmer_country.bind("<FocusIn>",self.focus_in)
				#self.efarmer_country.bind("<FocusOut>",self.focus_out)
				lfarmerlanguage=Label(self.xfarmer_FRame,text="Prefered Language",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
			   
				self.previous_choice=['English', 'Hindi', 'Kannada', 'Tamil', 'Telugu', 'Malayalam', 'Oriya', 'Gujarati', 'Bengali', 'Panjabi', 'Marathi' ]
				self.efarmerlanguage = ttk.Combobox(self.xfarmer_FRame,values=self.previous_choice,height=4)
				self.efarmerlanguage.current(0)
				bfarmer_register=Button(self.xfarmer_FRame,text="Next",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.nextxfamerregister_farmermanagement)
				#bfarmer_register.bind("<FocusIn>",self.bfocus_out)
				self.fmsg_box=Label(self.xfarmer_FRame,text="",bg="#F5F4EB",fg="#ff0000",font="BOLD 6")
				self.xfarmer_FRame.place(x=10,y=40,width=780,height=390)
				Main_Label1.place(x=200,y=10,width=400)
				
				#sub_label1.place(x=10,y=40)
				
				blang_lat=Button(self.farmer_FRame,text="Fetch location ",bg="#3e8ddc",fg="#fffdfd",font="centre 8",command=self.get_lat_long)				
				
				Bback.place(x=650,y=40,height=30,width=60)
				lfarmer_name.place(x=20,y=80,height=25)
				self.efarmer_name.place(x=160,y=80,width=300,height=25)
				lfarmer_userName.place(x=20,y=120,height=25)
				self.efarmer_userName.place(x=160,y=120,width=300,height=25)

				lfarmerlanguage.place(x=20,y=160,height=25)
				self.efarmerlanguage.place(x=160,y=160,width=300,height=25)
				lfarmer_contact.place(x=20,y=200,height=25)
				self.efarmer_contact.place(x=160,y=200,width=300,height=25)
				lfarmer_email.place(x=20,y=240,height=25)
				self.efarmer_email.place(x=160,y=240,width=300,height=25)
				lfarmer_address.place(x=20,y=280,height=25)
				
				self.efarmer_address.place(x=160,y=280,width=300,height=25)
				
				lfarmer_state.place(x=500,y=160,height=25)
				self.efarmer_geolong.place(x=580,y=160,width=100,height=25)
				lfarmer_country.place(x=500,y=200,height=25)
				self.efarmer_geolati.place(x=580,y=200,width=100,height=25)

				bfarmer_register.place(x=650,y=340,height=30,width=60)  
				blang_lat.place(x=260,y=340,height=20,width=140)   
				self.fmsg_box.place(x=30,y=350)
				self.keypad_label.place(x=18,y=15,width=40,height=20)                        
				self.bfocus_in.place(x=60,y=15,width=40,height=20)    
				self.bfocus_out.place(x=120,y=15,width=40,height=20) 				
			except Exception as e:
				errorstring = "/E-xfarmer_register()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass		    
				
		def get_lat_long(self):	
			try:	
				self.efarmer_geolong["state"] = NORMAL
				self.efarmer_geolati["state"] = NORMAL
				farmer_addr = self.efarmer_place.get()
				geolocator = Nominatim()
				location = geolocator.geocode(farmer_addr)
				
				self.location_longitude = location.longitude
				self.location_latitude = location.latitude
				wrapper = textwrap.TextWrapper(width=45) 
				disp_addr = wrapper.fill(text=location.address) 			
				self.lfarmer_wrongaddress.config(text="")
				self.lfarmer_fulladdress.config(text=disp_addr)
				self.effarmmer_geolong.set(self.location_longitude)
				self.effarmmer_geolati.set(self.location_latitude)
			except Exception as e:
				self.lfarmer_wrongaddress.config(text="*Please enter proper place name")
				self.lfarmer_fulladdress.config(text="")
				self.effarmmer_geolong.set("")
				self.effarmmer_geolati.set("")				
				errorstring = "/E-get_lat_long()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass				

		def newfarmer_register(self):
			try:
				self.Fpodashboard_FRame.destroy()
				self.farmer_FRame= Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)
				
				self.effarmmer_geolong=StringVar()
				self.effarmmer_geolati=StringVar()
				
				Main_Label1=Label(self.farmer_FRame,text="Farmer Personal Details",bg="#F5F4EB",fg="#254E58",font="BOLD  14 ")
				
				Bback=Button(self.farmer_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre 10",command=self.backfpo_pagereg)
				lfarmer_name=Label(self.farmer_FRame,text="Name",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_name=Entry(self.farmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")
				lfarmer_userName=Label(self.farmer_FRame,text="User Name",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_userName=Entry(self.farmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")
				lfarmer_contact=Label(self.farmer_FRame,text="Contact Number",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_contact=Entry(self.farmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")
				lfarmer_email=Label(self.farmer_FRame,text="Email",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_email=Entry(self.farmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")
				lfarmer_address=Label(self.farmer_FRame,text="Address",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_address=Entry(self.farmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")
				
				lfarmer_place=Label(self.farmer_FRame,text="Place (Name)",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_place=Entry(self.farmer_FRame,bg="#F5F4EB",font=("Calibri",8),justify="left")

				lfarmer_state=Label(self.farmer_FRame,text="Longitude",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_geolong=Entry(self.farmer_FRame,textvariable=self.effarmmer_geolong,bg="#F5F4EB",font=("Calibri",8),justify="left")
				lfarmer_country=Label(self.farmer_FRame,text="Latitude",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				self.efarmer_geolati=Entry(self.farmer_FRame,textvariable=self.effarmmer_geolati,bg="#F5F4EB",font=("Calibri",8),justify="left")
				
				self.efarmer_geolong["state"] = DISABLED
				self.efarmer_geolati["state"] = DISABLED

				self.lfarmer_fulladdress=Label(self.farmer_FRame,text="", anchor=W, justify=LEFT,bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
				
				self.lfarmer_wrongaddress=Label(self.farmer_FRame,text="", anchor=W, justify=LEFT,bg="#F5F4EB",fg="red",font="BOLD  8 ")
				#self.lfarmer_fulladdress["state"] = DISABLED
								
				lfarmerlanguage=Label(self.farmer_FRame,text="Prefered Language",bg="#F5F4EB",fg="#254E58",font="BOLD  8 ")
			   
				self.previous_choice=['English', 'Hindi', 'Kannada', 'Tamil', 'Telugu', 'Malayalam', 'Oriya', 'Gujarati', 'Bengali', 'Panjabi' ]
				self.efarmerlanguage = ttk.Combobox(self.farmer_FRame,values=self.previous_choice,height=4)
				self.efarmerlanguage.current(0)
				bfarmer_register=Button(self.farmer_FRame,text="Next",bg="#3e8ddc",fg="#fffdfd",font="centre 10",command=self.nextfamerregister_farmermanagement)
				self.fmsg_box=Label(self.farmer_FRame,text="",bg="#F5F4EB",fg="#ff0000",font="BOLD 6")
				self.farmer_FRame.place(x=10,y=40,width=780,height=390)
				Main_Label1.place(x=160,y=10,width=400)
				blang_lat=Button(self.farmer_FRame,text="Fetch location ",bg="#3e8ddc",fg="#fffdfd",font="centre 8",command=self.get_lat_long)				
				
				Bback.place(x=680,y=40,height=30,width=60)
				lfarmer_name.place(x=20,y=80,height=25)
				self.efarmer_name.place(x=160,y=80,width=300,height=25)
				lfarmer_userName.place(x=20,y=120,height=25)
				self.efarmer_userName.place(x=160,y=120,width=300,height=25)

				lfarmerlanguage.place(x=20,y=160,height=25)
				self.efarmerlanguage.place(x=160,y=160,width=300,height=25)
				lfarmer_contact.place(x=20,y=200,height=25)
				self.efarmer_contact.place(x=160,y=200,width=300,height=25)
				lfarmer_email.place(x=20,y=240,height=25)
				self.efarmer_email.place(x=160,y=240,width=300,height=25)
				lfarmer_address.place(x=20,y=280,height=25)
				self.efarmer_address.place(x=160,y=280,width=300,height=25)

				lfarmer_place.place(x=20,y=320,height=25)
				self.efarmer_place.place(x=160,y=320,width=300,height=25)

				lfarmer_state.place(x=500,y=160,height=25)
				self.efarmer_geolong.place(x=580,y=160,width=100,height=25)
				lfarmer_country.place(x=500,y=200,height=25)
				self.lfarmer_fulladdress.place(x=500,y=240,height=50)
				self.lfarmer_wrongaddress.place(x=480,y=320,height=25)
				self.efarmer_geolati.place(x=580,y=200,width=100,height=25)
				self.keypad_label.place(x=18,y=15,width=40,height=20)                        
				self.bfocus_in.place(x=60,y=15,width=40,height=20)    
				self.bfocus_out.place(x=120,y=15,width=40,height=20) 			
			
				blang_lat.place(x=260,y=360,height=20,width=140) 
				bfarmer_register.place(x=680,y=340,height=30,width=60)				   
				self.fmsg_box.place(x=30,y=350)
			except Exception as e:
				errorstring = "/E-new_farmer_register()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass		    

		def check_value(self):
			## take data from the database
			try:
				return (50/100)*100
			except Exception as e:
				errorstring = "/E-check_value()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass	        

		def bachrreagentfbodash(self):
			try:
				self.rEagent_FRame.destroy()
				self.fpo_dashboard()
			except Exception as e:
				errorstring = "/E-bachrreagentfbodash()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass		    

		def reagentidicator(self):
			try:
				self.rEagent_FRame= Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)
				reagentmsg=Label(self.rEagent_FRame,text="Reagent Indicator",bg="#F5F4EB",fg="#254E58",font="BOLD  23 ")        
				Bback=Button(self.rEagent_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.bachrreagentfbodash)
				canvas=Canvas(self.rEagent_FRame,bg="#F5F4EB")
				canvas.create_rectangle(10, 10, 540, 240,outline="#fb0",fill="#F5F4EB")
				canvas.place(x=60,y=80,width=550,height=250)
				self.progress = Progressbar(self.rEagent_FRame, orient=HORIZONTAL,length=100,  mode='determinate')

				self.rEagent_FRame.place(x=10,y=40,width=780,height=390)
				reagentmsg.place(x=5,y=20,height=40)
				self.progress.place(x=110,y=200,width=450,height=40)
				Bback.place(x=650,y=40,height=30,width=60)
				value=self.check_value()
				self.progress['value']=value
			except Exception as e:
				errorstring = "/E-reagent_indicator()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass			    

		def serch_back(self):
			try:
				self.searchfarmer_FRame.destroy()
				self.fpo_dashboard()
			except Exception as e:
				errorstring = "/E-search_back()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass		    
		    
		def resserch_back(self):
			try:
				self.search_result_Frame.destroy()
				self.fpo_dashboard()
			except Exception as e:
				errorstring = "/E-research_back()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass				

		def search_ffarmer(self):
			try:
				phnoe=self.esearchfarmerl_phoneNo.get()
				url=URL+"farmers?contact_no="+phnoe 
				headers={'Authorization': "Bearer "+token}
				r=requests.get(url,headers=headers)
				data=r.json()

				if(r.status_code == 200):
					if(len(data['data'])==0):
						messagebox.showerror("Search Result","Invalid Phone Number")
					else:
						self.searchfarmer_FRame.destroy()
						self.search_result_Frame= Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)
						self.welcomemsg=Label(self.search_result_Frame,text="Result of Search Farmer by Phone Number",bg="#F5F4EB",fg="#254E58",font="BOLD  23 ")
						Bback=Button(self.search_result_Frame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.resserch_back)
						canvas=Canvas(self.search_result_Frame,bg="#F5F4EB")
						canvas.create_rectangle(10, 10, 540, 240,outline="#fb0",fill="#F5F4EB")
						canvas.place(x=60,y=80,width=550,height=250)
						self.search_result_Frame.place(x=10,y=40,width=780,height=390)
						self.welcomemsg.place(x=5,y=20,height=40)
						Bback.place(x=650,y=80,height=30,width=60)
						table = Table(self.search_result_Frame, ["Name", "User Name", "uuid"], column_minwidths=[100, 100, 150])
						table.place(x=120,y=120,width=400,height=180)
						pr=[]
						for i in range(len(data['data'])):
							pr1=[data['data'][i]['name'],data['data'][i]['username'],data['data'][i]['uuid']]
							pr.append(pr1)
						table.set_data(pr)  
				else:
					messagebox.showerror("Search Result","Invalid Phone Number")
			except Exception as e:
				errorstring = "/E-search_ffarmer()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass			        
        

		def search_by_number(self):
			try:
				self.searchfarmer_FRame= Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)
				self.welcomemsg=Label(self.searchfarmer_FRame,text="Search Farmer by Phone Number",bg="#F5F4EB",fg="#254E58",font="BOLD  23 ")
				Bback=Button(self.searchfarmer_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.serch_back)
				canvas=Canvas(self.searchfarmer_FRame,bg="#F5F4EB")
				canvas.create_rectangle(10, 10, 540, 240,outline="#fb0",fill="#F5F4EB")
				canvas.place(x=60,y=80,width=550,height=250)
				lsearchfarmer_phoneNo=Label(self.searchfarmer_FRame,text="Phone Number\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  14 ")
				self.esearchfarmerl_phoneNo=Entry(self.searchfarmer_FRame,bg="#F5F4EB",font=("Calibri",14),justify="left")
				#self.efarmerlogin_phone.bind("<FocusIn>")#,self.focus_in)
				#self.efarmerlogin_phone.bind("<FocusOut>")#,self.focus_out)
				bfarmer_register=Button(self.searchfarmer_FRame,text="Next",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.search_ffarmer)
				#bfarmer_register.bind("<FocusIn>")#,self.bfocus_out)
				self.welcomemsg.place(x=5,y=20,height=40)
				self.searchfarmer_FRame.place(x=10,y=40,width=780,height=390)
				lsearchfarmer_phoneNo.place(x=80,y=190,height=25)
				self.esearchfarmerl_phoneNo.place(x=280,y=190,width=300)
				Bback.place(x=650,y=80,height=30,width=60)
				bfarmer_register.place(x=650,y=340,height=30,width=60) 
				self.keypad_label.place(x=18,y=15,width=40,height=20)                        
				self.bfocus_in.place(x=70,y=15,width=40,height=20)    
				self.bfocus_out.place(x=120,y=15,width=40,height=20) 
			except Exception as e:
				errorstring = "/E-search_by_number()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass		    

		def farm_back(self):
			try:
				self.Farmdashboard_FRame.destroy()
				self.fpo_dashboard()
			except Exception as e:
				errorstring = "/E-farm_back()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass			    

		def parseval(self):
			try:
				a=self.echoosefarm.get()

				global fr_uuid
				url=URL+"farmers/"+fr_uuid+"/areas"
				headers={'Authorization': "Bearer "+token}
				r=requests.get(url,headers=headers)
				data=r.json()
				if(a==''):
					logging.info ("error")
				else:
					for i in data:
						if(a==i['name']):
							self.effield_name.set(i['name'])
							self.efsoil_density.set(i['soil_density'])
							self.effarmer_surveyno.set(i['survey_no'])
							self.effarmer_lat.set(i['latitude'])
							self.effarmer_long.set(i['longitude'])
							#self.effarmer_crop.set(i['crop'][0])
							#print ("i['crop'][0] ==>",i['crop'][0])
							#print ("i['crop'] ==>",i['crop'])
							self.tkvarr2.set(i['crop'][0])
							self.tkvarr.set(i['soil_type'])
							self.effarmmer_area.set(i['area_size'])
							self.efield_name['state']='normal'
							self.esoil_density['state']='normal'
							self.efarmer_surveyno['state']='normal'
							self.efarmer_lat['state']='normal'
							self.efarmer_long['state']='normal'
							self.efarmer_crop['state']='normal'
							self.efarmmer_area['state']='normal'
							self.esample_type['state']='normal'
							self.editfarm['state']='normal'
							break
			except Exception as e:
				errorstring = "/E-parseval()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass
											
		def update_fieldinfo(self):
			try:
				global fr_fieldname
				global fr_fieldarea
				global fr_croptype
				global fr_soiltype
				global fr_farmlong
				global fr_farmlat
				global fr_farmsurveyno
				global fr_density
				global fr_soilden
				global URL
				global token
				global Name
				global fr_uuid
				global fr_farmuuid

				fr_fieldname=self.efield_name.get()
				fr_fieldarea=self.efarmmer_area.get()
				#fr_croptype=self.efarmer_crop.get()
				fr_croptype=self.tkvarr2.get()
				fr_soiltype=self.tkvarr.get()
				fr_farmlong=self.efarmer_long.get()
				fr_farmlat=self.efarmer_lat.get()
				fr_farmsurveyno=self.efarmer_surveyno.get()
				fr_soilden=1.3#self.esoil_density.get()
				
				if(fr_fieldarea=='' or fr_fieldarea=='' or fr_croptype=='' or fr_soiltype=='' or fr_farmlong=='' or fr_farmlat=='' or fr_farmsurveyno==''):
					messagebox.showerror("ERROR","Few of the fields are empty")
				else:
					url=URL+"farmers/"+fr_uuid+"/areas"
					headers={'Authorization': "Bearer "+token}
					r=requests.get(url,headers=headers)
					data=r.json()
					a=self.echoosefarm.get()
					for i in data:
						if i['name']==a:
							fr_farmuuid=i['uuid']
							break
					a=re.match("^[0-9]",fr_fieldarea)
					#b=re.match("^[0-9]",fr_farmlong)
					#c=re.match("^[0-9]",fr_farmlat)
					d=re.match("^[0-9]",fr_farmsurveyno)
					if(not a):
						messagebox.showerror("Value Error","Field area should be a number")
					#elif(not b):
					#	messagebox.showerror("Value Error","Longitude should be a number")
					#elif(not c):
					#	messagebox.showerror("Value Error","Latitude should be a number")
					elif(not d):
						messagebox.showerror("Value Error","Survey Number should be a number")
					else:
						url= URL +"farmers/"+fr_uuid+"/areas/"+fr_farmuuid
						payload={'name':fr_fieldname,'latitude':fr_farmlat,'longitude':fr_farmlong,'soil_density':fr_soilden,'crop':[fr_croptype],'soil_type':fr_soiltype,'survey_no':fr_farmsurveyno,'area_size':fr_fieldarea}
						headers={'Authorization': "Bearer "+token,'content-type': 'application/json'}
					#headers={'content-type': 'application/json'}
					#a=json.dumps(payload)
					#print(a)
						r=requests.put(url,data=json.dumps(payload),headers=headers)       
					#print(r)
					#print(r.content)
						data=r.json()
						if(r.status_code == 200):
							messagebox.showinfo("Success","Updated Info")
							self.farmerxmangement_FRame.destroy()
							self.farm_dashboard()
						else:
							if('name' in data['errors']):
								messagebox.showerror("Value Error","Name should be of length greater than 3")
			except Exception as e:
				errorstring = "/E-update_field_info()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 

		def farmer_editfarm(self):
			try:
				previous_choice=[]
				global fr_uuid
				url=URL+"farmers/"+fr_uuid+"/areas"
				headers={'Authorization': "Bearer "+token}
				r=requests.get(url,headers=headers)
				data=r.json()
				for i in data:
					previous_choice.append(i['name'])
				self.keyboard_process = None
				self.farmerxmangement_FRame = Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1,)
				managementmsg=Label(self.farmerxmangement_FRame,text="Edit Field",bg="#F5F4EB",fg="#254E58",font="BOLD  23 ")
				Bback=Button(self.farmerxmangement_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.backfarmer_management)
				canvas=Canvas(self.farmerxmangement_FRame)
				canvas.create_rectangle(5, 5, 505, 330,outline="#fb0",fill="#F5F4EB")
				canvas.place(x=170,y=50,width=510,height=335)
				self.editfarm=Button(self.farmerxmangement_FRame,text="Update",bg="#3e8ddc",fg="#fffdfd",font="centre 12",command=self.update_fieldinfo)
				lchoosefield=Label(self.farmerxmangement_FRame,text="Choose Field",bg="#F5F4EB",fg="#254E58",font="BOLD  13 ")
				
				self.echoosefarm = ttk.Combobox(self.farmerxmangement_FRame,values=previous_choice,height=4)
				self.effield_name=StringVar()
				self.efsoil_density=StringVar()
				self.effarmer_surveyno=StringVar()
				self.effarmer_lat=StringVar()
				self.effarmer_long=StringVar()
				self.effarmer_crop=StringVar()
				self.effarmmer_area=StringVar()
				Bparseval=Button(self.farmerxmangement_FRame,text="Parse Value\n=>",bg="#3e8ddc",fg="#fffdfd",font="centre 12",command=self.parseval)
				lfield_name=Label(self.farmerxmangement_FRame,text="Field Name\t\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  13 ")
				self.efield_name=Entry(self.farmerxmangement_FRame,textvariable=self.effield_name,bg="#F5F4EB",font=("Calibri",14),justify="left")
				lfamrmer_area=Label(self.farmerxmangement_FRame,text="Field Area (Acres)\t\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  13 ")
				self.efarmmer_area=Entry(self.farmerxmangement_FRame,textvariable=self.effarmmer_area,bg="#F5F4EB",font=("Calibri",14),justify="left")

######################################################################################################################################

				lfarmer_crop=Label(self.farmerxmangement_FRame,text="Crop Type\t\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  13 ")
				self.efarmer_crop=Entry(self.farmerxmangement_FRame,textvariable=self.effarmer_crop,bg="#F5F4EB",font=("Calibri",14),justify="left")
				lfarmer_soil=Label(self.farmerxmangement_FRame,text="Type\t\t\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  13 ")
				
				self.tkvarr2=StringVar(self.farmerxmangement_FRame)
				choice2={'Turmeric','Local cultivar','Cabbage','Rice','Wheat','Bajra','Barley','Maize','Mothbean','Guar','Castor','Sunflower','Oat','Sorghum','Soyabean','Pearlmillet','Chickpea','Pigeonpea'}
				self.tkvarr2.set('Turmeric')
				self.efarmer_crop=OptionMenu(self.farmerxmangement_FRame, self.tkvarr2, *choice2)
				#self.efarmer_crop=Entry(self.farmerxmangement_FRame,bg="#F5F4EB",font=("Calibri",14),justify="left")
				#self.efarmer_crop.bind("<FocusIn>",self.focus_in)
				#self.efarmer_crop.bind("<FocusOut>",self.focus_out)
				lfarmer_soil=Label(self.farmerxmangement_FRame,text="Soil Type\t\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  13 ")
				self.tkvarr=StringVar(self.farmerxmangement_FRame)
				choice={'Alfisol','Alfisol(Sandy Loam)','Alluvial','Alluvial Soil','Black Soil','Black soil (Vertisols)','Chalka Soils','Inceptisol','Inceptisols (Sandy loam)','Inceptisols(Sandy Clay Loam)','Red Loam Soil','Sandy Clay Loam','Seirozem(Inceptisols/Entisols)','Sierozem','Sierozem (Inceptisols/Verisols)','Typic Haplustept(Alluvial)','Vertisol'}
				self.tkvarr.set('Alfisol')
				self.esample_type= OptionMenu(self.farmerxmangement_FRame, self.tkvarr, *choice)


######################################################################################################################################				
				
				'''
				self.tkvarr=StringVar(self.farmerxmangement_FRame)
				#choice={'Water','Soil - Clay','Soil - Red','Soil - Black','Inceptisols','Alluvial','Sandy clay loam'}
				#self.tkvarr.set('Water')
				choice={'Alfisol','Alfisol(Sandy Loam)','Alluvial','Alluvial Soil','Black Soil','Black soil (Vertisols)','Chalka Soils','Inceptisol','Inceptisols (Sandy loam)','Inceptisols(Sandy Clay Loam)','Red Loam Soil','Sandy Clay Loam','Seirozem(Inceptisols/Entisols)','Sierozem','Sierozem (Inceptisols/Verisols)','Typic Haplustept(Alluvial)','Vertisol'}
				self.tkvarr.set('Alfisol')				
				self.esample_type= OptionMenu(self.farmerxmangement_FRame, self.tkvarr, *choice)
				'''
				
				lfarmer_long=Label(self.farmerxmangement_FRame,text="Geographical Longitude\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  13 ")
				self.efarmer_long=Entry(self.farmerxmangement_FRame,textvariable=self.effarmer_long,bg="#F5F4EB",font=("Calibri",14),justify="left")
				lfarmer_lat=Label(self.farmerxmangement_FRame,text="Geographical Latitude\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  13 ")
				self.efarmer_lat=Entry(self.farmerxmangement_FRame,textvariable=self.effarmer_lat,bg="#F5F4EB",font=("Calibri",14),justify="left")
				lfarmer_surveyno=Label(self.farmerxmangement_FRame,text="Survey Number\t\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  13 ")
				self.efarmer_surveyno=Entry(self.farmerxmangement_FRame,textvariable=self.effarmer_surveyno,bg="#F5F4EB",font=("Calibri",14),justify="left")
				lsoil_density=Label(self.farmerxmangement_FRame,text="Soil Density\t\t:",bg="#F5F4EB",fg="#254E58",font="BOLD  13 ")
				self.esoil_density=Entry(self.farmerxmangement_FRame,textvariable=self.efsoil_density,bg="#F5F4EB",font=("Calibri",14),justify="left")
				self.farmerxmangement_FRame.place(x=10,y=40,width=780,height=390)
				managementmsg.place(x=5,y=10,height=34)
				Bback.place(x=690,y=15,height=30,width=60)
				self.editfarm.place(x=690,y=340,height=30,width=60)    
				lchoosefield.place(x=20,y=100)
				self.echoosefarm.place(x=10,y=170,width=150,height=50)
				Bparseval.place(x=25,y=250)
				lfield_name.place(x=190,y=60,height=25)  
				self.efield_name.place(x=420,y=60,width=230,height=25)
				lfamrmer_area.place(x=190,y=100,height=25)  
				self.efarmmer_area.place(x=420,y=100,width=230,height=25)
				lfarmer_crop.place(x=190,y=140,height=25)  
				self.efarmer_crop.place(x=420,y=140,width=230,height=25)
				lfarmer_soil.place(x=190,y=180,height=25)  
				self.esample_type.place(x=420,y=180,width=230,height=25)
				lfarmer_long.place(x=190,y=220,height=25)  
				self.efarmer_long.place(x=420,y=220,width=230,height=25)
				lfarmer_lat.place(x=190,y=260,height=25)  
				self.efarmer_lat.place(x=420,y=260,width=230,height=25)
				lfarmer_surveyno.place(x=190,y=300,height=25)  
				self.efarmer_surveyno.place(x=420,y=300,width=230,height=25)
				self.esoil_density.place(x=420,y=340,width=230,height=25)
				lsoil_density.place(x=190,y=340,height=25)  
				
				self.keypad_label.place(x=18,y=15,width=40,height=20)                        
				self.bfocus_in.place(x=60,y=15,width=40,height=20)    
				self.bfocus_out.place(x=120,y=15,width=40,height=20)
								
				self.efield_name['state']='disabled'
				self.efarmmer_area['state']='disabled'
				self.efarmer_crop['state']='disabled'
				self.esample_type['state']='disabled'
				self.efarmer_long['state']='disabled'
				self.efarmer_lat['state']='disabled'
				self.efarmer_surveyno['state']='disabled'
				self.esoil_density['state']='disabled'
				self.editfarm['state']='disabled'
			except Exception as e:
				errorstring = "/E-farmer_editfarm()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 	

		def backfarmer_management2(self):
			try:
				self.farmer_deleteFRAME.destroy()
				self.farm_dashboard()
			except Exception as e:
				errorstring = "/E-backfarmer_management()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass	

		def backtofarm_dash(self):
			try:
				self.Con_FRame.destroy()
				self.farm_dashboard()
			except Exception as e:
				errorstring = "/E-backtofarm_dash()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass				

		def continueto_test(self):
			try:
				global fr_farmuuid
				url=URL+"farmers/"+fr_uuid+"/areas"
				headers={'Authorization': "Bearer "+token}
				r=requests.get(url,headers=headers)
				data=r.json()
				a=self.econchoosefarm.get()
				for i in data:
					if i['name']==a:
						fr_farmuuid=i['uuid']
						break
						
				self.txt_company_code = self.var_company_name.get()
				
				if self.txt_company_code == "":
					self.txt_company_code = "C-NULL"
				
				with open(self.result_path,"r+") as e:
				    a=json.load(e)	
				a["Company_code"] = self.txt_company_code 				    		
				obj=a

				with open(self.result_path,"w")as e:
					json.dump(obj,e)
						
				self.Con_FRame.destroy()
				self.test_page()
			except Exception as e:
				errorstring = "/E-continue_to_test()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass				
				
		def selectandcon(self):
			try:
				previous_choice=[]
				global fr_uuid
				url=URL+"farmers/"+fr_uuid+"/areas"
				headers={'Authorization': "Bearer "+token}
				r=requests.get(url,headers=headers)
				data=r.json()
				for i in data:
						previous_choice.append(i['name'])
				
				self.Con_FRame = Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1,)
				self.Con_FRame.place(x=10,y=40,width=780,height=390)
				welcomemsg=Label(self.Con_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  23 ")
				welcomemsg.place(x=5,y=20,height=30)
				canvas=Canvas(self.Con_FRame,bg="#F5F4EB")
				canvas.create_rectangle(10, 10, 390, 320,outline="#fb0",fill="#F5F4EB")
				canvas.place(x=200,y=50,width=400,height=330)
				lselecc=Label(self.Con_FRame,text="Select Farm",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
				lselecc.place(x=330,y=70)	

				self.econchoosefarm = ttk.Combobox(self.Con_FRame,values=previous_choice,height=4)
				
				self.econchoosefarm.place(x=250,y=140,height=50,width=300)
				Bback=Button(self.Con_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.backtofarm_dash)
				Bback.place(x=690,y=15,height=30,width=60)
				
				if len(previous_choice) >= 0:
					self.econchoosefarm.current(0)
				else:
					Bback['state']=DISABLE
					
				label_company_name=Label(self.Con_FRame,text="Company Code",bg="#F5F4EB",fg="#254E58",font="8")
				label_company_name.place(x=250,y=230,height=20)
				
				self.var_company_name=StringVar()

				self.entry_comapany_name=Entry(self.Con_FRame,textvariable=self.var_company_name,bg="#F5F4EB",font="8",justify="left")	
				self.entry_comapany_name.place(x=380,y=230,width=170,height=25)	
				
				Bconti=Button(self.Con_FRame,text="Continue",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.continueto_test)
				Bconti.place(x=250,y=290,height=50,width=300)
				
				self.keypad_label.place(x=18,y=15,width=40,height=20)                        
				self.bfocus_in.place(x=60,y=15,width=40,height=20)    
				self.bfocus_out.place(x=120,y=15,width=40,height=20) 				
			except Exception as e:
				errorstring = "/E-select_and_continue()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass				

		def farm_dashboard(self):
			try:
				global fr_name
				self.Farmdashboard_FRame = Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1,)
				self.Farmdashboard_FRame.place(x=10,y=40,width=780,height=390)
				
				self.welcomemsg=Label(self.Farmdashboard_FRame,text="WELCOME "+fr_name,bg="#F5F4EB",fg="#254E58",font="BOLD  10 ")
				canvas=Canvas(self.Farmdashboard_FRame,bg="#F5F4EB")
				canvas.create_rectangle(10, 10, 390, 320,outline="#fb0",fill="#F5F4EB")
				canvas.place(x=200,y=50,width=400,height=330)
				Bfarmback=Button(self.Farmdashboard_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre 10",command=self.farm_back)
				Bcreatefarm=Button(self.Farmdashboard_FRame,text="Create Field",bg="#F05E23",fg="#fff",font="centre 10",command=self.farmer_xmanagement)
				Beditfarm = Button(self.Farmdashboard_FRame,text="Edit Field",bg="#A79B94",fg="#2C2C2C",font="centre 10",command=self.farmer_editfarm)
				Bgeneratereport = Button(self.Farmdashboard_FRame,text="Select Field and Continue",bg="#F05E23",fg="#fff",font="centre 10",command=self.selectandcon)
				self.welcomemsg.place(x=5,y=20,height=30)
				Bfarmback.place(x=650,y=20,height=30,width=100)
				Bcreatefarm.place(x=265,y=90,width=250,height=50)
				Beditfarm.place(x=265,y=185,width=250,height=50)
				Bgeneratereport.place(x=265,y=280,width=250,height=50)
				
				self.keypad_label.place_forget()
				self.bfocus_in.place_forget()
				self.bfocus_out.place_forget()				
			except Exception as e:
				errorstring = "/E-farmer_dashboard()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass		    

		def fpo_dashboard(self):
			try:
				global Name
				self.machine_status_label.configure(text = "")
				self.Fpodashboard_FRame = Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1,)
				self.Fpodashboard_FRame.place(x=10,y=40,width=780,height=390)
				
				self.welcomemsg=Label(self.Fpodashboard_FRame,text="WELCOME "+ Name,bg="#F5F4EB",fg="#254E58",font="BOLD  14 ")
				canvas=Canvas(self.Fpodashboard_FRame,bg="#F5F4EB")
				canvas.create_rectangle(10, 10, 390, 320,outline="#fb0",fill="#F5F4EB")
				canvas.place(x=200,y=50,width=400,height=330)
				Bcalibur=Button(self.Fpodashboard_FRame,text="Calibrate",bg="#3e8ddc",fg="#fffdfd",font="centre 8",command=self.calibration)
				#Bservice=Button(self.Fpodashboard_FRame,text="Service Test",bg="#3e8ddc",fg="#fffdfd",font="centre 8 ",command=self.servicetest)
				Blogoutt=Button(self.Fpodashboard_FRame,text="Logout",bg="#3e8ddc",fg="#fffdfd",font="centre 8",command=self.fpo_logout)
				Bnewfarmwer=Button(self.Fpodashboard_FRame,text="New Farmer",bg="#F05E23",fg="#fff",font="centre 8",command=self.newfarmer_register)
				Bexistingfarmer=Button(self.Fpodashboard_FRame,text="ExistingFarmer",bg="#A79B94",fg="#2C2C2C",font="centre 8",command=self.existingfarmer_login)
				BSettings = Button(self.Fpodashboard_FRame,text="Settings",bg="#A79B94",fg="#2C2C2C",font="centre 8",command=self.init_settings)
				Bsearchph = Button(self.Fpodashboard_FRame,text="Search By Phone Number",bg="#F05E23",fg="#fff",font="centre 8",command=self.search_by_number)
				BReagentindicator = Button(self.Fpodashboard_FRame,text="Reagent Indicator",bg="#F05E23",fg="#fff",font="centre 8",command=self.reagentidicator)
				self.welcomemsg.place(x=5,y=20,height=30)
				Bcalibur.place(x=650,y=80,height=30,width=100)
				#Bservice.place(x=650,y=120,height=30,width=100)
				Blogoutt.place(x=650,y=40,height=30,width=100)
				Bnewfarmwer.place(x=265,y=70,width=250,height=30)
				Bexistingfarmer.place(x=265,y=130,width=250,height=30)
				Bsearchph.place(x=265,y=190,width=250,height=30)
				BSettings.place(x=265,y=250,width=250,height=30)
				BReagentindicator.place(x=265,y=310,width=250,height=30)
				BReagentindicator['state']='disabled'
				self.keypad_label.place_forget()
				self.bfocus_in.place_forget()
				self.bfocus_out.place_forget()	
				
				self.dispense_label.place(x=270,y=15,width=50,height=20)
				self.bsample_solution.place(x=330,y=15,width=50,height=20)    
				self.bdistilled_water.place(x=400,y=15,width=50,height=20) 
				self.bdistilled_water_ec.place(x=470,y=15,width=50,height=20)   						
				self.bstop_dispense.place(x=540,y=15,width=50,height=20) 
			except Exception as e:
				errorstring = "/E-fpo_dashboard()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass	
				
		def farmer_dashboard(self):
			try:
				global Name
				self.machine_status_label.configure(text = "")
				self.Fpodashboard_FRame = Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1,)
				self.Fpodashboard_FRame.place(x=10,y=40,width=780,height=390)
				
				self.welcomemsg=Label(self.Fpodashboard_FRame,text="WELCOME "+ Name,bg="#F5F4EB",fg="#254E58",font="BOLD  14 ")
				canvas=Canvas(self.Fpodashboard_FRame,bg="#F5F4EB")
				canvas.create_rectangle(10, 10, 390, 320,outline="#fb0",fill="#F5F4EB")
				canvas.place(x=200,y=50,width=400,height=330)
				Bcalibur=Button(self.Fpodashboard_FRame,text="Calibrate",bg="#3e8ddc",fg="#fffdfd",font="centre 8",command=self.calibration)
				Bservice=Button(self.Fpodashboard_FRame,text="Service Test",bg="#3e8ddc",fg="#fffdfd",font="centre 8 ",command=self.servicetest)
				Blogoutt=Button(self.Fpodashboard_FRame,text="Logout",bg="#3e8ddc",fg="#fffdfd",font="centre 8",command=self.fpo_logout)
				Bnewfarmwer=Button(self.Fpodashboard_FRame,text="New Farmer",bg="#F05E23",fg="#fff",font="centre 8",command=self.newfarmer_register)
				Bexistingfarmer=Button(self.Fpodashboard_FRame,text="ExistingFarmer",bg="#A79B94",fg="#2C2C2C",font="centre 8",command=self.existingfarmer_login)
				BSettings = Button(self.Fpodashboard_FRame,text="Settings",bg="#A79B94",fg="#2C2C2C",font="centre 8",command=self.init_settings)
				Bsearchph = Button(self.Fpodashboard_FRame,text="Search By Phone Number",bg="#F05E23",fg="#fff",font="centre 8",command=self.search_by_number)
				BReagentindicator = Button(self.Fpodashboard_FRame,text="Reagent Indicator",bg="#F05E23",fg="#fff",font="centre 8",command=self.reagentidicator)
				self.welcomemsg.place(x=5,y=20,height=30)
				Bcalibur.place(x=650,y=80,height=30,width=100)
				Bservice.place(x=650,y=120,height=30,width=100)
				Blogoutt.place(x=650,y=40,height=30,width=100)
				Bnewfarmwer.place(x=265,y=70,width=250,height=30)
				Bexistingfarmer.place(x=265,y=130,width=250,height=30)
				Bsearchph.place(x=265,y=190,width=250,height=30)
				BSettings.place(x=265,y=250,width=250,height=30)
				BReagentindicator.place(x=265,y=310,width=250,height=30)
				BReagentindicator['state']='disabled'
				self.keypad_label.place_forget()
				self.bfocus_in.place_forget()
				self.bfocus_out.place_forget()					
			except Exception as e:
				errorstring = "/E-fpo_dashboard()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass		    
					    

		def loginfpo_check(self):
			try:
				loginuser_name=self.euser_name.get()
				loginpass_Word=self.epass_word.get()
				
				#communicate to check 
				global URL
				global token
				global Name
				global device_id
				device_id=str(uuid.uuid5(uuid.NAMESPACE_DNS, hex(uuid.getnode())))
				url= URL +"app/login"
				payload={'username':loginuser_name,'password':loginpass_Word,'deviceID':device_id}
				headers={'content-type': 'application/json'}
				r=requests.post(url,data=json.dumps(payload),headers=headers)    

				self.machine_status_label.configure(text = "")
				if(r.status_code == 200):
					obj={"N":"0",
					"P":"0",
					"K":"0",
					"A":"0",
					"device_uuid":"0",
					"fr_uuid":"0",
					"EC":"0",
					"pH":"0",
					"Company_code":"0"
					}	
					
					with open(self.result_path,"w+") as e:
					    json.dump(obj,e)		
					    
					with open(self.result_path,"r+") as e:
					    a=json.load(e)	
					a["device_uuid"] = device_id 				    		
					#a.update({'device_uuid':device_id})
					obj=a

					with open(self.result_path,"w")as e:
						json.dump(obj,e)
					with open(self.result_path,"r+") as e:
						a=json.load(e)
					
					data=r.json()
					token=data['token']
					url= URL +"users/@me"    
					headers={'Authorization': "Bearer "+token}
					r=requests.get(url,headers=headers)
					data=r.json()
					Name=data['name']
					type_of=data['type']
					
					if(type_of=='fpo'):
						self.login_FRame.destroy()
						self.fpo_dashboard()
					elif(type_of=='service'):
						self.login_FRame.destroy()
						self.farmer_dashboard()
					elif(type_of=='deviceadmin'):
						pass
					else:
						pass
				else:
				    messagebox.showerror("Login Error", "Invalid username or password...")
				    pass
			except Exception as e:
					messagebox.showerror("Internet Connection Error", "Check Internet Connection...")
					errorstring = "/E-loginfpo_check()"
					logging.warning("%s", errorstring)
					logging.exception("Exception occurred") 
					
			finally:
					pass		        

		def front_page(self):
			try:
				self.keyboard_process = None
				self.machine_status_label.configure(text = "")
				self.login_FRame = Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1,)
				l1 = Label(self.login_FRame,text="WELCOME TO KRISHITANTRA",bg="#F5F4EB",fg="#254E58",font="BOLD  18 ")
				luser_name = Label(self.login_FRame,text="User Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")            
				self.euser_name = Entry(self.login_FRame,bg="#F5F4EB",font=("Calibri",14),justify="left", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)

				lpass_word = Label(self.login_FRame,text="Password",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
				self.epass_word = Entry(self.login_FRame,show="*",bg="#F5F4EB",font=("Calibri",14),justify="left", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)

				bforgetpassword = Button(self.login_FRame,text="Forgot Password ?",fg="#fffdfd",bg="#3e8ddc",font="centre 10",command=self.forget_page)
				blogin = Button(self.login_FRame,text="LOGIN",bg="#3e8ddc",fg="#fffdfd",font="centre 10",command=self.loginfpo_check)
				blogin.bind("<FocusIn>",self.bfocus_out)
				self.lmsgbox = Label(self.login_FRame,text="",bg="#F5F4EB",fg="#ff0000",font="BOLD 12")
				self.login_FRame.place(x=10,y=40,width=780,height=390)
			
				l1.place(x=140,y=50,width=500,height=50)
				luser_name.place(x=150,y=150)
				self.euser_name.place(x=310,y=150,width=300)
				lpass_word.place(x=150,y=220)
				self.epass_word.place(x=310,y=220,width=300)     

				bforgetpassword.place(x=110,y=320,width=200,height=35)
				blogin.place(x=560,y=320,width=100,height=35)
				self.lmsgbox.place(x=50,y=330)
				
				self.keypad_label.place(x=18,y=15,width=40,height=20)                        
				self.bfocus_in.place(x=70,y=15,width=40,height=20)    
				self.bfocus_out.place(x=120,y=15,width=40,height=20) 
								
			except Exception as e:
				errorstring = "/E-front_page()"
				logging.warning ("%s", errorstring)
			finally:
				pass		    
		
		def washaprtus(self):
			try:
				self.bconfirm_test['state'] = DISABLED
				
				with open(self.chemical_firmware_version) as equation_contents:
					equation_status_data = json.load(equation_contents)				        

				WashTestTube_DeviceFlush1 = equation_status_data["WashTestTube-DeviceFlush1"]
				WashTestTube_DeviceFlush2 = equation_status_data["WashTestTube-DeviceFlush2"]
				WashTestTube_DeviceFlush3 = equation_status_data["WashTestTube-DeviceFlush3"]
			
				WashCuvette_DeviceWash = equation_status_data["WashCuvette-DeviceWash"]		
				
				flush_success = 0
				abort_cmd  = "KT+ABORT\r\n"
				flush_ret_val = self.kt_sendcommand(abort_cmd,5,10)		
				#self.listboxx.config(state=NORMAL)			

				'''
				DeviceFlush1 = "KT+PR:"+WashTestTube_DeviceFlush1+"\r\n"
				flush_ret_val = self.kt_sendcommand(DeviceFlush1,103,10)
				DeviceFlush2 = "KT+PR:"+WashTestTube_DeviceFlush2+"\r\n"
				flush_ret_val = self.kt_sendcommand(DeviceFlush2,160,10)	
				DeviceFlush3 = "KT+PR:"+WashTestTube_DeviceFlush3+"\r\n"
				flush_ret_val = self.kt_sendcommand(DeviceFlush3,80,10)						
				'''
				
				if flush_ret_val == "SUCCESS":
					self.listboxx.config(state=NORMAL)				
					#self.bconfirm_test['state']=NORMAL
					flush_success = 1
				else:
					flush_success = 0
				
			except Exception as e:
				errorstring = "/E-washappartus()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
				flush_success = 0
			finally:
				if flush_success == 1:
					messagebox.showinfo("Test Ready", "System is ready for testing...")
					self.machine_status_label.configure(text = "")
				else:
					self.machine_status_label.configure(text = "")
				pass                         
		
		
		def kt_send_external_abort_command(self,scommand,timeinterval,errorcode):
			try:	
				self.machine_status_label.configure(text = "")
				device_return_value = 0
				device_state_flag = 0
				device_flush_flag = 0
				retry_status_count = 10
				comm_error_flag = 0
				
				for retry_flush_count in range(25,0,-1):
						acquired_actual_command = self.sem.acquire()
						self.ser.flushInput()
						self.ser.flushOutput()					        
						self.ser.write(scommand.encode()) 
						device_status2 = self.ser.readline()
						if acquired_actual_command:
							self.sem.release()									
						device_status2 = device_status2.decode("ISO-8859-1") 
						logging.info (scommand+"-device status flag-%s"+device_status2)

						if (device_status2 == "KT+OK\r\n"):
								device_flush_flag = 1
								timeinterval = int(timeinterval)
								time.sleep(timeinterval) 
								device_return_value = "SUCCESS"											
								break
						elif (device_status2 == "KT+BUSY\r\n"):
								time.sleep(5)   
						elif (device_status2 == "KT+ERROR\r\n"):
								device_return_value = 0#"Error:" + str(errorcode)						
						else:
								comm_error_flag= 1
								break
				if comm_error_flag == 1:
					self.machine_status_label.configure(text = "Error in serial Connection")
			except Exception as e:
				errorstring = "/E-kt_send_ext_abort_command()/"
				logging.warning("%s", errorstring + scommand)
				logging.exception("Exception occurred")
				self.machine_status_label.configure(text = "Error in serial Connection")
				device_return_value = "ERROR"
			finally:
				return device_return_value					        
				        
		def kt_send_external_command(self,scommand,timeinterval,errorcode):
			try:		
				self.machine_status_label.configure(text = "")		    				 			
				device_return_value = 0
				device_state_flag = 0
				device_flush_flag = 0
				retry_status_count = 10
				comm_error_flag = 0
				
				self.es_or_nitrogen_flag = 1
				
				for retry_status_count in range(25,0,-1):
						acquired_status_1 = self.sem.acquire()
						self.ser.flushInput()
						self.ser.flushOutput()
						self.ser.write("KT+EXTSTATUS\r\n".encode()) 
						device_status1 = self.ser.readline()
						if acquired_status_1:
							self.sem.release()							
						device_status1 = device_status1.decode("ISO-8859-1") #ser.readline returns a binary, convert to string
						logging.info (scommand + "EXTSTATUS"+ device_status1)
						
						split_device_status1 = device_status1.split("+")
						if (split_device_status1[1][0] == "0"):
							if (split_device_status1[1][1] == "7"):
								device_state_flag = 1
								break
							else:
								with open(self.image_path+"pump_servo_constants.json","r+") as e:
									a=json.load(e)	
													    		
								S1 = a["Servo1"]["01"]
								S2 = a["Servo1"]["02"]
								S3 = a["Servo1"]["03"]
								S4 = a["Servo1"]["04"]
								S5 = a["Servo1"]["05"]
								S6 = a["Servo1"]["06"]
								S7 = a["Servo1"]["07"]
								S8 = a["Servo1"]["08"]
								S9 = a["Servo1"]["09"]
								S10 = a["Servo1"]["10"]
								S11 = a["Servo1"]["11"]
								S12 = a["Servo1"]["12"]
								S13 = a["Servo1"]["13"]
								
								Servo_All_Constants = S1 + "+" + S2 + "+" + S3 + "+" + S4 + "+" + S5 + "+" + S6 + "+" + S7 + "+" + S8 + "+" + S9 + "+" + S10 + "+" + S11 + "+" + S12 + "+" + S13
						
								DP1 = a["D"]["01"]
								DP2 = a["D"]["02"]
								DP3 = a["D"]["03"]
								DP4 = a["D"]["04"]
								DP5 = a["D"]["05"]
								DP6 = a["D"]["06"]
								DP7 = a["D"]["07"]
								DP8 = a["D"]["08"]
								DP9 = a["D"]["09"]
								DP10 = a["D"]["10"]
								DP11 = a["D"]["11"]
								DP12 = a["D"]["12"]
								DP13 = a["D"]["13"]
								DP14 = a["D"]["14"]
								DP15 = a["D"]["15"]
								DP16 = a["D"]["16"]
						
								D_Pump_Constants = DP1 + "+" + DP2 + "+" + DP3 + "+" + DP4 + "+" + DP5 + "+" + DP6 + "+" + DP7 + "+" + DP8 + "+" + DP9 + "+" + DP10 + "+" + DP11 + "+" + DP12+ "+" + DP13+ "+" + DP14+ "+" + DP15+ "+" + DP16 
						
								MP1 = a["M"]["01"]
								MP2 = a["M"]["02"]
								MP3 = a["M"]["03"]
								MP4 = a["M"]["04"]
								MP5 = a["M"]["05"]
								MP6 = a["M"]["06"]
								MP7 = a["M"]["07"]
								MP8 = a["M"]["08"]
								MP9 = a["M"]["09"]
								MP10 = a["M"]["10"]
								MP11 = a["M"]["11"]
								MP12 = a["M"]["12"]
								MP13 = a["M"]["13"]
								MP14 = a["M"]["14"]
								MP15 = a["M"]["15"]
								MP16 = a["M"]["16"]
						
								ML_Pump_Constants = MP1 + "+" + MP2 + "+" + MP3 + "+" + MP4 + "+" + MP5 + "+" + MP6 + "+" + MP7 + "+" + MP8 + "+" + MP9 + "+" + MP10 + "+" + MP11 + "+" + MP12 + "+" + MP13 + "+" + MP14 + "+" + MP15 + "+" + MP16 
								
								acquired_status_constants1 = self.sem.acquire()
								cmd_Servo_All_Constants = "KT+WRITSERVOC:" + Servo_All_Constants + "\r\n"
								self.ser.write(cmd_Servo_All_Constants.encode())
								read_WRITSERVOC = self.ser.readline()
								
								cmd_D_Pump_Constants = "KT+WRITPUMPCD:" + D_Pump_Constants + "\r\n"
								self.ser.write(cmd_D_Pump_Constants.encode())
								read_WRITPUMPCD = self.ser.readline()
								
								cmd_ML_Pump_Constants = "KT+WRITPUMPCM:" + ML_Pump_Constants + "\r\n"
								self.ser.write(cmd_ML_Pump_Constants.encode())
								read_WRITPUMPCM = self.ser.readline()
								if acquired_status_constants1:
									self.sem.release()										
									
						elif (split_device_status1[0] == "1"):
								time.sleep(5)   
						else:
								comm_error_flag = 1
								errstr = "Communication Error : 01"						
				if device_state_flag == 1:
						for retry_flush_count in range(25,0,-1):
								#self.es_or_nitrogen_flag = 1
								acquired_actual_command = self.sem.acquire()
								self.ser.flushInput()
								self.ser.flushOutput()					        
								self.ser.write(scommand.encode()) 
								device_status2 = self.ser.readline()
								if acquired_actual_command:
									self.sem.release()									
								device_status2 = device_status2.decode("ISO-8859-1") #ser.readline returns a binary, convert to string
								logging.info (scommand+" device status flag "+device_status2)

								if (device_status2 == "KT+OK\r\n"):
										device_flush_flag = 1
										timeinterval = int(timeinterval)
										time.sleep(timeinterval) 											
										break
								elif (device_status2 == "KT+BUSY\r\n"):
										time.sleep(5)   
								elif (device_status2 == "KT+ERROR\r\n"):
										device_return_value = 0#"Error:" + str(errorcode)
								elif device_status2.startswith("KT+"):	
										device_return_value = device_status2	
										break								
								else:
										comm_error_flag = 1									
										break
										
				if device_flush_flag == 1:
						for retry_count in range(25,0,-1):
								acquired_status_2 = self.sem.acquire()
								self.ser.flushInput()
								self.ser.flushOutput()							
								self.ser.write("KT+EXTSTATUS\r\n".encode()) 
								device_status3 = self.ser.readline()
								if acquired_status_2:
									self.sem.release()									
								device_status3 = device_status3.decode("ISO-8859-1") #ser.readline returns a binary, convert to string
								logging.info (scommand + "2 - EXTSTATUS "+device_status3)
				
								split_device_status1 = device_status1.split("+")
								if (split_device_status1[1][0] == "0"):
									if (split_device_status1[1][1] == "7"):
										device_return_value = "SUCCESS"
										break
									else:
										with open(self.image_path+"pump_servo_constants.json","r+") as e:
											a=json.load(e)	
																	
										S1 = a["Servo1"]["01"]
										S2 = a["Servo1"]["02"]
										S3 = a["Servo1"]["03"]
										S4 = a["Servo1"]["04"]
										S5 = a["Servo1"]["05"]
										S6 = a["Servo1"]["06"]
										S7 = a["Servo1"]["07"]
										S8 = a["Servo1"]["08"]
										S9 = a["Servo1"]["09"]
										S10 = a["Servo1"]["10"]
										S11 = a["Servo1"]["11"]
										S12 = a["Servo1"]["12"]
										S13 = a["Servo1"]["13"]
								
										Servo_All_Constants = S1 + "+" + S2 + "+" + S3 + "+" + S4 + "+" + S5 + "+" + S6 + "+" + S7 + "+" + S8 + "+" + S9 + "+" + S10 + "+" + S11 + "+" + S12 + "+" + S13
								
										DP1 = a["D"]["01"]
										DP2 = a["D"]["02"]
										DP3 = a["D"]["03"]
										DP4 = a["D"]["04"]
										DP5 = a["D"]["05"]
										DP6 = a["D"]["06"]
										DP7 = a["D"]["07"]
										DP8 = a["D"]["08"]
										DP9 = a["D"]["09"]
										DP10 = a["D"]["10"]
										DP11 = a["D"]["11"]
										DP12 = a["D"]["12"]
										DP13 = a["D"]["13"]
										DP14 = a["D"]["14"]
										DP15 = a["D"]["15"]
										DP16 = a["D"]["16"]
										
										D_Pump_Constants = DP1 + "+" + DP2 + "+" + DP3 + "+" + DP4 + "+" + DP5 + "+" + DP6 + "+" + DP7 + "+" + DP8 + "+" + DP9 + "+" + DP10 + "+" + DP11 + "+" + DP12 + "+" + DP13+ "+" + DP14+ "+" + DP15+ "+" + DP16
								
										MP1 = a["M"]["01"]
										MP2 = a["M"]["02"]
										MP3 = a["M"]["03"]
										MP4 = a["M"]["04"]
										MP5 = a["M"]["05"]
										MP6 = a["M"]["06"]
										MP7 = a["M"]["07"]
										MP8 = a["M"]["08"]
										MP9 = a["M"]["09"]
										MP10 = a["M"]["10"]
										MP11 = a["M"]["11"]
										MP12 = a["M"]["12"]
										MP13 = a["M"]["13"]
										MP14 = a["M"]["14"]
										MP15 = a["M"]["15"]
										MP16 = a["M"]["16"]										
								
										ML_Pump_Constants = MP1 + "+" + MP2 + "+" + MP3 + "+" + MP4 + "+" + MP5 + "+" + MP6 + "+" + MP7 + "+" + MP8 + "+" + MP9 + "+" + MP10 + "+" + MP11 + "+" + MP12 + "+" + MP13 + "+" + MP14 + "+" + MP15 + "+" + MP16  
								
										acquired_status_constants2 = self.sem.acquire()
										
										cmd_Servo_All_Constants = "KT+WRITSERVOC:" + Servo_All_Constants + "\r\n"
										self.ser.write(cmd_Servo_All_Constants.encode())
										read_WRITSERVOC = self.ser.readline()
								
										cmd_D_Pump_Constants = "KT+WRITPUMPCD:" + D_Pump_Constants + "\r\n"
										self.ser.write(cmd_D_Pump_Constants.encode())
										read_WRITPUMPCD = self.ser.readline()
								
										cmd_ML_Pump_Constants = "KT+WRITPUMPCM:" + ML_Pump_Constants + "\r\n"
										self.ser.write(cmd_ML_Pump_Constants.encode())
										read_WRITPUMPCM = self.ser.readline()
										
										if acquired_status_constants2:
											self.sem.release()											
								elif (split_device_status1[0] == "1"):
										time.sleep(5)   
								else:
										comm_error_flag = 1
										device_return_value = "Communication Error : 01"						
				if comm_error_flag == 1:
					self.machine_status_label.configure(text = "Error in serial Connection")
			except Exception as e:
				errorstring = "/E-kt_send_ext_command()/"
				logging.warning("%s", errorstring +scommand)
				self.machine_status_label.configure(text = "Error in serial connection")
				device_return_value = "ERROR"
				logging.exception("Exception occurred")				
			finally:
				self.es_or_nitrogen_flag = 0			
				return device_return_value					        
				        
		def kt_sendcommand(self,scommand,timeinterval,errorcode):
			try:				 
				#self.machine_status_label.configure(text = "")   				 			
				device_return_value = 0
				device_state_flag = 0
				device_flush_flag = 0
				retry_status_count = 10
				comm_error_flag = 0
				
				for retry_status_count in range(25,0,-1):
						acquired_status_1 = self.sem.acquire()
						self.ser.flushInput()
						self.ser.flushOutput()
						self.ser.write("KT+STATUS\r\n".encode()) 
						device_status1 = self.ser.readline()
						if acquired_status_1:
							self.sem.release()							
						device_status1 = device_status1.decode("ISO-8859-1") #ser.readline returns a binary, convert to string
						logging.info (scommand + "STATUS"+ device_status1)
						split_device_status1 = device_status1.split("+")
						
						if (split_device_status1[1][0] == "0"):
							if (split_device_status1[1][1] == "7"):
								device_state_flag = 1
								break
							else:
								with open(self.image_path+"pump_servo_constants.json","r+") as e:
									a=json.load(e)	
													    		
								S1 = a["Servo1"]["01"]
								S2 = a["Servo1"]["02"]
								S3 = a["Servo1"]["03"]
								S4 = a["Servo1"]["04"]
								S5 = a["Servo1"]["05"]
								S6 = a["Servo1"]["06"]
								S7 = a["Servo1"]["07"]
								S8 = a["Servo1"]["08"]
								S9 = a["Servo1"]["09"]
								S10 = a["Servo1"]["10"]
								S11 = a["Servo1"]["11"]
								S12 = a["Servo1"]["12"]
								S13 = a["Servo1"]["13"]
								
								Servo_All_Constants = S1 + "+" + S2 + "+" + S3 + "+" + S4 + "+" + S5 + "+" + S6 + "+" + S7 + "+" + S8 + "+" + S9 + "+" + S10 + "+" + S11 + "+" + S12 + "+" + S13
						
								DP1 = a["D"]["01"]
								DP2 = a["D"]["02"]
								DP3 = a["D"]["03"]
								DP4 = a["D"]["04"]
								DP5 = a["D"]["05"]
								DP6 = a["D"]["06"]
								DP7 = a["D"]["07"]
								DP8 = a["D"]["08"]
								DP9 = a["D"]["09"]
								DP10 = a["D"]["10"]
								DP11 = a["D"]["11"]
								DP12 = a["D"]["12"]
								DP13 = a["D"]["13"]
								DP14 = a["D"]["14"]
								DP15 = a["D"]["15"]
								DP16 = a["D"]["16"]
								
						
								D_Pump_Constants = DP1 + "+" + DP2 + "+" + DP3 + "+" + DP4 + "+" + DP5 + "+" + DP6 + "+" + DP7 + "+" + DP8 + "+" + DP9 + "+" + DP10 + "+" + DP11 + "+" + DP12 + "+" + DP13+ "+" + DP14+ "+" + DP15+ "+" + DP16
						
								MP1 = a["M"]["01"]
								MP2 = a["M"]["02"]
								MP3 = a["M"]["03"]
								MP4 = a["M"]["04"]
								MP5 = a["M"]["05"]
								MP6 = a["M"]["06"]
								MP7 = a["M"]["07"]
								MP8 = a["M"]["08"]
								MP9 = a["M"]["09"]
								MP10 = a["M"]["10"]
								MP11 = a["M"]["11"]
								MP12 = a["M"]["12"]
								MP13 = a["M"]["13"]
								MP14 = a["M"]["14"]
								MP15 = a["M"]["15"]
								MP16 = a["M"]["16"]								
						
								ML_Pump_Constants = MP1 + "+" + MP2 + "+" + MP3 + "+" + MP4 + "+" + MP5 + "+" + MP6 + "+" + MP7 + "+" + MP8 + "+" + MP9 + "+" + MP10 + "+" + MP11 + "+" + MP12 + "+" + MP13 + "+" + MP14 + "+" + MP15 + "+" + MP16
								
								acquired_status_constants1 = self.sem.acquire()
								
								cmd_Servo_All_Constants = "KT+WRITSERVOC:" + Servo_All_Constants + "\r\n"
								logging.info ("Servo constants: %s ",cmd_Servo_All_Constants)								
								self.ser.write(cmd_Servo_All_Constants.encode())
								read_WRITSERVOC = self.ser.readline()
								
								logging.info ("device status flag: %s ",read_WRITSERVOC)

								cmd_D_Pump_Constants = "KT+WRITPUMPCD:" + D_Pump_Constants + "\r\n"
								logging.info ("Pump d constants: %s ",cmd_D_Pump_Constants)
								
								self.ser.write(cmd_D_Pump_Constants.encode())
								read_WRITPUMPCD = self.ser.readline()
								logging.info ("device status flag: %s ",read_WRITPUMPCD)
								
								cmd_ML_Pump_Constants = "KT+WRITPUMPCM:" + ML_Pump_Constants + "\r\n"
								logging.info ("Pump ML constants: %s ",cmd_ML_Pump_Constants)
								self.ser.write(cmd_ML_Pump_Constants.encode())
								read_WRITPUMPCM = self.ser.readline()
								logging.info ("device status flag: %s ",read_WRITPUMPCM)
								
								if acquired_status_constants1:
									self.sem.release()													
						elif (split_device_status1[1][0] == "1"):
								time.sleep(5)   
						else:
								comm_error_flag = 1
								errstr = "Communication Error : 01"						

				if device_state_flag == 1:
						for retry_flush_count in range(25,0,-1):
								acquired_actual_command = self.sem.acquire()
								self.ser.flushInput()
								self.ser.flushOutput()					        
								self.ser.write(scommand.encode()) 
								device_status2 = self.ser.readline()
								if acquired_actual_command:
									self.sem.release()									
								device_status2 = device_status2.decode("ISO-8859-1") #ser.readline returns a binary, convert to string
								logging.info (scommand+"device status flag "+device_status2)

								if (device_status2 == "KT+OK\r\n"):
										device_flush_flag = 1
										timeinterval = int(timeinterval)
										time.sleep(timeinterval) 											
										break
								elif (device_status2 == "KT+BUSY\r\n"):
										time.sleep(5)   
								elif (device_status2 == "KT+ERROR\r\n"):
										device_return_value = "Error:" + "10"
								elif device_status2.startswith("KT+"):	
										device_return_value = device_status2	
										break								
								else:
										comm_error_flag = 1
										break
										
				if device_flush_flag == 1:
						for retry_count in range(25,0,-1):
								acquired_status_2 = self.sem.acquire()
								self.ser.flushInput()
								self.ser.flushOutput()							
								self.ser.write("KT+STATUS\r\n".encode()) 
								device_status3 = self.ser.readline()
								if acquired_status_2:
									self.sem.release()									
								device_status3 = device_status3.decode("ISO-8859-1") #ser.readline returns a binary, convert to string
								logging.info (scommand + "2 - STATUS "+device_status3)

								split_device_status1 = device_status1.split("+")
								if (split_device_status1[1][0] == "0"):
									if (split_device_status1[1][1] == "7"):
										device_return_value = "SUCCESS"
										break
									else:
										with open(self.image_path+"pump_servo_constants.json","r+") as e:
											a=json.load(e)	
																	
										S1 = a["Servo1"]["01"]
										S2 = a["Servo1"]["02"]
										S3 = a["Servo1"]["03"]
										S4 = a["Servo1"]["04"]
										S5 = a["Servo1"]["05"]
										S6 = a["Servo1"]["06"]
										S7 = a["Servo1"]["07"]
										S8 = a["Servo1"]["08"]
										S9 = a["Servo1"]["09"]
										S10 = a["Servo1"]["10"]
										S11 = a["Servo1"]["11"]
										S12 = a["Servo1"]["12"]
										S13 = a["Servo1"]["13"]
								
										Servo_All_Constants = S1 + "+" + S2 + "+" + S3 + "+" + S4 + "+" + S5 + "+" + S6 + "+" + S7 + "+" + S8 + "+" + S9 + "+" + S10 + "+" + S11 + "+" + S12 + "+" + S13
								
										DP1 = a["D"]["01"]
										DP2 = a["D"]["02"]
										DP3 = a["D"]["03"]
										DP4 = a["D"]["04"]
										DP5 = a["D"]["05"]
										DP6 = a["D"]["06"]
										DP7 = a["D"]["07"]
										DP8 = a["D"]["08"]
										DP9 = a["D"]["09"]
										DP10 = a["D"]["10"]
										DP11 = a["D"]["11"]
										DP12 = a["D"]["12"]
										DP13 = a["D"]["13"]
										DP14 = a["D"]["14"]
										DP15 = a["D"]["15"]
										DP16 = a["D"]["16"]
								
										D_Pump_Constants = DP1 + "+" + DP2 + "+" + DP3 + "+" + DP4 + "+" + DP5 + "+" + DP6 + "+" + DP7 + "+" + DP8 + "+" + DP9 + "+" + DP10 + "+" + DP11 + "+" + DP12 + "+" + DP13+ "+" + DP14+ "+" + DP15+ "+" + DP16
								
										MP1 = a["M"]["01"]
										MP2 = a["M"]["02"]
										MP3 = a["M"]["03"]
										MP4 = a["M"]["04"]
										MP5 = a["M"]["05"]
										MP6 = a["M"]["06"]
										MP7 = a["M"]["07"]
										MP8 = a["M"]["08"]
										MP9 = a["M"]["09"]
										MP10 = a["M"]["10"]
										MP11 = a["M"]["11"]
										MP12 = a["M"]["12"]
										MP13 = a["M"]["13"]
										MP14 = a["M"]["14"]
										MP15 = a["M"]["15"]
										MP16 = a["M"]["16"]										
								
										ML_Pump_Constants = MP1 + "+" + MP2 + "+" + MP3 + "+" + MP4 + "+" + MP5 + "+" + MP6 + "+" + MP7 + "+" + MP8 + "+" + MP9 + "+" + MP10 + "+" + MP11 + "+" + MP12 + "+" + MP13 + "+" + MP14 + "+" + MP15 + "+" + MP16
										
										acquired_status_constants2 = self.sem.acquire()
										cmd_Servo_All_Constants = "KT+WRITSERVOC:" + Servo_All_Constants + "\r\n"
										self.ser.write(cmd_Servo_All_Constants.encode())
										read_WRITSERVOC = self.ser.readline()

										cmd_D_Pump_Constants = "KT+WRITPUMPCD:" + D_Pump_Constants + "\r\n"
										self.ser.write(cmd_D_Pump_Constants.encode())
										read_WRITPUMPCD = self.ser.readline()
								
										cmd_ML_Pump_Constants = "KT+WRITPUMPCM:" + ML_Pump_Constants + "\r\n"
										self.ser.write(cmd_ML_Pump_Constants.encode())
										read_WRITPUMPCM = self.ser.readline()
																				
										if acquired_status_constants2:
											self.sem.release()										
								elif (split_device_status1[1][0] == "1"):
										time.sleep(5)   
								else:
										comm_error_flag = 1
										device_return_value = "Communication Error : 01"						

				if comm_error_flag == 1:
					self.machine_status_label.configure(text = "Error in serial Connection !!!")

			except Exception as e:
				if self.servicetest_error_indication_flag == 1:
					messagebox.showerror("Serial Error !!!", "Error occured during serial operation. Redirecting to HOME page...")
					self.servicetest_error_indication_flag == 0
					self.front_page()
				errorstring = "/E-kt_send_command()/"
				logging.warning("%s", errorstring +scommand)
				self.machine_status_label.configure(text = "Error in serial connection !!!")
				device_return_value = "ERROR"
				logging.exception("Exception occurred")				
			finally:
				return device_return_value	
				        
		def connect(self, host='http://google.com'):
			try:
				urllib.request.urlopen(host) 
				return True
			except:
				return False

		def internet_connection(self):
			try:						
				while 1:
					if self.check_internet_connection_continuous():
						self.internet_conn_label.configure(text = "Connected to Internet")
					else:
						self.internet_conn_label.configure(text = "")				
					time.sleep(5)
			except:
				errorstring = "/E-internet_connection()/"
				logging.warning("%s", errorstring +scommand)
				logging.exception("Exception occurred")
			finally:
				sys.exit()
		        
		def system_shutdown(self):
			try:		
				MsgBox = messagebox.askquestion ('System Shutdown','Press yes to Shutdown the system / press no to goback',icon = 'warning')
				if MsgBox == 'yes':		
					texttosend = "KT+ABORT\r\n"
					read_shutdown_ret_val = self.kt_sendcommand(texttosend,2,10)			
					os.system("shutdown -h now")
				else:
					pass	
			except Exception as e:
				errorstring = "/E-system_shutdown()/"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass
			
		def system_reboot(self):
			try:		
				MsgBox = messagebox.askquestion ('System Reboot','Press yes to Reboot the system / press no to goback',icon = 'warning')
				if MsgBox == 'yes':	
					texttosend = "KT+ABORT\r\n"
					read_reboot_ret_val = self.kt_sendcommand(texttosend,2,10)			
					os.system("shutdown -r now")
				else:
					pass	
			except Exception as e:
				errorstring = "/E-system_reboot()/"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass					        
			        
		def ss_dispense(self):
			try:
				self.ext_ss_dispense = threading.Timer(0.1, self.button_samplesolution)
				self.ext_ss_dispense.start()	 	
			except Exception as e:
				errorstring = "/E-ss_dispense()/"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass				
				
		def oc_dispense(self):
			try:
				self.ext_oc_dispense = threading.Timer(0.1, self.button_ocsamplesolution)
				self.ext_oc_dispense.start()	 	
			except Exception as e:
				errorstring = "/E-ss_dispense()/"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass
								
		def dw_dispense(self):
			try:
				self.ext_dw_dispense = threading.Timer(0.1, self.button_distilledwater)
				self.ext_dw_dispense.start()		
			except Exception as e:
				errorstring = "/E-dw_dispense()/"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass				
				
		def dw_dispense_ec(self):
			try:
				self.ext_dw_dispense_ec = threading.Timer(0.1, self.button_distilledwater_ec)
				self.ext_dw_dispense_ec.start()					
			except Exception as e:
				errorstring = "/E-dw_dispense_ec()/"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass				
				
		def stop_dispense(self):
			try:
				self.ext_stop_disp_dispense = threading.Timer(0.1, self.external_abort)
				self.ext_stop_disp_dispense.start()	
			except Exception as e:
				errorstring = "/E-stop_dispense()/"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass															
						        		
		def external_abort(self):
			try:
				self.machine_status_label.configure(text = "")
				
				#self.bocsample_solution['state']=DISABLED
				self.bsample_solution['state']=DISABLED 
				self.bdistilled_water['state']=DISABLED
				self.bdistilled_water_ec['state']=DISABLED 
				self.bstop_dispense['state']=ACTIVE	
				texttosend = "KT+EXTABORT\r\n"			
				pss_ret_val = self.kt_send_external_abort_command(texttosend,0,10)			
				#self.es_ph_ec_msg_flag = 0 
				self.es_msg_flag = 1 
				self.ph_msg_flag = 1 
				self.ec_msg_flag = 1 
 	        
				if pss_ret_val == "SUCCESS":
					self.machine_status_label.configure(text = "Dispense: Operation aborted")
				else:
					self.machine_status_label.configure(text = "Dispense: Aborting process failed")

			except Exception as e:
				errorstring = "/E-external_abort()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				#self.bocsample_solution['state']=ACTIVE
				self.bsample_solution['state']=ACTIVE 
				self.bdistilled_water['state']=ACTIVE
				self.bdistilled_water_ec['state']=ACTIVE 
				self.bstop_dispense['state']=DISABLED				
				pass 
				
		def button_ocsamplesolution(self):
			try:
				self.machine_status_label.configure(text = "")
				
				#self.bocsample_solution['state']=DISABLED
				self.bsample_solution['state']=DISABLED 
				self.bdistilled_water['state']=DISABLED 
				self.bdistilled_water_ec['state']=DISABLED
				self.bstop_dispense['state']=ACTIVE
				
				texttosend = "KT+EXTDISPENSEM:13+10\r\n"
				pss_ret_val = self.kt_send_external_command(texttosend,20,10)
				
				texttosend = "KT+EXTDISPENSEM:14+10\r\n"
				pss_ret_val = self.kt_send_external_command(texttosend,20,10)	
					
				if 	self.es_msg_flag == 0:		        	        
					if pss_ret_val == "SUCCESS":
						self.machine_status_label.configure(text = "Organic Carbon Solution Dispense Successful")
					else:
						self.machine_status_label.configure(text = "Failed to Dispense Organic Carbon Solution")
					
			except Exception as e:
				errorstring = "/E-button_sample_solution()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				#self.bocsample_solution['state']=ACTIVE
				self.bsample_solution['state']=ACTIVE 
				self.bdistilled_water['state']=ACTIVE
				self.bdistilled_water_ec['state']=ACTIVE 
				self.bstop_dispense['state']=DISABLED
				pass				
			        						        								        	
		def button_samplesolution(self):
			try:
				self.machine_status_label.configure(text = "")
				texttosend = "KT+EXTDISPENSEM:09+50\r\n"
				#self.bocsample_solution['state']=DISABLED
				self.bsample_solution['state']=DISABLED 
				self.bdistilled_water['state']=DISABLED 
				self.bdistilled_water_ec['state']=DISABLED
				self.bstop_dispense['state']=ACTIVE
				pss_ret_val = self.kt_send_external_command(texttosend,100,10)	
				if 	self.es_msg_flag == 0:		        	        
					if pss_ret_val == "SUCCESS":
						self.machine_status_label.configure(text = "Sample Solution Dispense Successful")
					else:
						self.machine_status_label.configure(text = "Failed to Dispense Sample Solution")
					
			except Exception as e:
				errorstring = "/E-button_sample_solution()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				#self.bocsample_solution['state']=ACTIVE
				self.bsample_solution['state']=ACTIVE 
				self.bdistilled_water['state']=ACTIVE
				self.bdistilled_water_ec['state']=ACTIVE 
				self.bstop_dispense['state']=DISABLED
				pass
			
		def button_distilledwater(self):
			try:
				self.machine_status_label.configure(text = "")
				texttosend = "KT+EXTDISPENSEM:10+75\r\n"
				#self.bocsample_solution['state']=DISABLED
				self.bsample_solution['state']=DISABLED 
				self.bdistilled_water['state']=DISABLED
				self.bdistilled_water_ec['state']=DISABLED 
				self.bstop_dispense['state']=ACTIVE				
				pss_ret_val = self.kt_send_external_command(texttosend,150,10)	
				if 	self.ph_msg_flag == 0:						        	        
					if pss_ret_val == "SUCCESS":
						self.machine_status_label.configure(text = "Distilled water dispense Successful")
					else:
						self.machine_status_label.configure(text = "Failed to Dispense Distilled water")

			except Exception as e:
				errorstring = "/E-button_distilled_water()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				#self.bocsample_solution['state']=ACTIVE
				self.bsample_solution['state']=ACTIVE 
				self.bdistilled_water['state']=ACTIVE
				self.bdistilled_water_ec['state']=ACTIVE
				self.bstop_dispense['state']=DISABLED			
				pass 	
					
		def button_distilledwater_ec(self):
			try:
				self.machine_status_label.configure(text = "")
				texttosend = "KT+EXTDISPENSEM:10+40\r\n"
				#self.bocsample_solution['state']=DISABLED
				self.bsample_solution['state']=DISABLED 
				self.bdistilled_water['state']=DISABLED 
				self.bdistilled_water_ec['state']=DISABLED
				self.bstop_dispense['state']=ACTIVE				
				pss_ret_val = self.kt_send_external_command(texttosend,80,10)	
				if 	self.ec_msg_flag == 0:						        	        
					if pss_ret_val == "SUCCESS":
						self.machine_status_label.configure(text = "Distilled water dispense for EC Successful")
					else:
						self.machine_status_label.configure(text = "Failed to Dispense Distilled water for EC")
			except Exception as e:
				errorstring = "/E-button_distilled_water_ec()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				#self.bocsample_solution['state']=ACTIVE
				self.bsample_solution['state']=ACTIVE 
				self.bdistilled_water['state']=ACTIVE
				self.bdistilled_water_ec['state']=ACTIVE
				self.bstop_dispense['state']=DISABLED			
				pass 					
					
		def calibration_readdy(self):
			try:
				self.machine_status_label.configure(text = "")
				ph_timer = 0
				ec_timer = 0
				n_timer = 0
				p_timer = 0
				k_timer = 0
				
				wash_nitro = 0
				wash_potash = 0
				wash_phos = 0
				wash_boron = 0
				wash_iron = 0				
		
				lst_values = [self.calibration_listboxx.get(idx) for idx in self.calibration_listboxx.curselection()]				
				
				if "pH 4.0" in lst_values:
						timer_value_to_send = 63
				if "pH 7.0" in lst_values:
						timer_value_to_send = 63								
				if "EC" in lst_values:
						timer_value_to_send = 18
				if "Nitrogen" in lst_values:
						timer_value_to_send = 446#422#460
						wash_nitro = 45
						wash_potash = 0
						wash_phos = 0
				if "Potassium" in lst_values:
						timer_value_to_send = 690#669#669
						wash_nitro = 0
						wash_potash = 45
						wash_phos = 0
				if "Phosphorus" in lst_values:
						timer_value_to_send = 388#328#328
						wash_nitro = 0
						wash_potash = 0
						wash_phos = 45
				if "Boron" in lst_values:
						timer_value_to_send = 666#645
						wash_nitro = 0
						wash_potash = 0
						wash_phos = 0
						wash_boron = 45
						wash_iron = 0						
				if "Iron" in lst_values:
						timer_value_to_send = 666#642
						wash_nitro = 0
						wash_potash = 0
						wash_phos = 0
						wash_boron = 0
						wash_iron = 45	
				if "Organic Carbon" in lst_values:
						timer_value_to_send = 71
						wash_nitro = 0
						wash_potash = 0
						wash_phos = 0
						wash_boron = 0
						wash_iron = 45												

				timer_value_to_send = int (timer_value_to_send) 
				timer_value_to_send = timer_value_to_send + wash_nitro + wash_potash + wash_phos + wash_boron + wash_iron
				self.countdown(timer_value_to_send)      
			except Exception as e:
				errorstring = "/E-calibration_ready()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass

		def calibration_samplesolution(self):
			try:	
				self.c1.itemconfigure(self.r,fill="#FFA500")												
				file = pathlib.Path(self.chemical_firmware_version)
				if file.exists ():
					with open(self.chemical_firmware_version) as equation_contents:
						equation_status_data = json.load(equation_contents)
						
					CalibN1 = equation_status_data["CalibN1"]
					CalibN2 = equation_status_data["CalibN2"]
					CalibN3 = equation_status_data["CalibN3"]														
					CalibN4 = equation_status_data["CalibN4"]														
					
					CalibP1 = equation_status_data["CalibP1"]	
					CalibP2 = equation_status_data["CalibP2"]	
						
					CalibK1 = equation_status_data["CalibK1"]		
					CalibK2 = equation_status_data["CalibK2"]		
					CalibK3 = equation_status_data["CalibK3"]	
					
					CalibB1 = equation_status_data["CalibB1"]		
					CalibB2 = equation_status_data["CalibB2"]		
					CalibB3 = equation_status_data["CalibB3"]
					
					CalibI1 = equation_status_data["CalibI1"]		
					CalibI2 = equation_status_data["CalibI2"]		
					CalibI3 = equation_status_data["CalibI3"]						

					CalibOC1 = equation_status_data["CalibOC1"]		
					CalibOC2 = equation_status_data["CalibOC2"]		
					
					WashTestTube_DeviceFlush1 = equation_status_data["WashTestTube-DeviceFlush1"]
					WashTestTube_DeviceFlush2 = equation_status_data["WashTestTube-DeviceFlush2"]
					WashTestTube_DeviceFlush3 = equation_status_data["WashTestTube-DeviceFlush3"]						
				
					WashCuvette_DeviceWash = equation_status_data["WashCuvette-DeviceWash"]											
									
					lst_values = [self.calibration_listboxx.get(idx) for idx in self.calibration_listboxx.curselection()]
				
					constant_values = [self.constants_listboxx.get(idx) for idx in self.constants_listboxx.curselection()]

					self.nnitro = 0
					self.pphosphorus = 0
					self.kpotash = 0
					self.pph = 0
					self.eec = 0
					self.bboron = 0
					self.iiron = 0					
					
					if "pH 4.0" in lst_values:
						self.cal_sublabel.configure(text="pH 4.0")
						texttosend = "KT+STARTPH\r\n"

						self.msg_nitro.acquire()
						self.tablet_dispense = 1						
						self.msg_nitro.release()
						messagebox.showinfo("pH 4.0", "Dip pH probe in 4.0 buffer solution")
						self.msg_nitro.acquire()
						self.tablet_dispense = 0
						self.msg_nitro.release()
													
						startph_ret_val = self.kt_sendcommand(texttosend,60,10)		
						
						if 	startph_ret_val == "SUCCESS":					
							time.sleep(2)
							texttosend = "KT+READPH\r\n"
							readph_ret_val = self.kt_sendcommand(texttosend,5,10)	
							
							split_readph_ret_val = readph_ret_val.split("+")

							with open(self.image_path+"pump_servo_constants.json","r+") as e:
								a=json.load(e)	

							a["PH4"]["PHCONST"] = constant_values[0]		
							a["PH4"]["V"] = split_readph_ret_val[1]
							a["PH4"]["T"] = split_readph_ret_val[2]
					
							ph4temp = float (a["PH4"]["T"])
							ph7temp = float (a["PH7"]["T"])
							ph4const = float ( a["PH4"]["PHCONST"])
							ph7const = float (a["PH7"]["PHCONST"])
							ph4v = float (a["PH4"]["V"])
							ph7v = float (a["PH7"]["V"])
							
							avg_temp = (ph4temp + ph7temp) / 2
							m = (ph4v - ph7v) / (ph7const - ph4const)
							m = m / (avg_temp + 273.15)
							
							m = float("{0:0.6f}".format(m))
							ph7v = float("{0:0.2f}".format(ph7v))
							
							a["CONSTANB"]["B"] = m
							a["CONSTANB"]["A"] = ph7v
					
							obj=a

							with open(self.image_path+"pump_servo_constants.json","w")as e:
								json.dump(obj,e)
						
							messagebox.showinfo("pH 4.0", "pH 4.0 Calibration Successful")

						with open(self.calibration_status_path) as calib_contents:
							reset_all_calib_status_data = json.load(calib_contents)		
							reset_all_calib_status_data["pH4"]= "C"				
						with open(self.calibration_status_path, 'w') as fp:
							json.dump(reset_all_calib_status_data, fp)											
													
					if "pH 7.0" in lst_values:
						self.cal_sublabel.configure(text="pH 7.0")
						texttosend = "KT+STARTPH\r\n"

						self.msg_nitro.acquire()
						self.tablet_dispense = 1						
						self.msg_nitro.release()
						messagebox.showinfo("pH 7.0", "Dip pH probe in 7.0 buffer solution")
						self.msg_nitro.acquire()
						self.tablet_dispense = 0
						self.msg_nitro.release()
													
						startph_ret_val = self.kt_sendcommand(texttosend,60,10)		
						if 	startph_ret_val == "SUCCESS":					
							time.sleep(2)
							
							texttosend = "KT+READPH\r\n"
							readph_ret_val = self.kt_sendcommand(texttosend,5,10)	
							
							split_readph_ret_val = readph_ret_val.split("+")
							with open(self.image_path+"pump_servo_constants.json","r+") as e:
								a=json.load(e)	

							a["PH7"]["PHCONST"] = constant_values[0]		
							a["PH7"]["V"] = split_readph_ret_val[1]
							a["PH7"]["T"] = split_readph_ret_val[2]
					
							ph4temp = float (a["PH4"]["T"])
							ph7temp = float (a["PH7"]["T"])
							ph4const = float ( a["PH4"]["PHCONST"])
							ph7const = float (a["PH7"]["PHCONST"])
							ph4v = float (a["PH4"]["V"])
							ph7v = float (a["PH7"]["V"])
							
							avg_temp = (ph4temp + ph7temp) / 2
							m = (ph4v - ph7v) / (ph7const - ph4const)
							m = m / (avg_temp + 273.15)
							
							m = float("{0:0.6f}".format(m))
							ph7v = float("{0:0.2f}".format(ph7v))
							
							a["CONSTANB"]["B"] = m
							a["CONSTANB"]["A"] = ph7v
					
							obj=a

							with open(self.image_path+"pump_servo_constants.json","w")as e:
								json.dump(obj,e)
							
							messagebox.showinfo("pH 7.0", "pH 7.0 Calibration Successful")							

						with open(self.calibration_status_path) as calib_contents:
								reset_all_calib_status_data = json.load(calib_contents)		
								reset_all_calib_status_data["pH7"]= "C"				
						with open(self.calibration_status_path, 'w') as fp:
							json.dump(reset_all_calib_status_data, fp)															
								
					if "EC" in lst_values:
						self.cal_sublabel.configure(text="EC")
						texttosend = "KT+STARTEC\r\n"
						
						self.msg_nitro.acquire()
						self.tablet_dispense = 1						
						self.msg_nitro.release()
						messagebox.showinfo("EC", "Dip EC probe in 1.5 buffer solution")
						self.msg_nitro.acquire()
						self.tablet_dispense = 0
						self.msg_nitro.release()							
						
						startec_ret_val = self.kt_sendcommand(texttosend,15,10)	
						if 	startec_ret_val == "SUCCESS":					
							time.sleep(2)
							texttosend = "KT+ECCAL:"+constant_values[0]+"\r\n"
							readec_ret_val = self.kt_sendcommand(texttosend,5,10)	

							split_readec_ret_val = readec_ret_val.split(":")
							double_split_readec_ret_val = split_readec_ret_val[1].split("+")
							
							with open(self.image_path+"pump_servo_constants.json","r+") as e:
								a=json.load(e)	

							a["EC"]["K"] = double_split_readec_ret_val[1].rstrip()
							obj=a

							with open(self.image_path+"pump_servo_constants.json","w")as e:
								json.dump(obj,e)
									
							with open(self.calibration_status_path) as calib_contents:
								reset_all_calib_status_data = json.load(calib_contents)		
								reset_all_calib_status_data["EC"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)	
								
							messagebox.showinfo("EC", "EC Calibration Successful")											
								
					if "Nitrogen" in lst_values:
						if "00" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Nitrogen (0)")								
							d1n1_cmd_to_send = "KT+PR:"+CalibN1+"\r\n"
							n1_ret_val = self.kt_sendcommand(d1n1_cmd_to_send,1,10)

							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Nitrogen (0)", "Take 10 ml of Nitrogen (0) solution and put tablet A & B into it. Mix well and pour into test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()									
							
							d1n2_cmd_to_send = "KT+PR:"+CalibN2+"\r\n"
							n2_ret_val = self.kt_sendcommand(d1n2_cmd_to_send,0,10)
							
							d1n3_cmd_to_send = "KT+PR:"+CalibN3+"\r\n"
							n3_ret_val = self.kt_sendcommand(d1n3_cmd_to_send,160,10)		

							d1n4_cmd_to_send = "KT+PR:"+CalibN4+"\r\n"
							n4_ret_val = self.kt_sendcommand(d1n4_cmd_to_send,261,10)										

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,2,10)

							r_nnitro, g_nnitro, b_nnitro = self.n_cal_imagecapture("0")
						
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_nnitro_data = json.load(json_file)
							calib_rgb_nnitro_data["calibration"]["N"]["0"]["r"] = r_nnitro	
							calib_rgb_nnitro_data["calibration"]["N"]["0"]["g"] = g_nnitro
							calib_rgb_nnitro_data["calibration"]["N"]["0"]["b"] = b_nnitro	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_nnitro_data, fp)													
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,2,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)   
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["N0"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Nitrogen", "Nitrogen (0) Calibration Successful")
							
							
						if "05" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Nitrogen (05)")														
							
							d1n1_cmd_to_send = "KT+PR:"+CalibN1+"\r\n"
							n1_ret_val = self.kt_sendcommand(d1n1_cmd_to_send,1,10)

							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Nitrogen (05)", "Take 10 ml of Nitrogen (05) solution and put tablet A & B into it. Mix well and pour into test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()									
							
							d1n2_cmd_to_send = "KT+PR:"+CalibN2+"\r\n"
							n2_ret_val = self.kt_sendcommand(d1n2_cmd_to_send,0,10)

							d1n3_cmd_to_send = "KT+PR:"+CalibN3+"\r\n"
							n3_ret_val = self.kt_sendcommand(d1n3_cmd_to_send,160,10)		

							d1n4_cmd_to_send = "KT+PR:"+CalibN4+"\r\n"
							n4_ret_val = self.kt_sendcommand(d1n4_cmd_to_send,261,10)										
							
							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,2,10)     
					
							r_nnitro, g_nnitro, b_nnitro = self.n_cal_imagecapture("5")
						
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_nnitro_data = json.load(json_file)
							calib_rgb_nnitro_data["calibration"]["N"]["5"]["r"] = r_nnitro	
							calib_rgb_nnitro_data["calibration"]["N"]["5"]["g"] = g_nnitro
							calib_rgb_nnitro_data["calibration"]["N"]["5"]["b"] = b_nnitro	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_nnitro_data, fp)					
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,2,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)  
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["N5"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Nitrogen", "Nitrogen (5) Calibration Successful")		

						if "10" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Nitrogen (10)")								
							
							d1n1_cmd_to_send = "KT+PR:"+CalibN1+"\r\n"
							n1_ret_val = self.kt_sendcommand(d1n1_cmd_to_send,1,10)

							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Nitrogen (10)", "Take 10 ml of Nitrogen (10) solution and put tablet A & B into it. Mix well and pour into test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()									
							
							d1n2_cmd_to_send = "KT+PR:"+CalibN2+"\r\n"
							n2_ret_val = self.kt_sendcommand(d1n2_cmd_to_send,0,10)
							
							d1n3_cmd_to_send = "KT+PR:"+CalibN3+"\r\n"
							n3_ret_val = self.kt_sendcommand(d1n3_cmd_to_send,160,10)		

							d1n4_cmd_to_send = "KT+PR:"+CalibN4+"\r\n"
							n4_ret_val = self.kt_sendcommand(d1n4_cmd_to_send,261,10)									
							
							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,2,10)       
					
							r_nnitro, g_nnitro, b_nnitro = self.n_cal_imagecapture("10")
						
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_nnitro_data = json.load(json_file)
							calib_rgb_nnitro_data["calibration"]["N"]["10"]["r"] = r_nnitro	
							calib_rgb_nnitro_data["calibration"]["N"]["10"]["g"] = g_nnitro
							calib_rgb_nnitro_data["calibration"]["N"]["10"]["b"] = b_nnitro	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_nnitro_data, fp)													
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,2,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10) 
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["N10"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Nitrogen", "Nitrogen (10) Calibration Successful")
							
						if "20" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Nitrogen (20)")								
							
							d1n1_cmd_to_send = "KT+PR:"+CalibN1+"\r\n"
							n1_ret_val = self.kt_sendcommand(d1n1_cmd_to_send,1,10)

							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Nitrogen (20)", "Take 10 ml of Nitrogen (20) solution and put tablet A & B into it. Mix well and pour into test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()									
							
							d1n2_cmd_to_send = "KT+PR:"+CalibN2+"\r\n"
							n2_ret_val = self.kt_sendcommand(d1n2_cmd_to_send,0,10)
							
							d1n3_cmd_to_send = "KT+PR:"+CalibN3+"\r\n"
							n3_ret_val = self.kt_sendcommand(d1n3_cmd_to_send,160,10)		

							d1n4_cmd_to_send = "KT+PR:"+CalibN4+"\r\n"
							n4_ret_val = self.kt_sendcommand(d1n4_cmd_to_send,261,10)
															
							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,2,10)       
					
							r_nnitro, g_nnitro, b_nnitro = self.n_cal_imagecapture("20")
						
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_nnitro_data = json.load(json_file)
							calib_rgb_nnitro_data["calibration"]["N"]["20"]["r"] = r_nnitro	
							calib_rgb_nnitro_data["calibration"]["N"]["20"]["g"] = g_nnitro
							calib_rgb_nnitro_data["calibration"]["N"]["20"]["b"] = b_nnitro	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_nnitro_data, fp)													
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,2,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10) 
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["N20"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Nitrogen", "Nitrogen (20) Calibration Successful")	
							
						if "30" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Nitrogen (30)")								
							
							d1n1_cmd_to_send = "KT+PR:"+CalibN1+"\r\n"
							n1_ret_val = self.kt_sendcommand(d1n1_cmd_to_send,1,10)

							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Nitrogen (30)", "Take 10 ml of Nitrogen (30) solution and put tablet A & B into it. Mix well and pour into test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								
							
							d1n2_cmd_to_send = "KT+PR:"+CalibN2+"\r\n"
							n2_ret_val = self.kt_sendcommand(d1n2_cmd_to_send,0,10)
							
							d1n3_cmd_to_send = "KT+PR:"+CalibN3+"\r\n"
							n3_ret_val = self.kt_sendcommand(d1n3_cmd_to_send,160,10)		

							d1n4_cmd_to_send = "KT+PR:"+CalibN4+"\r\n"
							n4_ret_val = self.kt_sendcommand(d1n4_cmd_to_send,261,10)
															
							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,2,10)        
					
							r_nnitro, g_nnitro, b_nnitro = self.n_cal_imagecapture("30")
						
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_nnitro_data = json.load(json_file)
							calib_rgb_nnitro_data["calibration"]["N"]["30"]["r"] = r_nnitro	
							calib_rgb_nnitro_data["calibration"]["N"]["30"]["g"] = g_nnitro
							calib_rgb_nnitro_data["calibration"]["N"]["30"]["b"] = b_nnitro	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_nnitro_data, fp)													
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,2,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10) 
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["N30"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)										
					
							messagebox.showinfo("Nitrogen", "Nitrogen (30) Calibration Successful")	
							
						if "40" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Nitrogen (40)")
							
							d1n1_cmd_to_send = "KT+PR:"+CalibN1+"\r\n"
							n1_ret_val = self.kt_sendcommand(d1n1_cmd_to_send,1,10)

							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Nitrogen (40)", "Take 10 ml of Nitrogen (40) solution and put tablet A & B into it. Mix well and pour into test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								
							
							d1n2_cmd_to_send = "KT+PR:"+CalibN2+"\r\n"
							n2_ret_val = self.kt_sendcommand(d1n2_cmd_to_send,0,10)
							
							d1n3_cmd_to_send = "KT+PR:"+CalibN3+"\r\n"
							n3_ret_val = self.kt_sendcommand(d1n3_cmd_to_send,160,10)		

							d1n4_cmd_to_send = "KT+PR:"+CalibN4+"\r\n"
							n4_ret_val = self.kt_sendcommand(d1n4_cmd_to_send,261,10)									

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,2,10)       
					
							r_nnitro, g_nnitro, b_nnitro = self.n_cal_imagecapture("40")
						
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_nnitro_data = json.load(json_file)
							calib_rgb_nnitro_data["calibration"]["N"]["40"]["r"] = r_nnitro	
							calib_rgb_nnitro_data["calibration"]["N"]["40"]["g"] = g_nnitro
							calib_rgb_nnitro_data["calibration"]["N"]["40"]["b"] = b_nnitro	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_nnitro_data, fp)													
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,2,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10) 
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["N40"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Nitrogen", "Nitrogen (40) Calibration Successful")				
													                    
					if "Phosphorus" in lst_values:					
						if "00" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Phosphorus (0)")
							
							d1p1_cmd_to_send = "KT+PR:"+CalibP1+"\r\n"
							p1_ret_val = self.kt_sendcommand(d1p1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Phosphorus (0)", "Pour the Phosphorus solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1p2_cmd_to_send = "KT+PR:"+CalibP2+"\r\n"
							p2_ret_val = self.kt_sendcommand(d1p2_cmd_to_send,327,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_pphosphorus, g_pphosphorus, b_pphosphorus = self.p_cal_imagecapture("0")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_pphosphorus_data = json.load(json_file)
							calib_rgb_pphosphorus_data["calibration"]["P"]["0"]["r"] = r_pphosphorus	
							calib_rgb_pphosphorus_data["calibration"]["P"]["0"]["g"] = g_pphosphorus
							calib_rgb_pphosphorus_data["calibration"]["P"]["0"]["b"] = b_pphosphorus	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_pphosphorus_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["P0"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Phosphorus", "Phosphorus (0) Calibration Successful")		
							
						if "05" in constant_values:
							self.machine_status_label.configure(text = "")

							self.cal_sublabel.configure(text="Phosphorus (05)")
							
							d1p1_cmd_to_send = "KT+PR:"+CalibP1+"\r\n"
							p1_ret_val = self.kt_sendcommand(d1p1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Phosphorus (5)", "Pour the Phosphorus solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1p2_cmd_to_send = "KT+PR:"+CalibP2+"\r\n"
							p2_ret_val = self.kt_sendcommand(d1p2_cmd_to_send,327,10)					

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)             
					
							r_pphosphorus, g_pphosphorus, b_pphosphorus = self.p_cal_imagecapture("5")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_pphosphorus_data = json.load(json_file)
							calib_rgb_pphosphorus_data["calibration"]["P"]["5"]["r"] = r_pphosphorus	
							calib_rgb_pphosphorus_data["calibration"]["P"]["5"]["g"] = g_pphosphorus
							calib_rgb_pphosphorus_data["calibration"]["P"]["5"]["b"] = b_pphosphorus	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_pphosphorus_data, fp)							
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["P5"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)								
					
							messagebox.showinfo("Phosphorus", "Phosphorus (5) Calibration Successful")	

						if "10" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Phosphorus (10)")
							
							d1p1_cmd_to_send = "KT+PR:"+CalibP1+"\r\n"
							p1_ret_val = self.kt_sendcommand(d1p1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Phosphorus (10)", "Pour the Phosphorus solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1p2_cmd_to_send = "KT+PR:"+CalibP2+"\r\n"
							p2_ret_val = self.kt_sendcommand(d1p2_cmd_to_send,327,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)          
					
							r_pphosphorus, g_pphosphorus, b_pphosphorus = self.p_cal_imagecapture("10")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_pphosphorus_data = json.load(json_file)
							calib_rgb_pphosphorus_data["calibration"]["P"]["10"]["r"] = r_pphosphorus	
							calib_rgb_pphosphorus_data["calibration"]["P"]["10"]["g"] = g_pphosphorus
							calib_rgb_pphosphorus_data["calibration"]["P"]["10"]["b"] = b_pphosphorus	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_pphosphorus_data, fp)							
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)

							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["P10"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)
					
							messagebox.showinfo("Phosphorus", "Phosphorus (10) Calibration Successful")		
							
						if "15" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Phosphorus (15)")
							
							d1p1_cmd_to_send = "KT+PR:"+CalibP1+"\r\n"
							p1_ret_val = self.kt_sendcommand(d1p1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Phosphorus (15)", "Pour the Phosphorus solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1p2_cmd_to_send = "KT+PR:"+CalibP2+"\r\n"
							p2_ret_val = self.kt_sendcommand(d1p2_cmd_to_send,327,10)							

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)            
					
							r_pphosphorus, g_pphosphorus, b_pphosphorus = self.p_cal_imagecapture("15")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_pphosphorus_data = json.load(json_file)
							calib_rgb_pphosphorus_data["calibration"]["P"]["15"]["r"] = r_pphosphorus	
							calib_rgb_pphosphorus_data["calibration"]["P"]["15"]["g"] = g_pphosphorus
							calib_rgb_pphosphorus_data["calibration"]["P"]["15"]["b"] = b_pphosphorus	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_pphosphorus_data, fp)							
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)

							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["P15"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)
					
							messagebox.showinfo("Phosphorus", "Phosphorus (15) Calibration Successful")	
							
						if "20" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Phosphorus (20)")
							
							d1p1_cmd_to_send = "KT+PR:"+CalibP1+"\r\n"
							p1_ret_val = self.kt_sendcommand(d1p1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Phosphorus (20)", "Pour the Phosphorus solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1p2_cmd_to_send = "KT+PR:"+CalibP2+"\r\n"
							p2_ret_val = self.kt_sendcommand(d1p2_cmd_to_send,327,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)            
					
							r_pphosphorus, g_pphosphorus, b_pphosphorus = self.p_cal_imagecapture("20")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_pphosphorus_data = json.load(json_file)
							calib_rgb_pphosphorus_data["calibration"]["P"]["20"]["r"] = r_pphosphorus	
							calib_rgb_pphosphorus_data["calibration"]["P"]["20"]["g"] = g_pphosphorus
							calib_rgb_pphosphorus_data["calibration"]["P"]["20"]["b"] = b_pphosphorus	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_pphosphorus_data, fp)							
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["P20"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)
					
							messagebox.showinfo("Phosphorus", "Phosphorus (20) Calibration Successful")		
							
						if "25" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Phosphorus (25)")
							
							d1p1_cmd_to_send = "KT+PR:"+CalibP1+"\r\n"
							p1_ret_val = self.kt_sendcommand(d1p1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Phosphorus (25)", "Pour the Phosphorus solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1p2_cmd_to_send = "KT+PR:"+CalibP2+"\r\n"
							p2_ret_val = self.kt_sendcommand(d1p2_cmd_to_send,327,10)					

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)            
					
							r_pphosphorus, g_pphosphorus, b_pphosphorus = self.p_cal_imagecapture("25")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_pphosphorus_data = json.load(json_file)
							calib_rgb_pphosphorus_data["calibration"]["P"]["25"]["r"] = r_pphosphorus	
							calib_rgb_pphosphorus_data["calibration"]["P"]["25"]["g"] = g_pphosphorus
							calib_rgb_pphosphorus_data["calibration"]["P"]["25"]["b"] = b_pphosphorus	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_pphosphorus_data, fp)							
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)

							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["P25"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)						
					
							messagebox.showinfo("Phosphorus", "Phosphorus (25) Calibration Successful")					
													                
					if "Potassium" in lst_values:
						if "00" in constant_values:
							self.machine_status_label.configure(text = "")

							self.cal_sublabel.configure(text="Potassium (0)")
							
							d1k1_cmd_to_send = "KT+PR:"+CalibK1+"\r\n"
							k1_ret_val = self.kt_sendcommand(d1k1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Potassium (0)", "Pour the Potassium solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()									

							d1k2_cmd_to_send = "KT+PR:"+CalibK2+"\r\n"
							k2_ret_val = self.kt_sendcommand(d1k2_cmd_to_send,457,10)
							
							d1k3_cmd_to_send = "KT+PR:"+CalibK3+"\r\n"
							k3_ret_val = self.kt_sendcommand(d1k3_cmd_to_send,211,10)

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)       
					
							r_kpotash, g_kpotash, b_kpotash = self.k_cal_imagecapture("0")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_pphosphorus_data = json.load(json_file)
							calib_rgb_pphosphorus_data["calibration"]["K"]["0"]["r"] = r_kpotash	
							calib_rgb_pphosphorus_data["calibration"]["K"]["0"]["g"] = g_kpotash
							calib_rgb_pphosphorus_data["calibration"]["K"]["0"]["b"] = b_kpotash	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_pphosphorus_data, fp)								
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["K0"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)								
					
							messagebox.showinfo("Potassium", "Potassium (0) Calibration Successful")	
							
						if "10" in constant_values:
							self.machine_status_label.configure(text = "")

							self.cal_sublabel.configure(text="Potassium (10)")
							
							d1k1_cmd_to_send = "KT+PR:"+CalibK1+"\r\n"
							k1_ret_val = self.kt_sendcommand(d1k1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Potassium (10)", "Pour the Potassium solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()									

							d1k2_cmd_to_send = "KT+PR:"+CalibK2+"\r\n"
							k2_ret_val = self.kt_sendcommand(d1k2_cmd_to_send,457,10)
							
							d1k3_cmd_to_send = "KT+PR:"+CalibK3+"\r\n"
							k3_ret_val = self.kt_sendcommand(d1k3_cmd_to_send,211,10)					

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)          
					
							r_kpotash, g_kpotash, b_kpotash = self.k_cal_imagecapture("10")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_pphosphorus_data = json.load(json_file)
							calib_rgb_pphosphorus_data["calibration"]["K"]["10"]["r"] = r_kpotash	
							calib_rgb_pphosphorus_data["calibration"]["K"]["10"]["g"] = g_kpotash
							calib_rgb_pphosphorus_data["calibration"]["K"]["10"]["b"] = b_kpotash	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_pphosphorus_data, fp)								
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["K10"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)								
					
							messagebox.showinfo("Potassium", "Potassium (10) Calibration Successful")	
							
						if "20" in constant_values:
							self.machine_status_label.configure(text = "")

							self.cal_sublabel.configure(text="Potassium (20)")
							
							d1k1_cmd_to_send = "KT+PR:"+CalibK1+"\r\n"
							k1_ret_val = self.kt_sendcommand(d1k1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Potassium (20)", "Pour the Potassium solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()									

							d1k2_cmd_to_send = "KT+PR:"+CalibK2+"\r\n"
							k2_ret_val = self.kt_sendcommand(d1k2_cmd_to_send,457,10)
							
							d1k3_cmd_to_send = "KT+PR:"+CalibK3+"\r\n"
							k3_ret_val = self.kt_sendcommand(d1k3_cmd_to_send,211,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)          
					
							r_kpotash, g_kpotash, b_kpotash = self.k_cal_imagecapture("20")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_pphosphorus_data = json.load(json_file)
							calib_rgb_pphosphorus_data["calibration"]["K"]["20"]["r"] = r_kpotash	
							calib_rgb_pphosphorus_data["calibration"]["K"]["20"]["g"] = g_kpotash
							calib_rgb_pphosphorus_data["calibration"]["K"]["20"]["b"] = b_kpotash	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_pphosphorus_data, fp)								
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["K20"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)								
					
							messagebox.showinfo("Potassium", "Potassium (20) Calibration Successful")	
							
						if "40" in constant_values:
							self.machine_status_label.configure(text = "")

							self.cal_sublabel.configure(text="Potassium (40)")
							
							d1k1_cmd_to_send = "KT+PR:"+CalibK1+"\r\n"
							k1_ret_val = self.kt_sendcommand(d1k1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Potassium (40)", "Pour the Potassium solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()									

							d1k2_cmd_to_send = "KT+PR:"+CalibK2+"\r\n"
							k2_ret_val = self.kt_sendcommand(d1k2_cmd_to_send,457,10)
							
							d1k3_cmd_to_send = "KT+PR:"+CalibK3+"\r\n"
							k3_ret_val = self.kt_sendcommand(d1k3_cmd_to_send,211,10)					

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)          
					
							r_kpotash, g_kpotash, b_kpotash = self.k_cal_imagecapture("40")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_pphosphorus_data = json.load(json_file)
							calib_rgb_pphosphorus_data["calibration"]["K"]["40"]["r"] = r_kpotash	
							calib_rgb_pphosphorus_data["calibration"]["K"]["40"]["g"] = g_kpotash
							calib_rgb_pphosphorus_data["calibration"]["K"]["40"]["b"] = b_kpotash	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_pphosphorus_data, fp)								
					
							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["K40"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:					
									json.dump(reset_all_calib_status_data, fp)		

							messagebox.showinfo("Potassium", "Potassium (40) Calibration Successful")	
							
					if "Boron" in lst_values:					
						if "0.0" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Boron (0)")
							
							d1b1_cmd_to_send = "KT+PR:"+CalibB1+"\r\n"
							b1_ret_val = self.kt_sendcommand(d1b1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Boron (0.0)", "Pour the Boron solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1b2_cmd_to_send = "KT+PR:"+CalibB2+"\r\n"
							b2_ret_val = self.kt_sendcommand(d1b2_cmd_to_send,644,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_bboron, g_bboron, b_bboron = self.b_cal_imagecapture("00")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_bboron_data = json.load(json_file)
							print (calib_rgb_bboron_data["calibration"]["B"]["0.0"]["r"])
							print (calib_rgb_bboron_data["calibration"]["B"]["0.0"]["g"])
							print (calib_rgb_bboron_data["calibration"]["B"]["0.0"]["b"])									
							calib_rgb_bboron_data["calibration"]["B"]["0.0"]["r"] = r_bboron	
							calib_rgb_bboron_data["calibration"]["B"]["0.0"]["g"] = g_bboron
							calib_rgb_bboron_data["calibration"]["B"]["0.0"]["b"] = b_bboron	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_bboron_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["B0.0"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Boron", "Boron (0.0) Calibration Successful")		
							
						if "0.25" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Boron (0.25)")
							
							d1b1_cmd_to_send = "KT+PR:"+CalibB1+"\r\n"
							b1_ret_val = self.kt_sendcommand(d1b1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Boron (0.25)", "Pour the Boron solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1b2_cmd_to_send = "KT+PR:"+CalibB2+"\r\n"
							b2_ret_val = self.kt_sendcommand(d1b2_cmd_to_send,644,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_bboron, g_bboron, b_bboron = self.b_cal_imagecapture("025")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_bboron_data = json.load(json_file)
							print (calib_rgb_bboron_data["calibration"]["B"]["0.25"]["r"])
							print (calib_rgb_bboron_data["calibration"]["B"]["0.25"]["g"])
							print (calib_rgb_bboron_data["calibration"]["B"]["0.25"]["b"])									
							calib_rgb_bboron_data["calibration"]["B"]["0.25"]["r"] = r_bboron	
							calib_rgb_bboron_data["calibration"]["B"]["0.25"]["g"] = g_bboron
							calib_rgb_bboron_data["calibration"]["B"]["0.25"]["b"] = b_bboron	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_bboron_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["B0.25"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Boron", "Boron (0.25) Calibration Successful")		

						if "0.5" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Boron (0.5)")
							
							d1b1_cmd_to_send = "KT+PR:"+CalibB1+"\r\n"
							b1_ret_val = self.kt_sendcommand(d1b1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Boron (0.5)", "Pour the Boron solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1b2_cmd_to_send = "KT+PR:"+CalibB2+"\r\n"
							b2_ret_val = self.kt_sendcommand(d1b2_cmd_to_send,644,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_bboron, g_bboron, b_bboron = self.b_cal_imagecapture("05")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_bboron_data = json.load(json_file)
							print (calib_rgb_bboron_data["calibration"]["B"]["0.5"]["r"])
							print (calib_rgb_bboron_data["calibration"]["B"]["0.5"]["g"])
							print (calib_rgb_bboron_data["calibration"]["B"]["0.5"]["b"])									
							calib_rgb_bboron_data["calibration"]["B"]["0.5"]["r"] = r_bboron	
							calib_rgb_bboron_data["calibration"]["B"]["0.5"]["g"] = g_bboron
							calib_rgb_bboron_data["calibration"]["B"]["0.5"]["b"] = b_bboron	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_bboron_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["B0.5"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Boron", "Boron (0.5) Calibration Successful")		
							
						if "1.0" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Boron (1.0)")
							
							d1b1_cmd_to_send = "KT+PR:"+CalibB1+"\r\n"
							b1_ret_val = self.kt_sendcommand(d1b1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Boron (1.0)", "Pour the Boron solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1b2_cmd_to_send = "KT+PR:"+CalibB2+"\r\n"
							b2_ret_val = self.kt_sendcommand(d1b2_cmd_to_send,644,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_bboron, g_bboron, b_bboron = self.b_cal_imagecapture("10")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_bboron_data = json.load(json_file)
							print (calib_rgb_bboron_data["calibration"]["B"]["1.0"]["r"])
							print (calib_rgb_bboron_data["calibration"]["B"]["1.0"]["g"])
							print (calib_rgb_bboron_data["calibration"]["B"]["1.0"]["b"])									
							calib_rgb_bboron_data["calibration"]["B"]["1.0"]["r"] = r_bboron	
							calib_rgb_bboron_data["calibration"]["B"]["1.0"]["g"] = g_bboron
							calib_rgb_bboron_data["calibration"]["B"]["1.0"]["b"] = b_bboron	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_bboron_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["B1.0"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Boron", "Boron (1.0) Calibration Successful")		
							
						if "1.5" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Boron (1.5)")
							
							d1b1_cmd_to_send = "KT+PR:"+CalibB1+"\r\n"
							b1_ret_val = self.kt_sendcommand(d1b1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Boron (1.5)", "Pour the Boron solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1b2_cmd_to_send = "KT+PR:"+CalibB2+"\r\n"
							b2_ret_val = self.kt_sendcommand(d1b2_cmd_to_send,644,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_bboron, g_bboron, b_bboron = self.b_cal_imagecapture("15")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_bboron_data = json.load(json_file)
							print (calib_rgb_bboron_data["calibration"]["B"]["1.5"]["r"])
							print (calib_rgb_bboron_data["calibration"]["B"]["1.5"]["g"])
							print (calib_rgb_bboron_data["calibration"]["B"]["1.5"]["b"])									
							calib_rgb_bboron_data["calibration"]["B"]["1.5"]["r"] = r_bboron	
							calib_rgb_bboron_data["calibration"]["B"]["1.5"]["g"] = g_bboron
							calib_rgb_bboron_data["calibration"]["B"]["1.5"]["b"] = b_bboron	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_bboron_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["B1.5"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Boron", "Boron (1.5) Calibration Successful")		
							
						if "2.0" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Boron (2.0)")
							
							d1b1_cmd_to_send = "KT+PR:"+CalibB1+"\r\n"
							b1_ret_val = self.kt_sendcommand(d1b1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Boron (2.0)", "Pour the Boron solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1b2_cmd_to_send = "KT+PR:"+CalibB2+"\r\n"
							b2_ret_val = self.kt_sendcommand(d1b2_cmd_to_send,644,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_bboron, g_bboron, b_bboron = self.b_cal_imagecapture("20")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_bboron_data = json.load(json_file)
							print (calib_rgb_bboron_data["calibration"]["B"]["2.0"]["r"])
							print (calib_rgb_bboron_data["calibration"]["B"]["2.0"]["g"])
							print (calib_rgb_bboron_data["calibration"]["B"]["2.0"]["b"])									
							calib_rgb_bboron_data["calibration"]["B"]["2.0"]["r"] = r_bboron	
							calib_rgb_bboron_data["calibration"]["B"]["2.0"]["g"] = g_bboron
							calib_rgb_bboron_data["calibration"]["B"]["2.0"]["b"] = b_bboron	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_bboron_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["B2.0"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Boron", "Boron (2.0) Calibration Successful")		
							
					if "Iron" in lst_values:					
						if "0.0" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Iron (0)")
							
							d1i1_cmd_to_send = "KT+PR:"+CalibI1+"\r\n"
							i1_ret_val = self.kt_sendcommand(d1i1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Iron (0.0)", "Pour the Iron solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1i2_cmd_to_send = "KT+PR:"+CalibI2+"\r\n"
							i2_ret_val = self.kt_sendcommand(d1i2_cmd_to_send,641,10)						

							d1i3_cmd_to_send = "KT+PR:"+CalibI3+"\r\n"
							i3_ret_val = self.kt_sendcommand(d1i3_cmd_to_send,0,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_iiron, g_iiron, b_iiron = self.i_cal_imagecapture("00")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_iiron_data = json.load(json_file)
							print (calib_rgb_iiron_data["calibration"]["I"]["0.0"]["r"])
							print (calib_rgb_iiron_data["calibration"]["I"]["0.0"]["g"])
							print (calib_rgb_iiron_data["calibration"]["I"]["0.0"]["b"])									
							calib_rgb_iiron_data["calibration"]["I"]["0.0"]["r"] = r_iiron	
							calib_rgb_iiron_data["calibration"]["I"]["0.0"]["g"] = g_iiron
							calib_rgb_iiron_data["calibration"]["I"]["0.0"]["b"] = b_iiron
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_iiron_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["I0.0"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Iron", "Iron (0.0) Calibration Successful")		
							
						if "0.5" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Iron (0.5)")
							
							d1i1_cmd_to_send = "KT+PR:"+CalibI1+"\r\n"
							i1_ret_val = self.kt_sendcommand(d1i1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Iron (0.5)", "Pour the Iron solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1i2_cmd_to_send = "KT+PR:"+CalibI2+"\r\n"
							i2_ret_val = self.kt_sendcommand(d1i2_cmd_to_send,641,10)						

							d1i3_cmd_to_send = "KT+PR:"+CalibI3+"\r\n"
							i3_ret_val = self.kt_sendcommand(d1i3_cmd_to_send,0,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_iiron, g_iiron, b_iiron = self.i_cal_imagecapture("05")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_iiron_data = json.load(json_file)
							print (calib_rgb_iiron_data["calibration"]["I"]["0.5"]["r"])
							print (calib_rgb_iiron_data["calibration"]["I"]["0.5"]["g"])
							print (calib_rgb_iiron_data["calibration"]["I"]["0.5"]["b"])									
							calib_rgb_iiron_data["calibration"]["I"]["0.5"]["r"] = r_iiron	
							calib_rgb_iiron_data["calibration"]["I"]["0.5"]["g"] = g_iiron
							calib_rgb_iiron_data["calibration"]["I"]["0.5"]["b"] = b_iiron
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_iiron_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["I0.5"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Iron", "Iron (0.5) Calibration Successful")		

						if "1.0" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Iron (1.0)")
							
							d1i1_cmd_to_send = "KT+PR:"+CalibI1+"\r\n"
							i1_ret_val = self.kt_sendcommand(d1i1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Iron (1.0)", "Pour the Iron solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1i2_cmd_to_send = "KT+PR:"+CalibI2+"\r\n"
							i2_ret_val = self.kt_sendcommand(d1i2_cmd_to_send,641,10)						

							d1i3_cmd_to_send = "KT+PR:"+CalibI3+"\r\n"
							i3_ret_val = self.kt_sendcommand(d1i3_cmd_to_send,0,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_iiron, g_iiron, b_iiron = self.i_cal_imagecapture("10")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_iiron_data = json.load(json_file)
							print (calib_rgb_iiron_data["calibration"]["I"]["1.0"]["r"])
							print (calib_rgb_iiron_data["calibration"]["I"]["1.0"]["g"])
							print (calib_rgb_iiron_data["calibration"]["I"]["1.0"]["b"])									
							calib_rgb_iiron_data["calibration"]["I"]["1.0"]["r"] = r_iiron	
							calib_rgb_iiron_data["calibration"]["I"]["1.0"]["g"] = g_iiron
							calib_rgb_iiron_data["calibration"]["I"]["1.0"]["b"] = b_iiron
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_iiron_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["I1.0"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Iron", "Iron (1.0) Calibration Successful")		
							
						if "1.5" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Iron (1.5)")
							
							d1i1_cmd_to_send = "KT+PR:"+CalibI1+"\r\n"
							i1_ret_val = self.kt_sendcommand(d1i1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Iron (1.5)", "Pour the Iron solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1i2_cmd_to_send = "KT+PR:"+CalibI2+"\r\n"
							i2_ret_val = self.kt_sendcommand(d1i2_cmd_to_send,641,10)						

							d1i3_cmd_to_send = "KT+PR:"+CalibI3+"\r\n"
							i3_ret_val = self.kt_sendcommand(d1i3_cmd_to_send,0,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_iiron, g_iiron, b_iiron = self.i_cal_imagecapture("15")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_iiron_data = json.load(json_file)
							print (calib_rgb_iiron_data["calibration"]["I"]["1.5"]["r"])
							print (calib_rgb_iiron_data["calibration"]["I"]["1.5"]["g"])
							print (calib_rgb_iiron_data["calibration"]["I"]["1.5"]["b"])									
							calib_rgb_iiron_data["calibration"]["I"]["1.5"]["r"] = r_iiron	
							calib_rgb_iiron_data["calibration"]["I"]["1.5"]["g"] = g_iiron
							calib_rgb_iiron_data["calibration"]["I"]["1.5"]["b"] = b_iiron
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_iiron_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["I1.5"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Iron", "Iron (1.5) Calibration Successful")		
							
						if "2.0" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Iron (2.0)")
							
							d1i1_cmd_to_send = "KT+PR:"+CalibI1+"\r\n"
							i1_ret_val = self.kt_sendcommand(d1i1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							messagebox.showinfo("Iron (2.0)", "Pour the Iron solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1i2_cmd_to_send = "KT+PR:"+CalibI2+"\r\n"
							i2_ret_val = self.kt_sendcommand(d1i2_cmd_to_send,641,10)						

							d1i3_cmd_to_send = "KT+PR:"+CalibI3+"\r\n"
							i3_ret_val = self.kt_sendcommand(d1i3_cmd_to_send,0,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_iiron, g_iiron, b_iiron = self.i_cal_imagecapture("20")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_iiron_data = json.load(json_file)
							print (calib_rgb_iiron_data["calibration"]["I"]["2.0"]["r"])
							print (calib_rgb_iiron_data["calibration"]["I"]["2.0"]["g"])
							print (calib_rgb_iiron_data["calibration"]["I"]["2.0"]["b"])									
							calib_rgb_iiron_data["calibration"]["I"]["2.0"]["r"] = r_iiron	
							calib_rgb_iiron_data["calibration"]["I"]["2.0"]["g"] = g_iiron
							calib_rgb_iiron_data["calibration"]["I"]["2.0"]["b"] = b_iiron
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_iiron_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["I2.0"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Iron", "Iron (2.0) Calibration Successful")	
							
					if "Organic Carbon" in lst_values:					
						if "0.0" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Organic Carbon (0)")
							
							d1oc1_cmd_to_send = "KT+PR:"+CalibOC1+"\r\n"
							oc1_ret_val = self.kt_sendcommand(d1oc1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							
							messagebox.showinfo("Organic Carbon (0.0)", "Take 10ml of Standard Solution and place it under OC ")
							
							texttosend="KT+EXTDISPENSEM:13+05\r\n"
							dispense_ret_val = self.kt_send_external_command(texttosend,10,10)
							
							texttosend="KT+EXTDISPENSEM:14+05\r\n"
							dispense_ret_val = self.kt_send_external_command(texttosend,10,10)

							messagebox.showinfo("Organic Carbon (0.0)", "Mix it weel and Pour the solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1oc2_cmd_to_send = "KT+PR:"+CalibOC2+"\r\n"
							oc2_ret_val = self.kt_sendcommand(d1oc2_cmd_to_send,64,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_ooc, g_ooc, b_ooc = self.oc_cal_imagecapture("00")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_ooc_data = json.load(json_file)
							print (calib_rgb_ooc_data["calibration"]["OC"]["0.0"]["r"])
							print (calib_rgb_ooc_data["calibration"]["OC"]["0.0"]["g"])
							print (calib_rgb_ooc_data["calibration"]["OC"]["0.0"]["b"])									
							calib_rgb_ooc_data["calibration"]["OC"]["0.0"]["r"] = r_ooc	
							calib_rgb_ooc_data["calibration"]["OC"]["0.0"]["g"] = g_ooc
							calib_rgb_ooc_data["calibration"]["OC"]["0.0"]["b"] = b_ooc	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_ooc_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["OC0.0"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Organic Carbon", "Organic Carbon (0.0) Calibration Successful")		
							
						if "0.25" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Organic Carbon (0.25)")
							
							d1oc1_cmd_to_send = "KT+PR:"+CalibOC1+"\r\n"
							oc1_ret_val = self.kt_sendcommand(d1oc1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							
							messagebox.showinfo("Organic Carbon (0.25)", "Take 10ml of Standard Solution and place it under OC ")
							
							texttosend="KT+EXTDISPENSEM:13+05\r\n"
							dispense_ret_val = self.kt_send_external_command(texttosend,10,10)
							
							texttosend="KT+EXTDISPENSEM:14+05\r\n"
							dispense_ret_val = self.kt_send_external_command(texttosend,10,10)

							messagebox.showinfo("Organic Carbon (0.25)", "Mix it weel and Pour the solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1oc2_cmd_to_send = "KT+PR:"+CalibOC2+"\r\n"
							oc2_ret_val = self.kt_sendcommand(d1oc2_cmd_to_send,64,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_ooc, g_ooc, b_ooc = self.oc_cal_imagecapture("025")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_ooc_data = json.load(json_file)
							print (calib_rgb_ooc_data["calibration"]["OC"]["0.25"]["r"])
							print (calib_rgb_ooc_data["calibration"]["OC"]["0.25"]["g"])
							print (calib_rgb_ooc_data["calibration"]["OC"]["0.25"]["b"])									
							calib_rgb_ooc_data["calibration"]["OC"]["0.25"]["r"] = r_ooc	
							calib_rgb_ooc_data["calibration"]["OC"]["0.25"]["g"] = g_ooc
							calib_rgb_ooc_data["calibration"]["OC"]["0.25"]["b"] = b_ooc	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_ooc_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["OC0.25"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Organic Carbon", "Organic Carbon (0.25) Calibration Successful")		
							
						if "0.5" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Organic Carbon (0.5)")
							
							d1oc1_cmd_to_send = "KT+PR:"+CalibOC1+"\r\n"
							oc1_ret_val = self.kt_sendcommand(d1oc1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							
							messagebox.showinfo("Organic Carbon (0.5)", "Take 10ml of Standard Solution and place it under OC ")
							
							texttosend="KT+EXTDISPENSEM:13+05\r\n"
							dispense_ret_val = self.kt_send_external_command(texttosend,10,10)
							
							texttosend="KT+EXTDISPENSEM:14+05\r\n"
							dispense_ret_val = self.kt_send_external_command(texttosend,10,10)

							messagebox.showinfo("Organic Carbon (0.5)", "Mix it weel and Pour the solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1oc2_cmd_to_send = "KT+PR:"+CalibOC2+"\r\n"
							oc2_ret_val = self.kt_sendcommand(d1oc2_cmd_to_send,64,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_ooc, g_ooc, b_ooc = self.oc_cal_imagecapture("05")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_ooc_data = json.load(json_file)
							print (calib_rgb_ooc_data["calibration"]["OC"]["0.5"]["r"])
							print (calib_rgb_ooc_data["calibration"]["OC"]["0.5"]["g"])
							print (calib_rgb_ooc_data["calibration"]["OC"]["0.5"]["b"])									
							calib_rgb_ooc_data["calibration"]["OC"]["0.5"]["r"] = r_ooc	
							calib_rgb_ooc_data["calibration"]["OC"]["0.5"]["g"] = g_ooc
							calib_rgb_ooc_data["calibration"]["OC"]["0.5"]["b"] = b_ooc	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_ooc_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["OC0.5"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Organic Carbon", "Organic Carbon (0.5) Calibration Successful")
							
						if "0.75" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Organic Carbon (0.75)")
							
							d1oc1_cmd_to_send = "KT+PR:"+CalibOC1+"\r\n"
							oc1_ret_val = self.kt_sendcommand(d1oc1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							
							messagebox.showinfo("Organic Carbon (0.75)", "Take 10ml of Standard Solution and place it under OC ")
							
							texttosend="KT+EXTDISPENSEM:13+05\r\n"
							dispense_ret_val = self.kt_send_external_command(texttosend,10,10)
							
							texttosend="KT+EXTDISPENSEM:14+05\r\n"
							dispense_ret_val = self.kt_send_external_command(texttosend,10,10)

							messagebox.showinfo("Organic Carbon (0.75)", "Mix it weel and Pour the solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1oc2_cmd_to_send = "KT+PR:"+CalibOC2+"\r\n"
							oc2_ret_val = self.kt_sendcommand(d1oc2_cmd_to_send,64,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_ooc, g_ooc, b_ooc = self.oc_cal_imagecapture("075")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_ooc_data = json.load(json_file)
							print (calib_rgb_ooc_data["calibration"]["OC"]["0.75"]["r"])
							print (calib_rgb_ooc_data["calibration"]["OC"]["0.75"]["g"])
							print (calib_rgb_ooc_data["calibration"]["OC"]["0.75"]["b"])									
							calib_rgb_ooc_data["calibration"]["OC"]["0.75"]["r"] = r_ooc	
							calib_rgb_ooc_data["calibration"]["OC"]["0.75"]["g"] = g_ooc
							calib_rgb_ooc_data["calibration"]["OC"]["0.75"]["b"] = b_ooc	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_ooc_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["OC0.75"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Organic Carbon", "Organic Carbon (0.75) Calibration Successful")	
							
						if "1.0" in constant_values:
							self.machine_status_label.configure(text = "")
							
							self.cal_sublabel.configure(text="Organic Carbon (1.0)")
							
							d1oc1_cmd_to_send = "KT+PR:"+CalibOC1+"\r\n"
							oc1_ret_val = self.kt_sendcommand(d1oc1_cmd_to_send,1,10)
							
							self.msg_nitro.acquire()
							self.tablet_dispense = 1						
							self.msg_nitro.release()
							
							messagebox.showinfo("Organic Carbon (1.0)", "Take 10ml of Standard Solution and place it under OC ")
							
							texttosend="KT+EXTDISPENSEM:13+05\r\n"
							dispense_ret_val = self.kt_send_external_command(texttosend,10,10)
							
							texttosend="KT+EXTDISPENSEM:14+05\r\n"
							dispense_ret_val = self.kt_send_external_command(texttosend,10,10)

							messagebox.showinfo("Organic Carbon (1.0)", "Mix it weel and Pour the solution onto test tube")
							self.msg_nitro.acquire()
							self.tablet_dispense = 0
							self.msg_nitro.release()								

							d1oc2_cmd_to_send = "KT+PR:"+CalibOC2+"\r\n"
							oc2_ret_val = self.kt_sendcommand(d1oc2_cmd_to_send,64,10)						

							ledon_cmd_to_send = "KT+LEDON\r\n" 
							ledon_ret_val = self.kt_sendcommand(ledon_cmd_to_send,1,10)      
					
							r_ooc, g_ooc, b_ooc = self.oc_cal_imagecapture("10")
							
							with open(self.npk_calibration_values_path) as json_file:
								calib_rgb_ooc_data = json.load(json_file)
							print (calib_rgb_ooc_data["calibration"]["OC"]["1.0"]["r"])
							print (calib_rgb_ooc_data["calibration"]["OC"]["1.0"]["g"])
							print (calib_rgb_ooc_data["calibration"]["OC"]["1.0"]["b"])									
							calib_rgb_ooc_data["calibration"]["OC"]["1.0"]["r"] = r_ooc	
							calib_rgb_ooc_data["calibration"]["OC"]["1.0"]["g"] = g_ooc
							calib_rgb_ooc_data["calibration"]["OC"]["1.0"]["b"] = b_ooc	
							with open(self.npk_calibration_values_path, 'w') as fp:
								json.dump(calib_rgb_ooc_data, fp)													

							ledoff_cmd_to_send = "KT+LEDOFF\r\n" 
							ledoff_ret_val = self.kt_sendcommand(ledoff_cmd_to_send,1,10)

							texttosend = "KT+PR:"+WashCuvette_DeviceWash+"\r\n"
							wash_ret_val = self.kt_sendcommand(texttosend,45,10)
							
							with open(self.calibration_status_path) as calib_contents:
									reset_all_calib_status_data = json.load(calib_contents)		
									reset_all_calib_status_data["OC1.0"]= "C"				
							with open(self.calibration_status_path, 'w') as fp:
								json.dump(reset_all_calib_status_data, fp)									
					
							messagebox.showinfo("Organic Carbon", "Organic Carbon (1.0) Calibration Successful")		
							
					self.breportt=Button(self.Timm_FRame,text="Calibration Home",bg="blue",font="centre",fg="white",command=self.goback_cal_home_from_calibration)

					self.breportt.place(x=600,y=350,height=30)
					self.c1.itemconfigure(self.r,fill="#1f1")
				else:
					messagebox.showinfo("Chemical Firmware error", "Chemical Firmware file not created")
			except Exception as e:
				self.c1.itemconfigure(self.r,fill="#f11")				
				errorstring = "/E-calibration()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
						
		def calibration_onselect1(self,event):
			try:
				w = event.widget
				index = w.curselection()[0]
				if index == 0:
				    self.constants_listboxx.delete('0','end')
				    addlist = ['1.50']
				    for item in addlist:
				       self.constants_listboxx.insert(END, item) 					    
				elif index == 1:
				    self.constants_listboxx.delete('0','end')
				    addlist = ['03.51','03.52','03.53','03.54','03.55','03.56','03.57','03.58','03.59','03.60','03.61','03.62','03.63','03.64','03.65','03.66','03.67','03.68','03.69','03.70','03.71','03.72','03.73','03.74','03.75','03.76','03.77','03.78','03.79','03.80','03.81','03.82','03.83','03.84','03.85','03.86','03.87','03.88','03.89','03.90','03.91','03.92','03.93','03.94','03.95','03.96','03.97','03.98','03.99','04.00','04.01','04.02','04.03','04.04','04.05','04.06','04.07','04.08','04.09','04.10','04.11','04.12','04.13','04.14','04.15','04.16','04.17','04.18','04.19','04.20','04.21','04.22','04.23','04.24','04.25','04.26','04.27','04.28','04.29','04.30','04.31','04.32','04.33','04.34','04.35','04.36','04.37','04.38','04.39','04.40','04.41','04.42','04.43','04.44','04.45','04.46','04.47','04.48','04.49','04.50']
				    for item in addlist:
				       self.constants_listboxx.insert(END, item) 
				elif index == 2:
				    self.constants_listboxx.delete('0','end')  
				    addlist = ['06.51','06.52','06.53','06.54','06.55','06.56','06.57','06.58','06.59','06.60','06.61','06.62','06.63','06.64','06.65','06.66','06.67','06.68','06.69','06.70','06.71','06.72','06.73','06.74','06.75','06.76','06.77','06.78','06.79','06.80','06.81','06.82','06.83','06.84','06.85','06.86','06.87','06.88','06.89','06.90','06.91','06.92','06.93','06.94','06.95','06.96','06.97','06.98','06.99','07.00','07.01','07.02','07.03','07.04','07.05','07.06','07.07','07.08','07.09','07.10','07.11','07.12','07.13','07.14','07.15','07.16','07.17','07.18','07.19','07.20','07.21','07.22','07.23','07.24','07.25','07.26','07.27','07.28','07.29','07.30','07.31','07.32','07.33','07.34','07.35','07.36','07.37','07.38','07.39','07.40','07.41','07.42','07.43','07.44','07.45','07.46','07.47','07.48','07.49','07.50']
				    for item in addlist:
				       self.constants_listboxx.insert(END, item)
				elif index == 3:
				    self.constants_listboxx.delete('0','end')  
				    addlist = ['00','05','10','20','30','40']
				    for item in addlist:
				       self.constants_listboxx.insert(END, item) 				    
				elif index == 4:
				    self.constants_listboxx.delete('0','end')  
				    addlist = ['00','05','10','15','20','25']
				    for item in addlist:
				       self.constants_listboxx.insert(END, item) 				    			    
				elif index == 5:
				    self.constants_listboxx.delete('0','end')  
				    addlist = ['00','10','20','40']
				    for item in addlist:
				       self.constants_listboxx.insert(END, item) 	
				elif index == 6:
				    self.constants_listboxx.delete('0','end')  
				    addlist = ['0.0','0.25','0.5','1.0','1.5','2.0']
				    for item in addlist:
				       self.constants_listboxx.insert(END, item) 				       			    
				elif index == 7:
				    self.constants_listboxx.delete('0','end')  
				    addlist = ['0.0','0.5','1.0','1.5','2.0']
				    for item in addlist:
				       self.constants_listboxx.insert(END, item) 				       			    
				elif index == 8:
				    self.constants_listboxx.delete('0','end')  
				    addlist = ['0.0','0.25','0.5','0.75','1.0']
				    for item in addlist:
				       self.constants_listboxx.insert(END, item) 				       			    

				self.constants_listboxx.selection_set(0)    	
			except Exception as e:
				errorstring = "/E-calibration_onselect1()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass		
				 
		def Calibration_test_page(self):
			try:
				lst_values = [self.calibration_listboxx.get(idx) for idx in self.calibration_listboxx.curselection()] 
			
				self.Timm_FRame=Frame(self.root,bg="#F5F4EB", highlightbackground="#254E58", highlightcolor="#254E58", highlightthickness=1)

				if "pH 4.0" in lst_values :
					Mainlabel=Label(self.Timm_FRame,text="Calibration Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")								
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.cal_sublabel=Label(self.Timm_FRame,text="pH",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=160,height=100)
					self.timetext.place(x=500,y=125)

					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)								

					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.cal_sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)

				if "pH 7.0" in lst_values :
					Mainlabel=Label(self.Timm_FRame,text="Calibration Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")								
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.cal_sublabel=Label(self.Timm_FRame,text="pH",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=160,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)															

					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.cal_sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)
						
				if "EC" in lst_values:
					Mainlabel=Label(self.Timm_FRame,text="Calibration Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")								
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.cal_sublabel=Label(self.Timm_FRame,text="EC",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=160,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)								
					
					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.cal_sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)

				if "Nitrogen" in lst_values:
					Mainlabel=Label(self.Timm_FRame,text="Calibration Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")								
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.cal_sublabel=Label(self.Timm_FRame,text="Nitrogen",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=160,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)								

					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.cal_sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)

				if "Potassium" in lst_values :
					Mainlabel=Label(self.Timm_FRame,text="Calibration Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")								
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.cal_sublabel=Label(self.Timm_FRame,text="Potassium",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=160,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)								

					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.cal_sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)

				if "Phosphorus" in lst_values :
					Mainlabel=Label(self.Timm_FRame,text="Calibration Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.cal_sublabel=Label(self.Timm_FRame,text="Phosphorus",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=160,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)								

					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.cal_sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)
					
				if "Boron" in lst_values :
					Mainlabel=Label(self.Timm_FRame,text="Calibration Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.cal_sublabel=Label(self.Timm_FRame,text="Boron",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=160,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)								

					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.cal_sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)
					
				if "Iron" in lst_values :
					Mainlabel=Label(self.Timm_FRame,text="Calibration Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.cal_sublabel=Label(self.Timm_FRame,text="Iron",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=160,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)								

					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.cal_sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)

				if "Organic Carbon" in lst_values :
					Mainlabel=Label(self.Timm_FRame,text="Calibration Progress",bg="#F5F4EB",fg="#254E58",font="BOLD  20")
					canvas=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase=Canvas(self.Timm_FRame,bg="#F5F4EB")
					timecase_minute=Canvas(self.Timm_FRame,bg="#F5F4EB")
					canvas.create_rectangle(30, 10, 675, 180,outline="#fb0",fill="#F5F4EB")

					self.cal_sublabel=Label(self.Timm_FRame,text="Organic Carbon",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel3=Label(self.Timm_FRame,text="Test Name",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					sublabel2=Label(self.Timm_FRame,text="Status",bg="#F5F4EB",fg="#254E58",font="BOLD  12")

					lready=Label(self.Timm_FRame,text="Ready",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lwait=Label(self.Timm_FRame,text="Wait",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lsucc=Label(self.Timm_FRame,text="Success",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					lfail=Label(self.Timm_FRame,text="Failure",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
					canvas.place(x=10,y=80,width=700,height=200)

					self.c1=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c2=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c3=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c4=Canvas(self.Timm_FRame,bg="#F5F4EB")
					c5=Canvas(self.Timm_FRame,bg="#F5F4EB")

					self.timetext=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase.place(x=480,y=100,width=160,height=100)
					self.timetext.place(x=500,y=125)
					
					self.timetext_min=Label(self.Timm_FRame,text="",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
					timecase_minute.create_rectangle(10, 10, 60, 60,outline="#f00",fill="#F5F4EB")
					timecase_minute.place(x=580,y=100,width=100,height=100)
					self.timetext_min.place(x=600,y=125)								

					self.r=self.c1.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c2.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFFF00", width=1)
					c3.create_oval(10, 10, 20, 20, outline="#f11",fill="#FFA500", width=1)
					c4.create_oval(10, 10, 20, 20, outline="#f11",fill="#1f1", width=1)
					c5.create_oval(10, 10, 20, 20, outline="#f11",fill="#f11", width=1)

					self.Timm_FRame.place(x=10,y=40,width=780,height=390)
					self.c1.place(x=400,y=190,width=30,height=30)
					lready.place(x=70,y=300)
					c2.place(x=20,y=300,width=30,height=30)
					lwait.place(x=250,y=300)
					c3.place(x=200,y=300,width=30,height=30)
					lsucc.place(x=430,y=300)
					c4.place(x=380,y=300,width=30,height=30)
					lfail.place(x=610,y=300)
					c5.place(x=560,y=300,width=30,height=30)

					Mainlabel.place(x=20,y=20)
					self.cal_sublabel.place(x=100,y=190)
					sublabel3.place(x=100,y=110)
					sublabel2.place(x=400,y=110)

									
				self.timer_calibration_samplesolution = threading.Thread(target=self.calibration_samplesolution)
				self.timer_countdown=threading.Thread(target=self.calibration_readdy)
				
				self.timer_countdown.start()
				self.timer_calibration_samplesolution.start()
			except Exception as e:
				self.Timm_FRame.destroy()
				errorstring = "/E-Calibration test page()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass  
				
		def eccal(self):
			try:		
				MsgBox = messagebox.askquestion ('Reset EC','Press yes to reset EC / press no to goback',icon = 'warning')
				if MsgBox == 'yes':
					self.ec_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["EC"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)
			except Exception as e:
				errorstring = "/E-eccal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 		
				
		def ph4cal(self):
			try:		
				MsgBox = messagebox.askquestion ('Reset pH4','Press yes to reset pH4 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':				
					self.ph4_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["pH4"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-ph4cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass	
				
		def ph7cal(self):
			try:		
				MsgBox = messagebox.askquestion ('Reset pH7','Press yes to reset pH7 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':				
					self.ph7_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["pH7"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)
			except Exception as e:
				errorstring = "/E-ph7cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass										
				 				
		def n0cal(self):	
			try:		
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset N0 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':				
					self.n0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["N0"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-nocal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 							
			
		def n5cal(self):
			try:
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset N5 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':				
					self.n5_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["N5"]= "NC"					
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-n5cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 							

		def n10cal(self):
			try:		
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset N10 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					self.n10_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["N10"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-n10cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 								

		def n20cal(self):		
			try:	
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset N20 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':				
					self.n20_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["N20"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-n20cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 								

		def n30cal(self):
			try:
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset N30 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':				
					self.n30_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["N30"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)		
			except Exception as e:
				errorstring = "/E-n30cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 							

		def n40cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset N40 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					self.n40_status.config(bg="red")	
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["N40"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-n40cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 								

		def p0cal(self):	
			try:		
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset P0 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':				
					self.p0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["P0"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-p0cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 					
							
		def p5cal(self):
			try:
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset P5 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':				
					self.p5_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["P5"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-p5cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 					
							
		def p10cal(self):
			try:	
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset P10 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':						
					self.p10_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["P10"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-p10cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 					
							
		def p15cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset P15 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					self.p15_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["P15"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-p15cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 					
							
		def p20cal(self):
			try:
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset P20 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':				
					self.p20_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["P20"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-p20cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 					
							
		def p25cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset P25 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					self.p25_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["P25"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-p25cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 					
							
		def k0cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset K0 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					self.k0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["K0"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)
			except Exception as e:
				errorstring = "/E-k0cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 						
							
		def k10cal(self):
			try:
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset K10 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':						
					self.k10_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["K10"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-k10cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 					
							
		def k20cal(self):
			try:	
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset K20 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':						
					self.k20_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["K20"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-k20cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 					
								
		def k40cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset N0','Press yes to reset K40 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					self.k40_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["K40"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				errorstring = "/E-k40cal()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 	
				
		def b0p0cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset B0','Press yes to reset B0.0 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset b0p0cal entry")
					self.b0p0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["B0.0"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised b0p0cal Page")
				print (e)
			finally:
				pass 							

		def b0p25cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset B0.25','Press yes to reset B0.25 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset b0p25cal entry")
					self.b0p25_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["B0.25"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised b0p25cal Page")
				print (e)
			finally:
				pass
					
		def b0p5cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset B0.5','Press yes to reset B0.5 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset b0p5cal entry")
					self.b0p5_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["B0.5"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised b0p5cal Page")
				print (e)
			finally:
				pass
				
		def b1p0cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset B1.0','Press yes to reset B1.0 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset b1p0cal entry")
					self.b1p0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["B1.0"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised b1p0cal Page")
				print (e)
			finally:
				pass
				
		def b1p5cal(self):	
			try:
				MsgBox = messagebox.askquestion ('Reset B1.5','Press yes to reset B1.5 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':						
					print ("reset b1p5cal entry")
					self.b1p5_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["B1.5"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised b1p5cal Page")
				print (e)
			finally:
				pass				
								
		def b2p0cal(self):	
			try:
				MsgBox = messagebox.askquestion ('Reset B2.0','Press yes to reset B2.0 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':						
					print ("reset b2p0cal entry")
					self.b2p0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["B2.0"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised b2p0cal Page")
				print (e)
			finally:
				pass
				
		def i0p0cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset I0','Press yes to reset I0.0 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset i0p0cal entry")
					self.i0p0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["I0.0"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised c0p0cal Page")
				print (e)
			finally:
				pass
				
		def i0p5cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset 0.5','Press yes to reset I0.5 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset i0p5cal entry")
					self.i0p5_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["I0.5"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised i0p5cal Page")
				print (e)
			finally:
				pass	
				
		def i1p0cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset I1.0','Press yes to reset I1.0 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset i1p0cal entry")
					self.i1p0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["I1.0"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised i1p0cal Page")
				print (e)
			finally:
				pass	
				
		def i1p5cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset I1.5','Press yes to reset I1.5 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset i1p5cal entry")
					self.i1p5_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["I1.5"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised i1p5cal Page")
				print (e)
			finally:
				pass	
				
		def i2p0cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset I2.0','Press yes to reset I2.0 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset i2p0cal entry")
					self.i2p0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["I2.0"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised i2p0cal Page")
				print (e)
			finally:
				pass						

		def oc0p0cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset OC0.0','Press yes to reset OC0.0 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset oc0p0cal entry")
					self.oc0p0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["oc0.0"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised oc0p0cal Page")
				print (e)
			finally:
				pass						
				
		def oc0p25cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset OC0.25','Press yes to reset OC0.25 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset oc0p25cal entry")
					self.oc0p0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["oc0.25"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised oc0p25cal Page")
				print (e)
			finally:
				pass						

		def oc0p5cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset OC0.5','Press yes to reset OC0.5 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset oc0p5cal entry")
					self.oc0p0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["oc0.5"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised oc0p25cal Page")
				print (e)
			finally:
				pass						

		def oc0p75cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset OC0.75','Press yes to reset OC0.75 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset oc0p75cal entry")
					self.oc0p0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["oc0.75"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised oc0p75cal Page")
				print (e)
			finally:
				pass						

		def oc1p0cal(self):	
			try:	
				MsgBox = messagebox.askquestion ('Reset OC1.0','Press yes to reset OC1.0 / press no to goback',icon = 'warning')
				if MsgBox == 'yes':					
					print ("reset oc1p0cal entry")
					self.oc1p0_status.config(bg="red")
					with open(self.calibration_status_path) as calib_contents:
						reset_all_calib_status_data = json.load(calib_contents)		
						reset_all_calib_status_data["oc1.0"]= "NC"				
					with open(self.calibration_status_path, 'w') as fp:
						json.dump(reset_all_calib_status_data, fp)	
			except Exception as e:
				print ("Exception raised oc1p0cal Page")
				print (e)
			finally:
				pass						

		def resetall(self):	
			try:		
				self.ec_status.config(bg="red")
				self.ph4_status.config(bg="red")
				self.ph7_status.config(bg="red")
				self.n0_status.config(bg="red")
				self.n5_status.config(bg="red")
				self.n10_status.config(bg="red")
				self.n20_status.config(bg="red")
				self.n30_status.config(bg="red")
				self.n40_status.config(bg="red")
				self.p0_status.config(bg="red")
				self.p5_status.config(bg="red")
				self.p10_status.config(bg="red")
				self.p15_status.config(bg="red")
				self.p20_status.config(bg="red")
				self.p25_status.config(bg="red")
				self.k0_status.config(bg="red")
				self.k10_status.config(bg="red")
				self.k20_status.config(bg="red")
				self.k40_status.config(bg="red")
			
				with open(self.calibration_status_path) as calib_contents:
					reset_all_calib_status_data = json.load(calib_contents)		
					reset_all_calib_status_data["EC"] = "NC" 
					reset_all_calib_status_data["pH4"]= "NC" 
					reset_all_calib_status_data["pH7"]= "NC" 
					reset_all_calib_status_data["N0"]= "NC"
					reset_all_calib_status_data["N5"]= "NC"
					reset_all_calib_status_data["N10"]= "NC"
					reset_all_calib_status_data["N20"]= "NC"
					reset_all_calib_status_data["N30"]= "NC"
					reset_all_calib_status_data["N40"]= "NC"
					reset_all_calib_status_data["P0"]= "NC"
					reset_all_calib_status_data["P5"]= "NC"
					reset_all_calib_status_data["P10"]= "NC"
					reset_all_calib_status_data["P15"]= "NC"
					reset_all_calib_status_data["P20"]= "NC"
					reset_all_calib_status_data["P25"]= "NC"
					reset_all_calib_status_data["K0"] = "NC"
					reset_all_calib_status_data["K10"]= "NC"
					reset_all_calib_status_data["K20"]= "NC"
					reset_all_calib_status_data["K40"]= "NC"
						
				with open(self.calibration_status_path, 'w') as fp:
					json.dump(reset_all_calib_status_data, fp)
			except Exception as e:
				errorstring = "/E-resetall()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				
		def CalibResetEnable(self):
			try:
				self.bEC['state']=NORMAL
				self.bPH4['state']=NORMAL
				self.bPH7['state']=NORMAL
								
				self.bNitrogen0['state']=NORMAL
				self.bNitrogen5['state']=NORMAL
				self.bNitrogen10['state']=NORMAL	
				self.bNitrogen20['state']=NORMAL
				self.bNitrogen30['state']=NORMAL
				self.bNitrogen40['state']=NORMAL					
				
				self.bPhosphorus0['state']=NORMAL
				self.bPhosphorus5['state']=NORMAL
				self.bPhosphorus10['state']=NORMAL	
				self.bPhosphorus15['state']=NORMAL
				self.bPhosphorus20['state']=NORMAL
				self.bPhosphorus25['state']=NORMAL				
				
				self.bPotassium0['state']=NORMAL
				self.bPotassium10['state']=NORMAL
				self.bPotassium20['state']=NORMAL	
				self.bPotassium40['state']=NORMAL	
				
				self.bBoron0p0['state']=NORMAL
				self.bBoron0p25['state']=NORMAL
				self.bBoron0p5['state']=NORMAL	
				self.bBoron1p0['state']=NORMAL
				self.bBoron1p5['state']=NORMAL
				self.bBoron2p0['state']=NORMAL		
				
				self.bIron0p0['state']=NORMAL
				self.bIron0p5['state']=NORMAL
				self.bIron1p0['state']=NORMAL	
				self.bIron1p5['state']=NORMAL
				self.bIron2p0['state']=NORMAL
				
				self.boc0p0['state']=NORMAL
				self.boc0p25['state']=NORMAL
				self.boc0p5['state']=NORMAL	
				self.boc0p75['state']=NORMAL
				self.boc1p0['state']=NORMAL
			except Exception as e:
				errorstring = "/E-calibresetenable()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 	
				
		def CalibResetDisable(self):
			try:
				self.bEC['state']=DISABLED
				self.bPH4['state']=DISABLED
				self.bPH7['state']=DISABLED
								
				self.bNitrogen0['state']=DISABLED
				self.bNitrogen5['state']=DISABLED
				self.bNitrogen10['state']=DISABLED	
				self.bNitrogen20['state']=DISABLED
				self.bNitrogen30['state']=DISABLED
				self.bNitrogen40['state']=DISABLED					
				
				self.bPhosphorus0['state']=DISABLED
				self.bPhosphorus5['state']=DISABLED
				self.bPhosphorus10['state']=DISABLED	
				self.bPhosphorus15['state']=DISABLED
				self.bPhosphorus20['state']=DISABLED
				self.bPhosphorus25['state']=DISABLED				
				
				self.bPotassium0['state']=DISABLED
				self.bPotassium10['state']=DISABLED
				self.bPotassium20['state']=DISABLED	
				self.bPotassium40['state']=DISABLED	
				
				self.bBoron0p0['state']=DISABLED
				self.bBoron0p25['state']=DISABLED
				self.bBoron0p5['state']=DISABLED	
				self.bBoron1p0['state']=DISABLED
				self.bBoron1p5['state']=DISABLED
				self.bBoron2p0['state']=DISABLED		
				
				self.bIron0p0['state']=DISABLED
				self.bIron0p5['state']=DISABLED
				self.bIron1p0['state']=DISABLED	
				self.bIron1p5['state']=DISABLED
				self.bIron2p0['state']=DISABLED	
				
				self.boc0p0['state']=DISABLED
				self.boc0p25['state']=DISABLED
				self.boc0p5['state']=DISABLED	
				self.boc0p75['state']=DISABLED
				self.boc1p0['state']=DISABLED
											
			except Exception as e:
				errorstring = "/E-Calibresetdisable()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 																										

		def calibration(self):
			try:
				self.machine_status_label.configure(text = "")
				self.calibration_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				mainlabel=Label(self.calibration_FRame,text="Sample Calibration",bg="#F5F4EB",fg="#254E58",font="BOLD  14 ") 
				
				canvas=Canvas(self.calibration_FRame,bg="#F5F4EB")
				canvas.create_rectangle(2, 2, 695, 208,outline="#fb0",fill="#F5F4EB")
				   
				line=Label(self.calibration_FRame,text="##############################################################################")
				self.calibration_listboxx=Listbox(self.calibration_FRame,selectmode=SINGLE,width=15,height=8,font=("Calibri",10),exportselection=0 )
				self.calibration_listboxx.insert(1,"EC")
				self.calibration_listboxx.insert(2,"pH 4.0")
				self.calibration_listboxx.insert(3,"pH 7.0")
				self.calibration_listboxx.insert(4,"Nitrogen")
				self.calibration_listboxx.insert(5,"Phosphorus")
				self.calibration_listboxx.insert(6,"Potassium")
				self.calibration_listboxx.insert(7,"Boron")
				self.calibration_listboxx.insert(8,"Iron")	
				self.calibration_listboxx.selection_set(0)
							
				self.constants_listboxx=Listbox(self.calibration_FRame,selectmode=SINGLE,width=15,height=8,font=("Calibri",10),exportselection=0)
				
				self.constants_listboxx.insert(1,"1.50")
				self.constants_listboxx.selection_set(0)
				
				self.constants_listboxx.place(x=205,y=62)
				
				l1select = self.calibration_listboxx.bind('<<ListboxSelect>>',self.calibration_onselect1)
									
				self.bconfirm_calib=Button(self.calibration_FRame,text="Calibrate",bg="blue",font="centre 8",fg="white",command=self.Calibration_test_page)
				
				self.btodashboard=Button(self.calibration_FRame,text="Dashboard",bg="blue",font="centre 8",fg="white",command=self.goback_dashboard_from_calibration)					
				self.calibration_FRame.place(x=10,y=40,width=780,height=395)
				self.btodashboard.place(x=570,y=2)
				mainlabel.place(x=270,y=5)
				line.place(x=0,y=30)
				self.calibration_listboxx.place(x=75,y=62)
				self.bconfirm_calib.place(x=235,y=200)
				self.calibration_status_label=Label(self.calibration_FRame,text="Calibration Status",bg="#F5F4EB",fg="light green",font="BOLD  14")
				self.ec_calibration_status_label=Label(self.calibration_FRame,text="EC",bg="#F5F4EB",fg="#254E58",font="BOLD  8")  
				self.ph_calibration_status_label=Label(self.calibration_FRame,text="pH",bg="#F5F4EB",fg="#254E58",font="BOLD  8")
				self.n_calibration_status_label=Label(self.calibration_FRame,text="Nitrogen",bg="#F5F4EB",fg="#254E58",font="BOLD  8")  
				self.p_calibration_status_label=Label(self.calibration_FRame,text="Phosphorus",bg="#F5F4EB",fg="#254E58",font="BOLD  8")
				self.k_calibration_status_label=Label(self.calibration_FRame,text="Potassium",bg="#F5F4EB",fg="#254E58",font="BOLD  8")
				self.b_calibration_status_label=Label(self.calibration_FRame,text="Boron",bg="#F5F4EB",fg="#254E58",font="BOLD  8")
				self.i_calibration_status_label=Label(self.calibration_FRame,text="Iron",bg="#F5F4EB",fg="#254E58",font="BOLD  8")
				self.oc_calibration_status_label=Label(self.calibration_FRame,text="Organic C",bg="#F5F4EB",fg="#254E58",font="BOLD  8")

				with open(self.calibration_status_path) as calib_contents:
					calib_status_data = json.load(calib_contents)
					
				if calib_status_data["EC"] == "NC":
					self.ec_status=Label(self.calibration_FRame,text="1.5",bg="red",fg="#254E58",font="BOLD  8") 
				else:		
					self.ec_status=Label(self.calibration_FRame,text="1.5",bg="green",fg="#254E58",font="BOLD  8") 

				if calib_status_data["pH4"] == "NC":					  	
					self.ph4_status=Label(self.calibration_FRame,text="4.0",bg="red",fg="#254E58",font="BOLD  8")
				else:					  	
					self.ph4_status=Label(self.calibration_FRame,text="4.0",bg="green",fg="#254E58",font="BOLD  8")		
					
				if calib_status_data["pH7"] == "NC":					  	
					self.ph7_status=Label(self.calibration_FRame,text="7.0",bg="red",fg="#254E58",font="BOLD  8")
				else:					  	
					self.ph7_status=Label(self.calibration_FRame,text="7.0",bg="green",fg="#254E58",font="BOLD  8")				
									
				if calib_status_data["N0"] == "NC":					  	
					self.n0_status=Label(self.calibration_FRame,text="00",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.n0_status=Label(self.calibration_FRame,text="00",bg="green",fg="#254E58",font="BOLD  8")		

				if calib_status_data["N5"] == "NC":					  	
					self.n5_status=Label(self.calibration_FRame,text="05",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.n5_status=Label(self.calibration_FRame,text="05",bg="green",fg="#254E58",font="BOLD  8")
					
				if calib_status_data["N10"] == "NC":					  	
					self.n10_status=Label(self.calibration_FRame,text="10",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.n10_status=Label(self.calibration_FRame,text="10",bg="green",fg="#254E58",font="BOLD  8")	
			
				if calib_status_data["N20"] == "NC":					  	
					self.n20_status=Label(self.calibration_FRame,text="20",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.n20_status=Label(self.calibration_FRame,text="20",bg="green",fg="#254E58",font="BOLD  8")	
					
				if calib_status_data["N30"] == "NC":					  	
					self.n30_status=Label(self.calibration_FRame,text="30",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.n30_status=Label(self.calibration_FRame,text="30",bg="green",fg="#254E58",font="BOLD  8")				
					
				if calib_status_data["N40"] == "NC":					  	
					self.n40_status=Label(self.calibration_FRame,text="40",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.n40_status=Label(self.calibration_FRame,text="40",bg="green",fg="#254E58",font="BOLD  8")	
								
				if calib_status_data["P0"] == "NC":					  	
					self.p0_status=Label(self.calibration_FRame,text="00",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.p0_status=Label(self.calibration_FRame,text="00",bg="green",fg="#254E58",font="BOLD  8")
								
				if calib_status_data["P5"] == "NC":					  	
					self.p5_status=Label(self.calibration_FRame,text="05",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.p5_status=Label(self.calibration_FRame,text="05",bg="green",fg="#254E58",font="BOLD  8")
								
				if calib_status_data["P10"] == "NC":					  	
					self.p10_status=Label(self.calibration_FRame,text="10",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.p10_status=Label(self.calibration_FRame,text="10",bg="green",fg="#254E58",font="BOLD  8")
								
				if calib_status_data["P15"] == "NC":					  	
					self.p15_status=Label(self.calibration_FRame,text="15",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.p15_status=Label(self.calibration_FRame,text="15",bg="green",fg="#254E58",font="BOLD  8")
								
				if calib_status_data["P20"] == "NC":					  	
					self.p20_status=Label(self.calibration_FRame,text="20",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.p20_status=Label(self.calibration_FRame,text="20",bg="green",fg="#254E58",font="BOLD  8")
								
				if calib_status_data["P25"] == "NC":					  	
					self.p25_status=Label(self.calibration_FRame,text="25",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.p25_status=Label(self.calibration_FRame,text="25",bg="green",fg="#254E58",font="BOLD  8")				

				if calib_status_data["K0"] == "NC":					  	
					self.k0_status=Label(self.calibration_FRame,text="00",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.k0_status=Label(self.calibration_FRame,text="00",bg="green",fg="#254E58",font="BOLD  8")	
					
				if calib_status_data["K10"] == "NC":					  	
					self.k10_status=Label(self.calibration_FRame,text="10",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.k10_status=Label(self.calibration_FRame,text="10",bg="green",fg="#254E58",font="BOLD  8")	

				if calib_status_data["K20"] == "NC":					  	
					self.k20_status=Label(self.calibration_FRame,text="20",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.k20_status=Label(self.calibration_FRame,text="20",bg="green",fg="#254E58",font="BOLD  8")	

				if calib_status_data["K40"] == "NC":					  	
					self.k40_status=Label(self.calibration_FRame,text="40",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.k40_status=Label(self.calibration_FRame,text="40",bg="green",fg="#254E58",font="BOLD  8")	
					
				if calib_status_data["B0.0"] == "NC":					  	
					self.b0p0_status=Label(self.calibration_FRame,text="0.0",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.b0p0_status=Label(self.calibration_FRame,text="0.0",bg="green",fg="#254E58",font="BOLD  8")	
					
				if calib_status_data["B0.25"] == "NC":					  	
					self.b0p25_status=Label(self.calibration_FRame,text="0.25",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.b0p25_status=Label(self.calibration_FRame,text="0.25",bg="green",fg="#254E58",font="BOLD  8")
					
				if calib_status_data["B0.5"] == "NC":					  	
					self.b0p5_status=Label(self.calibration_FRame,text="0.5",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.b0p5_status=Label(self.calibration_FRame,text="0.5",bg="green",fg="#254E58",font="BOLD  8")	
					
				if calib_status_data["B1.0"] == "NC":					  	
					self.b1p0_status=Label(self.calibration_FRame,text="1.0",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.b1p0_status=Label(self.calibration_FRame,text="1.0",bg="green",fg="#254E58",font="BOLD  8")
					
				if calib_status_data["B1.5"] == "NC":					  	
					self.b1p5_status=Label(self.calibration_FRame,text="1.5",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.b1p5_status=Label(self.calibration_FRame,text="1.5",bg="green",fg="#254E58",font="BOLD  8")
					
				if calib_status_data["B2.0"] == "NC":					  	
					self.b2p0_status=Label(self.calibration_FRame,text="2.0",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.b2p0_status=Label(self.calibration_FRame,text="2.0",bg="green",fg="#254E58",font="BOLD  8")
					
				if calib_status_data["I0.0"] == "NC":					  	
					self.i0p0_status=Label(self.calibration_FRame,text="0.0",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.i0p0_status=Label(self.calibration_FRame,text="0.0",bg="green",fg="#254E58",font="BOLD  8")
										
				if calib_status_data["I0.5"] == "NC":					  	
					self.i0p5_status=Label(self.calibration_FRame,text="0.5",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.i0p5_status=Label(self.calibration_FRame,text="0.5",bg="green",fg="#254E58",font="BOLD  8")

				if calib_status_data["I1.0"] == "NC":					  	
					self.i1p0_status=Label(self.calibration_FRame,text="1.0",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.i1p0_status=Label(self.calibration_FRame,text="1.0",bg="green",fg="#254E58",font="BOLD  8")

				if calib_status_data["I1.5"] == "NC":					  	
					self.i1p5_status=Label(self.calibration_FRame,text="1.5",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.i1p5_status=Label(self.calibration_FRame,text="1.5",bg="green",fg="#254E58",font="BOLD  8")

				if calib_status_data["I2.0"] == "NC":					  	
					self.i2p0_status=Label(self.calibration_FRame,text="2.0",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.i2p0_status=Label(self.calibration_FRame,text="2.0",bg="green",fg="#254E58",font="BOLD  8")

				'''
				if calib_status_data["OC0.0"] == "NC":					  	
					self.oc0p0_status=Label(self.calibration_FRame,text="0.0",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.oc0p0_status=Label(self.calibration_FRame,text="0.0",bg="green",fg="#254E58",font="BOLD  8")
										
				if calib_status_data["OC0.25"] == "NC":					  	
					self.oc0p25_status=Label(self.calibration_FRame,text="0.25",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.oc0p25_status=Label(self.calibration_FRame,text="0.25",bg="green",fg="#254E58",font="BOLD  8")

				if calib_status_data["OC0.5"] == "NC":					  	
					self.oc0p5_status=Label(self.calibration_FRame,text="0.5",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.oc0p5_status=Label(self.calibration_FRame,text="0.5",bg="green",fg="#254E58",font="BOLD  8")

				if calib_status_data["OC0.75"] == "NC":					  	
					self.oc0p75_status=Label(self.calibration_FRame,text="0.75",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.oc0p75_status=Label(self.calibration_FRame,text="0.75",bg="green",fg="#254E58",font="BOLD  8")

				if calib_status_data["OC1.0"] == "NC":					  	
					self.oc1p0_status=Label(self.calibration_FRame,text="1.0",bg="red",fg="#254E58",font="BOLD  8")
				else:
					self.oc1p0_status=Label(self.calibration_FRame,text="1.0",bg="green",fg="#254E58",font="BOLD  8")
				'''
				self.calibration_status_label.place(x=570,y=70) 
				 			
				self.ec_calibration_status_label.place(x=340,y=60) 
				self.ph_calibration_status_label.place(x=340,y=85) 
				self.n_calibration_status_label.place(x=340,y=110) 
				self.p_calibration_status_label.place(x=340,y=135) 
				self.k_calibration_status_label.place(x=340,y=160)
				self.b_calibration_status_label.place(x=340,y=185)
				self.i_calibration_status_label.place(x=340,y=210)
				#self.oc_calibration_status_label.place(x=340,y=235)				

				canvas_cal_reset=Canvas(self.calibration_FRame,bg="#F5F4EB")
				canvas_cal_reset.create_rectangle(2, 2, 695, 130,outline="#fb0",fill="#F5F4EB")						
				canvas.place(x=65,y=55,width=700,height=200)					
				
				calibration_reset_label=Label(self.calibration_FRame,text="Calibration Reset",bg="#F5F4EB",fg="#254E58",font="BOLD  10 ")
				canvas_cal_reset.place(x=65,y=255,width=700,height=135)
				
				calibration_reset_label.place(x=80,y=270)	

				self.bResetEnable=Button(self.calibration_FRame,text="Enable",bg="blue",font="centre 10",fg="red",command=self.CalibResetEnable)		
				self.bResetEnable.place(x=100, y=300, width=80, height=30)	
				
				self.bResetDisable=Button(self.calibration_FRame,text="Disable",bg="blue",font="centre 10",fg="red",command=self.CalibResetDisable)		
				self.bResetDisable.place(x=200, y=300, width=80, height=30)	
				
				self.bEC=Button(self.calibration_FRame,text="EC",bg="light blue",font="centre 6",fg="red",command=self.eccal)		
				#self.bEC.place(x=100, y=300, width=30, height=15)	
				self.bEC.place(x=700, y=285, width=30, height=20)	
				
				self.bPH4=Button(self.calibration_FRame,text="pH 4.0",bg="light blue",font="centre 6",fg="red",command=self.ph4cal)		
				#self.bPH4.place(x=165, y=300, width=30, height=15)	
				self.bPH4.place(x=700, y=310, width=40, height=15)	
				
				self.bPH7=Button(self.calibration_FRame,text="pH 7.0",bg="light blue",font="centre 6",fg="red",command=self.ph7cal)		
				self.bPH7.place(x=700, y=330, width=40, height=15)
				
				#self.bALL=Button(self.calibration_FRame,text="RESET ALL (EC,PH,N,P,K)",bg="red",font="centre",fg="white",command=self.resetall)		
				#self.bALL.place(x=100, y=310)					
				
				self.n_label=Label(self.calibration_FRame,text="Nitrogen",bg="white",fg="#254E58",font="centre  6")						
				
				self.bNitrogen0=Button(self.calibration_FRame,text="00", bg="light blue",font="centre 6",fg="red",command=self.n0cal)		
				self.bNitrogen0.place(x=420, y=270, width=20, height=15)	
				
				self.bNitrogen5=Button(self.calibration_FRame,text="05",bg="light blue",font="centre 6",fg="red",command=self.n5cal)		
				self.bNitrogen5.place(x=460, y=270, width=20, height=15)					
				
				self.bNitrogen10=Button(self.calibration_FRame,text="10",bg="light blue",font="centre 6",fg="red",command=self.n10cal)		
				self.bNitrogen10.place(x=500, y=270, width=20, height=15)	
				
				self.bNitrogen20=Button(self.calibration_FRame,text="20",bg="light blue",font="centre 6",fg="red",command=self.n20cal)		
				self.bNitrogen20.place(x=540, y=270, width=20, height=15)	
				
				self.bNitrogen30=Button(self.calibration_FRame,text="30",bg="light blue",font="centre 6",fg="red",command=self.n30cal)		
				self.bNitrogen30.place(x=580, y=270, width=20, height=15)					
				
				self.bNitrogen40=Button(self.calibration_FRame,text="40",bg="light blue",font="centre 6",fg="red",command=self.n40cal)		
				self.bNitrogen40.place(x=620, y=270, width=20, height=15)	
				
				self.n_label.place(x=340, y= 270, width=40, height=15)	
				
				self.p_label=Label(self.calibration_FRame,text="Phosphorus",bg="white",fg="#254E58",font="centre  6")						
				
				self.bPhosphorus0=Button(self.calibration_FRame,text="00",bg="light blue",font="centre 6",fg="red",command=self.p0cal)		
				self.bPhosphorus0.place(x=420, y=290, width=20, height=15)	
				
				self.bPhosphorus5=Button(self.calibration_FRame,text="05",bg="light blue",font="centre 6",fg="red",command=self.p5cal)		
				self.bPhosphorus5.place(x=460, y=290, width=20, height=15)					
				
				self.bPhosphorus10=Button(self.calibration_FRame,text="10",bg="light blue",font="centre 6",fg="red",command=self.p10cal)
				self.bPhosphorus10.place(x=500, y=290, width=20, height=15)	
				
				self.bPhosphorus15=Button(self.calibration_FRame,text="15",bg="light blue",font="centre 6",fg="red",command=self.p15cal)
				self.bPhosphorus15.place(x=540, y=290, width=20, height=15)	
				
				self.bPhosphorus20=Button(self.calibration_FRame,text="20",bg="light blue",font="centre 6",fg="red",command=self.p20cal)
				self.bPhosphorus20.place(x=580, y=290, width=20, height=15)					
				
				self.bPhosphorus25=Button(self.calibration_FRame,text="25",bg="light blue",font="centre 6",fg="red",command=self.p25cal)
				self.bPhosphorus25.place(x=620, y=290, width=20, height=15)	
				
				self.p_label.place(x=340, y= 290, width=50, height=15)	
				
				self.k_label=Label(self.calibration_FRame,text="Potassium",bg="white",fg="#254E58",font="centre  6")						
				
				self.bPotassium0=Button(self.calibration_FRame,text="00",bg="light blue",font="centre 6",fg="red",command=self.k0cal)		
				self.bPotassium0.place(x=420, y=310, width=20, height=15)	
				
				self.bPotassium10=Button(self.calibration_FRame,text="10",bg="light blue",font="centre 6",fg="red",command=self.k10cal)		
				self.bPotassium10.place(x=460, y=310, width=20, height=15)					
				
				self.bPotassium20=Button(self.calibration_FRame,text="20",bg="light blue",font="centre 6",fg="red",command=self.k20cal)		
				self.bPotassium20.place(x=500, y=310, width=20, height=15)	
				
				self.bPotassium40=Button(self.calibration_FRame,text="40",bg="light blue",font="centre 6",fg="red",command=self.k40cal)		
				self.bPotassium40.place(x=540, y=310, width=20, height=15)		
				
				self.k_label.place(x=340, y= 310, width=40, height=15)	
				
				self.b_label=Label(self.calibration_FRame,text="Boron",bg="white",fg="#254E58",font="centre  6")						
				
				self.bBoron0p0=Button(self.calibration_FRame,text="0.0",bg="light blue",font="centre 6",fg="red",command=self.b0p0cal)		
				self.bBoron0p0.place(x=420, y=330, width=20, height=15)	
				
				self.bBoron0p25=Button(self.calibration_FRame,text="0.25",bg="light blue",font="centre 6",fg="red",command=self.b0p25cal)
				self.bBoron0p25.place(x=460, y=330, width=20, height=15)					
				
				self.bBoron0p5=Button(self.calibration_FRame,text="0.5",bg="light blue",font="centre 6",fg="red",command=self.b0p5cal)		
				self.bBoron0p5.place(x=500, y=330, width=20, height=15)					

				self.bBoron1p0=Button(self.calibration_FRame,text="1.0",bg="light blue",font="centre 6",fg="red",command=self.b1p0cal)		
				self.bBoron1p0.place(x=540, y=330, width=20, height=15)	
				
				self.bBoron1p5=Button(self.calibration_FRame,text="1.5",bg="light blue",font="centre 6",fg="red",command=self.b1p5cal)		
				self.bBoron1p5.place(x=580, y=330, width=20, height=15)	
				
				self.bBoron2p0=Button(self.calibration_FRame,text="2.0",bg="light blue",font="centre 6",fg="red",command=self.b2p0cal)		
				self.bBoron2p0.place(x=620, y=330, width=20, height=15)					
				
				self.b_label.place(x=340, y= 330, width=40, height=15)	
				
				self.i_label=Label(self.calibration_FRame,text="Iron",bg="white",fg="#254E58",font="centre  6")						
				
				self.bIron0p0=Button(self.calibration_FRame,text="0.0",bg="light blue",font="centre 6",fg="red",command=self.i0p0cal)		
				self.bIron0p0.place(x=420, y=350, width=20, height=15)	
				
				self.bIron0p5=Button(self.calibration_FRame,text="0.5",bg="light blue",font="centre 6",fg="red",command=self.i0p5cal)		
				self.bIron0p5.place(x=460, y=350, width=20, height=15)					
				
				self.bIron1p0=Button(self.calibration_FRame,text="1.0",bg="light blue",font="centre 6",fg="red",command=self.i1p0cal)		
				self.bIron1p0.place(x=500, y=350, width=20, height=15)					

				self.bIron1p5=Button(self.calibration_FRame,text="1.5",bg="light blue",font="centre 6",fg="red",command=self.i1p5cal)		
				self.bIron1p5.place(x=540, y=350, width=20, height=15)	
				
				self.bIron2p0=Button(self.calibration_FRame,text="2.0",bg="light blue",font="centre 6",fg="red",command=self.i2p0cal)		
				self.bIron2p0.place(x=580, y=350, width=20, height=15)	
				
				self.i_label.place(x=340, y= 350, width=40, height=15)	
				
				'''
				self.oc_label=Label(self.calibration_FRame,text="Organic C",bg="white",fg="#254E58",font="centre  6")
				
				self.boc0p0=Button(self.calibration_FRame,text="0.0",bg="light blue",font="centre 6",fg="red",command=self.oc0p0cal)		
				self.boc0p0.place(x=420, y=370, width=20, height=15)	
				
				self.boc0p25=Button(self.calibration_FRame,text="0.25",bg="light blue",font="centre 6",fg="red",command=self.oc0p25cal)
				self.boc0p25.place(x=460, y=370, width=20, height=15)					
				
				self.boc0p5=Button(self.calibration_FRame,text="0.5",bg="light blue",font="centre 6",fg="red",command=self.oc0p5cal)		
				self.boc0p5.place(x=500, y=370, width=20, height=15)					

				self.boc0p75=Button(self.calibration_FRame,text="0.75",bg="light blue",font="centre 6",fg="red",command=self.oc0p75cal)		
				self.boc0p75.place(x=540, y=370, width=20, height=15)	
				
				self.boc1p0=Button(self.calibration_FRame,text="1.0",bg="light blue",font="centre 6",fg="red",command=self.oc1p0cal)		
				self.boc1p0.place(x=580, y=370, width=20, height=15)	
				
				self.oc_label.place(x=340, y= 370, width=50, height=15)	
				'''
				
				self.bEC['state']=DISABLED
				self.bPH4['state']=DISABLED
				self.bPH7['state']=DISABLED
								
				self.bNitrogen0['state']=DISABLED
				self.bNitrogen5['state']=DISABLED
				self.bNitrogen10['state']=DISABLED	
				self.bNitrogen20['state']=DISABLED
				self.bNitrogen30['state']=DISABLED
				self.bNitrogen40['state']=DISABLED					
				
				self.bPhosphorus0['state']=DISABLED
				self.bPhosphorus5['state']=DISABLED
				self.bPhosphorus10['state']=DISABLED	
				self.bPhosphorus15['state']=DISABLED
				self.bPhosphorus20['state']=DISABLED
				self.bPhosphorus25['state']=DISABLED				
				
				self.bPotassium0['state']=DISABLED
				self.bPotassium10['state']=DISABLED
				self.bPotassium20['state']=DISABLED	
				self.bPotassium40['state']=DISABLED					
				
				self.bBoron0p0['state']=DISABLED
				self.bBoron0p25['state']=DISABLED
				self.bBoron0p5['state']=DISABLED	
				self.bBoron1p0['state']=DISABLED
				self.bBoron1p5['state']=DISABLED
				self.bBoron2p0['state']=DISABLED		
				
				self.bIron0p0['state']=DISABLED
				self.bIron0p5['state']=DISABLED
				self.bIron1p0['state']=DISABLED	
				self.bIron1p5['state']=DISABLED
				self.bIron2p0['state']=DISABLED
				'''
				self.boc0p0['state']=DISABLED
				self.boc0p25['state']=DISABLED
				self.boc0p5['state']=DISABLED	
				self.boc0p75['state']=DISABLED
				self.boc1p0['state']=DISABLED
				'''
				self.ec_status.place(x=420,y=60) 
				
				self.ph4_status.place(x=420,y=85) 
				self.ph7_status.place(x=470,y=85)                           

				self.n0_status.place(x=420,y=110) 
				self.n5_status.place(x=470,y=110) 
				self.n10_status.place(x=520,y=110) 
				self.n20_status.place(x=570,y=110) 
				self.n30_status.place(x=620,y=110) 
				self.n40_status.place(x=670,y=110)
				
				self.p0_status.place(x=420,y=135) 
				self.p5_status.place(x=470,y=135) 
				self.p10_status.place(x=520,y=135) 
				self.p15_status.place(x=570,y=135) 
				self.p20_status.place(x=620,y=135) 
				self.p25_status.place(x=670,y=135)
				
				self.k0_status.place(x=420,y=160) 
				self.k10_status.place(x=470,y=160) 
				self.k20_status.place(x=520,y=160) 
				self.k40_status.place(x=570,y=160) 
				
				print ("done till k ")
				self.b0p0_status.place(x=420,y=185)
				self.b0p25_status.place(x=470,y=185)
				self.b0p5_status.place(x=520,y=185)
				self.b1p0_status.place(x=570,y=185)
				self.b1p5_status.place(x=620,y=185)
				self.b2p0_status.place(x=670,y=185)
				
				print ("done till z ")
				
				self.i0p0_status.place(x=420,y=210)
				self.i0p5_status.place(x=470,y=210)
				self.i1p0_status.place(x=520,y=210)
				self.i1p5_status.place(x=570,y=210)
				self.i2p0_status.place(x=620,y=210)
				'''
				self.oc0p0_status.place(x=420,y=235)
				self.oc0p25_status.place(x=470,y=235)
				self.oc0p5_status.place(x=520,y=235)
				self.oc0p75_status.place(x=570,y=235)
				self.oc1p0_status.place(x=620,y=235)
				'''
				print ("done till c ")
				#self.root.mainloop()    #removing this check
			except Exception as e:
				errorstring = "/E-Calibration()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
						 
		def servicetest_instructions(self):
			try:
				self.bconfirm_service['state']=DISABLED
				self.machine_status_label.configure(text = "")						

				servicetest_lst_values = [self.servicetest_listboxx.get(idx) for idx in self.servicetest_listboxx.curselection()] 
				
				if servicetest_lst_values[0]=="P1-FSS":
					pumpnotosend = "01"
				if servicetest_lst_values[0]=="P2-K-A":
					pumpnotosend = "02"
				if servicetest_lst_values[0]=="P3-K-B":
					pumpnotosend = "03"
				if servicetest_lst_values[0]=="P4-DW":
					pumpnotosend = "04"	
				if servicetest_lst_values[0]=="P5-P":
					pumpnotosend = "05"
				if servicetest_lst_values[0]=="P6-B-A":
					pumpnotosend = "06"
				if servicetest_lst_values[0]=="P7-SW":
					pumpnotosend = "07"
				if servicetest_lst_values[0]=="P8-B-B":
					pumpnotosend = "08"		
				if servicetest_lst_values[0]=="P9-ES":
					external_pumpnotosend = "09"
				if servicetest_lst_values[0]=="P10-DWTop":
					external_pumpnotosend = "10"
				if servicetest_lst_values[0]=="P11-I-A":
					pumpnotosend = "11"		
				if servicetest_lst_values[0]=="P12-I-B":
					pumpnotosend = "12"	
				if servicetest_lst_values[0]=="P13-N-A":
					pumpnotosend = "13"		
				if servicetest_lst_values[0]=="P14-N-B":
					pumpnotosend = "14"		
				
				dorml_lst_values = [self.dorml_listboxx.get(idx) for idx in self.dorml_listboxx.curselection()] 

				quantity_lst_values = [self.quantity_listboxx.get(idx) for idx in self.quantity_listboxx.curselection()] 
				
				if dorml_lst_values[0] == "d":
					if quantity_lst_values[0]=="01":
						tinterval_to_send = 2
					if quantity_lst_values[0]=="02":
						tinterval_to_send = 4
					if quantity_lst_values[0]=="03":
						tinterval_to_send = 6
					if quantity_lst_values[0]=="04":
						tinterval_to_send = 8	
					if quantity_lst_values[0]=="05":
						tinterval_to_send = 10
					if quantity_lst_values[0]=="06":
						tinterval_to_send = 12
					if quantity_lst_values[0]=="07":
						tinterval_to_send = 14
					if quantity_lst_values[0]=="08":
						tinterval_to_send = 16		
					if quantity_lst_values[0]=="09":
						tinterval_to_send = 18
					if quantity_lst_values[0]=="10":
						tinterval_to_send = 20
					if quantity_lst_values[0]=="11":
						tinterval_to_send = 22
					if quantity_lst_values[0]=="12":
						tinterval_to_send = 24	
					if quantity_lst_values[0]=="13":
						tinterval_to_send = 26
					if quantity_lst_values[0]=="14":
						tinterval_to_send = 28
					if quantity_lst_values[0]=="15":
						tinterval_to_send = 30
					dormltosend = "D"																	
				if dorml_lst_values[0] == "ml":
					if quantity_lst_values[0]=="01":
						tinterval_to_send = 2
					if quantity_lst_values[0]=="02":
						tinterval_to_send = 4
					if quantity_lst_values[0]=="03":
						tinterval_to_send = 6
					if quantity_lst_values[0]=="04":
						tinterval_to_send = 8	
					if quantity_lst_values[0]=="05":
						tinterval_to_send = 10
					if quantity_lst_values[0]=="06":
						tinterval_to_send = 12
					if quantity_lst_values[0]=="07":
						tinterval_to_send = 14
					if quantity_lst_values[0]=="08":
						tinterval_to_send = 16		
					if quantity_lst_values[0]=="09":
						tinterval_to_send = 18
					if quantity_lst_values[0]=="10":
						tinterval_to_send = 20
					if quantity_lst_values[0]=="11":
						tinterval_to_send = 22
					if quantity_lst_values[0]=="12":
						tinterval_to_send = 24	
					if quantity_lst_values[0]=="13":
						tinterval_to_send = 26
					if quantity_lst_values[0]=="14":
						tinterval_to_send = 28
					if quantity_lst_values[0]=="15":
						tinterval_to_send = 30
					if quantity_lst_values[0]=="16":
						tinterval_to_send = 32
					if quantity_lst_values[0]=="17":
						tinterval_to_send = 34
					if quantity_lst_values[0]=="18":
						tinterval_to_send = 36
					if quantity_lst_values[0]=="19":
						tinterval_to_send = 38	
					if quantity_lst_values[0]=="20":
						tinterval_to_send = 40
					if quantity_lst_values[0]=="21":
						tinterval_to_send = 42
					if quantity_lst_values[0]=="22":
						tinterval_to_send = 44
					if quantity_lst_values[0]=="23":
						tinterval_to_send = 46		
					if quantity_lst_values[0]=="24":
						tinterval_to_send = 48
					if quantity_lst_values[0]=="25":
						tinterval_to_send = 50
					if quantity_lst_values[0]=="26":
						tinterval_to_send = 52
					if quantity_lst_values[0]=="27":
						tinterval_to_send = 54	
					if quantity_lst_values[0]=="28":
						tinterval_to_send = 56
					if quantity_lst_values[0]=="29":
						tinterval_to_send = 58
					if quantity_lst_values[0]=="30":
						tinterval_to_send = 60	
					dormltosend = "M"	
					
				if servicetest_lst_values[0]=="P1-FSS":
					self.kt_sendcommand("KT+MOVSERVO1:07\r\n",2,10)
				if servicetest_lst_values[0]=="P2-K-A":
					self.kt_sendcommand("KT+MOVSERVO1:07\r\n",2,10)
				if servicetest_lst_values[0]=="P3-K-B":
					self.kt_sendcommand("KT+MOVSERVO1:08\r\n",2,10)
				if servicetest_lst_values[0]=="P4-DW":
					self.kt_sendcommand("KT+MOVSERVO1:08\r\n",2,10)
				if servicetest_lst_values[0]=="P5-P":
					self.kt_sendcommand("KT+MOVSERVO1:09\r\n",2,10)
				if servicetest_lst_values[0]=="P6-B-A":
					self.kt_sendcommand("KT+MOVSERVO1:03\r\n",2,10)
				if servicetest_lst_values[0]=="P8-B-B":
					self.kt_sendcommand("KT+MOVSERVO1:03\r\n",2,10)		
				if servicetest_lst_values[0]=="P11-I-A":
					self.kt_sendcommand("KT+MOVSERVO1:04\r\n",2,10)
				if servicetest_lst_values[0]=="P12-I-B":
					self.kt_sendcommand("KT+MOVSERVO1:04\r\n",2,10)		
				if servicetest_lst_values[0]=="P13-N-A":
					self.kt_sendcommand("KT+MOVSERVO1:04\r\n",2,10)
				if servicetest_lst_values[0]=="P14-N-B":
					self.kt_sendcommand("KT+MOVSERVO1:04\r\n",2,10)											
										
				if servicetest_lst_values[0]=="P9-ES" or servicetest_lst_values[0]=="P10-DWTop":
					texttosend="KT+EXTDISPENSE" + dormltosend + ":"+ external_pumpnotosend + "+" + quantity_lst_values[0] + "\r\n"
					dispense_ret_val = self.kt_send_external_command(texttosend,tinterval_to_send,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_service['state']=NORMAL							
				else:
					texttosend="KT+DISPENSE" + dormltosend + ":"+ pumpnotosend + "+" + quantity_lst_values[0] + "\r\n"
					dispense_ret_val = self.kt_sendcommand(texttosend,tinterval_to_send,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_service['state']=NORMAL
			except Exception as e:
				errorstring = "/E-servicetest instruction()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				self.bconfirm_service['state']=NORMAL			
				pass      
						
		def servo_motor_test(self):
			try:
				self.ecorphvaluelabel.configure(text = "")

				self.machine_status_label.configure(text = "")
				servo_motor_test_lst_values = [self.servo_listboxx.get(idx) for idx in self.servo_listboxx.curselection()] 
				
				if servo_motor_test_lst_values[0]=="Servo-M":
					servonotosend = "1"
																											
				servo_pos_lst_values = [self.servo_pos_listboxx.get(idx) for idx in self.servo_pos_listboxx.curselection()] 
				
				if servo_pos_lst_values[0]=="ON":
					texttosend = "KT+LEDON"+"\r\n"
					self.kt_sendcommand(texttosend,0,10)								
				if servo_pos_lst_values[0]=="OFF":
					texttosend = "KT+LEDOFF"+"\r\n"
					self.kt_sendcommand(texttosend,0,10)
				if servo_pos_lst_values[0]=="01":
					servo_pos_to_send = "01"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)							
				if servo_pos_lst_values[0]=="02":
					servo_pos_to_send = "02"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)							
				if servo_pos_lst_values[0]=="03":
					servo_pos_to_send = "03"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)							
				if servo_pos_lst_values[0]=="04":
					servo_pos_to_send = "04"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)							
				if servo_pos_lst_values[0]=="05":
					servo_pos_to_send = "05"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)							
				if servo_pos_lst_values[0]=="06":
					servo_pos_to_send = "06"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)							
				if servo_pos_lst_values[0]=="07":
					servo_pos_to_send = "07"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)							
				if servo_pos_lst_values[0]=="08":
					servo_pos_to_send = "08"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)							
				if servo_pos_lst_values[0]=="09":
					servo_pos_to_send = "09"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)							
				if servo_pos_lst_values[0]=="10":
					servo_pos_to_send = "10"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)							
				if servo_pos_lst_values[0]=="11":
					servo_pos_to_send = "11"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)							
				if servo_pos_lst_values[0]=="12":
					servo_pos_to_send = "12"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)							
				if servo_pos_lst_values[0]=="13":
					servo_pos_to_send = "13"
					texttosend = "KT+MOVSERVO" + servonotosend +":" + servo_pos_to_send + "\r\n"
					self.kt_sendcommand(texttosend,0,10)
				if servo_pos_lst_values[0]=="CAM-ON":
					texttosend = "KT+LEDON"+"\r\n"
					self.kt_sendcommand(texttosend,0,10)	
					time.sleep(2)					
					camera = picamera.PiCamera()
					time.sleep(1)
					camera.start_preview()
					time.sleep(5)
					camera.stop_preview()
					texttosend = "KT+LEDOFF"+"\r\n"
					self.kt_sendcommand(texttosend,0,10)							
					camera.close()	
				if servo_pos_lst_values[0]=="EC":
					texttosend = "KT+STARTEC\r\n"
					startec_ret_val = self.kt_sendcommand(texttosend,15,10)		
					if 	startec_ret_val == "SUCCESS":					
						time.sleep(2)
						texttosend = "KT+READEC\r\n"
						readec_ret_val = self.kt_sendcommand(texttosend,5,10)
					else:
						readec_ret_val = "ERROR"
					readec_ret_val = "EC: " + readec_ret_val	
					self.ecorphvaluelabel.configure(text = readec_ret_val)	
				if servo_pos_lst_values[0]=="PH":
					texttosend = "KT+STARTPH\r\n"
					startph_ret_val = self.kt_sendcommand(texttosend,60,10)		
					if 	startph_ret_val == "SUCCESS":					
						time.sleep(2)
						texttosend = "KT+READPH\r\n"
						readph_ret_val = self.kt_sendcommand(texttosend,5,10)
					else:
						readph_ret_val = "ERROR"	
					readph_ret_val = "PH: " + readph_ret_val
					self.ecorphvaluelabel.configure(text = readph_ret_val)	
			except Exception as e:
				errorstring = "/E-servo_motor_test()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				
		def incconstant(self):
			try:
				self.machine_status_label.configure(text = "")
				inc_status_flag = 0
				with open(self.image_path+"pump_servo_constants.json","r+") as e:
					a=json.load(e)					    		

				obj=a
				
				for key1, value1 in obj.items():
					for key2, value2 in value1.items():
						floatvalue2 = float(value2)
						if key1 == "D" and floatvalue2 > 3.0:
							 messagebox.showerror("Value Error !!!", "D - Value cannot be more than 3")
							 inc_status_flag = 1
							 break
						if key1 == "M" and floatvalue2 > 3.0:
							 messagebox.showerror("Value Error !!!", "ML - Value cannot be more than 3")
							 inc_status_flag = 1
							 break	
						if key1 == "Servo1" and floatvalue2 > 150:
							 messagebox.showerror("Value Error !!!", "Servo - Value cannot be more than 150")
							 inc_status_flag = 1
							 break	
				
				if inc_status_flag == 0:
					incdec_servicetest_values = [self.incdec_servicetest_listboxx.get(idx) for idx in self.incdec_servicetest_listboxx.curselection()]
						
					if incdec_servicetest_values[0]=="P1-FSS":
						pumpnotosend = "01"
					if incdec_servicetest_values[0]=="P2-K-A":
						pumpnotosend = "02"
					if incdec_servicetest_values[0]=="P3-K-B":
						pumpnotosend = "03"
					if incdec_servicetest_values[0]=="P4-DW":
						pumpnotosend = "04"	
					if incdec_servicetest_values[0]=="P5-P":
						pumpnotosend = "05"
					if incdec_servicetest_values[0]=="P6-B-A":
						pumpnotosend = "06"
					if incdec_servicetest_values[0]=="P7-SW":
						pumpnotosend = "07"
					if incdec_servicetest_values[0]=="P8-B-B":
						pumpnotosend = "08"		
					if incdec_servicetest_values[0]=="P9-ES":
						pumpnotosend = "09"
					if incdec_servicetest_values[0]=="P10-DWTop":
						pumpnotosend = "10"
					if incdec_servicetest_values[0]=="P11-I-A":
						pumpnotosend = "11"
					if incdec_servicetest_values[0]=="P12-I-B":
						pumpnotosend = "12"
					if incdec_servicetest_values[0]=="P13-N-A":
						pumpnotosend = "13"
					if incdec_servicetest_values[0]=="P14-N-B":
						pumpnotosend = "14"						

					if incdec_servicetest_values[0]=="Servo1":
						pumpnotosend = "1"
		
					self.incdec_dorml_values = [self.incdec_dorml_listboxx.get(idx) for idx in self.incdec_dorml_listboxx.curselection()]	
			
					if self.incdec_dorml_values[0]=="d":
						dormltosend = "D"
					if self.incdec_dorml_values[0]=="ml":
						dormltosend = "M"
					if self.incdec_dorml_values[0]=="1":
						dormltosend = "01"
					if self.incdec_dorml_values[0]=="2":
						dormltosend = "02"
					if self.incdec_dorml_values[0]=="3":
						dormltosend = "03"
					if self.incdec_dorml_values[0]=="4":
						dormltosend = "04"
					if self.incdec_dorml_values[0]=="5":
						dormltosend = "05"
					if self.incdec_dorml_values[0]=="6":
						dormltosend = "06"
					if self.incdec_dorml_values[0]=="7":
						dormltosend = "07"
					if self.incdec_dorml_values[0]=="8":
						dormltosend = "08"
					if self.incdec_dorml_values[0]=="9":
						dormltosend = "09"	
					if self.incdec_dorml_values[0]=="10":
						dormltosend = "10"	
					if self.incdec_dorml_values[0]=="11":
						dormltosend = "11"	
					if self.incdec_dorml_values[0]=="12":
						dormltosend = "12"	
					if self.incdec_dorml_values[0]=="13":
						dormltosend = "13"
			
					if incdec_servicetest_values[0]=="Servo1":	
						inc_texttosend = "KT+INCRSERVO" + pumpnotosend +"C" +":"+ dormltosend + "\r\n"
					else:
						inc_texttosend = "KT+INCRC" + dormltosend +":"+ pumpnotosend + "\r\n"	

					self.kt_sendcommand(inc_texttosend,0,10)
					if incdec_servicetest_values[0]=="Servo1":
						read_servo_const_inside_incconstant = "KT+READSERVO" + pumpnotosend +"C:" + dormltosend + "\r\n"

						read_inc_const_value = self.kt_sendcommand(read_servo_const_inside_incconstant, 0,10)
						read_inc_const_split_value = read_inc_const_value.split("+")

						if self.incdec_dorml_values[0]=="1":
							self.servoconstlabel1.configure(text = read_inc_const_split_value[1])
						if self.incdec_dorml_values[0]=="2":
							self.servoconstlabel2.configure(text = read_inc_const_split_value[1])
						if self.incdec_dorml_values[0]=="3":
							self.servoconstlabel3.configure(text = read_inc_const_split_value[1])
						if self.incdec_dorml_values[0]=="4":
							self.servoconstlabel4.configure(text = read_inc_const_split_value[1])
						if self.incdec_dorml_values[0]=="5":
							self.servoconstlabel5.configure(text = read_inc_const_split_value[1])
						if self.incdec_dorml_values[0]=="6":
							self.servoconstlabel6.configure(text = read_inc_const_split_value[1])
						if self.incdec_dorml_values[0]=="7":
							self.servoconstlabel7.configure(text = read_inc_const_split_value[1])			
						if self.incdec_dorml_values[0]=="8":
							self.servoconstlabel8.configure(text = read_inc_const_split_value[1])
						if self.incdec_dorml_values[0]=="9":
							self.servoconstlabel9.configure(text = read_inc_const_split_value[1])			
						if self.incdec_dorml_values[0]=="10":
							self.servoconstlabel10.configure(text = read_inc_const_split_value[1])			
						if self.incdec_dorml_values[0]=="11":
							self.servoconstlabel11.configure(text = read_inc_const_split_value[1])			
						if self.incdec_dorml_values[0]=="12":
							self.servoconstlabel12.configure(text = read_inc_const_split_value[1])			
						if self.incdec_dorml_values[0]=="13":
							self.servoconstlabel13.configure(text = read_inc_const_split_value[1])											

						with open(self.image_path+"pump_servo_constants.json","r+") as e:
							a=json.load(e)	
				
						a['Servo1'][dormltosend] = read_inc_const_split_value[1].rstrip()
				
						obj=a

						with open(self.image_path+"pump_servo_constants.json","w")as e:
							json.dump(obj,e)
					else:
						read_inc_const = "KT+READPUMPC" + dormltosend + ":" + pumpnotosend + "\r\n"
						read_inc_const_value = self.kt_sendcommand(read_inc_const, 0,10)
						read_inc_const_split_value = read_inc_const_value.split("+")	
						if incdec_servicetest_values[0]=="P1-FSS":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel1.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel1.configure(text = read_inc_const_split_value[1])
						if incdec_servicetest_values[0]=="P2-K-A":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel2.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel2.configure(text = read_inc_const_split_value[1])								
						if incdec_servicetest_values[0]=="P3-K-B":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel3.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel3.configure(text = read_inc_const_split_value[1])
						if incdec_servicetest_values[0]=="P4-DW":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel4.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel4.configure(text = read_inc_const_split_value[1])
						if incdec_servicetest_values[0]=="P5-P":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel5.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel5.configure(text = read_inc_const_split_value[1])
						if incdec_servicetest_values[0]=="P6-B-A":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel6.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel6.configure(text = read_inc_const_split_value[1])
						if incdec_servicetest_values[0]=="P7-SW":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel7.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel7.configure(text = read_inc_const_split_value[1])
						if incdec_servicetest_values[0]=="P8-B-B":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel8.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel8.configure(text = read_inc_const_split_value[1])	
						if incdec_servicetest_values[0]=="P9-ES":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel9.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel9.configure(text = read_inc_const_split_value[1])
						if incdec_servicetest_values[0]=="P10-DWTop":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel10.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel10.configure(text = read_inc_const_split_value[1])
						if incdec_servicetest_values[0]=="P11-I-A":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel11.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel11.configure(text = read_inc_const_split_value[1])
						if incdec_servicetest_values[0]=="P12-I-B":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel12.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel12.configure(text = read_inc_const_split_value[1])
						if incdec_servicetest_values[0]=="P13-N-A":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel13.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel13.configure(text = read_inc_const_split_value[1])
						if incdec_servicetest_values[0]=="P14-N-B":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel14.configure(text = read_inc_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel14.configure(text = read_inc_const_split_value[1])

						with open(self.image_path+"pump_servo_constants.json","r+") as e:
							a=json.load(e)	

						a[dormltosend][pumpnotosend] = read_inc_const_split_value[1].rstrip()
						obj=a

						with open(self.image_path+"pump_servo_constants.json","w")as e:
							json.dump(obj,e)
			except Exception as e:
				errorstring = "/E-inc constant()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
					
		def decconstant(self):
			try:
				self.machine_status_label.configure(text = "")
				dec_status_flag = 0
				with open(self.image_path+"pump_servo_constants.json","r+") as e:
					a=json.load(e)					    		

				obj=a
				
				for key1, value1 in obj.items():
					for key2, value2 in value1.items():
						floatvalue2 = float(value2)
						if key1 == "D" and floatvalue2 < 0.03:
							 messagebox.showerror("Value Error !!!", "D - Value cannot be less than or equal to 0.02")
							 dec_status_flag = 1
							 break
						if key1 == "M" and floatvalue2 < 0.06:
							 messagebox.showerror("Value Error !!!", "ML - Value cannot be less than or equal to 0.05")
							 dec_status_flag = 1
							 break	
						if key1 == "Servo1" and floatvalue2 <  6.0:
							 messagebox.showerror("Value Error !!!", "Servo - Value cannot be less than or equal to 5")
							 dec_status_flag = 1
							 break	
						
				if dec_status_flag == 0:
					incdec_servicetest_values = [self.incdec_servicetest_listboxx.get(idx) for idx in self.incdec_servicetest_listboxx.curselection()]
							
					if incdec_servicetest_values[0]=="P1-FSS":
						pumpnotosend = "01"
					if incdec_servicetest_values[0]=="P2-K-A":
						pumpnotosend = "02"
					if incdec_servicetest_values[0]=="P3-K-B":
						pumpnotosend = "03"
					if incdec_servicetest_values[0]=="P4-DW":
						pumpnotosend = "04"	
					if incdec_servicetest_values[0]=="P5-P":
						pumpnotosend = "05"
					if incdec_servicetest_values[0]=="P6-B-A":
						pumpnotosend = "06"
					if incdec_servicetest_values[0]=="P7-SW":
						pumpnotosend = "07"
					if incdec_servicetest_values[0]=="P8-B-B":
						pumpnotosend = "08"		
					if incdec_servicetest_values[0]=="P9-ES":
						pumpnotosend = "09"
					if incdec_servicetest_values[0]=="P10-DWTop":
						pumpnotosend = "10"
					if incdec_servicetest_values[0]=="P11-I-A":
						pumpnotosend = "11"
					if incdec_servicetest_values[0]=="P12-I-B":
						pumpnotosend = "12"
					if incdec_servicetest_values[0]=="P13-N-A":
						pumpnotosend = "13"
					if incdec_servicetest_values[0]=="P14-N-B":
						pumpnotosend = "14"							

					if incdec_servicetest_values[0]=="Servo1":
						pumpnotosend = "1"											
			
					self.incdec_dorml_values = [self.incdec_dorml_listboxx.get(idx) for idx in self.incdec_dorml_listboxx.curselection()]
				
					if self.incdec_dorml_values[0]=="d":
						dormltosend = "D"
					if self.incdec_dorml_values[0]=="ml":
						dormltosend = "M"
					if self.incdec_dorml_values[0]=="1":
						dormltosend = "01"
					if self.incdec_dorml_values[0]=="2":
						dormltosend = "02"
					if self.incdec_dorml_values[0]=="3":
						dormltosend = "03"
					if self.incdec_dorml_values[0]=="4":
						dormltosend = "04"
					if self.incdec_dorml_values[0]=="5":
						dormltosend = "05"
					if self.incdec_dorml_values[0]=="6":
						dormltosend = "06"
					if self.incdec_dorml_values[0]=="7":
						dormltosend = "07"
					if self.incdec_dorml_values[0]=="8":
						dormltosend = "08"
					if self.incdec_dorml_values[0]=="9":
						dormltosend = "09"
					if self.incdec_dorml_values[0]=="10":
						dormltosend = "10"
					if self.incdec_dorml_values[0]=="11":
						dormltosend = "11"
					if self.incdec_dorml_values[0]=="12":
						dormltosend = "12"
					if self.incdec_dorml_values[0]=="13":
						dormltosend = "13"
					
					if incdec_servicetest_values[0]=="Servo1":	
						dec_texttosend = "KT+DECRSERVO" + pumpnotosend +"C" +":"+ dormltosend + "\r\n"
					else:
						dec_texttosend = "KT+DECRC" + dormltosend +":"+ pumpnotosend + "\r\n"	

					self.kt_sendcommand(dec_texttosend,0,10)						
				
					if incdec_servicetest_values[0]=="Servo1":
						read_servo_const_inside_decconstant = "KT+READSERVO" + pumpnotosend +"C:" + dormltosend + "\r\n"
						read_dec_const_value = self.kt_sendcommand(read_servo_const_inside_decconstant, 0,10)

						read_dec_const_split_value = read_dec_const_value.split("+")
						if self.incdec_dorml_values[0]=="1":
							self.servoconstlabel1.configure(text = read_dec_const_split_value[1])
						if self.incdec_dorml_values[0]=="2":
							self.servoconstlabel2.configure(text = read_dec_const_split_value[1])
						if self.incdec_dorml_values[0]=="3":
							self.servoconstlabel3.configure(text = read_dec_const_split_value[1])
						if self.incdec_dorml_values[0]=="4":
							self.servoconstlabel4.configure(text = read_dec_const_split_value[1])
						if self.incdec_dorml_values[0]=="5":
							self.servoconstlabel5.configure(text = read_dec_const_split_value[1])
						if self.incdec_dorml_values[0]=="6":
							self.servoconstlabel6.configure(text = read_dec_const_split_value[1])
						if self.incdec_dorml_values[0]=="7":
							self.servoconstlabel7.configure(text = read_dec_const_split_value[1])							
						if self.incdec_dorml_values[0]=="8":
							self.servoconstlabel8.configure(text = read_dec_const_split_value[1])
						if self.incdec_dorml_values[0]=="9":
							self.servoconstlabel9.configure(text = read_dec_const_split_value[1])							
						if self.incdec_dorml_values[0]=="10":
							self.servoconstlabel10.configure(text = read_dec_const_split_value[1])							
						if self.incdec_dorml_values[0]=="11":
							self.servoconstlabel11.configure(text = read_dec_const_split_value[1])							
						if self.incdec_dorml_values[0]=="12":
							self.servoconstlabel12.configure(text = read_dec_const_split_value[1])							
						if self.incdec_dorml_values[0]=="13":
							self.servoconstlabel13.configure(text = read_dec_const_split_value[1])	
						
						with open(self.image_path+"pump_servo_constants.json","r+") as e:
							a=json.load(e)	
				
						a['Servo1'][dormltosend] = read_dec_const_split_value[1].rstrip()
					
						obj=a

						with open(self.image_path+"pump_servo_constants.json","w")as e:
							json.dump(obj,e)
					else:
						read_dec_const = "KT+READPUMPC" + dormltosend + ":" + pumpnotosend + "\r\n"
						read_dec_const_value = self.kt_sendcommand(read_dec_const, 0,10)
					
						read_dec_const_split_value = read_dec_const_value.split("+")	
					
						if incdec_servicetest_values[0]=="P1-FSS":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel1.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel1.configure(text = read_dec_const_split_value[1])
						if incdec_servicetest_values[0]=="P2-K-A":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel2.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel2.configure(text = read_dec_const_split_value[1])								
						if incdec_servicetest_values[0]=="P3-K-B":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel3.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel3.configure(text = read_dec_const_split_value[1])
						if incdec_servicetest_values[0]=="P4-DW":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel4.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel4.configure(text = read_dec_const_split_value[1])
						if incdec_servicetest_values[0]=="P5-P":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel5.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel5.configure(text = read_dec_const_split_value[1])
						if incdec_servicetest_values[0]=="P6-B-A":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel6.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel6.configure(text = read_dec_const_split_value[1])
						if incdec_servicetest_values[0]=="P7-SW":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel7.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel7.configure(text = read_dec_const_split_value[1])
						if incdec_servicetest_values[0]=="P8-B-B":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel8.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel8.configure(text = read_dec_const_split_value[1])	
						if incdec_servicetest_values[0]=="P9-ES":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel9.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel9.configure(text = read_dec_const_split_value[1])
						if incdec_servicetest_values[0]=="P10-DWTop":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel10.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel10.configure(text = read_dec_const_split_value[1])
						if incdec_servicetest_values[0]=="P11-I-A":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel11.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel11.configure(text = read_dec_const_split_value[1])
						if incdec_servicetest_values[0]=="P12-I-B":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel12.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel12.configure(text = read_dec_const_split_value[1])
						if incdec_servicetest_values[0]=="P13-N-A":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel13.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel13.configure(text = read_dec_const_split_value[1])
						if incdec_servicetest_values[0]=="P14-N-B":
							if self.incdec_dorml_values[0]=="d":
								self.dpumpconstlabel14.configure(text = read_dec_const_split_value[1])
							if self.incdec_dorml_values[0]=="ml":
								self.mlpumpconstlabel14.configure(text = read_dec_const_split_value[1])								
							
						with open(self.image_path+"pump_servo_constants.json","r+") as e:
							a=json.load(e)	
				
						a[dormltosend][pumpnotosend] = read_dec_const_split_value[1].rstrip()
					
						obj=a

						with open(self.image_path+"pump_servo_constants.json","w")as e:
							json.dump(obj,e)
			except Exception as e:
				errorstring = "/E-dec constant()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass  
												  						                  
		def onselect1(self,event):
			try:
				w = event.widget
				index = w.curselection()[0]
				if index == 0:
				    self.quantity_listboxx.delete('0','end')
				    addlist = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']
				    for item in addlist:
				       self.quantity_listboxx.insert(END, item) 
				    #self.servicestatuslabel['text'] = "Udyavara"
				elif index == 1:
				    self.quantity_listboxx.delete('0','end')  
				    addlist = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
				    for item in addlist:
				       self.quantity_listboxx.insert(END, item)
				    #self.servicestatuslabel['text'] = "udupi" 	
				self.quantity_listboxx.selection_set(0)    	
			except Exception as e:
				errorstring = "/E-onselect1()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				
		def onselect2(self,event):
			logging.info ("onselect2")					
			
		def onselect3(self,event):
			try:
				w = event.widget
				index = w.curselection()[0]

				if index == 0:
				    self.servo_pos_listboxx.delete('0','end')
				    addlist = ['01','02','03','04','05','06','07','08','09','10','11','12','13']
				    for item in addlist:
				       self.servo_pos_listboxx.insert(END, item) 
				    #self.servicestatuslabel['text'] = "Udyavara"
				elif index == 1:
				    self.servo_pos_listboxx.delete('0','end')  
				    addlist = ['ON','OFF']
				    for item in addlist:
				       self.servo_pos_listboxx.insert(END, item)
				    #self.servicestatuslabel['text'] = "udupi" 	
				elif index == 2:
				    self.servo_pos_listboxx.delete('0','end')  
				    addlist = ['CAM-ON']
				    for item in addlist:
				       self.servo_pos_listboxx.insert(END, item)
				    #self.servicestatuslabel['text'] = "udupi" 	
				elif index == 3:
				    self.servo_pos_listboxx.delete('0','end')  
				    addlist = ['EC','PH']
				    for item in addlist:
				       self.servo_pos_listboxx.insert(END, item)
				    #self.servicestatuslabel['text'] = "udupi" 
				    
				self.servo_pos_listboxx.selection_set(0)    	
			except Exception as e:
				errorstring = "/E-onselect3()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 			
			
		def onselect_incdec_servo_constants(self,event):
			try:
				w = event.widget
				index = w.curselection()[0]
				if index == 0:
				    self.incdec_dorml_listboxx.delete('0','end')
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item) 
				    #self.servicestatuslabel['text'] = "1"
				elif index == 1:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				    #self.servicestatuslabel['text'] = "2"
				elif index == 2:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				    #self.servicestatuslabel['text'] = "3"
				elif index == 3:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				    #self.servicestatuslabel['text'] = "4"
				elif index == 4:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				    #self.servicestatuslabel['text'] = "5"	
				elif index == 5:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				    #self.servicestatuslabel['text'] = "6"
				elif index == 6:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				    #self.servicestatuslabel['text'] = "7"	
				elif index == 7:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				    #self.servicestatuslabel['text'] = "8"	
				elif index == 8:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				    #self.servicestatuslabel['text'] = "9"	
				elif index == 9:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				elif index == 10:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				elif index == 11:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				elif index == 12:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				elif index == 13:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['d','ml']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				elif index == 14:
				    self.incdec_dorml_listboxx.delete('0','end')  
				    addlist = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
				    for item in addlist:
				       self.incdec_dorml_listboxx.insert(END, item)
				    			    				    				    	
				self.incdec_dorml_listboxx.selection_set(0)    	
			except Exception as e:
				errorstring = "/E-onselect_inc_dec_servo_constants()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				 
		def download_countdown(self,a):
			try:
				self.machine_status_label.configure(text = "")
				self.dw_timetext.configure(text="30")
				p = 0.00
				t = time.time()
				n = a
				# Loop while the number of seconds is less than the integer defined in "p"
				while p - t < n : 
					p = time.time()
					if p == t + n:
						self.dw_timetext.configure(text="Time's up !!")
					else:    
						time_value = round((t+n) - p) 
						self.dw_timetext.configure(text=time_value)
					time.sleep(0.5)
			except Exception as e:
				errorstring = "/E-download_countdown()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 		
				        
		def dw_countdown_timer(self):
			try:			
				self.download_countdown(90)
			except Exception as e:
				errorstring = "/E-dw_countdown_timer()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass				

		def dw_from_git(self):
			try:
				self.bconfirm_sw["state"] = DISABLED
				self.breturn_from_software_update_to_service["state"] = DISABLED			
				os.chdir(self.firmware_update_path)
				stream=os.popen('git fetch')
				time.sleep(30)
				stream2=os.popen('git log ..origin/master --oneline | wc -l')
				output=int(stream2.read())

				if(output==0):
					time.sleep(60)
					messagebox.showinfo("Software Update !!!", "Latest Software present in the system") 
				else:	
					os.chdir(self.firmware_update_path)
					out=os.popen('git pull origin master')
					self.machine_status_label.configure(text = "Please wait...  System will be rebooted after 60 seconds")
					time.sleep(60)
					os.system("shutdown -r now")
			except Exception as e:
				errorstring = "/E-dw_from_git()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				self.bconfirm_sw["state"] = ACTIVE
				self.breturn_from_software_update_to_service["state"] = ACTIVE
				pass 		    
        
		def update_software_from_internet(self):
			try:	
				self.machine_status_label.configure(text = "Starting software Updating process. Please wait... ")					

				timer_dw_countdown=threading.Timer(0,self.dw_countdown_timer)
				timer_dw_countdown.start()	
				timer_dw_from_git=threading.Timer(0,self.dw_from_git)
				timer_dw_from_git.start()		
			except Exception as e:
				errorstring = "/E-update software from internet()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 										 			
				 
		def software_update(self):
			try:	
				self.machine_status_label.configure(text = "")	
				self.servicetest_FRame.destroy()				
				self.softwareupdate_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				
				dw_Mainlabel=Label(self.softwareupdate_FRame,text="Software Update",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
				
				canvas=Canvas(self.softwareupdate_FRame,bg="#F5F4EB")
				canvas.create_rectangle(5, 5, 745, 215, outline="#fb0",fill="#F5F4EB")	
				canvas.place(x=10,y=50,width=750,height=220)
		
				dw_timecase=Canvas(self.softwareupdate_FRame,bg="#F5F4EB")					
				
				self.dw_timetext=Label(self.softwareupdate_FRame,text="NIL",bg="#F5F4EB",fg="#254E58",font="BOLD  12")
				dw_timecase.create_rectangle(15, 20, 130, 80,outline="#f00",fill="#F5F4EB")
				dw_timecase.place(x=230,y=100,width=150,height=100)
				self.dw_timetext.place(x=280,y=135)									
														
				self.bconfirm_sw=Button(self.softwareupdate_FRame,text="Update",bg="blue",font="centre 8",fg="white",command=self.update_software_from_internet)
				
				self.breturn_from_software_update_to_service=Button(self.softwareupdate_FRame,text="Service Home",bg="blue",font="centre 8",fg="white",command=self.goback_service_from_softwareupdate)					
												
				self.bconfirm_sw.place(x=550,y=300)
				self.breturn_from_software_update_to_service.place(x=650,y=300)
				self.softwareupdate_FRame.place(x=10,y=40,width=780,height=390)	
				
				dw_Mainlabel.place(x=20,y=10)
			except Exception as e:
				messagebox.showerror("Software Update Error !!!", "Error occured while updating software")
				self.front_page()
				errorstring = "/E-software update()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				
		def center(self, win):
			win.update_idletasks()
			width = win.winfo_width()
			frm_width = win.winfo_rootx() - win.winfo_x()
			win_width = width + 2 * frm_width
			height = win.winfo_height()
			titlebar_height = win.winfo_rooty() - win.winfo_y()
			win_height = height + titlebar_height + frm_width
			x = win.winfo_screenwidth() // 2 - win_width // 2
			y = win.winfo_screenheight() // 2 - win_height // 2
			win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
			win.deiconify()				
				
		def logger_log(self):
			try:
				self.machine_status_label.configure(text = "")	
				self.servicetest_FRame.destroy()				
				self.systemlog_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				
				#dw_Mainlabel=Label(self.systemlog_FRame,text="System Log",bg="#F5F4EB",fg="#254E58",font="BOLD  16")
				#dw_Mainlabel.place(x=5,y=5)
				
				self.ret_app = Application(self.systemlog_FRame)
				
				'''
				canvas=Canvas(self.systemlog_FRame,bg="#F5F4EB")
				canvas.create_rectangle(5, 5, 745, 325, outline="#fb0",fill="#F5F4EB")	
				canvas.place(x=10,y=50,width=750,height=330)
				
				self.level = tk.StringVar()
				self.level = 'INFO'
				lvl = getattr(logging, self.level)

				log_file = pathlib.Path(self.logpath + "log")
				if log_file.exists ():					
					readlogfile = open(self.logpath + "log","r+")
					a = readlogfile.read()
				logger.log(lvl, a)				
				
				table = Table(self.systemlog_FRame, ["System Log"], column_minwidths=[740])
				table.place(x=15,y=55,width=740,height=320)
				table.set_data([([a])])  
				'''
		
				self.breturn_from_log_to_service=Button(self.systemlog_FRame,text="Service Home",bg="blue",font="centre 8",fg="white",command=self.goback_service_from_log)					
												
				self.breturn_from_log_to_service.place(x=650,y=0)
				self.systemlog_FRame.place(x=10,y=40,width=780,height=390)	
				
				'''
				self.rt = Tk()
				self.rt.title('Krishi-Rastaa Log')
				self.rt.geometry('600x400')
				self.rt.configure(background="#F5F4EB")
				self.rt.resizable(0,0)
				
				self.center(self.rt)
				
				self.rt.columnconfigure(0, weight=1)
				self.rt.rowconfigure(0, weight=1)

				vertical_pane = ttk.PanedWindow(self.rt, orient=VERTICAL)
				vertical_pane.grid(row=0, column=0, sticky="nsew")
				horizontal_pane = ttk.PanedWindow(vertical_pane, orient=HORIZONTAL)
				vertical_pane.add(horizontal_pane)
				console_frame = ttk.Labelframe(horizontal_pane, text="Console")
				console_frame.columnconfigure(0, weight=1)
				console_frame.rowconfigure(0, weight=1)
				horizontal_pane.add(console_frame, weight=1)

				self.console = ConsoleUi(console_frame)

				self.level = tk.StringVar()
				self.level = 'INFO'
				lvl = getattr(logging, self.level)

				log_file = pathlib.Path(self.logpath + "log")
				if log_file.exists ():					
					readlogfile = open(self.logpath + "log","r+")
					a = readlogfile.read()
				logger.log(lvl, a)

				self.rt.protocol('WM_DELETE_WINDOW', self.quit)
				self.rt.bind('<Control-q>', self.quit)
				signal.signal(signal.SIGINT, self.quit)
				'''
								
			except Exception as e:
				messagebox.showerror("Software Update Error !!!", "Error occured while logging")
				#self.front_page()
				errorstring = "/E-system log()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				
		'''
		def quit(self, *args):
		    self.rt.destroy()					
		'''
				
		def goback_service_from_cameratest(self):
			try:
				self.count_pixel = 0
				self.servicetest()
			except Exception as e:
				errorstring = "/E-goback service from cameratest()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 	
				    
		def set_pixel_default(self):
			try:
				file = pathlib.Path(self.image_path+"fipcs.json")
				if file.exists ():					
					with open(self.image_path+"fipcs.json","r+") as e:
						a=json.load(e)					    		
						
					obj=a

					with open(self.image_path+"ipcs.json","w")as e:
						json.dump(obj,e)
					
					with open(self.image_path+"ipcs.json","r+") as e:
						a=json.load(e)

					messagebox.showinfo("Default", "Default Pixel values Set. Page will be redirected to service test page")
					self.count_pixel = 0
					self.servicetest()
				else:
					dictionary = ({
						"1": {"topx": 364, "topy": 246, "botx": 374, "boty": 256}, 
						"2": {"topx": 385, "topy": 180, "botx": 395, "boty": 190}, 
						"3": {"topx": 446, "topy": 235, "botx": 456, "boty": 245}, 
						"4": {"topx": 425, "topy": 257, "botx": 435, "boty": 267}, 
						"5": {"topx": 374, "topy": 202, "botx": 384, "boty": 212} 
					})
													
					with open(self.image_path+"fipcs.json","w")as e:
						json.dump(dictionary,e)
						
					with open(self.image_path+"ipcs.json","w") as e:
						json.dump(dictionary,e)
														
			except Exception as e:
				errorstring = "/E-set pixel default()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 		
						    					
		def set_pixel_info(self):
			try:		
				with open(self.image_path+"ipcs.json","r+") as e:
					a=json.load(e)					    		
				
					a.update({
						"1": {"topx": self.topx1  / self.npwpercent, "topy": self.topy1  / self.npwpercent, "botx": self.botx1  / self.npwpercent, "boty": self.boty1  / self.npwpercent}, 
						"2": {"topx": self.topx2  / self.npwpercent, "topy": self.topy2  / self.npwpercent, "botx": self.botx2  / self.npwpercent, "boty": self.boty2  / self.npwpercent}, 
						"3": {"topx": self.topx3  / self.npwpercent, "topy": self.topy3  / self.npwpercent, "botx": self.botx3  / self.npwpercent, "boty": self.boty3  / self.npwpercent}, 
						"4": {"topx": self.topx4  / self.npwpercent, "topy": self.topy4  / self.npwpercent, "botx": self.botx4  / self.npwpercent, "boty": self.boty4  / self.npwpercent}, 
						"5": {"topx": self.topx5  / self.npwpercent, "topy": self.topy5  / self.npwpercent, "botx": self.botx5  / self.npwpercent, "boty": self.boty5  / self.npwpercent} 
					})						
								
				obj=a

				with open(self.image_path+"ipcs.json","w")as e:
					json.dump(obj,e)
				with open(self.image_path+"ipcs.json","r+") as e:
					a=json.load(e)

				messagebox.showinfo("Set Pixel", "Selected Pixel values will be Used for future use. Page will be redirected to service test page")
				self.count_pixel = 0
				self.servicetest()					
			except Exception as e:
				errorstring = "/E-set pixel info()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
					
		def k_goback_service_from_cameratest(self):
			try:
				self.count_pixel = 0
				self.servicetest()
			except Exception as e:
				errorstring = "/E-k_goback_service_from_cameratest()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 	
				    
		def k_set_pixel_default(self):
			try:
				file = pathlib.Path(self.image_path+"kfipcs.json")
				if file.exists ():					
					with open(self.image_path+"kfipcs.json","r+") as e:
						a=json.load(e)					    		
						
					obj=a

					with open(self.image_path+"kipcs.json","w")as e:
						json.dump(obj,e)
					
					with open(self.image_path+"kipcs.json","r+") as e:
						a=json.load(e)

					messagebox.showinfo("Default", "Default Pixel values Set. Page will be redirected to service test page")
					self.count_pixel = 0
					self.servicetest()	
				else:
					dictionary = ({
						"1": {"topx": 364, "topy": 246, "botx": 374, "boty": 256}, 
						"2": {"topx": 385, "topy": 180, "botx": 395, "boty": 190}, 
						"3": {"topx": 446, "topy": 235, "botx": 456, "boty": 245}, 
						"4": {"topx": 425, "topy": 257, "botx": 435, "boty": 267}, 
						"5": {"topx": 374, "topy": 202, "botx": 384, "boty": 212} 
					})
													
					with open(self.image_path+"kfipcs.json","w")as e:
						json.dump(dictionary,e)
						
					with open(self.image_path+"kipcs.json","w") as e:
						json.dump(dictionary,e)
						
					messagebox.showinfo("Default", "Default Pixel values Set. Page will be redirected to service test page")
					self.count_pixel = 0
					self.servicetest()	
								
			except Exception as e:
				errorstring = "/E-ksetpixel_default()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 		
						    					
		def k_set_pixel_info(self):
			try:
				file = pathlib.Path(self.image_path+"kipcs.json")
				if file.exists ():						
					with open(self.image_path+"kipcs.json","r+") as e:
						a=json.load(e)					    		
						
					a.update({
						"1": {"topx": self.topx1  / self.kwpercent, "topy": self.topy1  / self.kwpercent, "botx": self.botx1  / self.kwpercent, "boty": self.boty1  / self.kwpercent}, 
						"2": {"topx": self.topx2  / self.kwpercent, "topy": self.topy2  / self.kwpercent, "botx": self.botx2  / self.kwpercent, "boty": self.boty2  / self.kwpercent}, 
						"3": {"topx": self.topx3  / self.kwpercent, "topy": self.topy3  / self.kwpercent, "botx": self.botx3  / self.kwpercent, "boty": self.boty3  / self.kwpercent}, 
						"4": {"topx": self.topx4  / self.kwpercent, "topy": self.topy4  / self.kwpercent, "botx": self.botx4  / self.kwpercent, "boty": self.boty4  / self.kwpercent}, 
						"5": {"topx": self.topx5  / self.kwpercent, "topy": self.topy5  / self.kwpercent, "botx": self.botx5  / self.kwpercent, "boty": self.boty5  / self.kwpercent} 
					})								
					obj=a

					with open(self.image_path+"kipcs.json","w")as e:
						json.dump(obj,e)
					with open(self.image_path+"kipcs.json","r+") as e:
						a=json.load(e)

					messagebox.showinfo("Set Pixel", "Selected Pixel values will be Used for future use. Page will be redirected to service test page")
					self.count_pixel = 0
					self.servicetest()
				else:
					dictionary = ({
						"1": {"topx": 364, "topy": 246, "botx": 374, "boty": 256}, 
						"2": {"topx": 385, "topy": 180, "botx": 395, "boty": 190}, 
						"3": {"topx": 446, "topy": 235, "botx": 456, "boty": 245}, 
						"4": {"topx": 425, "topy": 257, "botx": 435, "boty": 267}, 
						"5": {"topx": 374, "topy": 202, "botx": 384, "boty": 212} 
					})
													
					with open(self.image_path+"kipcs.json","w")as e:
						json.dump(dictionary,e)
						
					messagebox.showinfo("Default", "initial Pixel values Set. Page will be redirected to service test page")
					self.count_pixel = 0
					self.servicetest()									
			except Exception as e:
				errorstring = "/E-k_set_pixel_info()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
					
		def get_mouse_posn(self,event):
			try:	
				if self.count_pixel == 0:
					pic1 = Image.open(self.image_path+"select_pixel.png")
					self.topx1, self.topy1 = event.x, event.y

					self.botx1, self.boty1 = self.topx1+10, self.topy1+10
					self.dw_timecase.coords(self.rect_id1, self.topx1, self.topy1, self.botx1, self.boty1)  # Update selection rect.

					croppedpic1_1 = pic1.crop((self.topx1,self.topy1,self.botx1,self.boty1))
					imgData1_1 = croppedpic1_1.load()
					croppedpic1_1.save(self.image_path+"1_1_test_pixel_select.png")
					load = Image.open(self.image_path+"1_1_test_pixel_select.png")
					render = ImageTk.PhotoImage(load)
					img1 = Label(self.cameratest_FRame, image=render)
					img1.image = render
					img1.place(x=650, y=60)
		
		
				if self.count_pixel == 1:
					pic1 = Image.open(self.image_path+"select_pixel.png")
					self.topx2, self.topy2 = event.x, event.y

					self.botx2, self.boty2 = self.topx2+10, self.topy2+10
					self.dw_timecase.coords(self.rect_id2, self.topx2, self.topy2, self.botx2, self.boty2)  # Update selection rect.
				
					croppedpic1_2 = pic1.crop((self.topx2,self.topy2,self.botx2,self.boty2))
					imgData1_2 = croppedpic1_2.load()
					croppedpic1_2.save(self.image_path+"1_2_test_pixel_select.png")
					load = Image.open(self.image_path+"1_2_test_pixel_select.png")
					render = ImageTk.PhotoImage(load)
					img2 = Label(self.cameratest_FRame, image=render)
					img2.image = render
					img2.place(x=650, y=120)		
		
			
				if self.count_pixel == 2:
					pic1 = Image.open(self.image_path+"select_pixel.png")	
					self.topx3, self.topy3 = event.x, event.y
					self.botx3, self.boty3 = self.topx3+10, self.topy3+10
					self.dw_timecase.coords(self.rect_id3, self.topx3, self.topy3, self.botx3, self.boty3)  # Update selection rect.
		
					croppedpic1_3 = pic1.crop((self.topx3,self.topy3,self.botx3,self.boty3))
					imgData1_3 = croppedpic1_3.load()
					croppedpic1_3.save(self.image_path+"1_3_test_pixel_select.png")
					load = Image.open(self.image_path+"1_3_test_pixel_select.png")
					render = ImageTk.PhotoImage(load)
					img3 = Label(self.cameratest_FRame, image=render)
					img3.image = render
					img3.place(x=650, y=180)		
		
			
				if self.count_pixel == 3:
					pic1 = Image.open(self.image_path+"select_pixel.png")	
					self.topx4, self.topy4 = event.x, event.y
					self.botx4, self.boty4 = self.topx4+10, self.topy4+10
					self.dw_timecase.coords(self.rect_id4, self.topx4, self.topy4, self.botx4, self.boty4)  # Update selection rect.
		
					croppedpic1_4 = pic1.crop((self.topx4,self.topy4,self.botx4,self.boty4))
					imgData1_4 = croppedpic1_4.load()
					croppedpic1_4.save(self.image_path+"1_4_test_pixel_select.png")
					load = Image.open(self.image_path+"1_4_test_pixel_select.png")
					render = ImageTk.PhotoImage(load)
					img4 = Label(self.cameratest_FRame, image=render)
					img4.image = render
					img4.place(x=650, y=240)		
		
					
				if self.count_pixel == 4:
					pic1 = Image.open(self.image_path+"select_pixel.png")	
					self.topx5, self.topy5 = event.x, event.y
					self.botx5, self.boty5 = self.topx5+10, self.topy5+10
					self.dw_timecase.coords(self.rect_id5, self.topx5, self.topy5, self.botx5, self.boty5)  # Update selection rect.
		
					#code to display image area in label
				
					croppedpic1_5 = pic1.crop((self.topx5,self.topy5,self.botx5,self.boty5))
					imgData1_5 = croppedpic1_5.load()
					croppedpic1_5.save(self.image_path+"1_5_test_pixel_select.png")	
					load = Image.open(self.image_path+"1_5_test_pixel_select.png")
					render = ImageTk.PhotoImage(load)
					img5 = Label(self.cameratest_FRame, image=render)
					img5.image = render
					img5.place(x=650, y=300)
				
					self.bconfirm_set_pixel['state']=ACTIVE			
		
				self.count_pixel = self.count_pixel + 1	
			except Exception as e:
				errorstring = "/E-get mouse position()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 				
			
		def cameratest(self):
			try:	
				self.machine_status_label.configure(text = "")	
				self.servicetest_FRame.destroy()				
				self.cameratest_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				
				canvas=Canvas(self.cameratest_FRame,bg="#F5F4EB")
				canvas.create_rectangle(5, 5, 495, 365, outline="#fb0",fill="#F5F4EB")	
				canvas.place(x=10,y=10,width=500,height=370)
		
				self.dw_timecase=Canvas(self.cameratest_FRame,width=490, height=360,borderwidth=0, highlightthickness=0, bg="#F5F4EB")		
				self.kt_sendcommand("KT+MOVSERVO1:06\r\n",2,10)

				texttosend = "KT+LEDON"+"\r\n"
				self.kt_sendcommand(texttosend,0,10)						
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(1)
				camera.capture(self.image_path+"select_pixel_orig.png")
				time.sleep(0.2)
				texttosend = "KT+LEDOFF"+"\r\n"
				self.kt_sendcommand(texttosend,0,10)							
				
				camera.close()
				time.sleep(0.1)
				
				basewidth = 600
				img = Image.open(self.image_path+"select_pixel_orig.png")	
				
				#####################################################################################################	

				self.npwpercent = (basewidth / float(img.size[0]))
				hsize = int((float(img.size[1]) * float(self.npwpercent)))
				img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
				img.save(self.image_path+"select_pixel.png")
								
				img = ImageTk.PhotoImage(Image.open(self.image_path+"select_pixel.png"))
				self.dw_timecase.place(x=20,y=20,width=480,height=350)
				self.dw_timecase.img = img  # Keep reference in case this code is put into a function.
				self.dw_timecase.create_image(0, 0, image=img, anchor=NW)
				
				with open(self.image_path+"ipcs.json","r+") as e:
					a=json.load(e)					    		
						
				d_topx1 = float(a["1"]["topx"]) * float(self.npwpercent)
				d_topy1 = float(a["1"]["topy"]) * float(self.npwpercent)
				d_botx1 = float(a["1"]["botx"]) * float(self.npwpercent)
				d_boty1 = float(a["1"]["boty"]) * float(self.npwpercent)
				
				d_topx2 = float(a["2"]["topx"]) * float(self.npwpercent)
				d_topy2 = float(a["2"]["topy"]) * float(self.npwpercent)
				d_botx2 = float(a["2"]["botx"]) * float(self.npwpercent)
				d_boty2 = float(a["2"]["boty"]) * float(self.npwpercent)

				d_topx3 = float(a["3"]["topx"]) * float(self.npwpercent)
				d_topy3 = float(a["3"]["topy"]) * float(self.npwpercent)
				d_botx3 = float(a["3"]["botx"]) * float(self.npwpercent)
				d_boty3 = float(a["3"]["boty"]) * float(self.npwpercent)

				d_topx4 = float(a["4"]["topx"]) * float(self.npwpercent)
				d_topy4 = float(a["4"]["topy"]) * float(self.npwpercent)
				d_botx4 = float(a["4"]["botx"]) * float(self.npwpercent)
				d_boty4 = float(a["4"]["boty"]) * float(self.npwpercent)

				d_topx5 = float(a["5"]["topx"]) * float(self.npwpercent)
				d_topy5 = float(a["5"]["topy"]) * float(self.npwpercent)
				d_botx5 = float(a["5"]["botx"]) * float(self.npwpercent)
				d_boty5 = float(a["5"]["boty"]) * float(self.npwpercent)
				

				d_topx1 = str(d_topx1)
				d_topy1 = str(d_topy1)
				d_botx1 = str(d_botx1)
				d_boty1 = str(d_boty1)
				
				d_topx2 = str(d_topx2)
				d_topy2 = str(d_topy2)
				d_botx2 = str(d_botx2)
				d_boty2 = str(d_boty2)

				d_topx3 = str(d_topx3)
				d_topy3 = str(d_topy3)
				d_botx3 = str(d_botx3)
				d_boty3 = str(d_boty3)

				d_topx4 = str(d_topx4)
				d_topy4 = str(d_topy4)
				d_botx4 = str(d_botx4)
				d_boty4 = str(d_boty4)

				d_topx5 = str(d_topx5)
				d_topy5 = str(d_topy5)
				d_botx5 = str(d_botx5)
				d_boty5 = str(d_boty5)
												
				d_rect_id1 = self.dw_timecase.create_rectangle(d_topx1, d_topy1, d_botx1, d_boty1,
									              dash=(2,2), fill='', width=2, outline='white')
									              
				d_rect_id2 = self.dw_timecase.create_rectangle(d_topx2, d_topy2, d_botx2, d_boty2,
									              dash=(2,2), fill='', width=2, outline='white')
									              
				d_rect_id3 = self.dw_timecase.create_rectangle(d_topx3, d_topy3, d_botx3, d_boty3,
									              dash=(2,2), fill='', width=2, outline='white')
									              
				d_rect_id4 = self.dw_timecase.create_rectangle(d_topx4, d_topy4, d_botx4, d_boty4,
									              dash=(2,2), fill='', width=2, outline='white')
									              
				d_rect_id5 = self.dw_timecase.create_rectangle(d_topx5, d_topy5, d_botx5, d_boty5,
									              dash=(2,2), fill='', width=2, outline='white')

############################################################################################################################################################					

				self.rect_id1 = self.dw_timecase.create_rectangle(self.topx1, self.topy1, self.topx1, self.topy1,
									              dash=(2,2), fill='', width=2, outline='black')
									              
				self.rect_id2 = self.dw_timecase.create_rectangle(self.topx2, self.topy2, self.topx2, self.topy2,
									              dash=(2,2), fill='', width=2, outline='black')
									              
				self.rect_id3 = self.dw_timecase.create_rectangle(self.topx3, self.topy3, self.topx3, self.topy3,
									              dash=(2,2), fill='', width=2, outline='black')
									              
				self.rect_id4 = self.dw_timecase.create_rectangle(self.topx4, self.topy4, self.topx4, self.topy4,
									              dash=(2,2), fill='', width=2, outline='black')
									              
				self.rect_id5 = self.dw_timecase.create_rectangle(self.topx5, self.topy5, self.topx5, self.topy5,
									              dash=(2,2), fill='', width=2, outline='black')
									                                                                                                                                                      
				self.ret_get_mouse_bind = self.dw_timecase.bind('<Button-1>', self.get_mouse_posn)
				
########################################################################################################################################										
				self.bconfirm_set_pixel=Button(self.cameratest_FRame,text="Set Pixel",bg="blue",font="centre",fg="white",command=self.set_pixel_info)
				
				self.bconfirm_set_default=Button(self.cameratest_FRame,text="Set Default",bg="blue",font="centre",fg="white",command=self.set_pixel_default)					
				
				self.breturn_from_cameratest_to_service=Button(self.cameratest_FRame,text="Service home",bg="blue",font="centre",fg="white",command=self.goback_service_from_cameratest)
				
				self.bconfirm_set_pixel['state']=DISABLED					
												
				self.bconfirm_set_pixel.place(x=550,y=350)
				self.bconfirm_set_default.place(x=650,y=350)
				self.breturn_from_cameratest_to_service.place(x=600,y=10)
				self.cameratest_FRame.place(x=10,y=40,width=780,height=390)	
			except Exception as e:
				messagebox.showerror("Camera Error !!!", "Error occured during N-P camera operation. Redirecting to HOME page...")
				self.front_page()
				errorstring = "/E-cameratest()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 	
				
		def kget_mouse_posn(self,event):
			try:	
				if self.count_pixel == 0:
					pic1 = Image.open(self.image_path+"kselect_pixel.png")
					self.topx1, self.topy1 = event.x, event.y

					self.botx1, self.boty1 = self.topx1+10, self.topy1+10
					self.dw_timecase.coords(self.rect_id1, self.topx1, self.topy1, self.botx1, self.boty1)  # Update selection rect.
		
					croppedpic1_1 = pic1.crop((self.topx1,self.topy1,self.botx1,self.boty1))
					imgData1_1 = croppedpic1_1.load()
					croppedpic1_1.save(self.image_path+"k1_1_test_pixel_select.png")
					load = Image.open(self.image_path+"k1_1_test_pixel_select.png")
					render = ImageTk.PhotoImage(load)
					img1 = Label(self.cameratest_FRame, image=render)
					img1.image = render
					img1.place(x=650, y=60)
		
		
				if self.count_pixel == 1:
					pic1 = Image.open(self.image_path+"kselect_pixel.png")
					self.topx2, self.topy2 = event.x, event.y

					self.botx2, self.boty2 = self.topx2+10, self.topy2+10
					self.dw_timecase.coords(self.rect_id2, self.topx2, self.topy2, self.botx2, self.boty2)  # Update selection rect.
		
					croppedpic1_2 = pic1.crop((self.topx2,self.topy2,self.botx2,self.boty2))
					imgData1_2 = croppedpic1_2.load()
					croppedpic1_2.save(self.image_path+"k1_2_test_pixel_select.png")
					load = Image.open(self.image_path+"k1_2_test_pixel_select.png")
					render = ImageTk.PhotoImage(load)
					img2 = Label(self.cameratest_FRame, image=render)
					img2.image = render
					img2.place(x=650, y=120)		
		
			
				if self.count_pixel == 2:
					pic1 = Image.open(self.image_path+"kselect_pixel.png")	
					self.topx3, self.topy3 = event.x, event.y
					self.botx3, self.boty3 = self.topx3+10, self.topy3+10
					self.dw_timecase.coords(self.rect_id3, self.topx3, self.topy3, self.botx3, self.boty3)  # Update selection rect.
		
					croppedpic1_3 = pic1.crop((self.topx3,self.topy3,self.botx3,self.boty3))
					imgData1_3 = croppedpic1_3.load()
					croppedpic1_3.save(self.image_path+"k1_3_test_pixel_select.png")
					load = Image.open(self.image_path+"k1_3_test_pixel_select.png")
					render = ImageTk.PhotoImage(load)
					img3 = Label(self.cameratest_FRame, image=render)
					img3.image = render
					img3.place(x=650, y=180)		
		
			
				if self.count_pixel == 3:
					pic1 = Image.open(self.image_path+"kselect_pixel.png")	
					self.topx4, self.topy4 = event.x, event.y

					self.botx4, self.boty4 = self.topx4+10, self.topy4+10
					self.dw_timecase.coords(self.rect_id4, self.topx4, self.topy4, self.botx4, self.boty4)  # Update selection rect.
		
					croppedpic1_4 = pic1.crop((self.topx4,self.topy4,self.botx4,self.boty4))
					imgData1_4 = croppedpic1_4.load()
					croppedpic1_4.save(self.image_path+"k1_4_test_pixel_select.png")
					load = Image.open(self.image_path+"k1_4_test_pixel_select.png")
					render = ImageTk.PhotoImage(load)
					img4 = Label(self.cameratest_FRame, image=render)
					img4.image = render
					img4.place(x=650, y=240)		
		
					
				if self.count_pixel == 4:
					pic1 = Image.open(self.image_path+"kselect_pixel.png")	
					self.topx5, self.topy5 = event.x, event.y

					self.botx5, self.boty5 = self.topx5+10, self.topy5+10
					self.dw_timecase.coords(self.rect_id5, self.topx5, self.topy5, self.botx5, self.boty5)  # Update selection rect.
		
					croppedpic1_5 = pic1.crop((self.topx5,self.topy5,self.botx5,self.boty5))
					imgData1_5 = croppedpic1_5.load()
					croppedpic1_5.save(self.image_path+"k1_5_test_pixel_select.png")	
					load = Image.open(self.image_path+"k1_5_test_pixel_select.png")
					render = ImageTk.PhotoImage(load)
					img5 = Label(self.cameratest_FRame, image=render)
					img5.image = render
					img5.place(x=650, y=300)
				
					self.bconfirm_set_pixel['state']=ACTIVE			
		
				self.count_pixel = self.count_pixel + 1	
			except Exception as e:
				errorstring = "/E-kget_mouse_posn()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 				
											 									
													
		def kcameratest(self):
			try:	
				self.machine_status_label.configure(text = "")	
				self.servicetest_FRame.destroy()				
				self.cameratest_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				
				canvas=Canvas(self.cameratest_FRame,bg="#F5F4EB")
				canvas.create_rectangle(5, 5, 495, 365, outline="#fb0",fill="#F5F4EB")	
				canvas.place(x=10,y=10,width=500,height=370)
		
				self.dw_timecase=Canvas(self.cameratest_FRame,width=490, height=360,borderwidth=0, highlightthickness=0, bg="#F5F4EB")					
				self.kt_sendcommand("KT+MOVSERVO1:05\r\n",2,10)

				texttosend = "KT+LEDON"+"\r\n"
				self.kt_sendcommand(texttosend,0,10)						
				time.sleep(2)
				camera = picamera.PiCamera()
				time.sleep(1)
				camera.capture(self.image_path+"kselect_pixel_orig.png")
				time.sleep(0.2)
				texttosend = "KT+LEDOFF"+"\r\n"
				self.kt_sendcommand(texttosend,0,10)							
				
				camera.close()
				time.sleep(0.1)
				
				basewidth = 600
				img = Image.open(self.image_path+"kselect_pixel_orig.png")	
				
				#####################################################################################################	

				self.kwpercent = (basewidth / float(img.size[0]))
				hsize = int((float(img.size[1]) * float(self.kwpercent)))
				img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
				img.save(self.image_path+"kselect_pixel.png")							
									
				img = ImageTk.PhotoImage(Image.open(self.image_path+"kselect_pixel.png"))
				self.dw_timecase.place(x=20,y=20,width=480,height=350)
				self.dw_timecase.img = img  # Keep reference in case this code is put into a function.
				self.dw_timecase.create_image(0, 0, image=img, anchor=NW)
				
				with open(self.image_path+"kipcs.json","r+") as e:
					a=json.load(e)					    		
						
				d_topx1 = float(a["1"]["topx"]) * float(self.kwpercent)
				d_topy1 = float(a["1"]["topy"]) * float(self.kwpercent)
				d_botx1 = float(a["1"]["botx"]) * float(self.kwpercent)
				d_boty1 = float(a["1"]["boty"]) * float(self.kwpercent)
				
				d_topx2 = float(a["2"]["topx"]) * float(self.kwpercent)
				d_topy2 = float(a["2"]["topy"]) * float(self.kwpercent)
				d_botx2 = float(a["2"]["botx"]) * float(self.kwpercent)
				d_boty2 = float(a["2"]["boty"]) * float(self.kwpercent)

				d_topx3 = float(a["3"]["topx"]) * float(self.kwpercent)
				d_topy3 = float(a["3"]["topy"]) * float(self.kwpercent)
				d_botx3 = float(a["3"]["botx"]) * float(self.kwpercent)
				d_boty3 = float(a["3"]["boty"]) * float(self.kwpercent)

				d_topx4 = float(a["4"]["topx"]) * float(self.kwpercent)
				d_topy4 = float(a["4"]["topy"]) * float(self.kwpercent)
				d_botx4 = float(a["4"]["botx"]) * float(self.kwpercent)
				d_boty4 = float(a["4"]["boty"]) * float(self.kwpercent)

				d_topx5 = float(a["5"]["topx"]) * float(self.kwpercent)
				d_topy5 = float(a["5"]["topy"]) * float(self.kwpercent)
				d_botx5 = float(a["5"]["botx"]) * float(self.kwpercent)
				d_boty5 = float(a["5"]["boty"]) * float(self.kwpercent)
				

				d_topx1 = str(d_topx1)
				d_topy1 = str(d_topy1)
				d_botx1 = str(d_botx1)
				d_boty1 = str(d_boty1)
				
				d_topx2 = str(d_topx2)
				d_topy2 = str(d_topy2)
				d_botx2 = str(d_botx2)
				d_boty2 = str(d_boty2)

				d_topx3 = str(d_topx3)
				d_topy3 = str(d_topy3)
				d_botx3 = str(d_botx3)
				d_boty3 = str(d_boty3)

				d_topx4 = str(d_topx4)
				d_topy4 = str(d_topy4)
				d_botx4 = str(d_botx4)
				d_boty4 = str(d_boty4)

				d_topx5 = str(d_topx5)
				d_topy5 = str(d_topy5)
				d_botx5 = str(d_botx5)
				d_boty5 = str(d_boty5)
												
				d_rect_id1 = self.dw_timecase.create_rectangle(d_topx1, d_topy1, d_botx1, d_boty1,
									              dash=(2,2), fill='', width=2, outline='white')
									              
				d_rect_id2 = self.dw_timecase.create_rectangle(d_topx2, d_topy2, d_botx2, d_boty2,
									              dash=(2,2), fill='', width=2, outline='white')
									              
				d_rect_id3 = self.dw_timecase.create_rectangle(d_topx3, d_topy3, d_botx3, d_boty3,
									              dash=(2,2), fill='', width=2, outline='white')
									              
				d_rect_id4 = self.dw_timecase.create_rectangle(d_topx4, d_topy4, d_botx4, d_boty4,
									              dash=(2,2), fill='', width=2, outline='white')
									              
				d_rect_id5 = self.dw_timecase.create_rectangle(d_topx5, d_topy5, d_botx5, d_boty5,
									              dash=(2,2), fill='', width=2, outline='white')

############################################################################################################################################################					

				# Create selection rectangle (invisible since corner points are equal).
				self.rect_id1 = self.dw_timecase.create_rectangle(self.topx1, self.topy1, self.topx1, self.topy1,
									              dash=(2,2), fill='', width=2, outline='black')
									              
				self.rect_id2 = self.dw_timecase.create_rectangle(self.topx2, self.topy2, self.topx2, self.topy2,
									              dash=(2,2), fill='', width=2, outline='black')
									              
				self.rect_id3 = self.dw_timecase.create_rectangle(self.topx3, self.topy3, self.topx3, self.topy3,
									              dash=(2,2), fill='', width=2, outline='black')
									              
				self.rect_id4 = self.dw_timecase.create_rectangle(self.topx4, self.topy4, self.topx4, self.topy4,
									              dash=(2,2), fill='', width=2, outline='black')
									              
				self.rect_id5 = self.dw_timecase.create_rectangle(self.topx5, self.topy5, self.topx5, self.topy5,
									              dash=(2,2), fill='', width=2, outline='black')
									                                                                                                                                                      
				self.ret_get_mouse_bind = self.dw_timecase.bind('<Button-1>', self.kget_mouse_posn)
				
########################################################################################################################################										
				self.bconfirm_set_pixel=Button(self.cameratest_FRame,text="Set Pixel",bg="blue",font="centre",fg="white",command=self.k_set_pixel_info)
				
				self.bconfirm_set_default=Button(self.cameratest_FRame,text="Set Default",bg="blue",font="centre",fg="white",command=self.k_set_pixel_default)					
				
				self.breturn_from_cameratest_to_service=Button(self.cameratest_FRame,text="Service home",bg="blue",font="centre",fg="white",command=self.k_goback_service_from_cameratest)
				
				self.bconfirm_set_pixel['state']=DISABLED					
												
				self.bconfirm_set_pixel.place(x=550,y=350)
				self.bconfirm_set_default.place(x=650,y=350)
				self.breturn_from_cameratest_to_service.place(x=600,y=10)
				self.cameratest_FRame.place(x=10,y=40,width=780,height=390)	
			except Exception as e:
				messagebox.showerror("Camera Error !!!", "Error occured during K camera operation. Redirecting to HOME page...")
				self.front_page()
				errorstring = "/E-kcameratest()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				
		def n_calib_images(self):
			try:	
			
				with open(self.npk_calibration_values_path) as json_file:
					n_calib_data_from_json_file = json.load(json_file)	

				n0r = n_calib_data_from_json_file["calibration"]["N"]["0"]["r"]
				n5r = n_calib_data_from_json_file["calibration"]["N"]["5"]["r"]
				n10r = n_calib_data_from_json_file["calibration"]["N"]["10"]["r"]
				n20r = n_calib_data_from_json_file["calibration"]["N"]["20"]["r"]	
				n30r = n_calib_data_from_json_file["calibration"]["N"]["30"]["r"]	
				n40r = n_calib_data_from_json_file["calibration"]["N"]["40"]["r"]	

				n0g = n_calib_data_from_json_file["calibration"]["N"]["0"]["g"]
				n5g = n_calib_data_from_json_file["calibration"]["N"]["5"]["g"]
				n10g = n_calib_data_from_json_file["calibration"]["N"]["10"]["g"]
				n20g = n_calib_data_from_json_file["calibration"]["N"]["20"]["g"]	
				n30g = n_calib_data_from_json_file["calibration"]["N"]["30"]["g"]	
				n40g = n_calib_data_from_json_file["calibration"]["N"]["40"]["g"]		

				n0b = n_calib_data_from_json_file["calibration"]["N"]["0"]["b"]
				n5b = n_calib_data_from_json_file["calibration"]["N"]["5"]["b"]
				n10b = n_calib_data_from_json_file["calibration"]["N"]["10"]["b"]
				n20b = n_calib_data_from_json_file["calibration"]["N"]["20"]["b"]	
				n30b = n_calib_data_from_json_file["calibration"]["N"]["30"]["b"]	
				n40b = n_calib_data_from_json_file["calibration"]["N"]["40"]["b"]	
				
				
				with open(self.image_path+"rgb_result.json") as json_file:
					n_rgb_json_file = json.load(json_file)	

				n_res_r = n_rgb_json_file["n_rgb"]["result_n_r"]
				n_res_g = n_rgb_json_file["n_rgb"]["result_n_g"]
				n_res_b = n_rgb_json_file["n_rgb"]["result_n_b"]
					
				self.machine_status_label.configure(text = "")	
				self.servicetest_FRame.destroy()				
				self.n_calib_images_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				
				basewidth = 250
				
				file = pathlib.Path(self.image_path+"nc1_0_fulltest.png")
				if file.exists ():	
					img = Image.open(self.image_path+"nc1_0_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.nc1_0_fulltest=Canvas(self.n_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_nc1_0_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_nc1_0_fulltest.png"))
					self.nc1_0_fulltest.place(x=10,y=30,width=180,height=180)
					self.nc1_0_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.nc1_0_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "N-0 Proper image will be loaded after calibration of device")
					pass			
				
#########################################################################################################################################

				basewidth = 250
				
				file = pathlib.Path(self.image_path+"nc1_5_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"nc1_5_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.nc1_5_fulltest=Canvas(self.n_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_nc1_5_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_nc1_5_fulltest.png"))
					self.nc1_5_fulltest.place(x=200,y=30,width=180,height=180)
					self.nc1_5_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.nc1_5_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "N-5 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250
				
				file = pathlib.Path(self.image_path+"nc1_10_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"nc1_10_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.nc1_10_fulltest=Canvas(self.n_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_nc1_10_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_nc1_10_fulltest.png"))
					self.nc1_10_fulltest.place(x=400,y=30,width=180,height=180)
					self.nc1_10_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.nc1_10_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "N-10 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250
						
				file = pathlib.Path(self.image_path+"nc1_20_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"nc1_20_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.nc1_20_fulltest=Canvas(self.n_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_nc1_20_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_nc1_20_fulltest.png"))
					self.nc1_20_fulltest.place(x=10,y=200,width=180,height=180)
					self.nc1_20_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.nc1_20_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "N-20 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250
						
				file = pathlib.Path(self.image_path+"nc1_30_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"nc1_30_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.nc1_30_fulltest=Canvas(self.n_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_nc1_30_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_nc1_30_fulltest.png"))
					self.nc1_30_fulltest.place(x=200,y=200,width=180,height=180)
					self.nc1_30_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.nc1_30_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "N-30 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"nc1_40_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"nc1_40_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.nc1_40_fulltest=Canvas(self.n_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_nc1_40_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_nc1_40_fulltest.png"))
					self.nc1_40_fulltest.place(x=400,y=200,width=180,height=180)
					self.nc1_40_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.nc1_40_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "N-40 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250
						
				img = Image.open(self.image_path+"N1_fulltest.png")	
				self.kwpercent = (basewidth / float(img.size[0]))
				hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
				self.N1_fulltest=Canvas(self.n_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
				img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
				img.save(self.image_path+"resize_N1_fulltest.png")							
				img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_N1_fulltest.png"))
				self.N1_fulltest.place(x=590,y=100,width=180,height=180)
				self.N1_fulltest.img = img  # Keep reference in case this code is put into a function.
				self.N1_fulltest.create_image(0, 0, image=img, anchor=NW)
				
				self.bnimages_servicetest=Button(self.n_calib_images_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.goback_servicetest_from_nimages)
				self.bnimages_servicetest.place(x=650,y=10,width=60,height=30)	
				
				self.nc0label=Label(self.n_calib_images_FRame,text="0",bg="#F5F4EB",fg="red",font="centre 6") 
				self.nc0label.place(x=15,y=35,width=20,height=20)
				
				self.nc05label=Label(self.n_calib_images_FRame,text="05",bg="#F5F4EB",fg="red",font="centre 6") 
				self.nc05label.place(x=205,y=35,width=20,height=20)
				
				self.nc10label=Label(self.n_calib_images_FRame,text="10",bg="#F5F4EB",fg="red",font="centre 6") 
				self.nc10label.place(x=405,y=35,width=20,height=20)
				
				self.nc15label=Label(self.n_calib_images_FRame,text="20",bg="#F5F4EB",fg="red",font="centre 6") 
				self.nc15label.place(x=15,y=205,width=20,height=20)
				
				self.nc20label=Label(self.n_calib_images_FRame,text="30",bg="#F5F4EB",fg="red",font="centre 6") 
				self.nc20label.place(x=205,y=205,width=20,height=20)
				
				self.nc25label=Label(self.n_calib_images_FRame,text="40",bg="#F5F4EB",fg="red",font="centre 6") 
				self.nc25label.place(x=405,y=205,width=20,height=20)				
				
				self.nlabel=Label(self.n_calib_images_FRame,text="sample",bg="#F5F4EB",fg="red",font="centre 6") 
				self.nlabel.place(x=595,y=105,width=60,height=20)	
				
				n0_rgb = "(" + str(n0r) + "," + str(n0g) + "," + str(n0b) + ")"
				self.n0rgblabel=Label(self.n_calib_images_FRame,text=n0_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.n0rgblabel.place(x=10,y=170,width=180,height=20)	
				
				n5_rgb = "(" + str(n5r) + "," + str(n5g) + "," + str(n5b) + ")"
				self.n5rgblabel=Label(self.n_calib_images_FRame,text=n5_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.n5rgblabel.place(x=200,y=170,width=180,height=20)	
				
				n10_rgb = "(" + str(n10r) + "," + str(n10g) + "," + str(n10b) + ")"
				self.n10rgblabel=Label(self.n_calib_images_FRame,text=n10_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.n10rgblabel.place(x=400,y=170,width=180,height=20)		
				
				n30_rgb = "(" + str(n30r) + "," + str(n30g) + "," + str(n30b) + ")"
				self.n30rgblabel=Label(self.n_calib_images_FRame,text=n30_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.n30rgblabel.place(x=10,y=360,width=180,height=20)	
				
				n20_rgb = "(" + str(n20r) + "," + str(n20g) + "," + str(n20b) + ")"
				self.n20rgblabel=Label(self.n_calib_images_FRame,text=n20_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.n20rgblabel.place(x=200,y=360,width=180,height=20)	
				
				n40_rgb = "(" + str(n40r) + "," + str(n40g) + "," + str(n40b) + ")"
				self.n40rgblabel=Label(self.n_calib_images_FRame,text=n40_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.n40rgblabel.place(x=400,y=360,width=180,height=20)	
				
				sample_rgb_n = "(" + str(n_res_r) + "," + str(n_res_g) + "," + str(n_res_b) + ")"
				self.sample_n_rgb_label=Label(self.n_calib_images_FRame,text=sample_rgb_n,bg="#F5F4EB",fg="red",font="centre 6") 
				self.sample_n_rgb_label.place(x=600,y=260,width=180,height=20)	
				
#######################################################################################################################################							
				self.n_calib_images_FRame.place(x=10,y=40,width=780,height=390)	
			except Exception as e:
				messagebox.showerror("Calibration Image Loading Error !!!", "Error while loading n calibration images. Redirecting to HOME page...")
				self.front_page()
				errorstring = "/E-n_calib_images()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 

		def p_calib_images(self):
			try:	
				with open(self.npk_calibration_values_path) as json_file:
					p_calib_data_from_json_file = json.load(json_file)					        

				p0r = p_calib_data_from_json_file["calibration"]["P"]["0"]["r"]
				p5r = p_calib_data_from_json_file["calibration"]["P"]["5"]["r"]
				p10r = p_calib_data_from_json_file["calibration"]["P"]["10"]["r"]
				p15r = p_calib_data_from_json_file["calibration"]["P"]["15"]["r"]	
				p20r = p_calib_data_from_json_file["calibration"]["P"]["20"]["r"]	
				p25r = p_calib_data_from_json_file["calibration"]["P"]["25"]["r"]	

				p0g = p_calib_data_from_json_file["calibration"]["P"]["0"]["g"]
				p5g = p_calib_data_from_json_file["calibration"]["P"]["5"]["g"]
				p10g = p_calib_data_from_json_file["calibration"]["P"]["10"]["g"]
				p15g = p_calib_data_from_json_file["calibration"]["P"]["15"]["g"]	
				p20g = p_calib_data_from_json_file["calibration"]["P"]["20"]["g"]	
				p25g = p_calib_data_from_json_file["calibration"]["P"]["25"]["g"]		

				p0b = p_calib_data_from_json_file["calibration"]["P"]["0"]["b"]
				p5b = p_calib_data_from_json_file["calibration"]["P"]["5"]["b"]
				p10b = p_calib_data_from_json_file["calibration"]["P"]["10"]["b"]
				p15b = p_calib_data_from_json_file["calibration"]["P"]["15"]["b"]	
				p20b = p_calib_data_from_json_file["calibration"]["P"]["20"]["b"]	
				p25b = p_calib_data_from_json_file["calibration"]["P"]["25"]["b"]	
				
				with open(self.image_path+"rgb_result.json") as json_file:
					p_rgb_json_file = json.load(json_file)	
																				
				p_res_r = p_rgb_json_file["p_rgb"]["result_p_r"]
				p_res_g = p_rgb_json_file["p_rgb"]["result_p_g"]
				p_res_b = p_rgb_json_file["p_rgb"]["result_p_b"]

				self.machine_status_label.configure(text = "")	
				self.servicetest_FRame.destroy()				
				self.p_calib_images_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				
				basewidth = 250
				
				file = pathlib.Path(self.image_path+"pc1_0_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"pc1_0_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
				
					self.pc1_0_fulltest=Canvas(self.p_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_pc1_0_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_pc1_0_fulltest.png"))
					self.pc1_0_fulltest.place(x=10,y=30,width=180,height=180)
					self.pc1_0_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.pc1_0_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "P-0 Proper image will be loaded after calibration of device")
					pass					
				
				
#########################################################################################################################################

				basewidth = 250
				file = pathlib.Path(self.image_path+"pc1_5_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"pc1_5_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.pc1_5_fulltest=Canvas(self.p_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_pc1_5_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_pc1_5_fulltest.png"))
					self.pc1_5_fulltest.place(x=200,y=30,width=180,height=180)
					self.pc1_5_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.pc1_5_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "P-5 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"pc1_10_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"pc1_10_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.pc1_10_fulltest=Canvas(self.p_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_pc1_10_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_pc1_10_fulltest.png"))
					self.pc1_10_fulltest.place(x=400,y=30,width=180,height=180)
					self.pc1_10_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.pc1_10_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "P-10 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"pc1_15_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"pc1_15_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.pc1_15_fulltest=Canvas(self.p_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_pc1_15_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_pc1_15_fulltest.png"))
					self.pc1_15_fulltest.place(x=10,y=200,width=180,height=180)
					self.pc1_15_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.pc1_15_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "P-15 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250
				
				file = pathlib.Path(self.image_path+"pc1_20_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"pc1_20_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.pc1_20_fulltest=Canvas(self.p_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_pc1_20_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_pc1_20_fulltest.png"))
					self.pc1_20_fulltest.place(x=200,y=200,width=180,height=180)
					self.pc1_20_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.pc1_20_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "P-20 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"pc1_25_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"pc1_25_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.pc1_25_fulltest=Canvas(self.p_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_pc1_25_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_pc1_25_fulltest.png"))
					self.pc1_25_fulltest.place(x=400,y=200,width=180,height=180)
					self.pc1_25_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.pc1_25_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "P-25 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250
				
				img = Image.open(self.image_path+"P1_fulltest.png")	
				self.kwpercent = (basewidth / float(img.size[0]))
				hsize = int((float(img.size[1]) * float(self.kwpercent)))
		
				self.P1_fulltest=Canvas(self.p_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
				img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
				img.save(self.image_path+"resize_P1_fulltest.png")							
				img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_P1_fulltest.png"))
				self.P1_fulltest.place(x=590,y=100,width=180,height=180)
				self.P1_fulltest.img = img  # Keep reference in case this code is put into a function.
				self.P1_fulltest.create_image(0, 0, image=img, anchor=NW)
				
#######################################################################################################################################

				self.bpimages_servicetest=Button(self.p_calib_images_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.goback_servicetest_from_pimages)
				self.bpimages_servicetest.place(x=650,y=10,width=60,height=30)	
				
				self.pc0label=Label(self.p_calib_images_FRame,text="0",bg="#F5F4EB",fg="red",font="centre 6") 
				self.pc0label.place(x=15,y=35,width=20,height=20)
				
				self.pc05label=Label(self.p_calib_images_FRame,text="05",bg="#F5F4EB",fg="red",font="centre 6") 
				self.pc05label.place(x=205,y=35,width=20,height=20)
				
				self.pc10label=Label(self.p_calib_images_FRame,text="10",bg="#F5F4EB",fg="red",font="centre 6") 
				self.pc10label.place(x=405,y=35,width=20,height=20)
				
				self.pc15label=Label(self.p_calib_images_FRame,text="15",bg="#F5F4EB",fg="red",font="centre 6") 
				self.pc15label.place(x=15,y=205,width=20,height=20)
				
				self.pc20label=Label(self.p_calib_images_FRame,text="20",bg="#F5F4EB",fg="red",font="centre 6") 
				self.pc20label.place(x=205,y=205,width=20,height=20)
				
				self.pc25label=Label(self.p_calib_images_FRame,text="25",bg="#F5F4EB",fg="red",font="centre 6") 
				self.pc25label.place(x=405,y=205,width=20,height=20)				
				
				self.plabel=Label(self.p_calib_images_FRame,text="sample",bg="#F5F4EB",fg="red",font="centre 6") 
				self.plabel.place(x=595,y=105,width=60,height=20)
				
				p0_rgb = "(" + str(p0r) + "," + str(p0g) + "," + str(p0b) + ")"
				self.p0rgblabel=Label(self.p_calib_images_FRame,text=p0_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.p0rgblabel.place(x=10,y=170,width=180,height=20)	
				
				p5_rgb = "(" + str(p5r) + "," + str(p5g) + "," + str(p5b) + ")"
				self.p5rgblabel=Label(self.p_calib_images_FRame,text=p5_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.p5rgblabel.place(x=200,y=170,width=180,height=20)	
				
				p10_rgb = "(" + str(p10r) + "," + str(p10g) + "," + str(p10b) + ")"
				self.p10rgblabel=Label(self.p_calib_images_FRame,text=p10_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.p10rgblabel.place(x=400,y=170,width=180,height=20)		
				
				p15_rgb = "(" + str(p15r) + "," + str(p15g) + "," + str(p15b) + ")"
				self.p15rgblabel=Label(self.p_calib_images_FRame,text=p15_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.p15rgblabel.place(x=10,y=360,width=180,height=20)	
				
				p20_rgb = "(" + str(p20r) + "," + str(p20g) + "," + str(p20b) + ")"
				self.p20rgblabel=Label(self.p_calib_images_FRame,text=p20_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.p20rgblabel.place(x=200,y=360,width=180,height=20)	
				
				p25_rgb = "(" + str(p25r) + "," + str(p25g) + "," + str(p25b) + ")"
				self.p25rgblabel=Label(self.p_calib_images_FRame,text=p25_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.p25rgblabel.place(x=400,y=360,width=180,height=20)	
				
				sample_rgb_p = "(" + str(p_res_r) + "," + str(p_res_g) + "," + str(p_res_b) + ")"
				self.sample_p_rgb_label=Label(self.p_calib_images_FRame,text=sample_rgb_p,bg="#F5F4EB",fg="red",font="centre 6") 
				self.sample_p_rgb_label.place(x=600,y=260,width=180,height=20)	
				
				self.p_calib_images_FRame.place(x=10,y=40,width=780,height=390)	
			except Exception as e:
				messagebox.showerror("Calibration Image Loading Error !!!", "Error while loading p calibration images. Redirecting to HOME page...")
				self.front_page()
				errorstring = "/E-p_calib_images()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				
		def k_calib_images(self):
			try:
				with open(self.npk_calibration_values_path) as json_file:
					k_calib_data_from_json_file = json.load(json_file)					        

				k0r = k_calib_data_from_json_file["calibration"]["K"]["0"]["r"]
				k10r = k_calib_data_from_json_file["calibration"]["K"]["10"]["r"]
				k20r = k_calib_data_from_json_file["calibration"]["K"]["20"]["r"]	
				k40r = k_calib_data_from_json_file["calibration"]["K"]["40"]["r"]	

				k0g = k_calib_data_from_json_file["calibration"]["K"]["0"]["g"]
				k10g = k_calib_data_from_json_file["calibration"]["K"]["10"]["g"]
				k20g = k_calib_data_from_json_file["calibration"]["K"]["20"]["g"]	
				k40g = k_calib_data_from_json_file["calibration"]["K"]["40"]["g"]		

				k0b = k_calib_data_from_json_file["calibration"]["K"]["0"]["b"]
				k10b = k_calib_data_from_json_file["calibration"]["K"]["10"]["b"]
				k20b = k_calib_data_from_json_file["calibration"]["K"]["20"]["b"]	
				k40b = k_calib_data_from_json_file["calibration"]["K"]["40"]["b"]	
				
				with open(self.image_path+"rgb_result.json") as json_file:
					k_rgb_json_file = json.load(json_file)							
				
				k_res_r = k_rgb_json_file["k_rgb"]["result_k_r"]
				k_res_g = k_rgb_json_file["k_rgb"]["result_k_g"]
				k_res_b = k_rgb_json_file["k_rgb"]["result_k_b"]
								
				self.machine_status_label.configure(text = "")	
				self.servicetest_FRame.destroy()				
				self.k_calib_images_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				
				basewidth = 250

				file = pathlib.Path(self.image_path+"kc1_0_fulltest.png")
				if file.exists ():
					img = Image.open(self.image_path+"kc1_0_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.kc1_0_fulltest=Canvas(self.k_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_kc1_0_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_kc1_0_fulltest.png"))
					self.kc1_0_fulltest.place(x=60,y=10,width=200,height=180)
					self.kc1_0_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.kc1_0_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "K-0 Proper image will be loaded after calibration of device")
					pass				
				
#########################################################################################################################################

				basewidth = 250
				
				file = pathlib.Path(self.image_path+"kc1_10_fulltest.png")
				if file.exists ():
					img = Image.open(self.image_path+"kc1_10_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.kc1_0_fulltest=Canvas(self.k_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_kc1_10_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_kc1_10_fulltest.png"))
					self.kc1_0_fulltest.place(x=300,y=10,width=200,height=180)
					self.kc1_0_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.kc1_0_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "K-10 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"kc1_20_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"kc1_20_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.kc1_0_fulltest=Canvas(self.k_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_kc1_20_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_kc1_20_fulltest.png"))
					self.kc1_0_fulltest.place(x=60,y=200,width=200,height=180)
					self.kc1_0_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.kc1_0_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "K-20 Proper image will be loaded after calibration of device")
					pass						
				
#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"kc1_40_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"kc1_40_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.kc1_0_fulltest=Canvas(self.k_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_kc1_40_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_kc1_40_fulltest.png"))
					self.kc1_0_fulltest.place(x=300,y=200,width=200,height=180)
					self.kc1_0_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.kc1_0_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "K40 - Proper image will be loaded after calibration of device")
					pass						
				
#######################################################################################################################################	

				basewidth = 250
						
				img = Image.open(self.image_path+"K1_fulltest.png")	
				self.kwpercent = (basewidth / float(img.size[0]))
				hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
				self.K1_fulltest=Canvas(self.k_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
				img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
				img.save(self.image_path+"resize_K1_fulltest.png")							
				img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_K1_fulltest.png"))
				self.K1_fulltest.place(x=550,y=100,width=200,height=200)
				self.K1_fulltest.img = img  # Keep reference in case this code is put into a function.
				self.K1_fulltest.create_image(0, 0, image=img, anchor=NW)
				
#######################################################################################################################################	

				self.bkimages_servicetest=Button(self.k_calib_images_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.goback_servicetest_from_kimages)
				self.bkimages_servicetest.place(x=650,y=10,width=60,height=30)	
				
				self.kc0label=Label(self.k_calib_images_FRame,text="0",bg="#F5F4EB",fg="red",font="centre 6") 
				self.kc0label.place(x=70,y=20,width=20,height=20)
				
				self.kc10label=Label(self.k_calib_images_FRame,text="10",bg="#F5F4EB",fg="red",font="centre 6") 
				self.kc10label.place(x=310,y=20,width=20,height=20)
				
				self.kc20label=Label(self.k_calib_images_FRame,text="20",bg="#F5F4EB",fg="red",font="centre 6") 
				self.kc20label.place(x=70,y=210,width=20,height=20)
				
				self.kc40label=Label(self.k_calib_images_FRame,text="40",bg="#F5F4EB",fg="red",font="centre 6") 
				self.kc40label.place(x=310,y=220,width=20,height=20)
				
				self.klabel=Label(self.k_calib_images_FRame,text="sample",bg="#F5F4EB",fg="red",font="centre 6") 
				self.klabel.place(x=560,y=110,width=60,height=20)	
				
				k0_rgb = "(" + str(k0r) + "," + str(k0g) + "," + str(k0b) + ")"
				self.k0rgblabel=Label(self.k_calib_images_FRame,text=k0_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.k0rgblabel.place(x=60,y=160,width=180,height=20)
				
				k10_rgb = "(" + str(k10r) + "," + str(k10g) + "," + str(k10b) + ")"
				self.k10rgblabel=Label(self.k_calib_images_FRame,text=k10_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.k10rgblabel.place(x=300,y=160,width=180,height=20)		
				
				k20_rgb = "(" + str(k20r) + "," + str(k20g) + "," + str(k20b) + ")"
				self.k20rgblabel=Label(self.k_calib_images_FRame,text=k20_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.k20rgblabel.place(x=60,y=360,width=180,height=20)
				
				k40_rgb = "(" + str(k40r) + "," + str(k40g) + "," + str(k40b) + ")"
				self.k40rgblabel=Label(self.k_calib_images_FRame,text=k40_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.k40rgblabel.place(x=300,y=360,width=180,height=20)						
													
				sample_rgb_k = "(" + str(k_res_r) + "," + str(k_res_g) + "," + str(k_res_b) + ")"
				self.sample_k_rgb_label=Label(self.k_calib_images_FRame,text=sample_rgb_k,bg="#F5F4EB",fg="red",font="centre 6") 
				self.sample_k_rgb_label.place(x=560,y=260,width=180,height=20)	
													
				self.k_calib_images_FRame.place(x=10,y=40,width=780,height=390)	
			except Exception as e:
				messagebox.showerror("Calibration Image Loading Error !!!", "Error while loading k calibration images. Redirecting to HOME page...")
				self.front_page()
				errorstring = "/E-k_calib_images()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				
		def b_calib_images(self):
			try:	
				with open(self.npk_calibration_values_path) as json_file:
					b_calib_data_from_json_file = json.load(json_file)					        

				b0r = b_calib_data_from_json_file["calibration"]["B"]["0.0"]["r"]
				b5r = b_calib_data_from_json_file["calibration"]["B"]["0.25"]["r"]
				b10r = b_calib_data_from_json_file["calibration"]["B"]["0.5"]["r"]
				b15r = b_calib_data_from_json_file["calibration"]["B"]["1.0"]["r"]	
				b20r = b_calib_data_from_json_file["calibration"]["B"]["1.5"]["r"]	
				b25r = b_calib_data_from_json_file["calibration"]["B"]["2.0"]["r"]	

				b0g = b_calib_data_from_json_file["calibration"]["B"]["0.0"]["g"]
				b5g = b_calib_data_from_json_file["calibration"]["B"]["0.25"]["g"]
				b10g = b_calib_data_from_json_file["calibration"]["B"]["0.5"]["g"]
				b15g = b_calib_data_from_json_file["calibration"]["B"]["1.0"]["g"]	
				b20g = b_calib_data_from_json_file["calibration"]["B"]["1.5"]["g"]	
				b25g = b_calib_data_from_json_file["calibration"]["B"]["2.0"]["g"]		

				b0b = b_calib_data_from_json_file["calibration"]["B"]["0.0"]["b"]
				b5b = b_calib_data_from_json_file["calibration"]["B"]["0.25"]["b"]
				b10b = b_calib_data_from_json_file["calibration"]["B"]["0.5"]["b"]
				b15b = b_calib_data_from_json_file["calibration"]["B"]["1.0"]["b"]	
				b20b = b_calib_data_from_json_file["calibration"]["B"]["1.5"]["b"]	
				b25b = b_calib_data_from_json_file["calibration"]["B"]["2.0"]["b"]	
				
				with open(self.image_path+"rgb_result.json") as json_file:
					b_rgb_json_file = json.load(json_file)	
																				
				b_res_r = b_rgb_json_file["b_rgb"]["result_b_r"]
				b_res_g = b_rgb_json_file["b_rgb"]["result_b_g"]
				b_res_b = b_rgb_json_file["b_rgb"]["result_b_b"]

				self.machine_status_label.configure(text = "")	
				self.servicetest_FRame.destroy()				
				self.b_calib_images_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				
				basewidth = 250
				
				file = pathlib.Path(self.image_path+"bc1_00_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"bc1_00_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
				
					self.bc1_00_fulltest=Canvas(self.b_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_bc1_00_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_bc1_00_fulltest.png"))
					self.bc1_00_fulltest.place(x=10,y=30,width=180,height=180)
					self.bc1_00_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.bc1_00_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "B-0 Proper image will be loaded after calibration of device")
					pass					
				
#########################################################################################################################################

				basewidth = 250
				file = pathlib.Path(self.image_path+"bc1_025_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"bc1_025_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.bc1_025_fulltest=Canvas(self.b_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_bc1_025_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_bc1_025_fulltest.png"))
					self.bc1_025_fulltest.place(x=200,y=30,width=180,height=180)
					self.bc1_025_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.bc1_025_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "B-5 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"bc1_05_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"bc1_05_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.bc1_05_fulltest=Canvas(self.b_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_bc1_05_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_bc1_05_fulltest.png"))
					self.bc1_05_fulltest.place(x=400,y=30,width=180,height=180)
					self.bc1_05_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.bc1_05_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "B-10 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"bc1_10_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"bc1_10_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.bc1_10_fulltest=Canvas(self.b_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_bc1_10_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_bc1_10_fulltest.png"))
					self.bc1_10_fulltest.place(x=10,y=200,width=180,height=180)
					self.bc1_10_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.bc1_10_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "B-15 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250
				
				file = pathlib.Path(self.image_path+"bc1_15_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"bc1_15_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.bc1_15_fulltest=Canvas(self.b_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_bc1_15_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_bc1_15_fulltest.png"))
					self.bc1_15_fulltest.place(x=200,y=200,width=180,height=180)
					self.bc1_15_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.bc1_15_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "B-20 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"bc1_20_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"bc1_20_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.bc1_20_fulltest=Canvas(self.b_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_bc1_20_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_bc1_20_fulltest.png"))
					self.bc1_20_fulltest.place(x=400,y=200,width=180,height=180)
					self.bc1_20_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.bc1_20_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "B-25 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250
				
				img = Image.open(self.image_path+"B1_fulltest.png")	
				self.kwpercent = (basewidth / float(img.size[0]))
				hsize = int((float(img.size[1]) * float(self.kwpercent)))
		
				self.B1_fulltest=Canvas(self.b_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
				img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
				img.save(self.image_path+"resize_B1_fulltest.png")							
				img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_B1_fulltest.png"))
				self.B1_fulltest.place(x=590,y=100,width=180,height=180)
				self.B1_fulltest.img = img  # Keep reference in case this code is put into a function.
				self.B1_fulltest.create_image(0, 0, image=img, anchor=NW)
				
#######################################################################################################################################

				self.bbimages_servicetest=Button(self.b_calib_images_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.goback_servicetest_from_bimages)
				self.bbimages_servicetest.place(x=650,y=10,width=60,height=30)	
				
				self.bc0label=Label(self.b_calib_images_FRame,text="0.0",bg="#F5F4EB",fg="red",font="centre 6") 
				self.bc0label.place(x=15,y=35,width=20,height=20)
				
				self.bc05label=Label(self.b_calib_images_FRame,text="0.25",bg="#F5F4EB",fg="red",font="centre 6") 
				self.bc05label.place(x=205,y=35,width=20,height=20)
				
				self.bc10label=Label(self.b_calib_images_FRame,text="0.5",bg="#F5F4EB",fg="red",font="centre 6") 
				self.bc10label.place(x=405,y=35,width=20,height=20)
				
				self.bc15label=Label(self.b_calib_images_FRame,text="1.0",bg="#F5F4EB",fg="red",font="centre 6") 
				self.bc15label.place(x=15,y=205,width=20,height=20)
				
				self.bc20label=Label(self.b_calib_images_FRame,text="1.5",bg="#F5F4EB",fg="red",font="centre 6") 
				self.bc20label.place(x=205,y=205,width=20,height=20)
				
				self.bc25label=Label(self.b_calib_images_FRame,text="2.0",bg="#F5F4EB",fg="red",font="centre 6") 
				self.bc25label.place(x=405,y=205,width=20,height=20)				
				
				self.blabel=Label(self.b_calib_images_FRame,text="sample",bg="#F5F4EB",fg="red",font="centre 6") 
				self.blabel.place(x=595,y=105,width=60,height=20)
				
				b0_rgb = "(" + str(b0r) + "," + str(b0g) + "," + str(b0b) + ")"
				self.b0rgblabel=Label(self.b_calib_images_FRame,text=b0_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.b0rgblabel.place(x=10,y=170,width=180,height=20)	
				
				b5_rgb = "(" + str(b5r) + "," + str(b5g) + "," + str(b5b) + ")"
				self.b5rgblabel=Label(self.b_calib_images_FRame,text=b5_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.b5rgblabel.place(x=200,y=170,width=180,height=20)	
				
				b10_rgb = "(" + str(b10r) + "," + str(b10g) + "," + str(b10b) + ")"
				self.b10rgblabel=Label(self.b_calib_images_FRame,text=b10_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.b10rgblabel.place(x=400,y=170,width=180,height=20)		
				
				b15_rgb = "(" + str(b15r) + "," + str(b15g) + "," + str(b15b) + ")"
				self.b15rgblabel=Label(self.b_calib_images_FRame,text=b15_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.b15rgblabel.place(x=10,y=360,width=180,height=20)	
				
				b20_rgb = "(" + str(b20r) + "," + str(b20g) + "," + str(b20b) + ")"
				self.b20rgblabel=Label(self.b_calib_images_FRame,text=b20_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.b20rgblabel.place(x=200,y=360,width=180,height=20)	
				
				b25_rgb = "(" + str(b25r) + "," + str(b25g) + "," + str(b25b) + ")"
				self.b25rgblabel=Label(self.b_calib_images_FRame,text=b25_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.b25rgblabel.place(x=400,y=360,width=180,height=20)	
				
				sample_rgb_b = "(" + str(b_res_r) + "," + str(b_res_g) + "," + str(b_res_b) + ")"
				self.sample_b_rgb_label=Label(self.b_calib_images_FRame,text=sample_rgb_b,bg="#F5F4EB",fg="red",font="centre 6") 
				self.sample_b_rgb_label.place(x=600,y=260,width=180,height=20)	
				
				self.b_calib_images_FRame.place(x=10,y=40,width=780,height=390)	
			except Exception as e:
				messagebox.showerror("Calibration Image Loading Error !!!", "Error while loading b calibration images. Redirecting to HOME page...")
				self.front_page()
				errorstring = "/E-b_calib_images()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				
		def i_calib_images(self):
			try:	
				with open(self.npk_calibration_values_path) as json_file:
					i_calib_data_from_json_file = json.load(json_file)					        

				i00r = i_calib_data_from_json_file["calibration"]["I"]["0.0"]["r"]
				i05r = i_calib_data_from_json_file["calibration"]["I"]["0.5"]["r"]
				i10r = i_calib_data_from_json_file["calibration"]["I"]["1.0"]["r"]	
				i15r = i_calib_data_from_json_file["calibration"]["I"]["1.5"]["r"]	
				i20r = i_calib_data_from_json_file["calibration"]["I"]["2.0"]["r"]	

				i00g = i_calib_data_from_json_file["calibration"]["I"]["0.0"]["g"]
				i05g = i_calib_data_from_json_file["calibration"]["I"]["0.5"]["g"]
				i10g = i_calib_data_from_json_file["calibration"]["I"]["1.0"]["g"]	
				i15g = i_calib_data_from_json_file["calibration"]["I"]["1.5"]["g"]	
				i20g = i_calib_data_from_json_file["calibration"]["I"]["2.0"]["g"]		

				i00b = i_calib_data_from_json_file["calibration"]["I"]["0.0"]["b"]
				i05b = i_calib_data_from_json_file["calibration"]["I"]["0.5"]["b"]
				i10b = i_calib_data_from_json_file["calibration"]["I"]["1.0"]["b"]	
				i15b = i_calib_data_from_json_file["calibration"]["I"]["1.5"]["b"]	
				i20b = i_calib_data_from_json_file["calibration"]["I"]["2.0"]["b"]	
				
				with open(self.image_path+"rgb_result.json") as json_file:
					i_rgb_json_file = json.load(json_file)	
																				
				i_res_r = i_rgb_json_file["i_rgb"]["result_i_r"]
				i_res_g = i_rgb_json_file["i_rgb"]["result_i_g"]
				i_res_b = i_rgb_json_file["i_rgb"]["result_i_b"]

				self.machine_status_label.configure(text = "")	
				self.servicetest_FRame.destroy()				
				self.i_calib_images_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				
				basewidth = 250
				
				file = pathlib.Path(self.image_path+"ic1_00_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"ic1_00_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
				
					self.ic1_00_fulltest=Canvas(self.i_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_ic1_00_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_ic1_00_fulltest.png"))
					self.ic1_00_fulltest.place(x=10,y=30,width=180,height=180)
					self.ic1_00_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.ic1_00_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "I-0.0 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"ic1_05_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"ic1_05_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.ic1_05_fulltest=Canvas(self.i_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_ic1_05_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_ic1_05_fulltest.png"))
					self.ic1_05_fulltest.place(x=400,y=30,width=180,height=180)
					self.ic1_05_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.ic1_05_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "I-0.5 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"ic1_10_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"ic1_10_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.ic1_10_fulltest=Canvas(self.i_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_ic1_10_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_ic1_10_fulltest.png"))
					self.ic1_10_fulltest.place(x=10,y=200,width=180,height=180)
					self.ic1_10_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.ic1_10_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "I-1.0 Proper image will be loaded after calibration of device")
					pass				
				
#######################################################################################################################################	

				basewidth = 250
				
				file = pathlib.Path(self.image_path+"ic1_15_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"ic1_15_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.ic1_15_fulltest=Canvas(self.i_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_ic1_15_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_ic1_15_fulltest.png"))
					self.ic1_15_fulltest.place(x=200,y=200,width=180,height=180)
					self.ic1_15_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.ic1_15_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "I-1.5 Proper image will be loaded after calibration of device")
					pass					
				
#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"ic1_20_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"ic1_20_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.ic1_20_fulltest=Canvas(self.i_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_ic1_20_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_ic1_20_fulltest.png"))
					self.ic1_20_fulltest.place(x=400,y=200,width=180,height=180)
					self.ic1_20_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.ic1_20_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "I-2.0 Proper image will be loaded after calibration of device")
					pass				
				
#######################################################################################################################################	

				basewidth = 250
				
				img = Image.open(self.image_path+"I1_fulltest.png")	
				self.kwpercent = (basewidth / float(img.size[0]))
				hsize = int((float(img.size[1]) * float(self.kwpercent)))
		
				self.I1_fulltest=Canvas(self.i_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
				img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
				img.save(self.image_path+"resize_I1_fulltest.png")							
				img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_I1_fulltest.png"))
				self.I1_fulltest.place(x=590,y=100,width=180,height=180)
				self.I1_fulltest.img = img  # Keep reference in case this code is put into a function.
				self.I1_fulltest.create_image(0, 0, image=img, anchor=NW)
				
#######################################################################################################################################

				self.biimages_servicetest=Button(self.i_calib_images_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.goback_servicetest_from_iimages)
				self.biimages_servicetest.place(x=650,y=10,width=60,height=30)	
				
				self.ic0label=Label(self.i_calib_images_FRame,text="0.0",bg="#F5F4EB",fg="red",font="centre 6") 
				self.ic0label.place(x=15,y=35,width=20,height=20)
				
				self.ic05label=Label(self.i_calib_images_FRame,text="0.5",bg="#F5F4EB",fg="red",font="centre 6") 
				self.ic05label.place(x=405,y=35,width=20,height=20)
				
				self.ic10label=Label(self.i_calib_images_FRame,text="1.0",bg="#F5F4EB",fg="red",font="centre 6") 
				self.ic10label.place(x=15,y=205,width=20,height=20)
				
				self.ic15label=Label(self.i_calib_images_FRame,text="1.5",bg="#F5F4EB",fg="red",font="centre 6") 
				self.ic15label.place(x=205,y=205,width=20,height=20)
				
				self.ic20label=Label(self.i_calib_images_FRame,text="2.0",bg="#F5F4EB",fg="red",font="centre 6") 
				self.ic20label.place(x=405,y=205,width=20,height=20)				
				
				self.ilabel=Label(self.i_calib_images_FRame,text="sample",bg="#F5F4EB",fg="red",font="centre 6") 
				self.ilabel.place(x=595,y=105,width=60,height=20)
				
				i0_rgb = "(" + str(i00r) + "," + str(i00g) + "," + str(i00b) + ")"
				self.i0rgblabel=Label(self.i_calib_images_FRame,text=i0_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.i0rgblabel.place(x=10,y=170,width=180,height=20)	
				
				i5_rgb = "(" + str(i05r) + "," + str(i05g) + "," + str(i05b) + ")"
				self.i5rgblabel=Label(self.i_calib_images_FRame,text=i5_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.i5rgblabel.place(x=400,y=170,width=180,height=20)	
				
				i10_rgb = "(" + str(i10r) + "," + str(i10g) + "," + str(i10b) + ")"
				self.i10rgblabel=Label(self.i_calib_images_FRame,text=i10_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.i10rgblabel.place(x=10,y=360,width=180,height=20)		
				
				i15_rgb = "(" + str(i15r) + "," + str(i15g) + "," + str(i15b) + ")"
				self.i15rgblabel=Label(self.i_calib_images_FRame,text=i15_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.i15rgblabel.place(x=200,y=360,width=180,height=20)	
				
				i20_rgb = "(" + str(i20r) + "," + str(i20g) + "," + str(i20b) + ")"
				self.i20rgblabel=Label(self.i_calib_images_FRame,text=i20_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.i20rgblabel.place(x=400,y=360,width=180,height=20)	
				
				sample_rgb_i = "(" + str(i_res_r) + "," + str(i_res_g) + "," + str(i_res_b) + ")"
				self.sample_i_rgb_label=Label(self.i_calib_images_FRame,text=sample_rgb_i,bg="#F5F4EB",fg="red",font="centre 6") 
				self.sample_i_rgb_label.place(x=600,y=260,width=180,height=20)	
				
				self.i_calib_images_FRame.place(x=10,y=40,width=780,height=390)	
			except Exception as e:
				messagebox.showerror("Calibration Image Loading Error !!!", "Error while loading b calibration images. Redirecting to HOME page...")
				self.front_page()
				errorstring = "/E-i_calib_images()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
				
		def oc_calib_images(self):
			try:	
				with open(self.npk_calibration_values_path) as json_file:
					oc_calib_data_from_json_file = json.load(json_file)					        

				oc00r = oc_calib_data_from_json_file["calibration"]["OC"]["0.0"]["r"]
				oc025r = oc_calib_data_from_json_file["calibration"]["OC"]["0.25"]["r"]
				oc05r = oc_calib_data_from_json_file["calibration"]["OC"]["0.5"]["r"]
				oc075r = oc_calib_data_from_json_file["calibration"]["OC"]["0.75"]["r"]	
				oc10r = oc_calib_data_from_json_file["calibration"]["OC"]["1.0"]["r"]					

				oc00g = oc_calib_data_from_json_file["calibration"]["OC"]["0.0"]["g"]
				oc025g = oc_calib_data_from_json_file["calibration"]["OC"]["0.25"]["g"]
				oc05g = oc_calib_data_from_json_file["calibration"]["OC"]["0.5"]["g"]
				oc075g = oc_calib_data_from_json_file["calibration"]["OC"]["0.75"]["g"]	
				oc10g = oc_calib_data_from_json_file["calibration"]["OC"]["1.0"]["g"]					

				oc00b = oc_calib_data_from_json_file["calibration"]["OC"]["0.0"]["b"]
				oc025b = oc_calib_data_from_json_file["calibration"]["OC"]["0.25"]["b"]
				oc05b = oc_calib_data_from_json_file["calibration"]["OC"]["0.5"]["b"]
				oc075b = oc_calib_data_from_json_file["calibration"]["OC"]["0.75"]["b"]	
				oc10b = oc_calib_data_from_json_file["calibration"]["OC"]["1.0"]["b"]					
				
				with open(self.image_path+"rgb_result.json") as json_file:
					oc_rgb_json_file = json.load(json_file)	
																				
				oc_res_r = oc_rgb_json_file["oc_rgb"]["result_oc_r"]
				oc_res_g = oc_rgb_json_file["oc_rgb"]["result_oc_g"]
				oc_res_b = oc_rgb_json_file["oc_rgb"]["result_oc_b"]

				self.machine_status_label.configure(text = "")	
				self.servicetest_FRame.destroy()				
				self.oc_calib_images_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				
				basewidth = 250
				
				file = pathlib.Path(self.image_path+"occ1_00_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"occ1_00_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
				
					self.occ1_00_fulltest=Canvas(self.oc_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_occ1_00_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_occ1_00_fulltest.png"))
					self.occ1_00_fulltest.place(x=10,y=30,width=180,height=180)
					self.occ1_00_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.occ1_00_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "OC-0 Proper image will be loaded after calibration of device")
					pass

#########################################################################################################################################

				basewidth = 250
				file = pathlib.Path(self.image_path+"occ1_025_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"occ1_025_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.occ1_025_fulltest=Canvas(self.oc_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_occ1_025_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_occ1_025_fulltest.png"))
					self.occ1_025_fulltest.place(x=200,y=30,width=180,height=180)
					self.occ1_025_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.occ1_025_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "OC-0.25 Proper image will be loaded after calibration of device")
					pass

#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"occ1_05_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"occ1_05_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.bc1_05_fulltest=Canvas(self.oc_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_occ1_05_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_occ1_05_fulltest.png"))
					self.occ1_05_fulltest.place(x=400,y=30,width=180,height=180)
					self.occ1_05_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.occ1_05_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "OC-0.5 Proper image will be loaded after calibration of device")
					pass

#######################################################################################################################################	

				basewidth = 250

				file = pathlib.Path(self.image_path+"occ1_075_fulltest.png")
				if file.exists ():						
					img = Image.open(self.image_path+"occ1_075_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.occ1_10_fulltest=Canvas(self.oc_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_occ1_075_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_occ1_075_fulltest.png"))
					self.occ1_10_fulltest.place(x=10,y=200,width=180,height=180)
					self.occ1_10_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.occ1_10_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "OC-0.75 Proper image will be loaded after calibration of device")
					pass

#######################################################################################################################################	

				basewidth = 250
				
				file = pathlib.Path(self.image_path+"occ1_10_fulltest.png")
				if file.exists ():				
					img = Image.open(self.image_path+"occ1_10_fulltest.png")	
					self.kwpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1]) * float(self.kwpercent)))
			
					self.occ1_15_fulltest=Canvas(self.oc_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
					img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
					img.save(self.image_path+"resize_occ1_10_fulltest.png")							
					img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_occ1_10_fulltest.png"))
					self.occ1_15_fulltest.place(x=200,y=200,width=180,height=180)
					self.occ1_15_fulltest.img = img  # Keep reference in case this code is put into a function.
					self.occ1_15_fulltest.create_image(0, 0, image=img, anchor=NW)
				else:
					messagebox.showinfo("Calibration required", "OC-1.0 Proper image will be loaded after calibration of device")
					pass

#######################################################################################################################################	

				basewidth = 250
				
				img = Image.open(self.image_path+"OC1_fulltest.png")	
				self.kwpercent = (basewidth / float(img.size[0]))
				hsize = int((float(img.size[1]) * float(self.kwpercent)))
		
				self.OC1_fulltest=Canvas(self.oc_calib_images_FRame,width=basewidth, height=hsize,borderwidth=0, highlightthickness=0, bg="#F5F4EB")
				img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
				img.save(self.image_path+"resize_OC1_fulltest.png")							
				img = ImageTk.PhotoImage(Image.open(self.image_path+"resize_OC1_fulltest.png"))
				self.OC1_fulltest.place(x=590,y=100,width=180,height=180)
				self.OC1_fulltest.img = img  # Keep reference in case this code is put into a function.
				self.OC1_fulltest.create_image(0, 0, image=img, anchor=NW)
				
#######################################################################################################################################

				self.bocimages_servicetest=Button(self.oc_calib_images_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.goback_servicetest_from_ocimages)
				self.bocimages_servicetest.place(x=650,y=10,width=60,height=30)	
				
				self.occ0label=Label(self.oc_calib_images_FRame,text="0.0",bg="#F5F4EB",fg="red",font="centre 6") 
				self.occ0label.place(x=15,y=35,width=20,height=20)
				
				self.occ10label=Label(self.oc_calib_images_FRame,text="0.25",bg="#F5F4EB",fg="red",font="centre 6") 
				self.occ10label.place(x=405,y=35,width=20,height=20)
				
				self.occ15label=Label(self.oc_calib_images_FRame,text="0.5",bg="#F5F4EB",fg="red",font="centre 6") 
				self.occ15label.place(x=15,y=205,width=20,height=20)
				
				self.occ20label=Label(self.oc_calib_images_FRame,text="0.75",bg="#F5F4EB",fg="red",font="centre 6") 
				self.occ20label.place(x=205,y=205,width=20,height=20)
				
				self.occ25label=Label(self.oc_calib_images_FRame,text="1.0",bg="#F5F4EB",fg="red",font="centre 6") 
				self.occ25label.place(x=405,y=205,width=20,height=20)				
				
				self.oclabel=Label(self.oc_calib_images_FRame,text="sample",bg="#F5F4EB",fg="red",font="centre 6") 
				self.oclabel.place(x=595,y=105,width=60,height=20)
				
				oc0_rgb = "(" + str(oc00r) + "," + str(oc00g) + "," + str(oc00b) + ")"
				self.oc0rgblabel=Label(self.oc_calib_images_FRame,text=oc0_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.oc0rgblabel.place(x=10,y=170,width=180,height=20)	
				
				oc5_rgb = "(" + str(oc025r) + "," + str(oc025g) + "," + str(oc025b) + ")"
				self.oc5rgblabel=Label(self.oc_calib_images_FRame,text=oc5_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.oc5rgblabel.place(x=200,y=170,width=180,height=20)	
				
				oc10_rgb = "(" + str(oc05r) + "," + str(oc05g) + "," + str(oc05b) + ")"
				self.oc10rgblabel=Label(self.oc_calib_images_FRame,text=oc10_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.oc10rgblabel.place(x=400,y=170,width=180,height=20)		
				
				oc15_rgb = "(" + str(oc075r) + "," + str(oc075g) + "," + str(oc075b) + ")"
				self.oc15rgblabel=Label(self.oc_calib_images_FRame,text=oc15_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.oc15rgblabel.place(x=10,y=360,width=180,height=20)	
				
				oc20_rgb = "(" + str(oc10r) + "," + str(oc10g) + "," + str(oc10b) + ")"
				self.oc20rgblabel=Label(self.oc_calib_images_FRame,text=oc20_rgb,bg="#F5F4EB",fg="red",font="centre 6") 
				self.oc20rgblabel.place(x=200,y=360,width=180,height=20)	
				
				sample_rgb_oc = "(" + str(oc_res_r) + "," + str(oc_res_g) + "," + str(oc_res_b) + ")"
				self.sample_oc_rgb_label=Label(self.oc_calib_images_FRame,text=sample_rgb_oc,bg="#F5F4EB",fg="red",font="centre 6") 
				self.sample_oc_rgb_label.place(x=600,y=260,width=180,height=20)	
				
				self.oc_calib_images_FRame.place(x=10,y=40,width=780,height=390)	
			except Exception as e:
				messagebox.showerror("Calibration Image Loading Error !!!", "Error while loading b calibration images. Redirecting to HOME page...")
				self.front_page()
				errorstring = "/E-oc_calib_images()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 
								
		def goback_servicetest_from_nimages(self):
			try:
				self.n_calib_images_FRame.destroy()
				self.servicetest()
			except Exception as e:
				errorstring = "/E-goback_servicetest_from_n_images()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass	
				
		def goback_servicetest_from_pimages(self):
			try:
				self.p_calib_images_FRame.destroy()
				self.servicetest()
			except Exception as e:
				errorstring = "/E-goback_servicetest_from_p_images()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass
				
		def goback_servicetest_from_kimages(self):
			try:
				self.k_calib_images_FRame.destroy()
				self.servicetest()
			except Exception as e:
				errorstring = "/E-goback_servicetest_from_k_images()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass
				
		def goback_servicetest_from_bimages(self):
			try:
				self.b_calib_images_FRame.destroy()
				self.servicetest()
			except Exception as e:
				errorstring = "/E-goback_servicetest_from_b_images()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass															

		def goback_servicetest_from_iimages(self):
			try:
				self.i_calib_images_FRame.destroy()
				self.servicetest()
			except Exception as e:
				errorstring = "/E-goback_servicetest_from_iimages()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass															
				
		def goback_servicetest_from_ocimages(self):
			try:
				self.oc_calib_images_FRame.destroy()
				self.servicetest()
			except Exception as e:
				errorstring = "/E-goback_servicetest_from_ocimages()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass
								
		def servicetest(self):
			try:			
				self.servicetest_error_indication_flag = 1
				self.machine_status_label.configure(text = "")														
				with open(self.image_path+"pump_servo_constants.json","r+") as e:
					a=json.load(e)	
									    		
				s1constant1 = a["Servo1"]["01"]
				s1constant2 = a["Servo1"]["02"]
				s1constant3 = a["Servo1"]["03"]
				s1constant4 = a["Servo1"]["04"]
				s1constant5 = a["Servo1"]["05"]
				s1constant6 = a["Servo1"]["06"]
				s1constant7 = a["Servo1"]["07"]
				s1constant8 = a["Servo1"]["08"]
				s1constant9 = a["Servo1"]["09"]
				s1constant10 = a["Servo1"]["10"]
				s1constant11 = a["Servo1"]["11"]
				s1constant12 = a["Servo1"]["12"]
				s1constant13 = a["Servo1"]["13"]
				
				dconstant1 = a["D"]["01"]
				dconstant2 = a["D"]["02"]
				dconstant3 = a["D"]["03"]
				dconstant4 = a["D"]["04"]
				dconstant5 = a["D"]["05"]
				dconstant6 = a["D"]["06"]
				dconstant7 = a["D"]["07"]
				dconstant8 = a["D"]["08"]
				dconstant9 = a["D"]["09"]
				dconstant10 = a["D"]["10"]
				dconstant11 = a["D"]["11"]
				dconstant12 = a["D"]["12"]
				dconstant13 = a["D"]["13"]
				dconstant14 = a["D"]["14"]
				dconstant15 = a["D"]["15"]
				dconstant16 = a["D"]["16"]								
				
				mlconstant1 = a["M"]["01"]
				mlconstant2 = a["M"]["02"]
				mlconstant3 = a["M"]["03"]
				mlconstant4 = a["M"]["04"]
				mlconstant5 = a["M"]["05"]
				mlconstant6 = a["M"]["06"]
				mlconstant7 = a["M"]["07"]
				mlconstant8 = a["M"]["08"]
				mlconstant9 = a["M"]["09"]
				mlconstant10 = a["M"]["10"]
				mlconstant11 = a["M"]["11"]
				mlconstant12 = a["M"]["12"]
				mlconstant13 = a["M"]["13"]
				mlconstant14 = a["M"]["14"]
				mlconstant15 = a["M"]["15"]
				mlconstant16 = a["M"]["16"]								
				
				self.servicetest_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)
				canvas=Canvas(self.servicetest_FRame,bg="#F5F4EB")
				canvas.create_rectangle(5, 5, 315, 145, outline="#fb0",fill="#F5F4EB")	
				
				self.servicetest_listboxx=Listbox(self.servicetest_FRame,selectmode=SINGLE,width=10,height=5,font=("Calibri",8),exportselection=0)
				self.servicetest_listboxx.insert(1,"P1-FSS")
				self.servicetest_listboxx.insert(2,"P2-K-A")
				self.servicetest_listboxx.insert(3,"P3-K-B")
				self.servicetest_listboxx.insert(4,"P4-DW")
				self.servicetest_listboxx.insert(5,"P5-P")
				self.servicetest_listboxx.insert(6,"P6-B-A")
				self.servicetest_listboxx.insert(7,"P7-SW")
				self.servicetest_listboxx.insert(8,"P8-B-B")
				self.servicetest_listboxx.insert(9,"P9-ES")
				self.servicetest_listboxx.insert(10,"P10-DWTop")
				self.servicetest_listboxx.insert(11,"P11-I-A")
				self.servicetest_listboxx.insert(12,"P12-I-B")								
				self.servicetest_listboxx.insert(13,"P13-N-A")
				self.servicetest_listboxx.insert(14,"P14-N-B")								
								
				self.servicetest_listboxx.selection_set(0)
				
				self.dorml_listboxx=Listbox(self.servicetest_FRame,selectmode=SINGLE,width=10,height=5,font=("Calibri",8),exportselection=0)
				self.dorml_listboxx.insert(1,"d")
				self.dorml_listboxx.insert(2,"ml")
				self.dorml_listboxx.selection_set(0)					

				self.quantity_listboxx=Listbox(self.servicetest_FRame,selectmode=SINGLE,width=10,height=5,font=("Calibri",8),exportselection=0)
				self.quantity_listboxx.insert(1,"01")
				self.quantity_listboxx.insert(2,"02")
				self.quantity_listboxx.insert(3,"03")
				self.quantity_listboxx.insert(4,"04")	
				self.quantity_listboxx.insert(5,"05")
				self.quantity_listboxx.insert(6,"06")
				self.quantity_listboxx.insert(7,"07")
				self.quantity_listboxx.insert(8,"08")
				self.quantity_listboxx.insert(9,"09")
				self.quantity_listboxx.insert(10,"10")
				self.quantity_listboxx.insert(11,"11")
				self.quantity_listboxx.insert(12,"12")
				self.quantity_listboxx.insert(13,"13")
				self.quantity_listboxx.insert(14,"14")
				self.quantity_listboxx.insert(15,"15")
				self.quantity_listboxx.selection_set(0)				
				
				l1select = self.dorml_listboxx.bind('<<ListboxSelect>>',self.onselect1)
				l2select = self.quantity_listboxx.bind('<<ListboxSelect>>',self.onselect2)
																	
				canvas.place(x=80,y=60,width=320,height=150)
				
				canvas3=Canvas(self.servicetest_FRame,bg="#F5F4EB")
				canvas3.create_rectangle(5, 5, 315, 145, outline="#fb0",fill="#F5F4EB")
				
				self.servo_listboxx=Listbox(self.servicetest_FRame,selectmode=SINGLE,width=10,height=5,font=("Calibri",8),exportselection=0)
				self.servo_listboxx.insert(1,"Servo-M")
				self.servo_listboxx.insert(2,"LED")
				self.servo_listboxx.insert(3,"CAMERA")
				self.servo_listboxx.insert(4,"TEST")

				self.servo_listboxx.selection_set(0)				

				self.servo_pos_listboxx=Listbox(self.servicetest_FRame,selectmode=SINGLE,width=10,height=5,font=("Calibri",8),exportselection=0)
				self.servo_pos_listboxx.insert(1,"01")
				self.servo_pos_listboxx.insert(2,"02")
				self.servo_pos_listboxx.insert(3,"03")
				self.servo_pos_listboxx.insert(4,"04")	
				self.servo_pos_listboxx.insert(5,"05")
				self.servo_pos_listboxx.insert(6,"06")
				self.servo_pos_listboxx.insert(7,"07")
				self.servo_pos_listboxx.insert(8,"08")
				self.servo_pos_listboxx.insert(9,"09")
				self.servo_pos_listboxx.insert(10,"10")
				self.servo_pos_listboxx.insert(11,"11")
				self.servo_pos_listboxx.insert(12,"12")
				self.servo_pos_listboxx.insert(13,"13")
				self.servo_pos_listboxx.selection_set(0)	
				
				l3select = self.servo_listboxx.bind('<<ListboxSelect>>',self.onselect3)			
																
				canvas3.place(x=80,y=210,width=320,height=150)					
									
				canvas2=Canvas(self.servicetest_FRame,bg="#F5F4EB")
				canvas2.create_rectangle(5, 5, 315, 295, outline="#fb0",fill="#F5F4EB")		
				
				self.incdec_servicetest_listboxx=Listbox(self.servicetest_FRame,selectmode=SINGLE,width=7,height=12,font=("Calibri",8),exportselection=0)
				self.incdec_servicetest_listboxx.insert(1,"P1-FSS")
				self.incdec_servicetest_listboxx.insert(2,"P2-K-A")
				self.incdec_servicetest_listboxx.insert(3,"P3-K-B")
				self.incdec_servicetest_listboxx.insert(4,"P4-DW")
				self.incdec_servicetest_listboxx.insert(5,"P5-P")
				self.incdec_servicetest_listboxx.insert(6,"P6-B-A")
				self.incdec_servicetest_listboxx.insert(7,"P7-SW")
				self.incdec_servicetest_listboxx.insert(8,"P8-B-B")
				self.incdec_servicetest_listboxx.insert(9,"P9-ES")
				self.incdec_servicetest_listboxx.insert(10,"P10-DWTop")
				self.incdec_servicetest_listboxx.insert(11,"P11-I-A")
				self.incdec_servicetest_listboxx.insert(12,"P12-I-B")
				self.incdec_servicetest_listboxx.insert(13,"P13-N-A")
				self.incdec_servicetest_listboxx.insert(14,"P14-N-B")																
				self.incdec_servicetest_listboxx.insert(15,"Servo1")

				self.incdec_servicetest_listboxx.selection_set(0)
				
				l3select = self.incdec_servicetest_listboxx.bind('<<ListboxSelect>>',self.onselect_incdec_servo_constants)				
				
				self.incdec_dorml_listboxx=Listbox(self.servicetest_FRame,selectmode=SINGLE,width=3,height=12,font=("Calibri",8),exportselection=0)
				self.incdec_dorml_listboxx.insert(1,"d")
				self.incdec_dorml_listboxx.insert(2,"ml")
				self.incdec_dorml_listboxx.selection_set(0)
												
				canvas2.place(x=400,y=60,width=320,height=300)
									
				self.bconfirm_service=Button(self.servicetest_FRame,text="Send",bg="blue",font="centre 8",fg="white",command=self.servicetest_instructions)
				
				self.binc=Button(self.servicetest_FRame,text="INC",bg="blue",font="centre 8",fg="white",command=self.incconstant)
				
				self.bdec=Button(self.servicetest_FRame,text="DEC",bg="blue",font="centre 8",fg="white",command=self.decconstant)										
				self.servicetest_FRame.place(x=10,y=40,width=780,height=390)
				
				self.bservotest=Button(self.servicetest_FRame,text="Send",bg="blue",font="centre 8",fg="white",command=self.servo_motor_test)	
				
				self.ecorphvaluelabel=Label(self.servicetest_FRame,text="EC / PH Test values",bg="#F5F4EB",fg="red",font="centre 6") 
				self.ecorphvaluelabel.place(x=100, y=320,height=30,width=200)									
				
				self.servicestatustext = ""
				
				d = "d"
				self.dlabelname=Label(self.servicetest_FRame,text=d,bg="green",fg="#F5F4EB",font="BOLD 8") 
				self.dlabelname.place(x=545,y=75)
				
				d = "ml"
				self.mllabelname=Label(self.servicetest_FRame,text=d,bg="green",fg="#F5F4EB",font="BOLD 8") 
				self.mllabelname.place(x=585,y=75)					
				
				self.dpumpconstlabel1=Label(self.servicetest_FRame,text=dconstant1,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel1.place(x=535,y=102)					
				
				self.mlpumpconstlabel1=Label(self.servicetest_FRame,text=mlconstant1,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.mlpumpconstlabel1.place(x=580,y=102)	
				
				self.dpumpconstlabel2=Label(self.servicetest_FRame,text=dconstant2,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel2.place(x=535,y=117)					
				
				self.mlpumpconstlabel2=Label(self.servicetest_FRame,text=mlconstant2,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.mlpumpconstlabel2.place(x=580,y=117)	
				
				self.dpumpconstlabel3=Label(self.servicetest_FRame,text=dconstant3,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel3.place(x=535,y=132)					
				
				self.mlpumpconstlabel3=Label(self.servicetest_FRame,text=mlconstant3,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.mlpumpconstlabel3.place(x=580,y=132)			
				
				self.dpumpconstlabel4=Label(self.servicetest_FRame,text=dconstant4,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel4.place(x=535,y=147)					
				
				self.mlpumpconstlabel4=Label(self.servicetest_FRame,text=mlconstant4,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.mlpumpconstlabel4.place(x=580,y=147)													
				
				self.dpumpconstlabel5=Label(self.servicetest_FRame,text=dconstant5,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel5.place(x=535,y=162)					
				
				self.mlpumpconstlabel5=Label(self.servicetest_FRame,text=mlconstant5,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.mlpumpconstlabel5.place(x=580,y=162)	
				
				self.dpumpconstlabel6=Label(self.servicetest_FRame,text=dconstant6,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel6.place(x=535,y=177)					
				
				self.mlpumpconstlabel6=Label(self.servicetest_FRame,text=mlconstant6,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.mlpumpconstlabel6.place(x=580,y=177)		
				
				self.dpumpconstlabel7=Label(self.servicetest_FRame,text=dconstant7,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel7.place(x=535,y=192)					
				
				self.mlpumpconstlabel7=Label(self.servicetest_FRame,text=mlconstant7,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.mlpumpconstlabel7.place(x=580,y=192)	
				
				self.dpumpconstlabel8=Label(self.servicetest_FRame,text=dconstant8,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel8.place(x=535,y=207)					
				
				self.mlpumpconstlabel8=Label(self.servicetest_FRame,text=mlconstant8,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.mlpumpconstlabel8.place(x=580,y=207)	
				
				self.dpumpconstlabel9=Label(self.servicetest_FRame,text=dconstant9,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel9.place(x=535,y=222)					
				
				self.mlpumpconstlabel9=Label(self.servicetest_FRame,text=mlconstant9,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.mlpumpconstlabel9.place(x=580,y=222)
				
				self.dpumpconstlabel10=Label(self.servicetest_FRame,text=dconstant10,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel10.place(x=535,y=237)					
				
				self.mlpumpconstlabel10=Label(self.servicetest_FRame,text=mlconstant10,bg="#F5F4EB",fg="green",font="BOLD  8") 
				self.mlpumpconstlabel10.place(x=580,y=237)		
				
				self.dpumpconstlabel11=Label(self.servicetest_FRame,text=dconstant10,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel11.place(x=535,y=252)					
				
				self.mlpumpconstlabel11=Label(self.servicetest_FRame,text=mlconstant10,bg="#F5F4EB",fg="green",font="BOLD  8") 
				self.mlpumpconstlabel11.place(x=580,y=252)	
				
				self.dpumpconstlabel12=Label(self.servicetest_FRame,text=dconstant10,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel12.place(x=535,y=267)					
				
				self.mlpumpconstlabel12=Label(self.servicetest_FRame,text=mlconstant10,bg="#F5F4EB",fg="green",font="BOLD  8") 
				self.mlpumpconstlabel12.place(x=580,y=267)
				
				self.dpumpconstlabel13=Label(self.servicetest_FRame,text=dconstant10,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel13.place(x=535,y=282)					
				
				self.mlpumpconstlabel13=Label(self.servicetest_FRame,text=mlconstant10,bg="#F5F4EB",fg="green",font="BOLD  8") 
				self.mlpumpconstlabel13.place(x=580,y=282)		
				
				self.dpumpconstlabel14=Label(self.servicetest_FRame,text=dconstant10,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.dpumpconstlabel14.place(x=535,y=297)					
				
				self.mlpumpconstlabel14=Label(self.servicetest_FRame,text=mlconstant10,bg="#F5F4EB",fg="green",font="BOLD  8") 
				self.mlpumpconstlabel14.place(x=580,y=297)		
				
##########################################################################################################################################
				d = "S1"
				self.s1labelname=Label(self.servicetest_FRame,text=d,bg="green",fg="#F5F4EB",font="BOLD 8") 
				self.s1labelname.place(x=635,y=75)
								
				self.servoconstlabel1=Label(self.servicetest_FRame,text=s1constant1,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel1.place(x=635,y=102)					
								
				self.servoconstlabel2=Label(self.servicetest_FRame,text=s1constant2,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel2.place(x=635,y=116)					
								
				self.servoconstlabel3=Label(self.servicetest_FRame,text=s1constant3,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel3.place(x=635,y=130)					
								
				self.servoconstlabel4=Label(self.servicetest_FRame,text=s1constant4,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel4.place(x=635,y=144)					
									
				self.servoconstlabel5=Label(self.servicetest_FRame,text=s1constant5,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel5.place(x=635,y=158)					
									
				self.servoconstlabel6=Label(self.servicetest_FRame,text=s1constant6,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel6.place(x=635,y=172)					
									
				self.servoconstlabel7=Label(self.servicetest_FRame,text=s1constant7,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel7.place(x=635,y=186)					
				
				self.servoconstlabel8=Label(self.servicetest_FRame,text=s1constant8,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel8.place(x=635,y=200)	
				
				self.servoconstlabel9=Label(self.servicetest_FRame,text=s1constant9,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel9.place(x=635,y=214)
				
				self.servoconstlabel10=Label(self.servicetest_FRame,text=s1constant10,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel10.place(x=635,y=228)

				self.servoconstlabel11=Label(self.servicetest_FRame,text=s1constant11,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel11.place(x=635,y=242)	
					
				self.servoconstlabel12=Label(self.servicetest_FRame,text=s1constant12,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel12.place(x=635,y=256)	

				self.servoconstlabel13=Label(self.servicetest_FRame,text=s1constant13,bg="#F5F4EB",fg="green",font="BOLD  8 ") 
				self.servoconstlabel13.place(x=635,y=270)	
					
				
##########################################################################################################################################																						
				
				self.bsoftware_update=Button(self.servicetest_FRame,text="Software Update",bg="red",font="centre 8",fg="white",command=self.software_update)

				self.blog=Button(self.servicetest_FRame,text="LOG",bg="red",font="centre 8",fg="white",command=self.logger_log)

				
				self.bcalibInServicetest=Button(self.servicetest_FRame,text="Dashboard",bg="red",font="centre 8",fg="white",command=self.goback_home_from_servicetest)				

				self.bcameratest=Button(self.servicetest_FRame,text="N-P-B-I",bg="red",font="centre 8",fg="white",command=self.cameratest)
				self.bkcameratest=Button(self.servicetest_FRame,text="K",bg="red",font="centre 8",fg="white",command=self.kcameratest)
				self.bncalibimages=Button(self.servicetest_FRame,text="N",bg="red",font="centre 8",fg="white",command=self.n_calib_images)
				self.bpcalibimages=Button(self.servicetest_FRame,text="P",bg="red",font="centre 8",fg="white",command=self.p_calib_images)
				self.bkcalibimages=Button(self.servicetest_FRame,text="K",bg="red",font="centre 8",fg="white",command=self.k_calib_images)
				self.bbcalibimages=Button(self.servicetest_FRame,text="B",bg="red",font="centre 8",fg="white",command=self.b_calib_images)
				self.bicalibimages=Button(self.servicetest_FRame,text="I",bg="red",font="centre 8",fg="white",command=self.i_calib_images)
				#self.boccalibimages=Button(self.servicetest_FRame,text="OC",bg="red",font="centre 8",fg="white",command=self.oc_calib_images)
				
				
				self.servicetest_listboxx.place(x=100,y=82)
				self.dorml_listboxx.place(x=200,y=82)
				self.quantity_listboxx.place(x=300,y=82)
				
				self.servo_listboxx.place(x=100,y=232)

				self.servo_pos_listboxx.place(x=200,y=232)					
				
				self.incdec_servicetest_listboxx.place(x=420,y=102)
				self.incdec_dorml_listboxx.place(x=490,y=102)

				self.bncalibimages.place(x=125,y=15,height=20,width=20)
				self.bpcalibimages.place(x=155,y=15,height=20,width=20)
				self.bkcalibimages.place(x=185,y=15,height=20,width=20)	
				self.bbcalibimages.place(x=215,y=15,height=20,width=20)	
				self.bicalibimages.place(x=245,y=15,height=20,width=20)					
				#self.boccalibimages.place(x=275,y=15,height=20,width=20)	
								
				self.blog.place(x=360,y=15,height=20,width=30)	
											
				self.bkcameratest.place(x=402,y=15,height=20,width=20)
				self.bcameratest.place(x=430,y=15,height=20,width=60)	
				self.bsoftware_update.place(x=492,y=15,height=20,width=120)	
				self.bcalibInServicetest.place(x=630,y=15,height=20,width=70)
																				
				self.bconfirm_service.place(x=320,y=170,height=20,width=40)	
				self.bservotest.place(x=320, y=320,height=20,width=40)
				self.binc.place(x=480,y=320,height=20,width=40)
				self.bdec.place(x=600,y=320,height=20,width=40)		
				
				#self.root.mainloop()
			except Exception as e:
				self.front_page()
				errorstring = "/E-servicetest()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass 	
					
		def settings_instructions(self):
			try:
				self.bconfirm_init_setting['state']=DISABLED

				self.machine_status_label.configure(text = "")
				servicetest_lst_values = [self.servicetest_listboxx.get(idx) for idx in self.servicetest_listboxx.curselection()] 

				if servicetest_lst_values[0]=="Pump4 - Distilled water":
					self.machine_status_label.configure(text = "")
					self.kt_sendcommand("KT+MOVSERVO1:08\r\n",1,10)						 
					texttosend="KT+DISPENSEM:04+02\r\n"
					dispense_ret_val = self.kt_sendcommand(texttosend,4,10)	
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL								
																	
				if servicetest_lst_values[0]=="Pump9 - Extraction solution (top)": 
					texttosend="KT+EXTDISPENSEM:09+02\r\n"
					dispense_ret_val = self.kt_send_external_command(texttosend,4,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL								
																					
				if servicetest_lst_values[0]=="Pump10 - Distilled water (top)":
					texttosend="KT+EXTDISPENSEM:10+02\r\n"
					dispense_ret_val = self.kt_send_external_command(texttosend,4,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL

				if servicetest_lst_values[0]=="Pump13 - Nitrogen A":
					texttosend="KT+EXTDISPENSEM:13+02\r\n"
					dispense_ret_val = self.kt_send_external_command(texttosend,4,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL
																				
				if servicetest_lst_values[0]=="Pump14 - Nitrogen B":
					texttosend="KT+EXTDISPENSEM:14+02\r\n"
					dispense_ret_val = self.kt_send_external_command(texttosend,4,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL

				if servicetest_lst_values[0]=="Pump1 - Filtered Sample Solution":
					pumpnotosend = "01"
					self.kt_sendcommand("KT+MOVSERVO1:07\r\n",1,10)
					texttosend = "KT+DISPENSE" + "D:"+ pumpnotosend + "+01" + "\r\n"
					dispense_ret_val = self.kt_sendcommand(texttosend,2,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL								
						
				if servicetest_lst_values[0]=="Pump2 - Potassium A":
					pumpnotosend = "02"
					self.kt_sendcommand("KT+MOVSERVO1:07\r\n",1,10)
					texttosend = "KT+DISPENSE" + "D:"+ pumpnotosend + "+01" + "\r\n"
					dispense_ret_val = self.kt_sendcommand(texttosend,2,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL								
					
				if servicetest_lst_values[0]=="Pump3 - Potassium B":
					pumpnotosend = "03"
					self.kt_sendcommand("KT+MOVSERVO1:08\r\n",1,10)	
					texttosend = "KT+DISPENSE" + "D:"+ pumpnotosend + "+01" + "\r\n"
					dispense_ret_val = self.kt_sendcommand(texttosend,2,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL									
												
				if servicetest_lst_values[0]=="Pump5 - Phosphrous":
					pumpnotosend = "05"
					self.kt_sendcommand("KT+MOVSERVO1:09\r\n",1,10)
					texttosend = "KT+DISPENSE" + "D:"+ pumpnotosend + "+01" + "\r\n"
					dispense_ret_val = self.kt_sendcommand(texttosend,2,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL									
													
				if servicetest_lst_values[0]=="Pump6 - Boron A":
					pumpnotosend = "06"
					self.kt_sendcommand("KT+MOVSERVO1:03\r\n",1,10)	
					texttosend = "KT+DISPENSE" + "D:"+ pumpnotosend + "+01" + "\r\n"
					dispense_ret_val = self.kt_sendcommand(texttosend,2,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL							
												
				if servicetest_lst_values[0]=="Pump7 - Filter Wash (Inside)":
					pumpnotosend = "07"
					texttosend = "KT+DISPENSE" + "D:"+ pumpnotosend + "+01" + "\r\n"
					dispense_ret_val = self.kt_sendcommand(texttosend,2,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL							
					
				if servicetest_lst_values[0]=="Pump8 - Boron B":
					pumpnotosend = "08"	
					self.kt_sendcommand("KT+MOVSERVO1:03\r\n",1,10)	
					texttosend = "KT+DISPENSE" + "D:"+ pumpnotosend + "+01" + "\r\n"
					dispense_ret_val = self.kt_sendcommand(texttosend,2,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL		
						
				if servicetest_lst_values[0]=="Pump11 - Iron A":
					pumpnotosend = "11"	
					self.kt_sendcommand("KT+MOVSERVO1:04\r\n",1,10)	
					texttosend = "KT+DISPENSE" + "D:"+ pumpnotosend + "+01" + "\r\n"
					dispense_ret_val = self.kt_sendcommand(texttosend,2,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL	
						
				if servicetest_lst_values[0]=="Pump12 - Iron B":
					pumpnotosend = "12"	
					self.kt_sendcommand("KT+MOVSERVO1:04\r\n",1,10)	
					texttosend = "KT+DISPENSE" + "D:"+ pumpnotosend + "+01" + "\r\n"
					dispense_ret_val = self.kt_sendcommand(texttosend,2,10)
					if (dispense_ret_val == "SUCCESS"):
						self.bconfirm_init_setting['state']=NORMAL													
																		
			except (KeyError, ZeroDivisionError, serial.SerialException, ValueError) as e:
				self.bconfirm_init_setting['state']=NORMAL
				errorstring = "/E-setting_instructions()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				self.bconfirm_init_setting['state']=NORMAL			
				pass        						                  
																					 													
		def init_settings(self):
			try:						
				self.machine_status_label.configure(text = "")

				self.servicetest_FRame=Frame(self.root,bg="#F5F4EB",highlightbackground="#254E58",highlightcolor="#254E58",highlightthickness=1)

				Mainlabel=Label(self.servicetest_FRame,text="Settings",bg="#F5F4EB",fg="#254E58",font="BOLD  20")										
				canvas=Canvas(self.servicetest_FRame,bg="#F5F4EB")
				canvas.create_rectangle(5, 5, 645, 245, outline="#fb0",fill="#F5F4EB")	

				self.servicetest_listboxx=Listbox(self.servicetest_FRame,selectmode=SINGLE,width=25,height=10,font=("Calibri",11),exportselection=0)
				self.servicetest_listboxx.insert(1,"Pump1 - Filtered Sample Solution")
				self.servicetest_listboxx.insert(2,"Pump2 - Potassium A")
				self.servicetest_listboxx.insert(3,"Pump3 - Potassium B")
				self.servicetest_listboxx.insert(4,"Pump4 - Distilled water")
				self.servicetest_listboxx.insert(5,"Pump5 - Phosphrous")
				self.servicetest_listboxx.insert(6,"Pump6 - Boron A")
				self.servicetest_listboxx.insert(7,"Pump7 - Filter Wash (Inside)")
				self.servicetest_listboxx.insert(8,"Pump8 - Boron B")
				self.servicetest_listboxx.insert(9,"Pump9 - Extraction solution (top)")
				self.servicetest_listboxx.insert(10,"Pump10 - Distilled water (top)")
				self.servicetest_listboxx.insert(11,"Pump11 - Iron A")
				self.servicetest_listboxx.insert(12,"Pump12 - Iron B")
				#self.servicetest_listboxx.insert(13,"Pump13 - Nitrogen A")
				#self.servicetest_listboxx.insert(14,"Pump14 - Nitrogen B")
								
				self.servicetest_listboxx.selection_set(0)
																						
				canvas.place(x=80,y=80,width=650,height=250)
				
				Mainlabel.place(x=360,y=20)					
				
				self.bconfirm_init_setting=Button(self.servicetest_FRame,text="Send",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.settings_instructions)
				  
				
				self.bsetting_to_dashboard=Button(self.servicetest_FRame,text="Back",bg="#3e8ddc",fg="#fffdfd",font="centre",command=self.goback_home_from_settings)
				
				self.servicetest_FRame.place(x=10,y=40,width=780,height=390)
				
				self.servicetest_listboxx.place(x=220,y=110)
																	
				self.bconfirm_init_setting.place(x=650,y=340,height=30,width=60) 
				self.bsetting_to_dashboard.place(x=650,y=40,height=30,width=60)
				
				#self.bocsample_solution.place_forget(x=260,y=15,width=50,height=20) 
				self.dispense_label.place_forget()
				self.bsample_solution.place_forget()    
				self.bdistilled_water.place_forget() 
				self.bdistilled_water_ec.place_forget()   						
				self.bstop_dispense.place_forget() 
				#self.root.mainloop()
			except (KeyError, ZeroDivisionError, serial.SerialException, ValueError) as e:
				errorstring = "/E-init_settings()"
				logging.warning("%s", errorstring)
				logging.exception("Exception occurred")
			finally:
				pass
				
		def disable_event(self):
			pass				 
		
		def __init__(self):
			try:
				self.root=Tk()
				self.root.title("Krishitantra")
				self.root.geometry('800x480')
				self.root.configure(background="#F5F4EB")
				self.root.resizable(0,0)
				
				logging.info ("App Started")
				
				self.ser = serial.Serial(port="/dev/serial0", baudrate=2400, parity='N', stopbits=1, bytesize=8, timeout=8)
				self.sem = threading.Semaphore()				
				self.msg_nitro = threading.Semaphore()
				self.es_nitro_selection = threading.Semaphore()

				self.npk_calibration_values_path = "/home/pi/kt/npk-device-addon/npk_calibration_values.json" 
				self.calibration_status_path = "/home/pi/kt/npk-device-addon/calib_status.json" 
				self.chemical_firmware_version = "/home/pi/kt/npk-device-addon/Chemical_Firmware_V1.0.json" 
				self.result_path = "/home/pi/kt/npk-device-addon/result.json" 
				self.firmware_update_path = "/home/pi/kt/npkbi"
				self.image_path = "/home/pi/kt/npk-device-addon/"
				self.logpath = "/home/pi/kt/"
				
				self.internet_conn_label=Label(self.root,text="No Internet",bg="#F5F4EB",fg="red",font="BOLD  8 ")
				self.internet_conn_label.place(x=490,y=440,width=400)						
				
				timer_internet_conn = threading.Timer(0.1, self.internet_connection)
				timer_internet_conn.start()				
				
				pump_servo_constants_file = pathlib.Path(self.image_path+"pump_servo_constants.json")
				if pump_servo_constants_file.exists ():					
					with open(self.image_path+"pump_servo_constants.json","r+") as e:
						a=json.load(e)					    		

					obj=a

					with open(self.image_path+"pump_servo_constants.json","w")as e:
						json.dump(obj,e)
					
				else:
					dictionary = ({
						"D": {'01': "0.05", '02': "0.05", '03': "0.06", '04': "0.05", '05': "0.05", '06': "0.08", '07': "0.05", '08': "0.08", '09': "0.07", '10': "0.05", '11': "0.05", '12': "0.05", '13': "0.05", '14': "0.05", '15': "0.05", '16': "0.05"}, 
						"M": {'01': "1.12", '02': "1.12", '03': "1.15", '04': "1.15", '05': "1.39", '06': "1.39", '07': "1.12", '08': "1.39", '09': "1.10", '10': "1.15", '11': "1.12", '12': "1.12", '13': "1.12" , '14': "1.12", '15': "1.12", '16': "1.12"}, 
						"Servo1": {'01': "16", '02': "16", '03': "17", '04': "16", '05': "16", '06': "22", '07': "27", '08': "28", '09': "30", '10': "31", '11': "37", '12': "37", '13': "55"},
						"EC":{'K':"0.156789",'RWater':"12345",'T':"25.25"},
						"PH4":{'V':"1.12", 'T':"24.46", 'PHCONST':"4.00"},
						"PH7":{'V':"1.02", 'T':"24.46", 'PHCONST':"7.00"},
						"CONSTANB":{'A':"1.5", 'B':"2.8"}
					})
								
					with open(self.image_path+"pump_servo_constants.json","w")as e:
						json.dump(dictionary,e)
						
###########################################################################################################################################						
						
				npk_calibration_values_file = pathlib.Path(self.image_path+"npk_calibration_values.json")
				if npk_calibration_values_file.exists ():					
					with open(self.image_path+"npk_calibration_values.json","r+") as e:
						a=json.load(e)					    		

					obj=a

					with open(self.image_path+"npk_calibration_values.json","w")as e:
						json.dump(obj,e)

				else:
					dictionary = ({
									"calibration": 
										{
											"P": 
												{
													"0": {"g": 64, "r": 66, "b": 66},
													"5": {"g": 67, "r": 67, "b": 24},
													"10": {"g": 66, "r": 67, "b": 9}, 
													"15": {"g": 67, "r": 69, "b": 2}, 
													"20": {"g": 66, "r": 68, "b": 2},
													"25": {"g": 65, "r": 69, "b": 0}
												}, 
											"N": 
												{
													"0": {"g": 59, "r": 62, "b": 61},
													"5": {"g": 28, "r": 77, "b": 64}, 
													"10": {"g": 10, "r": 75, "b": 60},
													"20": {"g": 9, "r": 68, "b": 52}, 
													"30": {"g": 11, "r": 60, "b": 42}, 
													"40": {"g": 12, "r": 58, "b": 39} 
												
												}, 
											"K": 
												{
													"0": {"g": 26, "r": 25, "b": 26},
													"10": {"g": 32, "r": 31, "b": 32}, 
													"20": {"g": 37, "r": 37, "b": 37}, 
													"40": {"g": 28, "r": 27, "b": 28}
												}, 
											"I": 
												{
													"0.0": {"g": 59, "r": 62, "b": 61},
													"0.5": {"g": 28, "r": 77, "b": 64}, 
													"1.0": {"g": 10, "r": 75, "b": 60},
													"1.5": {"g": 9, "r": 68, "b": 52}, 
													"2.0": {"g": 11, "r": 60, "b": 42}
												
												},
											"B": 
												{
													"0.0": {"g": 59, "r": 62, "b": 61},
													"0.25": {"g": 28, "r": 77, "b": 64},
													"0.5": {"g": 28, "r": 77, "b": 64}, 
													"1.0": {"g": 10, "r": 75, "b": 60},
													"1.5": {"g": 9, "r": 68, "b": 52}, 
													"2.0": {"g": 11, "r": 60, "b": 42}
												
												},											
											"Z": 
												{
													"0.0": {"g": 59, "r": 62, "b": 61},
													"0.1": {"g": 59, "r": 62, "b": 61},
													"0.5": {"g": 28, "r": 77, "b": 64}, 
													"1.0": {"g": 10, "r": 75, "b": 60},
													"2.0": {"g": 9, "r": 68, "b": 52}, 
													"3.0": {"g": 11, "r": 60, "b": 42}, 
													"5.0": {"g": 12, "r": 58, "b": 39} 
												
												},
											"C": 
												{
													"0.0": {"g": 59, "r": 62, "b": 61},
													"0.2": {"g": 28, "r": 77, "b": 64}, 
													"0.4": {"g": 10, "r": 75, "b": 60},
													"0.6": {"g": 9, "r": 68, "b": 52}, 
													"0.8": {"g": 11, "r": 60, "b": 42}, 
													"1.0": {"g": 12, "r": 58, "b": 39} 
												},
											"OC": 
												{
													"0.0": {"g": 59, "r": 62, "b": 61},
													"0.25": {"g": 28, "r": 77, "b": 64}, 
													"0.5": {"g": 10, "r": 75, "b": 60},
													"0.75": {"g": 9, "r": 68, "b": 52}, 
													"1.0": {"g": 11, "r": 60, "b": 42}
												},
											"S": 
												{
													"0.0": {"g": 59, "r": 62, "b": 61},
													"0.25": {"g": 28, "r": 77, "b": 64},
													"0.5": {"g": 28, "r": 77, "b": 64}, 
													"1.0": {"g": 10, "r": 75, "b": 60},
													"1.5": {"g": 9, "r": 68, "b": 52}, 
													"2.0": {"g": 11, "r": 60, "b": 42}
												}													
										}

								})
								
					with open(self.image_path+"npk_calibration_values.json","w")as e:
						json.dump(dictionary,e)	
						
###########################################################################################################################################

				Chemical_Firmware_V1_file = pathlib.Path(self.image_path+"Chemical_Firmware_V1.0.json")
				if Chemical_Firmware_V1_file.exists ():					
					with open(self.image_path+"Chemical_Firmware_V1.0.json","r+") as e:
						a=json.load(e)					    		

					obj=a

					with open(self.image_path+"Chemical_Firmware_V1.0.json","w")as e:
						json.dump(obj,e)

				else:
					dictionary = ({
										"D1N1":"MS107+0105M+RNS10+MS113+MS107+0105M+MS111+00000+00000+00000",
                                        "D1N2":"MIX10+DL060+MIX10+DL060+00000+00000+00000+00000+00000+00000",
                                        "D1N3":"MS106+DL240+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "D1P1":"MS107+0103M+RNS10+MS113+MS107+0102M+MS108+0408M+MS109+0505D",
                                        "D1P2":"MIX10+DL150+MIX10+DL150+MS106+00000+00000+00000+00000+00000",
                                        "D1P3":"00000+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "D1K1":"MS107+0103M+RNS10+MS113+MS107+0105M+MS108+0405M+MS107+0205D",
                                        "D1K2":"MIX10+MS108+0310D+MIX10+DL200+MIX10+DL200+MIX10+DL200+MIX10",
                                        "D1K3":"MS105+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "D1I1":"MS107+0103M+RNS10+MS113+MS107+0105M+MS104+1105D+1202M+00000",
                                        "D1I2":"MIX10+DL180+MIX10+DL240+MIX10+DL180+MS106+00000+00000+00000",
                                        "D1I3":"00000+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "D1B1":"MS107+0103M+RNS10+MS113+MS107+0105M+MS103+0602M+0804M+MIX10",
                                        "D1B2":"DL180+MIX10+DL240+MIX10+DL180+MS106+00000+00000+00000+00000",
                                        "D1B3":"00000+00000+00000+00000+00000+00000+00000+00000+00000+00000",                       
                                        "D1Z1":"MS107+0105M+RNS10+MS113+MS107+0105M+0210D+MIX10+MS108+0305D",
                                        "D1Z2":"MS109+0505D+0603D+MIX10+DL180+MIX10+DL240+MIX10+DL180+MS106",
                                        "D1Z3":"00000+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "D1C1":"MS107+0103M+RNS10+MS113+MS107+0105M+MS104+0813D+MIX10+DL060",
                                        "D1C2":"MS106+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "D1C3":"00000+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "D1S1":"MS107+0105M+RNS10+MS113+MS107+0110M+MS110+1015D+11D/M+MIX10",
                                        "D1S2":"DL180+MIX10+DL240+MIX10+DL180+MS106+00000+00000+00000+00000",
                                        "D1S3":"00000+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "D1OC1":"MS107+0105M+RNS10+MS113+MS107+0105M+DL060+MS106+00000+00000",
                                        "D1OC2":"00000+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "D1OC3":"00000+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibZ1":"MS112+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibZ2":"MS107+0210D+MIX10+MS108+0305D+MS109+0505D+0603D+MIX10+DL180",
                                        "CalibZ3":"MIX10+DL240+MIX10+DL180+MS106+00000+00000+00000+00000+00000",
                                        "CalibC1":"MS112+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibC2":"MS104+0813D+MIX10+DL060+MS106+00000+00000+00000+00000+00000",
                                        "CalibS1":"MS112+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibS2":"MS110+1015D+11D/M+MIX10+DL180+MIX10+DL240+MIX10+DL180+MS106",
                                        "CalibS3":"00000+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibOC1":"MS112+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibOC2":"MIX10+DL060+MS106+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibN1":"MS112+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibN2":"00000+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibN3":"MIX20+DL060+MIX20+DL060+00000+00000+00000+00000+00000+00000",
                                        "CalibN4":"MIX20+MS106+DL240+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibP1":"MS112+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibP2":"MS109+0505D+MIX10+DL150+MIX10+DL150+MS106+00000+00000+00000",
                                        "CalibK1":"MS112+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibK2":"MS107+0205D+MIX10+MS108+0310D+MIX10+DL200+MIX10+DL200+MIX10",
                                        "CalibK3":"DL200+MIX10+MS105+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibI1":"MS112+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibI2":"MS104+1105D+1202M+MIX10+DL180+MIX10+DL240+MIX10+DL180+MS106",
                                        "CalibI3":"00000+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibB1":"MS112+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "CalibB2":"MS103+0602M+0804M+MIX10+DL180+MIX10+DL240+MIX10+DL180+MS106",
                                        "CalibB3":"00000+00000+00000+00000+00000+00000+00000+00000+00000+00000",
                                        "WashTestTube-DeviceFlush1":"MS113+MS107+0115M+MS113+MS107+0115M+MS113+MS107+0115M+MS113",
                                        "WashTestTube-DeviceFlush2":"MS107+0115M+MS113+0760M+MS107+0115M+MIX05+MS113+MS107+0115M",
                                        "WashTestTube-DeviceFlush3":"MIX05+MS113+MS107+0115M+MIX05+MS113+MS107+0115M+MIX05+MS113",
                                        "WashCuvette-DeviceWash":"MS113+MS108+0415M+MIX10+MS113+00000+00000+00000+00000+00000"
					})
								
					with open(self.image_path+"Chemical_Firmware_V1.0.json","w")as e:
						json.dump(dictionary,e)	
						
###########################################################################################################################################	

				calib_status_file = pathlib.Path(self.image_path+"calib_status.json")
				if calib_status_file.exists ():					
					with open(self.image_path+"calib_status.json","r+") as e:
						a=json.load(e)					    		

					obj=a

					with open(self.image_path+"calib_status.json","w")as e:
						json.dump(obj,e)

				else:
					dictionary = ({
										"N40": "C",
										"N0": "C", 
										"P20": "C", 
										"P5": "C", 
										"pH7": "C", 
										"K0": "C", 
										"N30": "C", 
										"N10": "C", 
										"K20": "C", 
										"pH4": "C", 
										"K40": "NC", 
										"P0": "C", 
										"EC": "C", 
										"P15": "C", 
										"P25": "C", 
										"N5": "C", 
										"P10": "C", 
										"N20": "C", 
										"K10": "C", 
										"B0.0":"NC",
										"B0.25":"NC",
										"B0.5":"NC",
										"B1.0":"NC",
										"B1.5":"NC",
										"B2.0":"NC",
										"I0.0":"NC",
										"I0.5":"NC",
										"I1.0":"NC",
										"I1.5":"NC",
										"I2.0":"NC",						
										"C0.0":"NC",
										"C0.2":"NC",
										"C0.4":"NC",
										"C0.6":"NC",
										"C0.8":"NC",
										"C1.0":"NC",
										"Z0.0":"NC",
										"Z0.1":"NC",
										"Z0.5":"NC",
										"Z1.0":"NC",
										"Z2.0":"NC",
										"Z3.0":"NC",
										"Z5.0":"NC",
										"OC0.0":"NC",
										"OC0.25":"NC",
										"OC0.5":"NC",
										"OC0.75":"NC",
										"OC1.0":"NC",
										"S0.0":"NC",
										"S0.5":"NC",
										"S1.0":"NC",
										"S1.5":"NC",
										"S2.0":"NC"
					})
								
					with open(self.image_path+"calib_status.json","w")as e:
						json.dump(dictionary,e)	
						
###########################################################################################################################################	

				fipcs_file = pathlib.Path(self.image_path+"fipcs.json")
				if fipcs_file.exists ():					
					with open(self.image_path+"fipcs.json","r+") as e:
						a=json.load(e)					    		

					obj=a

					with open(self.image_path+"fipcs.json","w")as e:
						json.dump(obj,e)

				else:
					dictionary = ({
										"1": {"topx": 364, "topy": 246, "botx": 374, "boty": 256}, 
										"2": {"topx": 385, "topy": 180, "botx": 395, "boty": 190}, 
										"3": {"topx": 446, "topy": 235, "botx": 456, "boty": 245}, 
										"4": {"topx": 425, "topy": 257, "botx": 435, "boty": 267}, 
										"5": {"topx": 374, "topy": 202, "botx": 384, "boty": 212} 
					})
								
					with open(self.image_path+"fipcs.json","w")as e:
						json.dump(dictionary,e)	
						
###########################################################################################################################################

				ipcs_file = pathlib.Path(self.image_path+"ipcs.json")
				if ipcs_file.exists ():					
					with open(self.image_path+"ipcs.json","r+") as e:
						a=json.load(e)					    		

					obj=a

					with open(self.image_path+"ipcs.json","w")as e:
						json.dump(obj,e)

				else:
					dictionary = ({
										"1": {"topx": 364, "topy": 246, "botx": 374, "boty": 256}, 
										"2": {"topx": 385, "topy": 180, "botx": 395, "boty": 190}, 
										"3": {"topx": 446, "topy": 235, "botx": 456, "boty": 245}, 
										"4": {"topx": 425, "topy": 257, "botx": 435, "boty": 267}, 
										"5": {"topx": 374, "topy": 202, "botx": 384, "boty": 212} 
					})
								
					with open(self.image_path+"ipcs.json","w")as e:
						json.dump(dictionary,e)	
						
###########################################################################################################################################

				result_file = pathlib.Path(self.image_path+"result.json")
				if result_file.exists ():					
					with open(self.image_path+"result.json","r+") as e:
						a=json.load(e)					    		

					obj=a

					with open(self.image_path+"result.json","w")as e:
						json.dump(obj,e)

				else:
					dictionary = ({
										"device_uuid": "72fe12ee-e28e-562f-bd5e-57f80a3b1c06", 
										"fr_uuid": "4f34a3aa-200c-4a18-be5e-96cbdb9b5dea", 
										"EC": "0", 
										"pH": "0", 
										"N": "0", 
										"P": "0", 
										"K": "0",
										"B": "0",
										"I": "0",										
										"Z": "0", 
										"C": "0", 
										"S": "0",
										"OC": "0",
										"Company_code":"krt-1234"
					})
								
					with open(self.image_path+"result.json","w")as e:
						json.dump(dictionary,e)	
						
###########################################################################################################################################

				rgb_result_file = pathlib.Path(self.image_path+"rgb_result.json")
				if rgb_result_file.exists ():					
					with open(self.image_path+"rgb_result.json","r+") as e:
						a=json.load(e)					    		

					obj=a

					with open(self.image_path+"rgb_result.json","w")as e:
						json.dump(obj,e)

				else:
					dictionary = ({
									"n_rgb": {"result_n_r": 120, "result_n_g": 80, "result_n_b": 135}, 
									"p_rgb": {"result_p_r": 45, "result_p_g": 86, "result_p_b": 121}, 
									"k_rgb": {"result_k_r": 234, "result_k_g": 58, "result_k_b": 180},
									"b_rgb": {"result_p_r": 45, "result_p_g": 86, "result_p_b": 121}, 
									"i_rgb": {"result_k_r": 234, "result_k_g": 58, "result_k_b": 180},						
									"z_rgb": {"result_z_r": 120, "result_z_g": 80, "result_z_b": 135}, 
									"s_rgb": {"result_s_r": 45, "result_s_g": 86, "result_s_b": 121}, 
									"c_rgb": {"result_c_r": 234, "result_c_g": 58, "result_c_b": 180},
									"oc_rgb": {"result_oc_r": 45, "result_oc_g": 86, "result_oc_b": 121} 
					})
								
					with open(self.image_path+"rgb_result.json","w")as e:
						json.dump(dictionary,e)	
						
###########################################################################################################################################
										
				file = pathlib.Path(self.image_path+"kipcs.json")
				if file.exists ():					
					with open(self.image_path+"kipcs.json","r+") as e:
						a=json.load(e)					    		
						
					obj=a

					with open(self.image_path+"kipcs.json","w")as e:
						json.dump(obj,e)
					
				else:
					dictionary = ({
						"1": {"topx": 364, "topy": 246, "botx": 374, "boty": 256}, 
						"2": {"topx": 385, "topy": 180, "botx": 395, "boty": 190}, 
						"3": {"topx": 446, "topy": 235, "botx": 456, "boty": 245}, 
						"4": {"topx": 425, "topy": 257, "botx": 435, "boty": 267}, 
						"5": {"topx": 374, "topy": 202, "botx": 384, "boty": 212} 
					})
													
					with open(self.image_path+"kipcs.json","w")as e:
						json.dump(dictionary,e)
						
###########################################################################################################################################

				file = pathlib.Path(self.image_path+"kfipcs.json")
				if file.exists ():					
					with open(self.image_path+"kfipcs.json","r+") as e:
						a=json.load(e)					    		
						
					obj=a

					with open(self.image_path+"kfipcs.json","w")as e:
						json.dump(obj,e)
					
				else:
					dictionary = ({
						"1": {"topx": 364, "topy": 246, "botx": 374, "boty": 256}, 
						"2": {"topx": 385, "topy": 180, "botx": 395, "boty": 190}, 
						"3": {"topx": 446, "topy": 235, "botx": 456, "boty": 245}, 
						"4": {"topx": 425, "topy": 257, "botx": 435, "boty": 267}, 
						"5": {"topx": 374, "topy": 202, "botx": 384, "boty": 212} 
					})
													
					with open(self.image_path+"kfipcs.json","w")as e:
						json.dump(dictionary,e)
						
###########################################################################################################################################
				
				log_file = pathlib.Path(self.logpath+"log")
				
				if log_file.exists ():					
					logging.info ("Log file Read")
				else:
					readlogfile = open(self.logpath+"log","w+")
					logging.info ("Log file Created")
					
###########################################################################################################################################					

				self.keypad_label=Label(self.root,text="Keypad",bg="#F5F4EB",fg="red",font="centre  6 ")		
				self.bfocus_in=Button(self.root,text="Open",bg="blue",fg="white",font="centre 6",command=self.focus_in)             
				self.bfocus_out=Button(self.root,text="Close",bg="blue",fg="white",font="centre 6",command=self.focus_out)

				self.keypad_label.place(x=18,y=15,width=40,height=20)                        
				self.bfocus_in.place(x=60,y=15,width=40,height=20)    
				self.bfocus_out.place(x=120,y=15,width=40,height=20)   
		
				self.dispense_label=Label(self.root,text="Dispense",bg="#F5F4EB",fg="red",font="centre  6 ")
				self.dispense_label.place(x=270,y=15,width=50,height=20)

				self.machine_status_label=Label(self.root,text="",bg="#F5F4EB",fg="red",font="BOLD  8 ")
				self.machine_status_label.place(x=20,y=440)						

				#self.bocsample_solution=Button(self.root,text="OC",bg="blue",fg="white",font="centre 6",command=self.oc_dispense)
				self.bsample_solution=Button(self.root,text="ES",bg="blue",fg="white",font="centre 6",command=self.ss_dispense)
				self.bdistilled_water=Button(self.root,text="DW (pH)",bg="blue",fg="white",font="centre 6",command=self.dw_dispense)
				self.bdistilled_water_ec=Button(self.root,text="DW (EC)",bg="blue",fg="white",font="centre 6",command=self.dw_dispense_ec)
				
				self.bstop_dispense=Button(self.root,text="Stop",bg="black",fg="white",font="centre 6",command=self.stop_dispense)
				
				self.bShutdown=Button(self.root,text="Shutdown",bg="red",fg="black",font="centre 6",command=self.system_shutdown)
				self.bReboot=Button(self.root,text="Reboot",bg="red",fg="black",font="centre 6",command=self.system_reboot)

				#self.babort_main=Button(self.root,text="Reboot",bg="#A79B94",fg="white",font="centre",command=self.abort_main)
				#self.bocsample_solution.place(x=260,y=15,width=50,height=20) 
				self.bsample_solution.place(x=330,y=15,width=50,height=20)    
				self.bdistilled_water.place(x=400,y=15,width=50,height=20) 
				self.bdistilled_water_ec.place(x=470,y=15,width=50,height=20)   						
				self.bstop_dispense.place(x=540,y=15,width=50,height=20) 
				
				self.bShutdown.place(x=680,y=15,width=50,height=20)
				self.bReboot.place(x=740,y=15,width=40,height=20)
				
				#self.babort_main.place(x=260,y=5) 

				self.bstop_dispense['state']=DISABLED  

				#main_thread = threading.Timer(1, self.log)
				#main_thread.start()		
				self.tablet_dispense = 0
				self.count_pixel = 0	
				self.topx1 = 0
				self.topy1 = 0
				self.botx1 = 0
				self.boty1 = 0
				
				self.topx2 = 0
				self.topy2 = 0
				self.botx2 = 0
				self.boty2 = 0

				self.topx3 = 0
				self.topy3 = 0
				self.botx3 = 0
				self.boty3 = 0

				self.topx4 = 0
				self.topy4 = 0
				self.botx4 = 0
				self.boty4 = 0

				self.topx5 = 0
				self.topy5 = 0
				self.botx5 = 0
				self.boty5 = 0
				
				self.es_ph_ec_msg_flag = 0
				self.es_msg_flag = 0
				self.ph_msg_flag = 0
				self.ec_msg_flag = 0
				
				self.es_or_nitrogen_flag = 0
				
				self.servicetest_error_indication_flag= 0
				
				self.location_longitude = ""
				self.location_latitude = ""
				
				#self.root.attributes('-fullscreen', True)
				#self.root.attributes('-type', 'splash')
				#self.root.attributes('-type', 'dock')
				#self.root.focus_force()
				#self.root.resizable(0,0)

				#self.root.protocol("WM_DELETE_WINDOW", self.disable_event)
				#self.root.overrideredirect(1)
				
				self.front_page()					
				self.root.mainloop()
			except Exception as e:
				errorstring = "/E-Init App()"
				logging.warning ("%s", errorstring)
				self.machine_status_label.configure(text = "Error Occurred while initializing application")
				logging.exception("Exception occurred")
			finally:
				#texttosend = "KT+ABORT\r\n"
				#read_abort_ret_val = self.kt_sendcommand(texttosend,2,10)			
				#texttosend = "KT+EXTABORT\r\n"			
				#ext_abort_ret_val = self.kt_send_external_abort_command(texttosend,0,10)			
				#self.ser.close()
				#logging.info ("Serial Port Closed")
				pass		

MainPAGE()
