#!/usr/bin/env python3

import rarfile
import os

class Movie():

	def __init__(self, pattern):
		self.pattern = pattern
		self.directory = str()
		# self.download_dir = os.path.join("/", "home", "highlike", "Downloads")
		# self.movie_dir = os.path.join("/", "home", "highlike", "Movies")

	def find_videos(self):
		os.chdir(self.movie_dir)
		for entry in os.listdir():
			os.chdir(self.movie_dir)
			if self.name in entry:
				os.chdir(entry)
				for entry in os.listdir():
					video = self.__get_video_name__(entry)
					self.videos.add(video)

	def __get_video_name__(self, entry):
		# cut off file suffix
		video = entry.split(".")[0]
		return video


class Ares275(Movie):
	"""for movies uploaded by Ares275"""

	def __get_video_name__(self, entry):
		video = entry.split(".")[1]
		return video

	def extract_archive(self, movie, video):
		dest_dir = os.path.join(old_movie.directory, movie)
		os.chdir(new_movie.directory)
		for item in os.listdir():
			if item.startswith(movie + "." + video):
				os.chdir(item)
				for archive in os.listdir():
					if "part1" in archive and rarfile.is_rarfile(archive):
						rf = rarfile.RarFile(archive)
						rf.extractall(path=dest_dir, pwd="Ares275")
						os.rename(dest_dir +"/"+ rf.infolist()[0].filename, os.path.join(dest_dir, video) + ".mkv")


if __name__ == '__main__':
	OldMovies
	old_movies = dict()
	new_movies = dict()
	unsorted_movies = dict()
	print(":: searching for unsorted movies ::")
	for movie in movies:
		old_movies[movie] = {video for video in Movie(movie)}
		new_movies[movie] = {video for video in Ares275(movie)}
		# find unsorted movies
		unsorted_movies[movie] = new_movies[movie].difference(old_movies[movie]) 
		for video in unsorted_movies[movie]:
			print("## found", movie + ":", video, "##")
			extract_archive(movie, video)
	print(":: DONE ::")
