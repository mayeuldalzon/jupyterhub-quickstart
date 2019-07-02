from setuptools import setup

__version__ = 0.1

setup(name='ulkubespawner', 
      version=__version__,
      py_modules=['ulkubespawner'],
      install_requires=['jupyterhub', 'jupyterhub-kubespawner'])
