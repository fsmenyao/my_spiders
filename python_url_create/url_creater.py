import pandas as pd
import time
import urllib


def baidu():
    csvfile = pd.read_csv('words.csv', encoding='gbk')
    words_np = csvfile.values
    words = [word[0] for word in words_np]

    csvfile = pd.read_csv('starts.csv', encoding='gbk')
    words_np = csvfile.values
    starts = [word[0] for word in words_np]

    csvfile = pd.read_csv('ends.csv', encoding='gbk')
    words_np = csvfile.values
    ends = [word[0] for word in words_np]

    for i, word in enumerate(words):
        txtfile = open('.\\URL_BAIDU_A\\url_baidu_' + word + '.csv', 'a+', encoding='utf-8')
        one = 86400

        timeArray = time.strptime(starts[i], "%Y-%m-%d")
        # timeArray = time.strptime("2018-01-01", "%Y-%m-%d")
        timeStamp = int(time.mktime(timeArray))
        start = timeStamp

        timeArray = time.strptime(ends[i], "%Y-%m-%d")
        # timeArray = time.strptime('2018-01-02', "%Y-%m-%d")
        timeStamp = int(time.mktime(timeArray))
        end = timeStamp

        print(i, word)
        print(start)
        print(end)

        a = start
        while True:
            b = a + one
            if b > end:
                print('end time------------------')
                break
            url = "https://www.baidu.com/s?rtt=4&bsst=1&cl=2&tn=news&rn=50" + \
                  "&word=" + urllib.parse.quote(word) + \
                  "&gpc=stf%3D" + str(a) + "%2C" + str(b)+"%7Cstftype%3D2"
            # print(url)
            txtfile.write(url + '\n')
            a = b
        txtfile.close()


def google():
    csvfile = pd.read_csv('wordsH.csv', encoding='gbk')
    words_np = csvfile.values
    words = [word[0] for word in words_np]

    csvfile = pd.read_csv('starts.csv', encoding='gbk')
    words_np = csvfile.values
    starts = [word[0] for word in words_np]

    csvfile = pd.read_csv('ends.csv', encoding='gbk')
    words_np = csvfile.values
    ends = [word[0] for word in words_np]

    for i, word in enumerate(words):
        urlfile = open('.\\URL_GOOGLE_CSV_H' + '\\url_google_' + word + '.csv', 'a+', encoding='utf-8')
        one = 86400

        timeArray = time.strptime(starts[i], "%Y-%m-%d")
        # timeArray = time.strptime("2018-01-01", "%Y-%m-%d")
        timeStamp = int(time.mktime(timeArray))
        start = timeStamp

        timeArray = time.strptime(ends[i], "%Y-%m-%d")
        # timeArray = time.strptime('2018-01-02', "%Y-%m-%d")
        timeStamp = int(time.mktime(timeArray))
        end = timeStamp

        print(i, word)
        # print(start)
        # print(end)

        a = start
        while True:
            b = a + one
            if b > end:
                # print('end time------------------')
                break
            url = "https://www.google.com.hk/search?q=" + \
                  urllib.parse.quote(word) + \
                  "&newwindow=1&safe=strict" + \
                  "&tbs=cdr:1,cd_min:" + stamp2localtime(a) + ",cd_max:" + stamp2localtime(b) + ",sbd:1" + \
                  "&tbm=nws&source=lnt&sa=X&ved=0ahUKEwiv24LZr5ziAhWBErwKHSo4ATYQpwUIHQ&biw=1163&bih=560&dpr=1.65"
            # print(url)
            urlfile.write(url + '\n')
            a = b
        urlfile.close()


def stamp2localtime(timestamp):
    # 转换成localtime
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%m/%d/%Y", time_local)
    return dt


if __name__ == '__main__':
    # google()
    baidu()
