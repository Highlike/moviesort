#!/usr/bin/env python3

import rarfile
import os

password = "Ares275"
download_dir = "/home/highlike/Downloads/"
movie_dir = "/home/highlike/Movies/"
movies = ["TAAHM", "TBBT"]

def extract_archive(movie, video):
	dest_dir = movie_dir +os.sep+ movie +os.sep
	os.chdir(download_dir)
	for item in os.listdir():
		if item.startswith(movie + "." + video):
			os.chdir(item)
			for archive in os.listdir():
				if "part1" in archive and rarfile.is_rarfile(archive):
					rf = rarfile.RarFile(archive)
					rf.extractall(path=dest_dir, pwd=password)
					os.rename(dest_dir + rf.infolist()[0].filename, dest_dir + video + ".mkv")
					return

def find_movies():
	# old movies
	old_movies = dict()
	os.chdir(movie_dir)
	for movie in os.listdir():
		os.chdir(movie_dir)
		old_movies[movie] = set()
		try:
			os.chdir(movie)
		except NotADirectoryError:
			pass
		for video in os.listdir():
			video = video.split(".")[0]
			old_movies[movie].add(video)

	# new movies
	new_movies = dict()
	os.chdir(download_dir)
	for movie in movies:
		os.chdir(download_dir)
		new_movies[movie] = set()
		for video in os.listdir():
			if movie in video:
				video = video.split(".")[1]
				new_movies[movie].add(video)
	
	return old_movies, new_movies

if __name__ == '__main__':
	old_movies, new_movies = find_movies()
	unsorted_movies = dict()
	print(":: searching for unsorted movies ::")
	for movie in movies:
		unsorted_movies[movie] = new_movies[movie].difference(old_movies[movie]) # find unsorted movies
		for video in unsorted_movies[movie]:
			print("## found", movie + ":", video, "##")
			extract_archive(movie, video)
	print(":: DONE ::")
