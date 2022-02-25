from setuptools import setup

setup(
   name='l_systems',
   version='1.0',
   description='L-system Package',
   author='Daniel Tyebkhan',
   author_email='',
   packages=['l_systems'],  #same as name
   install_requires=['graphviz'], #external packages as dependencies
)