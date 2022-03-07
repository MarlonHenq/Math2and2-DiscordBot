FROM python:3.8

RUN pip3 install discord
RUN pip3 install jsons
RUN pip3 install flask
RUN pip3 install requests

RUN sudo apt install octave

EXPOSE 1123

COPY . .
CMD ["python", "main.py"]