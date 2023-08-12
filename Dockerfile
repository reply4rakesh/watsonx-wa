FROM ubuntu:latest
#FROM python:3.7
RUN apt-get update
RUN apt-get install -y python3.10
RUN apt-get install -y vim

RUN apt-get -y install python3-pip

#    && pip install --upgrade pip
# add python file to working directory
ADD app.py /
ADD ibm-gartner.json /
ADD question.py /
ADD requirements.txt /

ADD Dengue.pdf /


RUN pip install requests
RUN pip install langchain==0.0.249
#RUN pip install genai
RUN pip install python-dotenv
RUN pip install Flask==2.0.3
RUN pip install pypdf==3.15
RUN pip install ibm-generative-ai==0.1.19
RUN pip install jsonify
RUN pip install flask-requests
RUN pip install requests
RUN pip install ibm_watson_machine_learning



CMD [ "python3", "./app.py"]
