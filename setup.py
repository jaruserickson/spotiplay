from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(
    name='spotiplay',
    version=__version__,
    description='Spotify rooms.',
    long_description='https://github.com/jaruserickson/spotiplay',
    url='https://github.com/jaruserickson/spotiplay',
    download_url='https://pypi.python.org/pypi/pytify',
    author='jaruserickson [pytify: bjarneo]',
    author_email='jarus.erickson@gmail.com',
    license='MIT',
    keywords='spotify spotiplay pytify spotipy dj room song search curses',
    packages=find_packages(),
    install_requires=[
        'requests ~= 2.4.3',
        'spotipy~=2.3.8',
        'prompt-toolkit==1.0.0',
        'pycrypto~=2.6.1'
    ],
    entry_points={
        'console_scripts': [
            'spotiplay=spotiplay.cli:main'
        ]
    },
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console :: Curses',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Terminals',
    ],
)
