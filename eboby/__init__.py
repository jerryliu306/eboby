# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/10/15 17:37
# @Author: Jtyoui@qq.com
from jtyoui.neuralNetwork.paddle import ernie_st, ernie_match
from jpype import startJVM, JClass, getDefaultJVMPath
from config import Log, Models_DIR
import os
import jtyoui

HanNLP_path = os.path.dirname(__file__) + os.sep + 'hanlp-1.7.4.jar'
st = ernie_st(Models_DIR)
sep = ':' if os.name != 'nt' else ';'

# 开始初始化Java虚拟机
startJVM(getDefaultJVMPath(), F"-Djava.class.path={HanNLP_path}{sep}{os.path.dirname(__file__)}")
HanNLP = JClass('com.hankcs.hanlp.HanLP')


@jtyoui.log(Log)
def extract_summary(word, num=3):
    """摘要提取
    :param word:一段文字
    :param num: 提取的数量
    """
    result = HanNLP.extractSummary(word, num).toString()
    return result[1:-1]


@jtyoui.log(Log)
def extract_keyword(word, num=3):
    """关键字提取
    :param word:一段文字
    :param num: 关键字数量
    """
    result = HanNLP.extractKeyword(word, num).toString()
    return result[1:-1]


def extract_st(word):
    """抽取实体"""
    data = ernie_match(word, st)
    data = [int(d) for d in data]
    addr = jtyoui.key_value_re(word, data, value_re='[45]+')
    person = jtyoui.key_value_re(word, data, value_re='[01]+')
    org = jtyoui.key_value_re(word, data, value_re='[23]+')
    return data, addr, person, org
