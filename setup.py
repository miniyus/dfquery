from setuptools import setup, find_packages

setup(name='dfquery',
      version='0.0.1',
      description='dfquery',
      author='Yoo Seong-min',
      author_email='miniyu97@gmail.com',
      url='https://github.com/miniyus/dfquery',
      license='MIT',
      python_requires='>=3.8',
      install_requires=['pandas~=1.2.3'],
      packages=find_packages()
      )
