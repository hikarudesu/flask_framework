FROM python:3

ENV HOME=/app

WORKDIR $HOME/
COPY . $HOME/
EXPOSE 5000
RUN apt-get update
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
ADD ./ /app
WORKDIR /app
RUN pip3 install -r requirements.txt



# RUN ln -sv $ORACLE_HOME/libclntsh.so.12.1 $ORACLE_HOME/libclntsh.so
RUN apt-get install -y libaio1

CMD ["python3","-u", "main.py"]