from setuptools import setup, find_packages

setup(name='etlearn',
      version='0.0',
      description='Machine Learning for Survival Time Data in Python',
      author='Bowen Li',
      author_email='bowen0701@gmail.com',
      url='https://github.com/bowen0701/survival-learn',
      license='BSD',
      install_requires=['numpy',
                        'scipy',
                        'pandas'],
      extras_require={
          'TBD': ['TBD']
      },
      classifiers=[
          'Programming Language :: Python :: 3.5',
          'Development Status :: 0 - Beta',
          'Natural Language :: English',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=find_packages())
