FROM registry.cn-hangzhou.aliyuncs.com/jtyoui/p3j8
MAINTAINER Jytoui <jtyoui@qq.com>

ENV ProjectName eboby

COPY ../${ProjectName} /mnt/${ProjectName}
RUN yum install -y unzip
RUN wget -P /mnt/${ProjectName} http://cdn.tyoui.cn/model.zip
RUN unzip -o /mnt/${ProjectName}/model.zip -d /mnt/${ProjectName}/
RUN rm -rf /mnt/${ProjectName}/model.zip

EXPOSE 5000

RUN pip install --no-cache-dir -r /mnt/${ProjectName}/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["/mnt/${ProjectName}/app.sh"]
