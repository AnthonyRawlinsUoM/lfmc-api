FROM continuumio/anaconda3

LABEL maintainer="Anthony Rawlins <anthony.rawlins@unimelb.edu.au>"
COPY ./sources.list /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y nano
RUN conda update -n base conda
RUN conda install -y pandas xarray simplejson numpy rasterio opencv
RUN pip install hug -U 
RUN pip install marshmallow python-swiftclient python-keystoneclient
RUN pip install netcdf4
RUN apt-get install -y libgl1-mesa-glx 
RUN apt-get install -y ffmpeg
RUN conda install -y geopandas cartopy
RUN pip install regionmask
RUN pip install rx

ADD lfmc /lfmc
ADD VERSION .
ADD LFMCServer.py /
ADD logviewer.sh /
WORKDIR /FuelModels/
EXPOSE 8002
ENTRYPOINT ["hug", "-f", "/LFMCServer.py", "-p", "8002"]