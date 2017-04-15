# coding=utf-8
import re
import requests
from multiprocessing.dummy import Pool as ThreadPool
from optparse import OptionParser


TIMEOUT = 5


def _get_args():
    parser = OptionParser(usage="usage: %prog [options] args")
    parser.add_option("-u", "--url", help="Target URL", dest='url')
    parser.add_option("-d", "--dic", help="Dictionary path", dest='dic')
    parser.add_option("-n", "--number", help="Number of Thread,Default 10",
                      dest="num", type="int", default=10)
    parser.add_option("-t", "--timeout", help="Timeout,Default 5",
                      dest="timeout", type="int", default=5)
    opts, args = parser.parse_args()
    return opts


def _mult_getdata(alist, pro_num):
    '''开启多线程探测
       alist = [(url,dir),(url,dir)...]
    '''
    pool = ThreadPool(processes=pro_num)
    result = pool.map(_check, alist)
    pool.close()
    pool.join()
    return result


def _check(target_list):

    url, dirstr = target_list
    if dirstr.startswith('/'):
        dirstr = dirstr[1:]  # 字典中某些路径开头包括/，这里进行统一

    dirstr = dirstr.replace("\r\n", "")
    final_url = "%s/%s" % (url, dirstr)
    print final_url

    try:
        r = requests.head(final_url, timeout=TIMEOUT)
        if r.status_code not in [404, 500]:
            print("found one valid url!\nDo you want to continue?\n")
            return final_url
    except Exception as e:
        print e
    return ''


def main():
    opts = _get_args()
    url = opts.url
    if url.startswith("http") is False:
        url = "http://%s" % url
    if url.endswith("/"):
        url = url[:-1]
    num = opts.num
    dict_path = opts.dic or "all.txt"

    #switch the feature of station
    a=["asp.txt", "aspx.txt", "php.txt", "html.txt", "jsp.txt", "mdb.txt", "htm.txt", "txt.txt", "else.txt"]
    print("choose the feature: \n[0]asp\n[1]aspx\n[2]php\n[3]html\n[4]jsp\n[5]mdb\n[6]htm\n[7]txt\n[8]else...\npress enter to skip\n")
    flag = input("input: ")
    if int(flag)>=0 and int(flag)<=8:
        dict_path = a[int(flag)]

    global TIMEOUT
    TIMEOUT = opts.timeout
    if url:
        f = open(dict_path).read()
        dirs = f.split("\n")
        tempdirs = []
        print url
        for r in dirs:
            r = r.strip()
            #r = r.replace("\\","/")
            tempdirs.append((url, r))
        result = _mult_getdata(tempdirs, num)
        print "find dirs:", [x for x in result if x]
    else:
        print "Missing a mandatory option -u,use -h for help."
        return 0


if __name__ == "__main__":
    main()
