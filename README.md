# Distributed Crawler

A distributed python crawler using Celery

http://docs.celeryproject.org/en/latest/index.html

## Quick Start

```
docker run -it --rm --hostname my-rabbit --name some-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management

git clone https://github.com/ianchen06/distributed_crawler

cd distributed_crawler

pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# start worker
./run.sh

# submit job
python job.py
```
