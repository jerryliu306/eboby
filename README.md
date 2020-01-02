# **EBoby** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 实体抽取模块
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()


## Dockers安装
    cd /home
    git clone https://github.com/jtyoui/eboby.git
    cd eboby
    docker build -t eboby .
    docker run -d -v /home/eboby/:/mnt/eboby/ -p 9000:5000 eboby sh /mnt/eboby/app.sh 

## 摘要抽取接口
```shell script
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "data":"七牛云是国内企业级云服务商，致力以云技术驱动社会产业发展，同时专注于以数据智能和视觉智能为核心的云计算产业，围绕海量数据和各行业富媒体场景推出由融合 CDN、对象存储、云主机、大数据，内容识别平台等系列产品的智能视频云，为用户提供全面的云计算服务。"
}' \
 'http://ip:9000/summary'

# {"data": "七牛云是国内企业级云服务商, 致力以云技术驱动社会产业发展, 内容识别平台等系列产品的智能视频云","msg": "ok"}
```

## 关键字抽取接口
```shell script
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "data":"七牛云是国内企业级云服务商，致力以云技术驱动社会产业发展，同时专注于以数据智能和视觉智能为核心的云计算产业，围绕海量数据和各行业富媒体场景推出由融合 CDN、对象存储、云主机、大数据，内容识别平台等系列产品的智能视频云，为用户提供全面的云计算服务。"
}' \
 'http://ip:9000/keyWord'

# {"data": "云, 数据, 智能","msg": "ok"}
```

## 实体抽取接口
```shell script
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "data":"我在世贸大厦上班，我叫刘万光我是贵阳市南明村永乐乡水塘村的村民"
}' \
 'http://ip:9000/st' 

# {
# "address":["贵阳市南明村永乐乡水塘村"],
# "data":[6, 6, 2, 3, 3, 3, 6, 6, 6, 6, 6, 0, 1, 1, 6, 6, 4, 5, 5,…],
# "msg": "ok",
# "org":["世贸大厦"],
# "person":["刘万光"]
# }
```

### 实体抽取中的数字说明
    0-1 表示人名
    2-3 表示机构名
    4-5 表示地址
    6 表示无效信息


### 作者的邮箱
>>> jtyoui@qq.com  

***
[1]: https://blog.jtyoui.com
