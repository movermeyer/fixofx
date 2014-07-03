# coding: utf-8
import setuptools
import os

README = os.path.join(os.path.dirname(__file__), 'README.rst')

setuptools.setup(
    name='fixofx',
    version='3.0',
    description='Canonicalize various financial data file formats to OFX 2 (a.k.a XML)',
    long_description=open(README).read(),
    author='',
    author_email='',
    url='',
    #packages=[],
    install_requires=,
    entry_points={
        'console_scripts': [
            'fixofx = fixofx',
         ]
    },
    license='Apache 2.0',
    keywords='',
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries',
      ],
    url='http://github.com/henriquebastos/python-decouple/',)
