from setuptools import setup, find_packages
import os
import sys

version = '3.1.1'

setup(name='robotframework-metrics',
      version=version,
      description='Custom metrics based report for robot framework',
      long_description='Custom metrics based report for robot framework',
      classifiers=[
          'Framework :: Robot Framework',
          'Programming Language :: Python',
          'Topic :: Software Development :: Testing',
      ],
      keywords='robotframework report',
      author='Shiva Prasad Adirala',
      author_email='adiralashiva8@gmail.com',
      url='https://github.com/adiralashiva8/robotframework-metrics',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'robotframework',
          'beautifulsoup4',
      ],
      entry_points={
          'console_scripts': [
              'robotmetrics=robotframework_metrics.runner:main',
          ]
      },
      )
