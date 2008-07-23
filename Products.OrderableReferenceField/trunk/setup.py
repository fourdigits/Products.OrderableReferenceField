from setuptools import setup, find_packages
import os

version = '1.2-beta2'

setup(name='Products.OrderableReferenceField',
      version=version,
      description="This product provides an Archetype field that's very similiar to the",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='order of referenced objects.',
      author_email='Daniel Nouri <d.nouri [at] zestsoftware [dot] nl>',
      url='http://svn.plone.org/svn/archetypes/Products.OrderableReferenceField/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
