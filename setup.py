from setuptools import find_packages, setup

setup(
    name='lgtm',
    version='1.0.0',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'Click',
        'Pillow',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'lgtm=lgtm.core:cli'
        ]
    }
)
