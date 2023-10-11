from setuptools import setup, find_packages
setup(
    name="sok-core",
    version="0.1",
    packages=find_packages(),
    entry_points = {
        'console_scripts':
            ['core_main=core.core_main:main'],
    },
    zip_safe=True
)