
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    # This is the name of your project. The first time you publish this
    # $ pip install sampleproject
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    name='helpers', 
    version='1.0.0',  # Required
    description='installing distributing packages test',  
    #long_description=long_description,  # Optional
    #long_description_content_type='text/markdown',  # Optional (see note above)
    #url='https://github.com/pypa/sampleproject',  # Optional
    #author='A. Random Developer',  # Optional
    #author_email='author@example.com',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='helpers',  # Optional

    package_dir={'': 'src'},  # Optional\

    packages=find_packages(where='src'),  # Required

    python_requires='>=3.6, <4',

    #install_requires=['peppercorn'],  # Optional

    #extras_require={  # Optional
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    
    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    #data_files=[('my_data', ['data/data_file'])],  # Optional
    
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },

    # project_urls={  # Optional
    #     'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
    #     'Funding': 'https://donate.pypi.org',
    #     'Say Thanks!': 'http://saythanks.io/to/example',
    #     'Source': 'https://github.com/pypa/sampleproject/',
    # },
)
