# -*- coding: utf-8 -*-
# Created by zhangzhuo@360.cn on 17/6/20
from . import blueprint


@blueprint.route("/hi/", methods=['GET'], versions=[1])
def hello():
    return "hello"