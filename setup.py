from setuptools import setup, find_packages
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0'

long_description = (
    read('README.rst')
    + '\n' +
    read('CHANGES.txt')
    + '\n'
    )

setup(name='diazotheme.frameworks',
    version=version,
    description="A collection of Diazo themes with support to many CSS Frameworks",
    long_description=long_description,
    # Get more strings from
    # https://pypi.org/pypi?:action=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='web zope plone diazo theme html5 bootstrap foundation goldilocks kube css framework',
    author='Thijs Jonkman',
    author_email='t.jonkman@gmail.com',
    maintainer='Leonardo Caballero',
    maintainer_email='leonardocaballero@gmail.com',
    url='https://github.com/collective/diazotheme.frameworks',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['diazotheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
          'setuptools',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
