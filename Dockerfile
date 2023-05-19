FROM continuumio/anaconda3:latest

# Set environment variables
ENV PATH="/root/mambaforge/bin:$PATH"

# Install manba
RUN wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh \
    && bash Mambaforge-Linux-x86_64.sh -b \
    && rm Mambaforge-Linux-x86_64.sh \
    && echo 'export PATH="/root/mambaforge/bin:$PATH"' >> ~/.bashrc

# Install Conda packages for jupyter server
RUN mamba install -n base -c conda-forge jupyterlab_widgets jupyterlab nb_conda_kernels ipywidgets black isort -y
COPY environment.yaml /

# Create a new conda environment based on the environment.yaml file
RUN mamba env create -f /environment.yaml --quiet
RUN conda init

# Start Jupyter Lab
CMD ["/bin/bash", "-c", "jupyter lab --allow-root --no-browser --ip 0.0.0.0 --port 8888 --notebook-dir=./"]