FROM teamvaders/dangercat:latest

RUN git clone https://github.com/dangerbots/Plugins.git /root/dangercat

WORKDIR /root/dangercat

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/dangercat/bin:$PATH"

CMD ["python3", "-m", "dangercat"]
