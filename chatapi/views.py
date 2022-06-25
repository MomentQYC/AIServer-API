#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import paddlehub as hub
import json
import re

def index(request):
    try:
        lac = hub.Module(name="plato-mini")
        porn_detection_cnn = hub.Module(name="porn_detection_cnn")
        #Rumor_prediction = hub.Module(name="Rumor_prediction")有bug，等待修复
        if request.method=='GET':
            MSG=str(request.GET.get('msg',default='我不说话'))
            TYPE=str(request.GET.get('format',default='json'))
            ot2=[MSG]
            origin_text = MSG
        #pattern = re.compile(ur'((https|http|ftp|rtsp|mms)?:\/\/)[^\s]+[^\W]')
        result0 = porn_detection_cnn.detection(texts=ot2, use_gpu=False, batch_size=1)
        p_list = result0[0]
        p_num = p_list.get('porn_probs')
        print(p_num)
        porn_num = 0.675
        porn_code = 0
        if p_num >= porn_num:
            porn_code = 1
            code = 0
        if porn_code == 0:
            '''result2 = Rumor_prediction.Rumor(texts=ot2, use_gpu=False)
            r_list = result2[0]
            r_tf = r_list.get('prediction')
            r_code = 0
            if r_tf == '谣言':
                r_code = 1
                code = 0
            if r_code == 0:'''#这里等待上面的bug修复
            with lac.interactive_mode(max_turn=300):
                results = lac.predict(origin_text)
                code = 0
    except Exception as e:
        print(e)
        results = ['Internal Error.']
        code =- 1
    try:
        #print(porn_code,r_code)
        print(porn_code)
    #except: porn_code,r_code = 0
    except:
        porn_code = 0
    if porn_code == 1:
        results = ['内含色情信息，不予返回，如有误判，请联系管理员!']
    #elif r_code == 1:
        #results = ['内含疑似谣言信息，不予返回，如有误判，请联系管理员!']等待修复
    if TYPE == 'json':
        data={
            'result':code,
            'content':results[0],
        }
        return HttpResponse(json.dumps(data,ensure_ascii=False),content_type="application/json,charset=utf-8")
    '''elif TYPE == 'html':
        data={
            'result':code,
            'content':results[0],
        }
        #return HttpResponse(('{"result":',code,',"content":"',results[0],'"}'),content_type="text/html,charset='utf-8',lang=zh-cn")
        return HttpResponse(json.dumps(data,ensure_ascii=False),content_type="text/html,charset=utf-8")'''#BUG(zh)
    else:
        return HttpResponse('Error Format!')
