from setuptools import setup, find_packages
setup(
    name='syncwerk-server-python-django-shibboleth',
    version='20181227',
    author='Syncwerk GmbH',
    author_email='support@syncwerk.com',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    url='https://www.syncwerk.com',
    license='MIT',
    description='Django Shibboleth Remoteuser',
    long_description='Middleware for using Shibboleth with Django',
    platforms=['any'],
    include_package_data=True,
)
