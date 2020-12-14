FROM alpine:3.5
RUN apk add --update py2-pip
RUN pip3 install flask
RUN pip3 install requests
COPY req /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/req
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates
COPY templates/base.html /usr/src/app/templates
COPY templates/result.html /usr/src/app/templates
EXPOSE 5000
CMD ["python" , "app.py"]
