#!/usr/bin/env python

import os
import oschmod
import stat
import win32con, win32api
source = input('Which drive will you put this in? ') + ':/'
directory = {
	'Coding':0,
	'Downloads':1,
	'Music':2,
	'Pictures':3,
	'Videos':4
	}


def write_ini(file,Dir,key):
	global source
	source_icon = source + 'PortableApps/PortableApps.com/App/Graphics/WindowsFolderIcons/'
	
	with open(file,'w') as rec:
		rec.write('[.ShellClassInfo]\n')
		rec.write('ConfirmFileOp=0\n')
		rec.write('NoSharing=1\n')
		rec.write('IconFile=' + source_icon + 'folders.dll\n')
		rec.write('IconIndex=' + str(key) + '\n')
		rec.write('InfoTip=This is the ' + Dir + ' folder.')
		rec.close()

	hide = 'attrib +h ' + file
	os.system(hide)

	return


def Escalate_Permisson(file):
	try:
		os.remove(file)
	except PermissionError:
		print('PermissionError do change')
		os.chmod(file, stat.S_IWRITE)
		os.remove(file)

	if os.path.isfile(file) is True:
		win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_NORMAL)
		os.remove(file)
	else:
		pass

	return

def Search_n_Replace(source, directory):
	docs = 'Documents/'

	for Dir, key in directory.items():
		file = source + docs + Dir + '/Desktop.ini'

		if os.path.isfile(file) is True:
			Escalate_Permisson(file)
			write_ini(file,Dir,key)
		else:
			write_ini(file,Dir,key)


Search_n_Replace(source, directory)
