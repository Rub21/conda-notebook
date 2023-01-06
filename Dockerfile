FROM continuumio/miniconda3:4.10.3p1
RUN conda install \
    xarray \ 
    netCDF4 \ 
    bottleneck \
    numpy \
    pandas \
    matplotlib \
    jupyterlab

RUN conda install -c conda-forge pangeo-forge-recipes
RUN conda install -c conda-forge s3fs
RUN conda install -c conda-forge intake

CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]