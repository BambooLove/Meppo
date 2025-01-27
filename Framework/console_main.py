#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import argparse

from Config.config_api import FOFA_API_KEY
from Framework import console_attack
from Seek import fofaapi
from Framework.console_attack import get_urls
from Framework.console_list import moudle_list, payload_list, payload_list_all
from Moudle.Moudle_index import *



def Console():
    parser = argparse.ArgumentParser()
    M_POC = parser.add_argument_group('漏洞检测模块')
    M_SEEK = parser.add_argument_group('资产爬取模块')

########################################################################################################################
    parser.add_argument("-l", dest='list',help="list",action='store_true')
    parser.add_argument("-ll", dest='listall',help="list all",action='store_true')
    parser.add_argument("-m", dest='moudle',help="moudle")
    parser.add_argument("-u", dest='url',help="target url")
    parser.add_argument("-f", dest='file',help="the file of target list")


    #漏洞检测模块
    M_POC.add_argument("-poc", dest='poc',help="漏洞检测")


    #资产爬取模块
    M_SEEK.add_argument("-fofa", dest='fofa',help="资产爬取")
    M_SEEK.add_argument("-num", dest='num',help="资产数量")

    args = parser.parse_args()

########################################################################################################################

    if args.fofa:
        try:
            if FOFA_API_KEY:
                if args.num and int(args.num) > 10000:
                    print("Num Don't > 10000 PLS~")
                else:
                    fofaapi.run(args.fofa, 1000)
            else:
                print("如需使用FofaAPI，请在Config/config_api下完成相关配置")
        except:
            print("如需使用FofaAPI，请在Config/config_api下完成相关配置")
    elif args.poc:
        try:
            if args.url:
                console_attack.run_poc(args.poc, args.url)
            elif args.file:
                console_attack.run_poc(args.poc, get_urls(args.file))
            else:
                print("Usage:\n\tpython Meppo.py -poc xxx -u http:xxx\n\tpython Meppo.py -poc xxx -f target.txt")
        except:
            print("Usage:\n\tpython Meppo.py -poc xxx -u http:xxx\n\tpython Meppo.py -poc xxx -f target.txt")
    elif args.moudle:
        try:
            if args.list:
                payload_list(args.moudle)
            elif args.url:
                console_attack.run_moudle(args.moudle, args.url)
            elif args.file:
                console_attack.run_moudle(args.moudle, get_urls(args.file))
            else:
                print("Usage:\n\tpython Meppo.py -m -l\n\tpython Meppo.py -m xxx -u http:xxx\n\tpython Meppo.py -m -f target.txt")
        except:
            print("Usage:\n\tpython Meppo.py -m -l\n\tpython Meppo.py -m xxx -u http:xxx\n\tpython Meppo.py -m -f target.txt")
    elif args.list:
        moudle_list()
    elif args.listall:
        payload_list_all()
    else:
        print("Usage:"
              "\n\tpython Meppo.py -l\t\t\t\tList All Moudles"
              "\n\tpython Meppo.py -ll\t\t\t\tList All Payloads"
              "\n\tpython Meppo.py -m xxx -l\t\t\tList Payload Of The Moudle"
              "\n\tpython Meppo.py -poc xxx -u target\t\t单目标 单POC监测"
              "\n\tpython Meppo.py -poc xxx -f targets.txt\t\t多目标 单POC监测"
              "\n\tpython Meppo.py -m xxx -u target\t\t单目标 模块监测"
              "\n\tpython Meppo.py -m xxx -f targets.txt\t\t多目标 模块监测"
              "\n\tpython Meppo.py -fofa APP=\"DEMO\"\t\tFOFA API 报告导出 num默认1000"
              "\n\tpython Meppo.py -fofa APP=\"DEMO\" -num 100\tFOFA API 报告导出 自定义数量")


########################################################################################################################
