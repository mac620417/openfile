import serial  #載入串列函數
import datetime #載入時間函數
import configparser #載入config檔函數

config = configparser.ConfigParser() #啟動comfigparser
config.read('/etc/listenComCfg/config.ini') #將config由指定的ini檔讀進來

device = config['dev']['device']  # 定義將config secsion中的device讀進來
baudrate = config['dev']['buadrate']  # 定義將config secsion中的baudrate讀進來
#device = '/dev/ttyAMA0'  #由config中的secsion改變，好處是改config檔就好
#baudrate = 115200  #由config中的secsion改變，好處是改config檔就好
ser = serial.Serial(device, baudrate, timeout=1) #定義ser為(device,baudrate,和執行時間)
f = None #定義f


try:
    while True:
        now = datetime.datetime.now() #將now定義為抓取系統現在時間now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S") #定義otherStyleTime的顯示格式<now.strftime><請參照時間指令>
        ticks = otherStyleTime #定義ticks為otherStyleTime<這行是多的>
        linestr = ser.readlins() #定義linestr為上面定羕ser的內容中，將所有資料讀取<readline,readlines差異，請參考指令>
        total = ticks, linestr  #定義 total 為 ticks及linestr
        print (total)  #在執行時，會列印total的內容
        #將時間函數定義在這個while迴圈內，每次執行，會重新抓時間，避免執行檔案時，時間記錄會在第一次開啟檔案的時間，就不會每一秒跳一次

        if linestr:  #迴圈函數，只有linestr有資料讀入
            f = open('/tmp/the_com1.txt','wt') #打開指定目錄下之檔案，此檔案是可寫入w及指定文字格式t<請參考openflie指令函數>
            f.write(str(total))  #將上述定議之total以字串方式str寫入上一行開啟檔案的內容<若上述檔案後面指令函數無w，則無法寫入，也請注意在指定位置之檔案，檔案權限是否可寫入>
            break #若if這個迴圈寫入，就跳出這一段迴圈

except KeyboardInterrupt:  #呼應try迴圈，當鍵盤有任何指定進來就停止
    print ('keyboardInterrupt:')  #畫面會顯示鍵盤中斷

finally:    #請看finally指令參數
    if ser is not None: #若上述定義ser有資料
        ser.close()  #資料讀完後，會將ser這個執行序關閉
    if f is not None: #若上述定義f有資料完成時
        f.close()  #關閉開啟的檔案<只要有fopen，一定要有fclose>
