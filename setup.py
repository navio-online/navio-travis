from setuptools import setup
import navio.meta_travis
setup(
    name='navio-travis',
    version=navio.meta_travis.__version__,
    author='Navio Online OpenSource projects',
    author_email='oss@navio.online',
    url=navio.meta_travis.__website__,
    packages=['navio', 'navio.travis'],
    install_requires=['boto3'],
    license='Apache 2.0 license',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    keywords=['framework'],
    description='Travis CI helper libs',
    long_description=open('README.rst').read()+'\n'+open('CHANGES.rst').read()
)
