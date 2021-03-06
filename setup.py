import os.path
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


VERSION_NUMERIC = (0, 1, 0)
VERSION = '{0}.{1}.{2}'.format(*VERSION_NUMERIC)


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
      packages=['redispace', 'redispacetests'],
      version=VERSION,
      url='https://github.com/kimjayd/redispace',
      description='implements a ``redis`` wrapper for replication and sharding',
      long_description=get_readme(),
      install_requires=['redis'],
      extras_require={'docs': ['Sphinx']},
      tests_require=['Attest'],
      test_loader='attest:auto_reporter.test_loader',
      test_suite='redispacetests.suite',
      classifiers=[
          'Development Status :: 1 - Planning',
          'License :: OSI Approved :: MIT License',
          'Topic :: Database',
          'Programming Language :: Python',
      ]
)
