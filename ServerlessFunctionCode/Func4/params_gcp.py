import time
init_st = time.time() * 1000
import os
import subprocess
import random
import uuid
# from rdrand import RdRandom
init_ed = time.time() * 1000


def hello_world(requrst):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    fun_st = time.time() * 1000
    proc = subprocess.Popen(["cat /proc/sys/kernel/random/boot_id"], stdout=subprocess.PIPE, shell=True)
    output = ""
    proc = subprocess.Popen(["cat /proc/uptime"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    output = output + "uptime: " + str(out) + "\n"
    proc = subprocess.Popen(["cat /proc/meminfo"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    output = output + "meminfo: " + str(out) + "\n"
    print(out)
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    output = output + "mac: " + mac + "\n"
    print (os.uname())
    device = os.stat("/home").st_dev

    # Print the raw device number 
    print("Raw device number:", device)
    # Extract the device minor number 
    # from the above raw device number 
    output = output + "times: " + str(os.times()) + "\n"
    print (os.getrandom(200, os.GRND_RANDOM))
    
    fun_ed = time.time() * 1000
    # return json.dumps(result)
    return ',InitStart:{},'.format(init_st) + 'InitEnd:{},'.format(init_ed) + 'functionStart:{},'.format(fun_st) + 'functionEnd:{},'.format(fun_ed)
    # return output

# hello_world()
