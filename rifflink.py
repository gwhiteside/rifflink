#!/usr/bin/env python3

import argparse
import json
import os
import re
import subprocess

VIDEO_EXTENSIONS = {".avi", ".mkv", ".mov", ".mp4", ".mpeg", ".mpg", ".wmv"}

color_bcyan = "\u001b[36;1m"
color_bgreen = "\u001b[32;1m"
color_reset = "\u001b[0m"


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"source",
		help="top level movies directory"
		)
	parser.add_argument(
		"destination",
		help="RiffTrax directory"
		)
	parser.add_argument(
		"-d", "--dry-run",
		action="store_true",
		help="show what would be done, but don't do it"
		)
	args = parser.parse_args()

	with open("s01.json", "r") as movies_file:
		movies_dict = json.load(movies_file)
	movies_dict = {key.casefold(): value for key, value in movies_dict.items()}

	for root, directories, files in os.walk(args.source):
		for file in files:
			file_name, file_ext = os.path.splitext(file)

			if file_ext.lower() not in VIDEO_EXTENSIONS:
				continue

			fqfn = os.path.join(root, file)

			if not contains_rifftrax(fqfn):
				continue

			movie = file_name.casefold()
			if movie not in movies_dict:
				print("warning: no match for", file)
				continue

			out_filename = os.path.join(args.destination, movies_dict.get(movie))

			if not args.dry_run:
				os.symlink(fqfn, out_filename)

			print(
				color_bcyan + out_filename,
				color_reset + "->",
				color_bgreen + fqfn,
				color_reset
				)


def contains_rifftrax(file):
	cmd = [
		"ffprobe",
		"-v", "error",
		"-print_format", "csv",
		"-show_entries", "stream_tags=title",
		file
		]
	p = subprocess.Popen(
		cmd,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		universal_newlines=True
		)
	out, err = p.communicate()
	return re.search("riff", out, re.IGNORECASE)


if __name__ == "__main__":
	main()