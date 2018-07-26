import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="gpu-optimize",
	version="2018.07",
	author="Jackson Sipple",
	description="Drop-in replacement functions that run on NVIDIA GPUs, parallelized for speed",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="TBD",
	packages=setuptools.find_packages(),
	classifiers=(
		"Programming Language :: Python :: 2",
		"Operating System :: OS Independent",
	),
)