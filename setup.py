from setuptools import setup

setup(
    name='SelectFiles',
    version='0.1.0',
    packages=['selectfiles'],
    license='Apache-2.0',
    author='Jacques Supcik',
    author_email='jacques@supcik.net',
    description='Filter pages for assignments',
    install_requires=['mkdocs'],

    entry_points={
        'mkdocs.plugins': [
            'select-files = selectfiles.plugin:SelectFiles',
        ]
    },
)