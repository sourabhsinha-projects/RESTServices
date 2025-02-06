FROM continuumio/anaconda3:latest
MAINTAINER Sourabh Sinha <
COPY ./modelApi/ /usr/src/app/
EXPOSE 5000
WORKDIR /usr/src/app/
RUN pip install --upgrade pip \
&& pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt
CMD python irisPredictorApi.py