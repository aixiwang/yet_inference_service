#---------------------------------------------------------------------
# Yet Inference Service -- API
#
# Copyright by Aixi Wang <aixi.wang at hotmail dot com>
#----------------------------------------------------------------------

import os,sys,time
from redis import StrictRedis
#-----------------------------------------------------------------------
#                   global setting
#-----------------------------------------------------------------------

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASS = 'mypass'


SERVICE_NAME = 'yis'
Q_KEY = SERVICE_NAME + '@q'
R_KEY = SERVICE_NAME + '@r'
PID_KEY = SERVICE_NAME + '@pid'
#-----------------------------------------------------------------------
#                  common functions 
#-----------------------------------------------------------------------

#-------------------
# call_api
# input:  in_s
# output: out_s
#-------------------
def call_api(r,in_s):
    r.set(Q_KEY,in_s)
    n = 30
    while(n > 0):
        r_s = r.get(R_KEY)        
        # r_s get response
        print('call_genid r_s:',r_s)
        if r_s != None and len(r_s) > 0:
            r.delete(R_KEY)    
            return r_s
        
        time.sleep(0.1)
        n -= 1
        
    return None

#-----------------------
# set_encrypt_key
#-----------------------  
def set_encrypt_key(r,key):
    return 0
    
#-----------------------
# set_obj
#-----------------------
def set_obj(r,tag,obj):
    r.set(tag,obj)
    return 0

#-----------------------
# get_obj
#-----------------------  
def get_obj(r,tag):
    return r.get(tag)

    
#-----------------------
# del_obj
#-----------------------  
def del_obj(r,tag):
    r.delete(tag)
    return 0

#-----------------------
# install_app
#-----------------------
def install_app(r,app_filename,app_name):

    return 0

#-----------------------
# remove_app
#-----------------------
def remove_app(r,app_name):

    return 0


    
#-----------------------
# do_infer_sync
#-----------------------
def do_infer_sync(r,appname,tag):

    return 0

#-----------------------
# do_infer_async
#-----------------------
def do_infer_async(r,appname,tag):

    return 0


#-----------------------
# get_log
#-----------------------
def get_log(r):
    return get_obj(r,'log')

#-----------------------
# get_log
#-----------------------   
def del_log(r):
    return del_obj(r,'log')
    

#-----------------------
# stop_app
#-----------------------      
def stop_app(r,appname):
    return 0


#-----------------------
# get_app_list
#-----------------------   
def get_app_list(r):
    return get_obj(r,'app_list')


#-----------------------
# stop_all_app
#----------------------- 
def stop_all_app(r):
    return 0


    
#------------------------------------------------
#               main 
#------------------------------------------------
if __name__ == '__main__':
    if REDIS_PASS == '':
        r = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    else:
        r = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0, password=REDIS_PASS)

    print('connect to redis server, waiting for new rpc command ...')

    pass
