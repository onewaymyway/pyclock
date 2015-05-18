from toolfuns import *
import time
import datetime

dayTimeS=24*60*60*1000;

def getTimeStamp(timeStr):
    timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S");
    timeStamp = int(time.mktime(timeArray));
    return timeStamp;
    
def getTimeStr():
    now=datetime.datetime.now();
    dayTime=now.strftime("%Y-%m-%d");
    print(dayTime);
    return dayTime;


class TimeList:

    def __init__(self,fileName="timeList.txt"):
        global dayTimeS;
        f=open(fileName,"r",encoding="utf-8");
        data=f.readlines();
        f.close();
        times={};
        daytime=getTimeStr();
        ttTime=int(time.time());
        for line in data:
            line=line.strip();
            cr=line.split(",");
            tTime={};
            tTime["time"]=cr[1].strip();
            tTime["msg"]=cr[0].strip();
            tTime["ctime"]=getTimeStamp(daytime+" "+tTime["time"]);
            if tTime["ctime"]<ttTime:
                tTime["ctime"]=tTime["ctime"]+dayTimeS;
            print(tTime["ctime"]);
            times[tTime["time"]]=tTime;

        self.times=times;

    def tick(self):
        global dayTimeS;
        tTime=int(time.time());
        print("tTime:"+str(tTime));
        
        for timest in self.times:
            cTime=self.times[timest];
            if int(cTime["ctime"])<=tTime:
                print("time:"+cTime["msg"]);
                cTime["ctime"]=int(cTime["ctime"])+dayTimeS;
                print("next:"+str(cTime["ctime"]));
                notice(cTime["msg"]);

      
def mainLoop():
    tT=TimeList();
    while(1):
        tT.tick();
        time.sleep(10);


if __name__ == '__main__':
    mainLoop()
