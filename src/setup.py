from setuptools import setup, find_packages

setup(
    name='cloudfront-invalidator',
    version='0.1.0',
    description='A package to invalidate a CloudFront distribution',
    packages=find_packages(),
    install_requires=[
        'boto3',
    ],
)

