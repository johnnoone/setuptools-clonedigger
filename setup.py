from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    'clonedigger'
]

setup(name='setuptools-clonedigger',
    version=version,
    description="Setuptools command for clonedigger",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        "Topic :: Documentation",
        "Framework :: Setuptools Plugin",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: BSD License',
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='clonedigger setuptools command',
    author='Xavier Barbosa',
    author_email='',
    url='https://github.com/johnnoone/setuptools-clonedigger',
    license='BSD',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        "distutils.commands": [
            "clonedigger = setuptools_clonedigger.setuptools_command:ClonediggerCommand",
        ]
    }
)
