#!/usr/bin/env python3

import os
import shutil
import time

ROOT_PATH = "./music"
TMP_PATH = "./.tmp"

FILTERS = (
	".3gp", ".3GP",
	".aac", ".AAC",
	".flac", ".FLAC",
	".mp3", ".MP3", 
	".mp4", ".MP4",
	".ogg", ".OGG",
	".wav", ".WAV"
	".wma", ".WMA"
)

DEBUG = True

def print_debug(message):
	if DEBUG:
		print(message)

def main():
	if os.path.isdir(TMP_PATH):
		shutil.rmtree(TMP_PATH)
	
	os.makedirs(TMP_PATH)
	
	all_files = list()
	for root, directories, filenames in os.walk(ROOT_PATH):
		for filename in filenames:
			if filename.endswith(FILTERS):
				new_file = os.path.join(root, filename)
				print_debug("Append: " + new_file)
				all_files.append(new_file)
	
	all_files.sort(key=lambda x: x.lower())
	
	for filename in all_files:
		destination = os.path.join(TMP_PATH, filename)
		parent_dir = os.path.dirname(destination)
		if not os.path.isdir(parent_dir):
			os.makedirs(parent_dir)
		print_debug("Relocating: " + filename)
		shutil.move(filename, destination)
	
	shutil.rmtree(ROOT_PATH)
	shutil.move(os.path.join(TMP_PATH, ROOT_PATH), ".")
	
	print("Success!")
	return

if __name__ == "__main__":
	main()
