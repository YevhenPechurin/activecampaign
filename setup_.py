from setuptools import setup, find_packages
from .activecampaign_api.version import __version__

setup(name='activecampaign_api',
      version=__version__,
      description='Api for activecampaign',
      packages=find_packages(),
      author_email='yevhen.pechurin@gmail.com',
      zip_safe=False)
