#Author Joe Houng

import re, datetime, os, shutil

def ProcessFileName(Filename):
    #Split retrieved filename
    Dur = ""
    Start = ""
    Exp = ""
    SFileName = re.sub(r'\..+', "", Filename) 
    SFileName = SFileName.split("_")
    #Search through split filename for parameters dur, start, exp 
    for each in SFileName:
        if ("dur" in each):
            Dur = each.replace("dur", "")
            if Dur.isdigit() != True:
                Dur = ""
            #print Dur  
        if("start" in each):
            Start = each.replace("start", "")
            Start = completeISO(Start)
            if validate(Start) == -1:
                Start = ""
            #print Start
        if("exp" in each):
            Exp = each.replace("exp", "")
            Exp = completeISO(Exp)
            if validate(Exp) == -1:
                Exp = ""
            #print Exp  
    return [Dur, Start, Exp]

#Complete date string to ISO time standard of Year-Month-Day-Hour-Minuets-Seconds
def completeISO(date):
    dateList = date.split("-")
    while(len(dateList) < 6):
        dateList.append("00")
    dateList = "-".join(dateList)
    
    return dateList

#varify date string is ISO time standard
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d-%H-%M-%S')
        return 1
    except ValueError:
        return -1

#send a file to pp_home/pp_livetracks/Archived
def toArchive(runningFileName, pp_home):
    cwd = os.getcwd()
    parentDir = os.pardir
    src = pp_home + "/pp_live_tracks/" + runningFileName
    dst = pp_home + "/pp_live_tracks/Archived/"
    shutil.move(src,dst)
        
