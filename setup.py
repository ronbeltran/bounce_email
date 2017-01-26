from setuptools import setup

setup(
    name='bounce_email',
    version='0.0.1',
    description='Port of Ruby version bounce_email to Python to detect bounced emails',
    long_description=open('README.md').read(),
    keywords='gmail detect bounce email',
    url='http://github.com/ronbeltran/bounce_email',
    author='Ronnie Beltran',
    author_email='rbbeltran.09@gmail.com',
    license='MIT',
    packages=['bounce_email'],
    include_package_data=True,
    zip_safe=False,
)
