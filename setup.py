from setuptools import setup
from setuptools import find_packages
requires = [
    'flask',
    'requests',
    'html5lib',
    'spotipy',
    'requests_html',
    'beautifulsoup4',
    'youtube_dl',
    'pathlib',
    'pandas'
]

setup(
    name='SpotifyToYoutubeMP3',
    version='1.0',
    description='An application that gets your Spotify songs and downloads the YoutubeMP3 version',
    author='Jason',
    author_email='jasongoodisondevelopment@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)