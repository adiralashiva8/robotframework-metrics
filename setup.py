from setuptools import setup, find_packages

filename = 'robotframework_metrics/version.py'
exec(compile(open(filename, 'rb').read(), filename, 'exec'))

setup(name='robotframework-metrics',
      version=__version__,
      description='Custom report for robot framework',
      long_description='Custom html report generator using robot.result api',
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
          'jinja2',
          'pandas',
      ],
      entry_points={
          'console_scripts': [
              'robotmetrics=robotframework_metrics.runner:main',
          ]
      },
      )