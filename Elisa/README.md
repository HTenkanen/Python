# Python installation directions using Anaconda3

Here is documentation about the installation of Python related modules and the maintenance for RedHat Linux distribution. 

The installation of Python and the package managing / maintenance is done using __[Anaconda](https://www.continuum.io/why-anaconda)__ 
(miniconda installation with only the required modules)

## Install Anaconda (miniconda)

Create directory for Python related stuff:

    sudo su 
    mkdir /opt/Python
        
Download the miniconda installer script:

    cd /opt/Python
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

Install Anaconda (miniconda with minimum packages included by default):

    bash Miniconda3-latest-Linux-x86_64.sh
    
    # ==> Accept the licence term
     
    # When asked for installation location, set it as
    /opt/anaconda3
    
    # When asked if you want to add anaconda to system path say:
    yes
    
Add Anaconda to the system path of the user bash_profile (required for new users):

    # exit if you are root user at the moment
    exit
    cd $HOME
    nano .bash_profile
    
    # Add anaconda3 locations to PATH variable (separate with colon) (example)
    PATH=$PATH:$HOME/.local/bin:$HOME/bin:/opt/anaconda3:/opt/anaconda3/bin
    
Close and reopen a terminal and check that Anconda installation was succesfull (checks that conda works):

    conda --version
    
## Configure Anaconda

In this part we create an Anaconda environment for Python 3.4 interpreter because some essential packages are 
not yet ready to be used with Python 3.5 (as of Feb. 2015). 

Create Python 3.4 environment:

    conda create --name py34 python=3.4
    
Test to activate the Python 3.4 environment (py34) ==> Needs to be done every time when using the system:
    
    source activate py34
    
## Install Python modules

Using anaconda and conda package manager it is easy to install and manage the Python modules. Most of the basic Python modules that are required 
can be installed with conda package manager, but there are quite few packages that requires using pip.

The installed modules (+their dependencies) are:

   - numpy
   - pandas
   - scipy
   - matplotlib
   - bokeh
   - gdal
   - fiona
   - shapely
   - pyproj
   - psycopg2
   - descartes
   - geopandas
       
Activate Python 3.4 environment:
 
    source activate py34
   
Install following modules using conda:

    conda install numpy pandas scipy gdal fiona shapely pyproj psycopg2 matplotlib bokeh
    
    # Ensure that fiona / gdal / numpy / geopandas are working together ==> https://github.com/ioos/conda-recipes/issues/623 
    conda install -c https://conda.anaconda.org/ioos geopandas numpy=1.9 gdal=1.11.2
    
Install following packages using pip:

    pip install descartes geopandas 

Run [tests](Python_installation_test.py) and check that all Python modules are working properly:
   
    # Activate the python 3.4 environment
    source activate py34
    python3 Python_installation_test.py  
    


