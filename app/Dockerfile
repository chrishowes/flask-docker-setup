FROM python:2.7
RUN apt-get update && apt-get install -y ruby
RUN gem install sass
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
