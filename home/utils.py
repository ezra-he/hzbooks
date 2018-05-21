# -*- coding: utf-8 -*-

import random
import uuid
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


def getUID(param):

    tmp_uuid = uuid.uuid3(uuid.NAMESPACE_DNS,param)
    return_uuid = tmp_uuid.replace("-","")
    return return_uuid