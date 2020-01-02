FROM registry.cn-hangzhou.aliyuncs.com/jtyoui/p3j8
MAINTAINER Jytoui <jtyoui@qq.com>

RUN yum install -y unzip
RUN wget -P /home http://cdn.tyoui.cn/model.zip
RUN unzip -o /home/model.zip -d /home
RUN rm -rf /home/model.zip

COPY requirements.txt /home/

RUN pip3 install --no-cache-dir -r /home/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install --no-cache-dir uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["python"]
