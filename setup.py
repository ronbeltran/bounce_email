from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='bounce_email',
    version='0.0.3',
    description='Port of Ruby version bounce_email to Python to detect bounced emails',
    long_description=readme(),
    keywords='gmail detect bounce email',
    url='http://github.com/ronbeltran/bounce_email',
    author='Ronnie Beltran',
    author_email='rbbeltran.09@gmail.com',
    license='MIT',
    packages=['bounce_email'],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    test_require=['nose'],
)
