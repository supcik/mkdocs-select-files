# Copyright 2019 Jacques Supcik
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='mkdocs-select-files',
    version='0.3.6',
    packages=['selectfiles'],
    license='Apache-2.0',
    author='Jacques Supcik',
    author_email='jacques@supcik.net',
    description='Filter pages for assignments',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/supcik/mkdocs-select-files',
    install_requires=['mkdocs'],

    entry_points={
        'mkdocs.plugins': [
            'select-files = selectfiles.plugin:SelectFiles',
        ]
    },
)
