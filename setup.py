from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(
    name='drupal_chatbot',
    version=__version__,
    author='biswajeetparida07@gmail.com',
    description='A client for call Drupal api',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    classifiers=['Development Status :: 1 - Production/Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Topic :: Internet :: WWW/HTTP',
                 'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                 'Topic :: Software Development :: Libraries :: Application Frameworks',
                 'Topic :: Software Development :: Libraries :: Python Modules', ],
)
