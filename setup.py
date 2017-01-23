import os

from setuptools import setup

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
SOURCE_PATH = os.path.join(ROOT_PATH, 'source')
README_PATH = os.path.join(ROOT_PATH, 'README.rst')

setup(
    name='pw_MultiScriptEditor',
    version='2.0.3',
    description='Python Editor for CG Applications',
    url='https://github.com/mikedatsik/pw_MultiScriptEditor',
    author='paulwinex',
    license='Apache License (2.0)',
    packages=find_packages(SOURCE_PATH),
    package_dir={
        '': 'source'
    },
    zip_safe=False
)
