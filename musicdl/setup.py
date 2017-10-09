from setuptools import setup

setup(
    name='musicdl',
    version='1.0',
    description='Simple music downloader ',
    author='Alexis PETITJEAN',
    packages=['musicdl'],
    scripts=['musicdl'],
    install_requires=[
        'youtube-dl',
        'BeautifulSoup4',
        'eyed3',
        'requests'
    ],
)
