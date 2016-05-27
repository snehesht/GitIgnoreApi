FROM alpine:3.3

RUN apk update && \
	apk add --no-cache python3 && \
	apk add --no-cache git && \
	apk add --no-cache curl && \
	curl https://bootstrap.pypa.io/get-pip.py | python3

ADD start.sh /start.sh
RUN chmod +x /start.sh

RUN mkdir /var/www && \
	 cd /var/www && \
	 git clone https://github.com/snehesht/GitIgnoreApi && \
	 cd GitIgnoreApi && \
	 pip install virtualenv && \
	 virtualenv env && \
	 source env/bin/activate && \
	 pip install -r Requirements.txt && \
	 ls /var/www/GitIgnoreApi/

EXPOSE 8000
ENTRYPOINT ["/start.sh"]
