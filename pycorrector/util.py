# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief: 
import os
import pickle
import re

import jieba

from pycorrector.zhtools.langconv import Converter
jieba.initialize()

def remove_punctuation(strs):
    """
    去除标点符号
    :param strs:
    :return:
    """
    return re.sub("[\s+\.\!\/<>“”,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", strs.strip())


def traditional2simplified(sentence):
    """
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    """
    sentence = Converter('zh-hans').convert(sentence)
    return sentence


def simplified2traditional(sentence):
    """
    将sentence中的简体字转为繁体字
    :param sentence: 待转换的句子
    :return: 将句子中简体字转换为繁体字之后的句子
    """
    sentence = Converter('zh-hant').convert(sentence)
    return sentence


def segment(sentence):
    """
    切词
    :param sentence:
    :return: list
    """
    return jieba.lcut(sentence)


def tokenize(sentence, mode='default'):
    """
    切词并返回切词位置
    :param sentence:
    :return: (word, start_index, end_index) model='search'
    """
    return list(jieba.tokenize(sentence, mode=mode))


def load_pkl(pkl_path):
    """
    加载词典文件
    :param pkl_path:
    :return:
    """
    with open(pkl_path, 'rb') as f:
        result = pickle.load(f)
    return result


def dump_pkl(vocab, pkl_path, overwrite=True):
    """
    存储文件
    :param pkl_path:
    :param overwrite:
    :return:
    """
    if os.path.exists(pkl_path) and not overwrite:
        return
    with open(pkl_path, 'wb') as f:
        # pickle.dump(vocab, f, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(vocab, f, protocol=0)
