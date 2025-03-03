from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lucrum_safe_city/__init__.py
from lucrum_safe_city import __version__ as version

setup(
	name="lucrum_safe_city",
	version=version,
	description="Lucrum Safe City",
	author="usman",
	author_email="usman.amjad@tylextech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
