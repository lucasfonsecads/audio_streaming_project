from setuptools import find_packages, setup

setup(
    name='audio_streaming_project',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'torch',
        'pyspark',
    ],
)
