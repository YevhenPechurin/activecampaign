from setuptools import setup
from .version import __version__

setup(name='activecampaign_api',
      version=__version__,
      description='Api for activecampaign',
      packages=['activecampaign'],
      author_email='yevhen.pechurin@gmail.com',
      zip_safe=False)
