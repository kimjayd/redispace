import os.path
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import redispace


def get_readme(readme='README.rst'):
    try:
        with open(os.path.join(os.path.dirname(__file__), readme)) as f:
            return f.read()
    except:
        return ''


setup(name='redispace',
      author='Hyunjun Kim',
      author_email='kim@hyunjun.kr',
      maintainer='Hyunjun Kim',
      maintainer_email='kim@hyunjun.kr',
      py_modules=['redispace'],
      version=redispace.VERSION,
      url='https://github.com/kimjayd/redispace',
      description='implements a ``redis`` wrapper for replication and sharding',
      long_description=get_readme(),
      install_requires=['redis'],
      classifiers=[
          'Development Status :: 1 - Planning',
          'License :: OSI Approved :: MIT License',
          'Topic :: Database',
          'Programming Language :: Python',
      ]
)