from setuptools import setup, find_packages

VERSION = '0.3.7'
DESCRIPTION = 'Load disc data from chemcomp simulations.'
LONG_DESCRIPTION = 'Python package to load disc data from simulations from the semi-analytical viscous disc code "chemcomp" by Schneider & Bitsch 2021.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="chemcomp_loader", 
        version=VERSION,
        author="Joe Williams",
        author_email="joepw1@hotmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        download_url='https://github.com/AstroWilliams/chemcomp-plotter/archive/refs/tags/v_0.1.tar.gz',
        packages=find_packages(),
        install_requires=['tables', 'numpy', 'matplotlib', 'yaml', 'ast', 'astropy'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'chemcomp'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Topic :: Scientific/Engineering :: Astronomy",
            # "Operating System :: Microsoft :: Windows",
        ]
)