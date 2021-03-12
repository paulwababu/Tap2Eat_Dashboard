from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
import datetime
from datetime import timedelta
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from itertools import chain
from django.http import HttpResponse, HttpResponseRedirect
import csv


#global mrfff, mcffd, mdffd
mrfff = ""
mcffd = ""
mdffd = ""
#global tbtd, tbd, tbttd
tbtd = ""
tbd = ""
tbttd = ""
completedThors = ""
completedThorrs = ""
completedThorrrs = ""
completedWed = ""
completedWedd = ""
completedWeddd = ""
comptue = ""
comptues = ""
comptuesd = ""
comptuee = ""
comptuesdd = ""
comptuess = ""
completedWedo = ""
completedWeddo = ""
completedWedddo = ""
completedWebo = ""
completedWebbo = ""
completedWebbbo = ""
completedWebDo = ""
completedWebbDo = ""
completedWebbbDo = ""
completedMonm = ""
completedMonmm = ""
completedMonmmm = ""
coomptue = ""
cooomptues = ""
cooomptuesd = ""
cm = ""
cmmm = ""
cmmmm = ""
furahiday = ""
friesday = ""
furahia = ""
thurahiday = ""
thurahia = ""
thriesday = ""
completedWEBO = ""
completedWEBBO = ""
completedWEBBBO = ""       
completedWEBDO = ""
completedWEBBDO = ""
completedWEBBBDO = ""
cWEBBBDO = ""
cWEBDO = ""
cWEBBDO = ""

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['psw']
        response = requests.post("https://tap2eat.co.ke/pilot/api/v1/user/auth", json={"userContact": username, "password": password})
        if response.status_code == 200:
            request.session['user'] = username
            token = response.json()
            access = token['content']
            access_token = access['token']
            request.session['access_token'] = access_token
            return redirect('home')
    return render(request, 'signin.html')           

def home(request):
    try:
        token = request.session['access_token']
    except:
        print("Session Not found")
        return render(request, 'home2.html')
    newDateFeature = datetime.datetime.now()
    newDateFeatureYesterday = newDateFeature - timedelta(1)
    yesterdaysstartdate = str(newDateFeatureYesterday.date())
    newstartdate = str(newDateFeature.date())
    today12pm = newDateFeature.replace(hour=12, minute=30, second=0, microsecond=0)
    if newDateFeature < today12pm:
        newDateFormat = '?startDate='+ yesterdaysstartdate + '_00:00&endDate=' + yesterdaysstartdate + '_23:59'
        print("Showing yesterdays Summary Endpoint as it is not yet 12:30 pm")
    else:
        newDateFormat = '?startDate='+ newstartdate + '_00:00&endDate=' + newstartdate + '_23:59'
        print("Showing current Day Summary endpoint as 12:30 pm has reached!")
    summary = 'https://tap2eat.co.ke/pilot/api/v1/report/summary' 
    response2 = requests.get('https://tap2eat.co.ke/pilot/api/v1/report/summary'+newDateFormat, headers={'Authorization': f'Bearer {token}'})
    paymentsApi = 'https://tap2eat.co.ke/pilot/api/v1/payments'
    info = '?pgSize=40&pgNum=0&sortOrder=asc'
    response3 = requests.get(paymentsApi + info, headers={'Authorization': f'Bearer {token}'})
    if response2.status_code == 200 and 'user' in request.session:
        if response3.status_code == 200 and 'user' in request.session:
            current_user = request.session['user']
            data5 = response2.json()
            #print(data5)
            todoss = data5['content']
            usera =  todoss.get('devices', 0)
            data = {
                "devices": usera,
                }
            a = data['devices']#['nfc_tag']
            activee = (a.get('nfc_tag', None)) #
            tagg = (activee)
            ###########################################
            ###Amount Collected
            moneyCollected = todoss.get('transactions')
            for moneey in moneyCollected:
                if moneey['transactionType'] == 'acc_credit':
                    money = int(moneey['totalAmount'])
            #############################################################################
            #################Total Registered Users
            totalRegisteredUsers = data5['content']
            registered = totalRegisteredUsers.get('users', 0)
            ##print(registered)
            reg = {
                "regist":registered,
            }
            bbreg = reg['regist']
            registeredList = bbreg['totalRegisteredUsers']
            for register in registeredList:
                registeredTotalNi = register.get("role")
                if registeredTotalNi == 'student':
                    totalStudee = register['number']
            ##################### PENETRATION RATE #####################################################

            ######################TOTAL STUDENTS IN ENTITY########################################################
            responsible = requests.get('https://tap2eat.co.ke/pilot/api/v1/operational-entity/1', headers={'Authorization': f'Bearer {token}'})
            contentt = responsible.json()
            dataNeeded = contentt['content']
            ##print(dataNeeded)
            entity = dataNeeded.get('operationalEntityPops')
            for tt in entity:
                if tt['role']['name'] == 'student':
                    ndiini = tt['populationSize']
            ##############################################################################
            todoss = data5['content']
            useraa =  todoss.get('mealTaps', 0)
            ##print(useraa)
            data7 = {
                "mealTaps": useraa,
            }
            aa = data7['mealTaps']
            ##print(aa)
            for items in aa:
                correct = items.get('status', 0)
                if correct == 'complete':
                    completedCorrect = items['count']
                if correct == 'rejected':
                    rejection = items['count']
                if correct == 'duplicate':
                    duplication = items['count']             
            ######################################################################################
            project = data5['content']
            nextmeal = project.get('nextDayProjection', None)
            nextmealProjection = int(nextmeal or 0)

            day = datetime.datetime.now()
            tomorrow = day + timedelta(1)
            kesho_kutwa = tomorrow + timedelta(1)
            mtondo = kesho_kutwa +timedelta(1)
            ###TAP ANALYSIS
            #########################################################################################
            previousDay = day - timedelta(1)
            endingDate = day - timedelta(1)
            p = endingDate.date()
            startingDate = endingDate - timedelta(1)
            pp = startingDate.date()
            startDate = str(pp)
            endDate = str(p)
            currentDayTapsDate = '?startDate='+ startDate +'_00:00&endDate='+ endDate +'_23:59'
            currentDayTaps = requests.get(summary + currentDayTapsDate, headers={'Authorization': f'Bearer {token}'})
            ##print(currentDayTapsDate)
            rawData = currentDayTaps.json()
            contentdata = rawData['content']
            contentdata1 = contentdata.get('mealTaps', 0)
            for item in contentdata1:
                corrects = item.get('status', 1)
                if corrects == 'complete':
                    completedCorrects = item['count']
                if corrects == 'rejected':
                    completedCorrectss = item['count']
                if corrects == 'duplicate':
                    completedCorrectsss = item['count']               
            #previous day taps        
            previousDayTaps = completedCorrects
            ########################################################################################
            ########### WEEKLY TAP TRENDS NEW #########################################################
            #get current day
            leo = day.strftime("%A")
            if leo == 'Monday':
                startDateMon = str(day.date())
                endDateMon = str(day.date())
                reqForMonFormat = '?startDate='+ startDateMon + '_00:00&endDate=' + endDateMon + '_23:59'
                ##print(reqForMonFormat)
                requestMM = requests.get(summary + reqForMonFormat, headers={'Authorization': f'Bearer {token}'})
                dataMondM = requestMM.json()
                rawMondM = dataMondM['content']
                rawMondTM = rawMondM.get('mealTaps', None)
                ##print(rawMondTM)
                global completedMonm, completedMonmm, completedMonmmm
                for tapses in rawMondTM:
                    rawdD = tapses.get('status', None)
                    if rawdD == 'complete':
                        completedMonm = tapses['count']
                    if rawdD == 'rejected':
                        completedMonmm = tapses['count']
                    if rawdD == 'duplicate':
                        completedMonmmm = tapses['count']        
                ###########################################
            elif leo == 'Tuesday':
                startDateTues = str(day.date())
                endDateTues = str(day.date())
                reqForTueFormat = '?startDate='+ startDateTues + '_00:00&endDate=' + endDateTues + '_23:59'
                requestTuesday = requests.get(summary + reqForTueFormat, headers={'Authorization': f'Bearer {token}'})
                #make subsequent requests for tuesday and Monday
                ##
                dataTueM = requestTuesday.json()
                rawTueM = dataTueM['content']
                rawTueTM = rawTueM.get('mealTaps', 0)
                ##print(rawWedd)
                global cm, cmmm, cmmmm
                for tups in rawTueTM:
                    rawdDD = tups.get('status', 0)
                    if rawdDD == 'complete':
                        cm = tups['count']
                    if rawdDD == 'rejected':
                        cmmm = tups['count']
                    if rawdDD == 'duplicate':
                        cmmmm = tups['count']        
                #####Get subsequent request for Monday now
                MonEndD = day - timedelta(1)
                MonStartD = day - timedelta(1)
                MonEE = str(MonEndD.date())
                MonSS = str(MonStartD.date())
                reqMONForm = '?startDate='+ MonSS + '_00:00&endDate=' + MonEE + '_23:59'
                ##print(reqTueForm)
                requestYAmon = requests.get(summary + reqMONForm, headers={'Authorization': f'Bearer {token}'})
                dataMONDD = requestYAmon.json()
                rawMONDDD = dataMONDD['content']
                rawMOO = rawMONDDD.get('mealTaps', 0)
                ##print("sdwe",rawMOO)
                global coomptue, cooomptues, cooomptuesd
                for tops in rawMOO:
                    ruwwwTue = tops.get('status', 0)
                    if ruwwwTue == 'complete':
                        coomptue = tops['count']
                for topps in rawMOO:
                    riwwTue = topps.get('status', 0)
                    if riwwTue == 'rejected':
                        cooomptues = topps['count']
                        ##print(cooomptues)
                for toppps in rawMOO:
                    rwsTue = toppps.get('status', 0)
                    if rwsTue == 'duplicate':
                        cooomptuesd = toppps['count']
                        ##print(cooomptuesd)
                ###########################################
            elif leo == 'Wednesday':
                #get data for that day and subsequent request to be made for that day and also for previous days
                startDateWed = str(day.date())
                endDateWed = str(day.date())
                #?startDate=2021-01-04_00:02&endDate=2021-02-05_00:00
                reqForWedFormat = '?startDate='+ startDateWed + '_00:00&endDate=' + endDateWed + '_23:59'
                ##print(reqForWedFormat)
                requestWednesday = requests.get(summary + reqForWedFormat, headers={'Authorization': f'Bearer {token}'})
                dataWed = requestWednesday.json()
                rawWed = dataWed['content']
                rawWedd = rawWed.get('mealTaps', 0)
                ##print(rawWedd)
                global completedWed, completedWedd, completedWeddd
                for tapis in rawWedd:
                    rawWeddd = tapis.get('status', 0)
                    if rawWeddd == 'complete':
                        completedWed = tapis['count'] #wednesday taps success
                        ##print(completedWed)
                for tapiss in rawWedd:
                    rawWedddd = tapiss.get('status', 0)
                    if rawWedddd == 'rejected':
                        completedWedd = tapiss['count'] #wednesday taps rejected
                for tapisss in rawWedd:
                    rawWedddddd = tapisss.get('status', 0)
                    if rawWedddddd == 'duplicate':
                        completedWeddd = tapisss['count'] #wednesday taps duplicate
                #get subsequent request for tueday
                tueEndD = day - timedelta(1)
                tueStartD = day - timedelta(1)
                tueEE = str(tueEndD.date())
                tueSS = str(tueStartD.date())
                reqTueForm = '?startDate='+ tueEE + '_00:00&endDate=' + tueSS + '_23:59'
                ##print(reqTueForm)
                requesttue = requests.get(summary + reqTueForm, headers={'Authorization': f'Bearer {token}'})
                dataTueD = requesttue.json()
                rawTuesd = dataTueD['content']
                rawTuesday = rawTuesd.get('mealTaps', 0)
                ##print(rawTuesday)
                global comptue, comptues, comptuesd
                for tapos in rawTuesday:
                    rawwwTue = tapos.get('status', 0)
                    if rawwwTue == 'complete':
                        comptue = tapos['count']
                        ##print(comptue)
                for taposi in rawTuesday:
                    rawwTue = taposi.get('status', 0)
                    if rawwTue == 'rejected':
                        comptues = taposi['count']
                for taposii in rawTuesday:
                    rawsTue = taposii.get('status', 0)
                    if rawsTue == 'duplicate':
                        comptuesd = taposii['count']
                        ##print(comptuesd)
                #get subsequent Data for Monday now
                mondayendD = day - timedelta(2)
                mondaystartD = day - timedelta(2)
                monEE = str(mondayendD.date())
                monSS = str(mondaystartD.date())
                ##print(mondayendD)
                reqMonForm = '?startDate='+ monSS + '_00:00&endDate=' + monEE + '_23:59'
                ##print(reqMonForm)
                requestmond = requests.get(summary + reqMonForm, headers={'Authorization': f'Bearer {token}'})
                dataMonD = requestmond.json()
                rawMond = dataMonD['content']
                rawMonday = rawMond.get('mealTaps', 0)
                ##print(rawMonday)
                global comptuee, comptuess, comptuesdd
                for taos in rawMonday:
                    rawwMond = taos.get('status', 0)
                    if rawwMond == 'complete':
                        comptuee = taos['count']
                        ##print(comptuee)
                for taosi in rawMonday:
                    rawwwMond = taosi.get('status', 0)
                    if rawwwMond == 'rejected':
                        comptuess = taosi['count']
                for taosii in rawMonday:
                    rawwwwMond = taosii.get('status', 0)
                    if rawwwwMond == 'duplicate':
                        comptuesdd = taosii['count']                           
            elif leo == 'Thursday':
                startDateThor = str(day.date())
                endDateThor = str(day.date())
                reqForThorFormat = '?startDate='+ startDateThor + '_00:00&endDate=' + endDateThor + '_23:59'
                requestThursday = requests.get(summary + reqForThorFormat, headers={'Authorization': f'Bearer {token}'})
                #get json data for Thursday
                dataThur = requestThursday.json()
                rawThur = dataThur['content']
                rawThursd = rawThur.get('mealTaps', 0)
                global completedThors, completedThorrs, completedThorrrs
                for tapps in rawThursd:
                    rawThor = tapps.get('status', 0)
                    if rawThor == 'complete':
                        completedThors = tapps['count']
                    if rawThor == 'rejected':
                        completedThorrs = tapps['count']
                    if rawThor == 'duplicate':
                        completedThorrrs = tapps['count']       
                #Wednesday Taps on Thursday
                weddoStart = day - timedelta(1)
                weddoEnd = day - timedelta(1)
                wedEE = str(weddoEnd.date())
                wedSS = str(weddoStart.date())
                reqWedF = '?startDate='+ wedSS + '_00:00&endDate=' + wedEE + '_23:59'
                requestWED = requests.get(summary + reqWedF, headers={'Authorization': f'Bearer {token}'})
                datawedD = requestWED.json()
                rawWeds = datawedD['content']
                rawWednesday = rawWeds.get('mealTaps', 0)
                global completedWedo, completedWeddo, completedWedddo
                for taspis in rawWednesday:
                    raweddd = taspis.get('status', 0)
                    if raweddd == 'complete':
                        completedWedo = taspis['count']
                    if raweddd == 'rejected':
                        completedWeddo = taspis['count']
                    if raweddd == 'duplicate':
                        completedWed = taspis['count']
                        #######################################################################################
                #Tuesday Taps on Thursday
                tuStart = day - timedelta(2)
                tuEnd = day - timedelta(2)
                tuedEE = str(tuEnd.date())
                tuedSS = str(tuStart.date())
                reqtueF = '?startDate='+ tuedSS + '_00:00&endDate=' + tuedEE + '_23:59'
                requestTUE = requests.get(summary + reqtueF, headers={'Authorization': f'Bearer {token}'})
                dataTUEDraw = requestTUE.json()
                rawtuesdaY = dataTUEDraw['content']
                rawW = rawtuesdaY.get('mealTaps', 0)
                global completedWebo, completedWebbo, completedWebbbo
                for tagpis in rawW:
                    rawedddo = tagpis.get('status', 0)
                    if rawedddo == 'complete':
                        completedWebo = tagpis['count']
                for tagpisd in rawW:
                    deddd = tagpisd.get('status', 0)
                    if deddd == 'rejected':
                        completedWebbo = tagpisd['count']
                for tagpisdd in rawW:
                    dered = tagpisdd.get('status', 0)
                    if dered == 'duplicate':
                        completedWebbbo = tagpisdd['count']
                ###########################################################################
                # Monday
                #Monday Taps on Thursday
                tuStartM = day - timedelta(3)
                tuEndM = day - timedelta(3)
                tuedEEM = str(tuEndM.date())
                tuedSSM = str(tuStartM.date())
                reqmondF = '?startDate='+ tuedSSM + '_00:00&endDate=' + tuedEEM + '_23:59'
                requestmondo = requests.get(summary + reqmondF, headers={'Authorization': f'Bearer {token}'})
                dataMONDAYraw = requestmondo.json()
                rawDM = dataMONDAYraw['content']
                rawWDM = rawDM.get('mealTaps', 0)
                global completedWebDo, completedWebbDo, completedWebbbDo
                for tagp in rawWDM:
                    rawedddof = tagp.get('status', 0)
                    if rawedddof == 'complete':
                        completedWebDo = tagp['count']
                for tagpy in rawWDM:
                    dedddr = tagpy.get('status', 0)
                    if dedddr == 'rejected':
                        completedWebbDo = tagpy['count']
                for tagpyd in rawWDM:
                    deredb = tagpyd.get('status', 0)
                    if deredb == 'duplicate':
                        completedWebbbDo = tagpyd['count']                            
            else:
                startDateFri = str(day.date())
                endDateFri = str(day.date())
                reqForFriFormat = '?startDate='+ startDateFri + '_00:00&endDate=' + endDateFri + '_23:59'
                requestFriday = requests.get(summary + reqForFriFormat, headers={'Authorization': f'Bearer {token}'})
            ##########################SAMPLE!"£$&^*()(*&^%$%^&^%$%^&$$^&&*^%$"!"£$%^^&&*****")))))((((((((((((****************))))))))))))
                
                #get json data for Friday
                datafryd = requestFriday.json()
                rawFridayData = datafryd['content']
                rawFridayDataMealTaps = rawFridayData.get('mealTaps', 0)
                ##print(rawFridayDataMealTaps)
                global furahiday, furahia, friesday
                for ts in rawFridayDataMealTaps:
                    rawThorp = ts.get('status', 0)
                    if rawThorp == 'complete':
                        furahiday = ts['count'] #Thursday Taps
                for tsi in rawFridayDataMealTaps:
                    rawThorrp = tsi.get('status', 0)
                    if rawThorrp == 'rejected':
                        furahia = tsi['count']
                for tppo in rawFridayDataMealTaps:
                    rawThorrrp = tppo.get('status', 0)
                    if rawThorrrp == 'duplicate':
                        friesday = tppo['count']
                #Thursday Taps on Friday
                thuStart = day - timedelta(1)
                thuEnd = day - timedelta(1)
                thuEE = str(thuEnd.date())
                thuSS = str(thuStart.date())
                reqthuF = '?startDate='+ thuSS + '_00:00&endDate=' + thuEE + '_23:59'
                requestTHUR = requests.get(summary + reqthuF, headers={'Authorization': f'Bearer {token}'})
                datathufD = requestTHUR.json()
                rawThurr = datathufD['content']
                rawTHURSDAY = rawThurr.get('mealTaps', 0)
                global thurahia, thriesday, thurahiday
                for tspis in rawTHURSDAY:
                    rator = tspis.get('status', 0)
                    if rator == 'complete':
                        thurahia = tspis['count']
                for tdpis in rawTHURSDAY:
                    rddd = tdpis.get('status', 0)
                    if rddd == 'rejected':
                        thurahiday = tdpis['count']
                for tbpis in rawTHURSDAY:
                    rrddd = tbpis.get('status', 0)
                    if rrddd == 'duplicate':
                        thriesday = tbpis['count']
                        #######################################################################################
                #Wednesday Taps on friday
                ttart = day - timedelta(2)
                tEnd = day - timedelta(2)
                tudEE = str(tEnd.date())
                tudSS = str(ttart.date())
                reqtF = '?startDate='+ tudSS + '_00:00&endDate=' + tudEE + '_23:59'
                requestWEDNESDAY = requests.get(summary + reqtF, headers={'Authorization': f'Bearer {token}'})
                dataWEDNESDAYraw = requestWEDNESDAY.json()
                rawraw = dataWEDNESDAYraw['content']
                rawrawraw = rawraw.get('mealTaps', 0)
                global completedWEBO, completedWEBBO, completedWEBBBO
                for tgpis in rawrawraw:
                    rtdddo = tgpis.get('status', 0)
                    if rtdddo == 'complete':
                        completedWEBO = tgpis['count']
                for tgpisd in rawrawraw:
                    dedddw = tgpisd.get('status', 0)
                    if dedddw == 'rejected':
                        completedWEBBO = tgpisd['count']
                for tgpisdd in rawrawraw:
                    deredp = tgpisdd.get('status', 0)
                    if deredp == 'duplicate':
                        completedWEBBBO = tgpisdd['count']
                ###########################################################################
                #
                #Tuesday taps on Friday
                tuStartTuesday = day - timedelta(3)
                tuEndTuesday = day - timedelta(3)
                tuedE = str(tuEndTuesday.date())
                tuedS = str(tuStartTuesday.date())
                reqtuF = '?startDate='+ tuedS + '_00:00&endDate=' + tuedE + '_23:59'
                requestfortuesday = requests.get(summary + reqtuF, headers={'Authorization': f'Bearer {token}'})
                dataTUESDAYraw = requestfortuesday.json()
                rawTD = dataTUESDAYraw['content']
                rawTDD = rawTD.get('mealTaps', 0)
                global completedWEBDO, completedWEBBDO, completedWEBBBDO
                for tgp in rawTDD:
                    rawedddofDD = tgp.get('status', 0)
                    if rawedddofDD == 'complete':
                        completedWEBDO = tgp['count']
                for tgpy in rawTDD:
                    dedddrDD = tgpy.get('status', 0)
                    if dedddrDD == 'rejected':
                        completedWEBBDO = tgpy['count']
                        print(completedWEBBDO)
                for tgpyd in rawTDD:
                    deredbDD = tgpyd.get('status', 0)
                    if deredbDD == 'duplicate':
                        completedWEBBBDO = tgpyd['count']
                #######################################################

                #Monday taps on Friday
                tuStartMONDAY = day - timedelta(4)
                tuEndMONDAY = day - timedelta(4)
                tuedEDF = str(tuEndMONDAY.date())
                tuedSDF = str(tuStartMONDAY.date())
                reqtuFDF = '?startDate='+ tuedSDF + '_00:00&endDate=' + tuedEDF + '_23:59'
                requestformONDAY = requests.get(summary + reqtuFDF, headers={'Authorization': f'Bearer {token}'})
                dataMODNAYraw = requestformONDAY.json()
                rawTDC = dataMODNAYraw['content']
                rawTDDC = rawTDC.get('mealTaps', 0)
                global cWEBDO, cWEBBDO, cWEBBBDO
                for tg in rawTDDC:
                    dddofDD = tg.get('status', 0)
                    if dddofDD == 'complete':
                        cWEBDO = tg['count']
                for ty in rawTDDC:
                    dddrDD = ty.get('status', 0)
                    if dddrDD == 'rejected':
                        cWEBBDO = ty['count']
                for td in rawTDDC:
                    dbDD = td.get('status', 0)
                    if dbDD == 'duplicate':
                        cWEBBBDO = td['count']
            ##########################SAMPLE!"£$&^*()(*&^%$%^&^%$%^&$$^&&*^%$"!"£$%^^&&*****")))))((((((((((((****************))))))))))))
            
            
            #########################################################################################
            currentDay = day.strftime("%A")
            tomorroww = tomorrow.strftime("%A")
            kesho_kutwaa = kesho_kutwa.strftime("%A")
            mtondoo = mtondo.strftime("%A")
            ##print(currentDay)
            ##########################################################################################
            
            ##########################################################################################

            dataMpesa = response3.json()
            #todos = response2.json()
            mpesa = dataMpesa['content']
            tdata =mpesa.get('data', 0)
            #print(tdata)
            pp = Paginator(tdata, 10)
            pageNum = request.GET.get('page', 1)
            page1 = pp.page(pageNum)
        
            ######################################################################################
            ######################################################################################
            #Handling Pagination

            ######################################################################################
            
            projects = data5['content']
            useraaaa =  projects.get('endOfDay', 0)
            ##print(useraaaa)
            data77 = {
                "mealTapss": useraaaa,
            }
            aaa = data77['mealTapss']
            ##print(aaa)
            activeer = aaa['mealsShortfall']
            #print(activeer)
            #####################################################################################
            #####################################################################################
             ##################### PENETRATION RATE #####################################################
            penetration = totalStudee / ndiini * 100
            ##print(penetration)
            penetrationRate = int(penetration)
            #####################################################################################
            ####### Date time
            #day = datetime.datetime.now()
            #noww = datetime.now() # current date and time
            theDay = day.today().strftime('%A') #thursday
            theDate = day.strftime("%d") #25
            theMonth = day.strftime("%B") #'JANUARY'
            theYear = day.strftime("%Y") #2021
            #####################################################################################
            ############# Specific Date end point
            if request.method == 'POST' and 'btnform1' in request.POST:
                dayEntered = (request.POST['btnform1'])
                todaytoday = day.today().strftime('%A')
                #print(todaytoday)
                if todaytoday == 'Thursday':
                    #getDayEnteredOnForm = dayEntered
                    mondayday = day - timedelta(3)
                    tuesdayday = day -timedelta(2)
                    wednesdayday = day - timedelta(1)
                    #requests for each day
                    if dayEntered == 'Monday':
                        theDayM = "Monday" #thursday
                        theDateM = mondayday.strftime("%d") #25
                        theMonthM = mondayday.strftime("%B") #'JANUARY'
                        theYearM = mondayday.strftime("%Y") #2021
                        stdate = str(mondayday.date())
                        timeFormatDay = '?startDate='+ stdate + '_00:00&endDate=' + stdate + '_23:59'
                        requestMondayFormat = requests.get(summary + timeFormatDay, headers={'Authorization': f'Bearer {token}'})
                        #print("TESTING:", requestMondayFormat)
                        rawResponseMonday = requestMondayFormat.json()
                        cleanedMonday = rawResponseMonday['content']
                        usela =  cleanedMonday.get('mealTaps', None)
                        for monddd in usela:
                            mddd = monddd.get('status', None)
                            if mddd == 'complete':
                                m = monddd['count']
                                #print("COMPLETED MONDAY", m)
                            if mddd == 'rejected':
                                mm = monddd['count']
                                #print("Rejected MONDAY", mm)
                            if mddd == 'duplicate':
                                mmm = monddd['count']
                                #print("Duplicated MONDAY", mmm)
                        #missed meals
                        missedMealsMonday = rawResponseMonday['content']
                        missedMealsMon =  missedMealsMonday.get('endOfDay', None)
                        ##print()
                        datamissedmeals = {
                            "mealTapssd": missedMealsMon,
                        }
                        miss = datamissedmeals['mealTapssd']
                        ##print(aaa)
                        misses = miss['mealsShortfall']
                        #next meal projections
                        nextMl = rawResponseMonday['content']
                        nextmeal1 = nextMl.get('nextDayProjection', None)
                        nextmealProjection1 = int(nextmeal or 0)
                        #tag new issues
                        #todoss = data5['content']
                        tagNewIssues =  nextMl.get('devices', None)
                        ##print(usera)
                        dataRaw = {
                            "devicesc": tagNewIssues,
                            }
                        nfcc = dataRaw['devicesc']#['nfc_tag']
                        activeeTagg = (nfcc.get('nfc_tag', None)) #
                        taggMon = (activeeTagg)
                        ##Money Collected
                        getMoney = nextMl.get('transactions')
                        for getit in getMoney:
                            if getit['transactionType'] == 'acc_credit':
                                moneyT = int(getit['totalAmount'])
                        data23 = {
                            "moneyCollected":moneyT,
                            'current_user':current_user,
                            "theDate":theDateM,
                            "theMonth":theMonthM,
                            "theYear":theYearM,
                            "theDay":theDayM,
                            "cmmmm":cmmmm,
                            "cm":cm,
                            "cmmm":cmmm,
                            "coomptue":coomptue,
                            "cooomptues":cooomptues,
                            "cooomptuesd":cooomptuesd,
                            "currentDay":currentDay,
                            "completedMonmmm":completedMonmmm,
                            "completedMonmm":completedMonmm,
                            "completedMonm":completedMonm,
                            "furahiday":furahiday,
                            "tagg":taggMon,
                            "furahia":furahia,
                            "friesday":friesday,
                            "thurahia":thurahia,
                            "thurahiday":thurahiday,
                            "thriesday":thriesday,
                            "completedWEBO":completedWEBO,
                            "completedWEBBO":completedWEBBO,
                            "completedWEBBBO":completedWEBBBO,
                            "completedWEBDO":completedWEBDO,
                            "completedWEBBDO":completedWEBBDO,
                            "completedWEBBBDO":completedWEBBBDO,
                            "cWEBDO":cWEBDO,
                            "cWEBBDO":cWEBBDO,
                            "cWEBBBDO":cWEBBBDO,
                            "completedWebDo":completedWebDo,
                            "completedWebbDo":completedWebbDo,
                            "completedWebbbDo":completedWebbbDo,
                            "completedWebo":completedWebo,
                            "completedWebbo":completedWebbo,
                            "completedWebbbo":completedWebbbo,
                            "completedWedo":completedWedo,
                            "completedWeddo":completedWeddo,
                            "completedWedddo":completedWedddo,
                            "completedThors":completedThors,
                            "completedThorrs":completedThorrs,
                            "completedThorrrs":completedThorrrs,
                            "comptuee":comptuee,
                            "comptuess":comptuess,
                            "comptuesdd":comptuesdd,
                            "comptue":comptue,
                            "comptues":comptues,
                            "comptuesd":comptuesd,
                            "completedWed":completedWed,
                            "completedWedd":completedWedd,
                            "completedWeddd":completedWeddd,
                            "penetrationRate":penetrationRate,
                            "ndiini":ndiini,
                            "totalStudee":totalStudee,
                            "rejection":mm,
                            "duplication":mmm,
                            "completedCorrects":completedCorrects,
                            "completedCorrectss":completedCorrectss,
                            "completedCorrectsss":completedCorrectsss,
                            "completedCorrect":m,
                            "page1":page1,
                            "activee":activee,
                            "projectss":misses,
                            "nextmealProjection":nextmealProjection1,
                            "mealtaps":aa,
                            "money":mpesa,
                        }
                        return render(request, "home.html",  data23)
                    if dayEntered == 'Tuesday':
                        theDayT = "Tuesday" #thursday
                        theDateT = tuesdayday.strftime("%d") #25
                        theMonthT = tuesdayday.strftime("%B") #'JANUARY'
                        theYearT = tuesdayday.strftime("%Y") #2021
                        sttdate = str(tuesdayday.date())
                        timeFormatDayy = '?startDate='+ sttdate + '_00:00&endDate=' + sttdate + '_23:59'
                        requestTuesdayFormat = requests.get(summary + timeFormatDayy, headers={'Authorization': f'Bearer {token}'})
                        #print("TESTING:", requestTuesdayFormat)
                        rawResponseTuesday = requestTuesdayFormat.json()
                        cleanedTuesday = rawResponseTuesday['content']
                        usella =  cleanedTuesday.get('mealTaps', None)
                        for tueddd in usella:
                            tddd = tueddd.get('status', None)
                            if tddd == 'complete':
                                tb = tueddd['count']
                                #print("COMPLETED MONDAY", m)
                            if tddd == 'rejected':
                                tbt = tueddd['count']
                                #print("REJECTION TUESDAY:", tbt)
                            if tddd == 'duplicate':
                                tbtt = tueddd['count']   
                        #missed meals
                        missedMealsTue =  cleanedTuesday.get('endOfDay', None)
                        ##print()
                        datamissedmealsTue = {
                            "mealTapssdd": missedMealsTue,
                        }
                        missTue = datamissedmealsTue['mealTapssdd']
                        ##print(aaa)
                        missesd = missTue['mealsShortfall']
                        #next meal projections
                        nextmeal111 = cleanedTuesday.get('nextDayProjection', None)
                        nextmealProjection11 = int(nextmeal111 or 0)
                        #tags
                        tagNewIssuesTue =  cleanedTuesday.get('devices', None)
                        ##print(usera)
                        dataRawTuesday = {
                            "devicescd": tagNewIssuesTue,
                            }
                        nfccd = dataRawTuesday['devicescd']#['nfc_tag']
                        activeeTaggss = (nfccd.get('nfc_tag', None)) #
                        taggTue = (activeeTaggss)
                         ##Money Collected
                        getMoney1 = cleanedTuesday.get('transactions')
                        for getit1 in getMoney1:
                            if getit1['transactionType'] == 'acc_credit':
                                moneyT1 = int(getit1['totalAmount'])
                        data233 = {
                            "moneyCollected":moneyT1,
                            'current_user':current_user,
                            "theDate":theDateT,
                            "theMonth":theMonthT,
                            "theYear":theYearT,
                            "theDay":theDayT,
                            "cmmmm":cmmmm,
                            "cm":cm,
                            "cmmm":cmmm,
                            "coomptue":coomptue,
                            "cooomptues":cooomptues,
                            "cooomptuesd":cooomptuesd,
                            "currentDay":currentDay,
                            "completedMonmmm":completedMonmmm,
                            "completedMonmm":completedMonmm,
                            "completedMonm":completedMonm,
                            "furahiday":furahiday,
                            "tagg":taggTue,
                            "furahia":furahia,
                            "friesday":friesday,
                            "thurahia":thurahia,
                            "thurahiday":thurahiday,
                            "thriesday":thriesday,
                            "completedWEBO":completedWEBO,
                            "completedWEBBO":completedWEBBO,
                            "completedWEBBBO":completedWEBBBO,
                            "completedWEBDO":completedWEBDO,
                            "completedWEBBDO":completedWEBBDO,
                            "completedWEBBBDO":completedWEBBBDO,
                            "cWEBDO":cWEBDO,
                            "cWEBBDO":cWEBBDO,
                            "cWEBBBDO":cWEBBBDO,
                            "completedWebDo":completedWebDo,
                            "completedWebbDo":completedWebbDo,
                            "completedWebbbDo":completedWebbbDo,
                            "completedWebo":completedWebo,
                            "completedWebbo":completedWebbo,
                            "completedWebbbo":completedWebbbo,
                            "completedWedo":completedWedo,
                            "completedWeddo":completedWeddo,
                            "completedWedddo":completedWedddo,
                            "completedThors":completedThors,
                            "completedThorrs":completedThorrs,
                            "completedThorrrs":completedThorrrs,
                            "comptuee":comptuee,
                            "comptuess":comptuess,
                            "comptuesdd":comptuesdd,
                            "comptue":comptue,
                            "comptues":comptues,
                            "comptuesd":comptuesd,
                            "completedWed":completedWed,
                            "completedWedd":completedWedd,
                            "completedWeddd":completedWeddd,
                            "penetrationRate":penetrationRate,
                            "ndiini":ndiini,
                            "totalStudee":totalStudee,
                            "rejection":tbt,
                            "duplication":tbtt,
                            "completedCorrects":completedCorrects,
                            "completedCorrectss":completedCorrectss,
                            "completedCorrectsss":completedCorrectsss,
                            "completedCorrect":tb,
                            "page1":page1,
                            "activee":activee,
                            "projectss":missesd,
                            "nextmealProjection":nextmealProjection11,
                            "mealtaps":aa,
                            "money":mpesa,
                        }
                        return render(request, "home.html",  data233)
                    if dayEntered == 'Wednesday':
                        theDayW = "Wednesday" #thursday
                        theDateW = wednesdayday.strftime("%d") #25
                        theMonthW = wednesdayday.strftime("%B") #'JANUARY'
                        theYearW = wednesdayday.strftime("%Y") #2021
                        sttddate = str(wednesdayday.date())
                        timeFormatDayyy = '?startDate='+ sttddate + '_00:00&endDate=' + sttddate + '_23:59'
                        requestWednesdayFormat = requests.get(summary + timeFormatDayyy, headers={'Authorization': f'Bearer {token}'})
                        #print("TESTING:", requestTuesdayFormat)
                        rawResponseWednesday = requestWednesdayFormat.json()
                        cleanedWednesday = rawResponseWednesday['content']
                        usellla =  cleanedWednesday.get('mealTaps', None)
                        global tbtd, tbd, tbttd
                        for wedl in usellla:
                            wtddd = wedl.get('status', None)
                            if wtddd == 'complete':
                                tbd = wedl['count']
                                #print("COMPLETED MONDAY", m)
                            if wtddd == 'rejected':
                                tbtd = wedl['count']
                                print("REJECTION TUESDAY:", tbt)
                            if wtddd == 'duplicate':
                                tbttd = wedl['count']   
                        #missed meals
                        missedMealsWed = cleanedWednesday.get('endOfDay', None)
                        ##print()
                        datamissedmealsWed = {
                            "mealTapssdd": missedMealsWed,
                        }
                        missWed = datamissedmealsWed['mealTapssdd']
                        ##print(aaa)
                        missesdt = missWed['mealsShortfall']
                        #next meal projections
                        nextmeal222 = cleanedWednesday.get('nextDayProjection', None)
                        nextmealProjection111 = int(nextmeal222 or 0)
                        #tags
                        tagNewIssuesWed = cleanedWednesday.get('devices', None)
                        ##print(usera)
                        dataRawWednesday = {
                            "devicescdd": tagNewIssuesWed,
                            }
                        nfccdd = dataRawWednesday['devicescdd']#['nfc_tag']
                        activeeTaggssd = (nfccdd.get('nfc_tag', None)) #
                        taggWed = (activeeTaggssd)
                         ##Money Collected
                        getMoney2 = cleanedWednesday.get('transactions')
                        for getit2 in getMoney2:
                            if getit2['transactionType'] == 'acc_credit':
                                moneyT2 = int(getit2['totalAmount'])
                        data2334 = {
                            "moneyCollected":moneyT2,
                            'current_user':current_user,
                            "theDate":theDateW,
                            "theMonth":theMonthW,
                            "theYear":theYearW,
                            "theDay":theDayW,
                            "cmmmm":cmmmm,
                            "cm":cm,
                            "cmmm":cmmm,
                            "coomptue":coomptue,
                            "cooomptues":cooomptues,
                            "cooomptuesd":cooomptuesd,
                            "currentDay":currentDay,
                            "completedMonmmm":completedMonmmm,
                            "completedMonmm":completedMonmm,
                            "completedMonm":completedMonm,
                            "furahiday":furahiday,
                            "tagg":taggWed,
                            "furahia":furahia,
                            "friesday":friesday,
                            "thurahia":thurahia,
                            "thurahiday":thurahiday,
                            "thriesday":thriesday,
                            "completedWEBO":completedWEBO,
                            "completedWEBBO":completedWEBBO,
                            "completedWEBBBO":completedWEBBBO,
                            "completedWEBDO":completedWEBDO,
                            "completedWEBBDO":completedWEBBDO,
                            "completedWEBBBDO":completedWEBBBDO,
                            "cWEBDO":cWEBDO,
                            "cWEBBDO":cWEBBDO,
                            "cWEBBBDO":cWEBBBDO,
                            "completedWebDo":completedWebDo,
                            "completedWebbDo":completedWebbDo,
                            "completedWebbbDo":completedWebbbDo,
                            "completedWebo":completedWebo,
                            "completedWebbo":completedWebbo,
                            "completedWebbbo":completedWebbbo,
                            "completedWedo":completedWedo,
                            "completedWeddo":completedWeddo,
                            "completedWedddo":completedWedddo,
                            "completedThors":completedThors,
                            "completedThorrs":completedThorrs,
                            "completedThorrrs":completedThorrrs,
                            "comptuee":comptuee,
                            "comptuess":comptuess,
                            "comptuesdd":comptuesdd,
                            "comptue":comptue,
                            "comptues":comptues,
                            "comptuesd":comptuesd,
                            "completedWed":completedWed,
                            "completedWedd":completedWedd,
                            "completedWeddd":completedWeddd,
                            "penetrationRate":penetrationRate,
                            "ndiini":ndiini,
                            "totalStudee":totalStudee,
                            "rejection":tbtd,
                            "duplication":tbttd,
                            "completedCorrects":completedCorrects,
                            "completedCorrectss":completedCorrectss,
                            "completedCorrectsss":completedCorrectsss,
                            "completedCorrect":tbd,
                            "page1":page1,
                            "activee":activee,
                            "projectss":missesdt,
                            "nextmealProjection":nextmealProjection111,
                            "mealtaps":aa,
                            "money":mpesa,
                        }
                        return render(request, "home.html",  data2334)
                if todaytoday == 'Friday':
                    #getDayEnteredOnForm = dayEntered
                    mondaysiku = day - timedelta(4)
                    tuesdaysiku = day -timedelta(3)
                    wednesdaysiku = day - timedelta(2)
                    thursdaysiku = day - timedelta(1)
                    #requests for each day
                    if dayEntered == 'Monday':
                        theDayMT = "Monday" #thursday
                        theDateMT = mondaysiku.strftime("%d") #25
                        theMonthMT = mondaysiku.strftime("%B") #'JANUARY'
                        theYearMTT = mondaysiku.strftime("%Y") #2021
                        stidate = str(mondaysiku.date())
                        timeFormatDayFriday = '?startDate='+ stidate + '_00:00&endDate=' + stidate + '_23:59'
                        requestMondayFormatFri = requests.get(summary + timeFormatDayFriday, headers={'Authorization': f'Bearer {token}'})
                        #print("TESTING:", requestMondayFormat)
                        rawResponseMondayFri = requestMondayFormatFri.json()
                        cleanedMondayFri = rawResponseMondayFri['content']
                        uselda =  cleanedMondayFri.get('mealTaps', None)
                        for monfriddd in uselda:
                            mfddd = monfriddd.get('status', None)
                            if mfddd == 'complete':
                                mrf = monfriddd['count']
                                print("COMPLETED MONDAY", mrf)
                            if mfddd == 'rejected':
                                mcf = monfriddd['count']
                                print("Rejected MONDAY", mcf)
                            if mfddd == 'duplicate':
                                mdf = monfriddd['count']
                                print("Duplicated MONDAY", mdf)
                        #missed meals
                        missedMealsMonFri = cleanedMondayFri.get('endOfDay', None)
                        ##print()
                        datamissedmealsFri = {
                            "mealTapssfd": missedMealsMonFri,
                        }
                        missFri = datamissedmealsFri['mealTapssfd']
                        ##print(aaa)
                        missesFri = missFri['mealsShortfall']
                        #next meal projections
                        nextmeal123 = cleanedMondayFri.get('nextDayProjection', None)
                        nextmealProjection123 = int(nextmeal123 or 0)
                        #tag new issues
                        #todoss = data5['content']
                        tagNewIssuesMon = cleanedMondayFri.get('devices', None)
                        ##print(usera)
                        dataRawg = {
                            "devicescg": tagNewIssuesMon,
                            }
                        nfccq = dataRawg['devicescg']#['nfc_tag']
                        activeeTaggw = (nfccq.get('nfc_tag', None)) #
                        taggMonFri = (activeeTaggw)
                        #print(taggMonFri)
                         ##Money Collected
                        getMoney3 = cleanedMondayFri.get('transactions')
                        for getit3 in getMoney3:
                            if getit3['transactionType'] == 'acc_credit':
                                moneyT3 = int(getit3['totalAmount'])
                        data23345 = {
                            "moneyCollected":moneyT3,
                            'current_user':current_user,
                            "theDate":theDateMT,
                            "theMonth":theMonthMT,
                            "theYear":theYearMTT,
                            "theDay":theDayMT,
                            "cmmmm":cmmmm,
                            "cm":cm,
                            "cmmm":cmmm,
                            "coomptue":coomptue,
                            "cooomptues":cooomptues,
                            "cooomptuesd":cooomptuesd,
                            "currentDay":currentDay,
                            "completedMonmmm":completedMonmmm,
                            "completedMonmm":completedMonmm,
                            "completedMonm":completedMonm,
                            "furahiday":furahiday,
                            "tagg":taggMonFri,
                            "furahia":furahia,
                            "friesday":friesday,
                            "thurahia":thurahia,
                            "thurahiday":thurahiday,
                            "thriesday":thriesday,
                            "completedWEBO":completedWEBO,
                            "completedWEBBO":completedWEBBO,
                            "completedWEBBBO":completedWEBBBO,
                            "completedWEBDO":completedWEBDO,
                            "completedWEBBDO":completedWEBBDO,
                            "completedWEBBBDO":completedWEBBBDO,
                            "cWEBDO":cWEBDO,
                            "cWEBBDO":cWEBBDO,
                            "cWEBBBDO":cWEBBBDO,
                            "completedWebDo":completedWebDo,
                            "completedWebbDo":completedWebbDo,
                            "completedWebbbDo":completedWebbbDo,
                            "completedWebo":completedWebo,
                            "completedWebbo":completedWebbo,
                            "completedWebbbo":completedWebbbo,
                            "completedWedo":completedWedo,
                            "completedWeddo":completedWeddo,
                            "completedWedddo":completedWedddo,
                            "completedThors":completedThors,
                            "completedThorrs":completedThorrs,
                            "completedThorrrs":completedThorrrs,
                            "comptuee":comptuee,
                            "comptuess":comptuess,
                            "comptuesdd":comptuesdd,
                            "comptue":comptue,
                            "comptues":comptues,
                            "comptuesd":comptuesd,
                            "completedWed":completedWed,
                            "completedWedd":completedWedd,
                            "completedWeddd":completedWeddd,
                            "penetrationRate":penetrationRate,
                            "ndiini":ndiini,
                            "totalStudee":totalStudee,
                            "rejection":mcf,
                            "duplication":mdf,
                            "completedCorrects":completedCorrects,
                            "completedCorrectss":completedCorrectss,
                            "completedCorrectsss":completedCorrectsss,
                            "completedCorrect":mrf,
                            "page1":page1,
                            "activee":activee,
                            "projectss":missesFri,
                            "nextmealProjection":nextmealProjection123,
                            "mealtaps":aa,
                            "money":mpesa,
                        }
                        return render(request, "home.html",  data23345)
                    if dayEntered == 'Tuesday':
                        theDayTT = "Tuesday" #thursday
                        theDateTT = tuesdaysiku.strftime("%d") #25
                        theMonthTT = tuesdaysiku.strftime("%B") #'JANUARY'
                        theYearTT = tuesdaysiku.strftime("%Y") #2021
                        stiddate = str(tuesdaysiku.date())
                        timeFormatDD = '?startDate='+ stiddate + '_00:00&endDate=' + stiddate + '_23:59'
                        requestTuesdayFormatFri = requests.get(summary + timeFormatDD, headers={'Authorization': f'Bearer {token}'})
                        #print("TESTING:", requestMondayFormat)
                        rawResponseTuesdayFri = requestTuesdayFormatFri.json()
                        cleanedTuesdayFri = rawResponseTuesdayFri['content']
                        useldad =  cleanedTuesdayFri.get('mealTaps', None)
                        for friddd in useldad:
                            tfddd = friddd.get('status', None)
                            if tfddd == 'complete':
                                mrff = friddd['count']
                                #print("COMPLETED MONDAY", m)
                            if tfddd == 'rejected':
                                mcff = friddd['count']
                                #print("Rejected MONDAY", mm)
                            if tfddd == 'duplicate':
                                mdff = friddd['count']
                                #print("Duplicated MONDAY", mmm)
                        #missed meals
                        missedMealsTueFri = cleanedTuesdayFri.get('endOfDay', None)
                        ##print()
                        datamissedmealsFriTue = {
                            "mealTapssfds": missedMealsTueFri,
                        }
                        missFriqq = datamissedmealsFriTue['mealTapssfds']
                        ##print(aaa)
                        missesFriqq = missFriqq['mealsShortfall']
                        #next meal projections
                        nextmeal1234 = cleanedTuesdayFri.get('nextDayProjection', None)
                        nextmealProjection1234 = int(nextmeal1234 or 0)
                        #tag new issues
                        #todoss = data5['content']
                        tagNewIssuesTue = cleanedTuesdayFri.get('devices', None)
                        ##print(usera)
                        dataRawgf = {
                            "devicescgf": tagNewIssuesTue,
                            }
                        nfccqf = dataRawgf['devicescgf']#['nfc_tag']
                        activeeTaggwf = (nfccqf.get('nfc_tag', None)) #
                        taggTueFri = (activeeTaggwf)
                         ##Money Collected
                        getMoney4 = cleanedTuesdayFri.get('transactions')
                        for getit4 in getMoney4:
                            if getit4['transactionType'] == 'acc_credit':
                                moneyT4 = int(getit4['totalAmount'])
                        data235 = {
                            "moneyCollected":moneyT4,
                            'current_user':current_user,
                            "theDate":theDateTT,
                            "theMonth":theMonthTT,
                            "theYear":theYearTT,
                            "theDay":theDayTT,
                            "cmmmm":cmmmm,
                            "cm":cm,
                            "cmmm":cmmm,
                            "coomptue":coomptue,
                            "cooomptues":cooomptues,
                            "cooomptuesd":cooomptuesd,
                            "currentDay":currentDay,
                            "completedMonmmm":completedMonmmm,
                            "completedMonmm":completedMonmm,
                            "completedMonm":completedMonm,
                            "furahiday":furahiday,
                            "tagg":taggTueFri,
                            "furahia":furahia,
                            "friesday":friesday,
                            "thurahia":thurahia,
                            "thurahiday":thurahiday,
                            "thriesday":thriesday,
                            "completedWEBO":completedWEBO,
                            "completedWEBBO":completedWEBBO,
                            "completedWEBBBO":completedWEBBBO,
                            "completedWEBDO":completedWEBDO,
                            "completedWEBBDO":completedWEBBDO,
                            "completedWEBBBDO":completedWEBBBDO,
                            "cWEBDO":cWEBDO,
                            "cWEBBDO":cWEBBDO,
                            "cWEBBBDO":cWEBBBDO,
                            "completedWebDo":completedWebDo,
                            "completedWebbDo":completedWebbDo,
                            "completedWebbbDo":completedWebbbDo,
                            "completedWebo":completedWebo,
                            "completedWebbo":completedWebbo,
                            "completedWebbbo":completedWebbbo,
                            "completedWedo":completedWedo,
                            "completedWeddo":completedWeddo,
                            "completedWedddo":completedWedddo,
                            "completedThors":completedThors,
                            "completedThorrs":completedThorrs,
                            "completedThorrrs":completedThorrrs,
                            "comptuee":comptuee,
                            "comptuess":comptuess,
                            "comptuesdd":comptuesdd,
                            "comptue":comptue,
                            "comptues":comptues,
                            "comptuesd":comptuesd,
                            "completedWed":completedWed,
                            "completedWedd":completedWedd,
                            "completedWeddd":completedWeddd,
                            "penetrationRate":penetrationRate,
                            "ndiini":ndiini,
                            "totalStudee":totalStudee,
                            "rejection":mcff,
                            "duplication":mdff,
                            "completedCorrects":completedCorrects,
                            "completedCorrectss":completedCorrectss,
                            "completedCorrectsss":completedCorrectsss,
                            "completedCorrect":mrff,
                            "page1":page1,
                            "activee":activee,
                            "projectss":missesFriqq,
                            "nextmealProjection":nextmealProjection1234,
                            "mealtaps":aa,
                            "money":mpesa,
                        }
                        return render(request, "home.html",  data235)
                    if dayEntered == 'Wednesday':
                        DayTT = "Wednesday" #thursday
                        DateTT = wednesdaysiku.strftime("%d") #25
                        MonthTT = wednesdaysiku.strftime("%B") #'JANUARY'
                        YearTT = wednesdaysiku.strftime("%Y") #2021
                        iddate = str(wednesdaysiku.date())
                        timeFormatPP = '?startDate='+ iddate + '_00:00&endDate=' + iddate + '_23:59'
                        requestWednesdayFormatFri = requests.get(summary + timeFormatPP, headers={'Authorization': f'Bearer {token}'})
                        #print("TESTING:", requestMondayFormat)
                        rawResponseWednesdayFri = requestWednesdayFormatFri.json()
                        cleanedWednesdayFri = rawResponseWednesdayFri['content']
                        useldadf =  cleanedWednesdayFri.get('mealTaps', None)
                        global mrfff, mcffd, mdffd
                        for riddd in useldadf:
                            tdfddd = riddd.get('status', None)
                            if tdfddd == 'complete':
                                mrfff = riddd['count']
                                #print("COMPLETED MONDAY", m)
                            if tdfddd == 'rejected':
                                mcffd = riddd['count']
                                #print("Rejected MONDAY", mm)
                            if tdfddd == 'duplicate':
                                mdffd = riddd['count']
                                #print("Duplicated MONDAY", mmm)
                        #missed meals
                        missedMealsWedFri = cleanedWednesdayFri.get('endOfDay', None)
                        ##print()
                        datamissedmealsFriWed = {
                            "mealTapssfdsd": missedMealsWedFri,
                        }
                        missWedqq = datamissedmealsFriWed['mealTapssfdsd']
                        ##print(aaa)
                        missesWedqq = missWedqq['mealsShortfall']
                        #next meal projections
                        nextmeal12345 = cleanedWednesdayFri.get('nextDayProjection', None)
                        nextmealProjection12345 = int(nextmeal12345 or 0)
                        #tag new issues
                        #todoss = data5['content']
                        tagNewIssuesWed = cleanedWednesdayFri.get('devices', None)
                        ##print(usera)
                        dataRawgfd = {
                            "devicescgfd": tagNewIssuesWed,
                            }
                        nfccqfd = dataRawgfd['devicescgfd']#['nfc_tag']
                        activeeTaggwfd = (nfccqfd.get('nfc_tag', None)) #
                        taggWedFri = (activeeTaggwfd)
                         ##Money Collected
                        getMoney5 = cleanedWednesdayFri.get('transactions')
                        for getit5 in getMoney5:
                            if getit5['transactionType'] == 'acc_credit':
                                moneyT5 = int(getit5['totalAmount'])
                        data2356 = {
                            "moneyCollected":moneyT5,
                            'current_user':current_user,
                            "theDate":DateTT,
                            "theMonth":MonthTT,
                            "theYear":YearTT,
                            "theDay":DayTT,
                            "cmmmm":cmmmm,
                            "cm":cm,
                            "cmmm":cmmm,
                            "coomptue":coomptue,
                            "cooomptues":cooomptues,
                            "cooomptuesd":cooomptuesd,
                            "currentDay":currentDay,
                            "completedMonmmm":completedMonmmm,
                            "completedMonmm":completedMonmm,
                            "completedMonm":completedMonm,
                            "furahiday":furahiday,
                            "tagg":taggWedFri,
                            "furahia":furahia,
                            "friesday":friesday,
                            "thurahia":thurahia,
                            "thurahiday":thurahiday,
                            "thriesday":thriesday,
                            "completedWEBO":completedWEBO,
                            "completedWEBBO":completedWEBBO,
                            "completedWEBBBO":completedWEBBBO,
                            "completedWEBDO":completedWEBDO,
                            "completedWEBBDO":completedWEBBDO,
                            "completedWEBBBDO":completedWEBBBDO,
                            "cWEBDO":cWEBDO,
                            "cWEBBDO":cWEBBDO,
                            "cWEBBBDO":cWEBBBDO,
                            "completedWebDo":completedWebDo,
                            "completedWebbDo":completedWebbDo,
                            "completedWebbbDo":completedWebbbDo,
                            "completedWebo":completedWebo,
                            "completedWebbo":completedWebbo,
                            "completedWebbbo":completedWebbbo,
                            "completedWedo":completedWedo,
                            "completedWeddo":completedWeddo,
                            "completedWedddo":completedWedddo,
                            "completedThors":completedThors,
                            "completedThorrs":completedThorrs,
                            "completedThorrrs":completedThorrrs,
                            "comptuee":comptuee,
                            "comptuess":comptuess,
                            "comptuesdd":comptuesdd,
                            "comptue":comptue,
                            "comptues":comptues,
                            "comptuesd":comptuesd,
                            "completedWed":completedWed,
                            "completedWedd":completedWedd,
                            "completedWeddd":completedWeddd,
                            "penetrationRate":penetrationRate,
                            "ndiini":ndiini,
                            "totalStudee":totalStudee,
                            "rejection":mcffd,
                            "duplication":mdffd,
                            "completedCorrects":completedCorrects,
                            "completedCorrectss":completedCorrectss,
                            "completedCorrectsss":completedCorrectsss,
                            "completedCorrect":mrfff,
                            "page1":page1,
                            "activee":activee,
                            "projectss":missesWedqq,
                            "nextmealProjection":nextmealProjection12345,
                            "mealtaps":aa,
                            "money":mpesa,
                        }
                        return render(request, "home.html",  data2356)
                    if dayEntered == 'Thursday':
                        ayTT = "Thursday" #thursday
                        ateTT = thursdaysiku.strftime("%d") #25
                        onthTT = thursdaysiku.strftime("%B") #'JANUARY'
                        earTT = thursdaysiku.strftime("%Y") #2021
                        ddate = str(thursdaysiku.date())
                        ormatPP = '?startDate='+ ddate + '_00:00&endDate=' + ddate + '_23:59'
                        requestThursdayFormatFri = requests.get(summary + ormatPP, headers={'Authorization': f'Bearer {token}'})
                        #print("TESTING:", requestMondayFormat)
                        rawResponseThursdayFri = requestThursdayFormatFri.json()
                        cleanedThursdayFri = rawResponseThursdayFri['content']
                        useldadfft =  cleanedThursdayFri.get('mealTaps', None)
                        for idd in useldadfft:
                            dfdddg = idd.get('status', 0)
                            if dfdddg == 'complete':
                                mrffdfp = idd['count']
                                #print("COMPLETED MONDAY", m)
                            if dfdddg == 'rejected':
                                mcffdfp = idd['count']
                                #print("Rejected MONDAY", mm)
                            if dfdddg == 'duplicate':
                                mdffdfp = idd['count']
                                #print("Duplicated MONDAY", mmm)
                        #missed meals
                        missedMealsThurFi = cleanedThursdayFri.get('endOfDay', None)
                        ##print()
                        datamissedmealsThurWe = {
                            "mealTapssfdsdf9": missedMealsThurFi,
                        }
                        missThrqq = datamissedmealsThurWe['mealTapssfdsdf9']
                        ##print(aaa)
                        missesThrqq = missThrqq['mealsShortfall']
                        #next meal projections
                        nextmeal123456 = cleanedThursdayFri.get('nextDayProjection', None)
                        nextmealProjection123456 = int(nextmeal123456 or 0)
                        #tag new issues
                        #todoss = data5['content']
                        tagNewIssuesThur = cleanedThursdayFri.get('devices', None)
                        ##print(usera)
                        dataRawgfd4 = {
                            "devicescgfd4": tagNewIssuesThur,
                            }
                        nfccqfd4 = dataRawgfd4['devicescgfd4']#['nfc_tag']
                        activeeTaggwfd4 = (nfccqfd4.get('nfc_tag', None)) #
                        taggThurFri = (activeeTaggwfd4)
                         ##Money Collected
                        getMoney6 = cleanedThursdayFri.get('transactions')
                        for getit6 in getMoney6:
                            if getit6['transactionType'] == 'acc_credit':
                                moneyT6 = int(getit6['totalAmount'])
                        data23567 = {
                            "moneyCollected":moneyT6,
                            'current_user':current_user,
                            "theDate":ateTT,
                            "theMonth":onthTT,
                            "theYear":earTT,
                            "theDay":ayTT,
                            "cmmmm":cmmmm,
                            "cm":cm,
                            "cmmm":cmmm,
                            "coomptue":coomptue,
                            "cooomptues":cooomptues,
                            "cooomptuesd":cooomptuesd,
                            "currentDay":currentDay,
                            "completedMonmmm":completedMonmmm,
                            "completedMonmm":completedMonmm,
                            "completedMonm":completedMonm,
                            "furahiday":furahiday,
                            "tagg":taggThurFri,
                            "furahia":furahia,
                            "friesday":friesday,
                            "thurahia":thurahia,
                            "thurahiday":thurahiday,
                            "thriesday":thriesday,
                            "completedWEBO":completedWEBO,
                            "completedWEBBO":completedWEBBO,
                            "completedWEBBBO":completedWEBBBO,
                            "completedWEBDO":completedWEBDO,
                            "completedWEBBDO":completedWEBBDO,
                            "completedWEBBBDO":completedWEBBBDO,
                            "cWEBDO":cWEBDO,
                            "cWEBBDO":cWEBBDO,
                            "cWEBBBDO":cWEBBBDO,
                            "completedWebDo":completedWebDo,
                            "completedWebbDo":completedWebbDo,
                            "completedWebbbDo":completedWebbbDo,
                            "completedWebo":completedWebo,
                            "completedWebbo":completedWebbo,
                            "completedWebbbo":completedWebbbo,
                            "completedWedo":completedWedo,
                            "completedWeddo":completedWeddo,
                            "completedWedddo":completedWedddo,
                            "completedThors":completedThors,
                            "completedThorrs":completedThorrs,
                            "completedThorrrs":completedThorrrs,
                            "comptuee":comptuee,
                            "comptuess":comptuess,
                            "comptuesdd":comptuesdd,
                            "comptue":comptue,
                            "comptues":comptues,
                            "comptuesd":comptuesd,
                            "completedWed":completedWed,
                            "completedWedd":completedWedd,
                            "completedWeddd":completedWeddd,
                            "penetrationRate":penetrationRate,
                            "ndiini":ndiini,
                            "totalStudee":totalStudee,
                            "rejection":mcffdfp,
                            "duplication":mdffdfp,
                            "completedCorrects":completedCorrects,
                            "completedCorrectss":completedCorrectss,
                            "completedCorrectsss":completedCorrectsss,
                            "completedCorrect":mrffdfp,
                            "page1":page1,
                            "activee":activee,
                            "projectss":missesThrqq,
                            "nextmealProjection":nextmealProjection123456,
                            "mealtaps":aa,
                            "money":mpesa,
                        }
                        return render(request, "home.html",  data23567)
                if todaytoday == 'Wednesday':
                    #getDayEnteredOnForm = dayEntered
                    mondaysi = day - timedelta(2)
                    tuesdaysi = day -timedelta(1)
                    if dayEntered == 'Monday':
                        tDayMT = "Monday" #thursday
                        tDateMT = mondaysi.strftime("%d") #25
                        tMonthMT = mondaysi.strftime("%B") #'JANUARY'
                        tYearMTT = mondaysi.strftime("%Y") #2021
                        tidate = str(mondaysi.date())
                        timeFormatDayWedd = '?startDate='+ tidate + '_00:00&endDate=' + tidate + '_23:59'
                        requestMondayFormatM = requests.get(summary + timeFormatDayWedd, headers={'Authorization': f'Bearer {token}'})
                        #print("TESTING:", requestMondayFormat)
                        rawResponseMondayWED = requestMondayFormatM.json()
                        cleanedMondayWED = rawResponseMondayWED['content']
                        selda =  cleanedMondayWED.get('mealTaps', None)
                        for monwed in selda:
                            mfdddu = monwed.get('status', None)
                            if mfdddu == 'complete':
                                trf = monwed['count']
                                #print("COMPLETED MONDAY", m)
                            if mfdddu == 'rejected':
                                tcf = monwed['count']
                                #print("Rejected MONDAY", mm)
                            if mfdddu == 'duplicate':
                                tdf = monwed['count']
                                #print("Duplicated MONDAY", mmm)
                        #missed meals
                        missedMealsMonWED = cleanedMondayWED.get('endOfDay', None)
                        ##print()
                        datamissedmealsWEDO = {
                            "mealTapssfd1": missedMealsMonWED,
                        }
                        missWED1 = datamissedmealsWEDO['mealTapssfd1']
                        ##print(aaa)
                        missesWED1 = missWED1['mealsShortfall']
                        #next meal projections
                        nextmeal1230 = cleanedMondayWED.get('nextDayProjection', None)
                        nextmealProjection1230 = int(nextmeal1230 or 0)
                        #tag new issues
                        #todoss = data5['content']
                        tagNewIssuesWEDO = cleanedMondayWED.get('devices', None)
                        ##print(usera)
                        dataRawg19 = {
                            "devicescg9": tagNewIssuesWEDO,
                            }
                        nfccq21 = dataRawg19['devicescg9']#['nfc_tag']
                        activeeTaggw19 = (nfccq21.get('nfc_tag', None)) #
                        taggMonWEDO = (activeeTaggw19)
                         ##Money Collected
                        getMoney7 = cleanedMondayWED.get('transactions')
                        for getit7 in getMoney7:
                            if getit7['transactionType'] == 'acc_credit':
                                moneyT7 = int(getit7['totalAmount'])
                        data235678 = {
                            "moneyCollected":moneyT7,
                            'current_user':current_user,
                            "theDate":tDateMT,
                            "theMonth":tMonthMT,
                            "theYear":tYearMTT,
                            "theDay":tDayMT,
                            "cmmmm":cmmmm,
                            "cm":cm,
                            "cmmm":cmmm,
                            "coomptue":coomptue,
                            "cooomptues":cooomptues,
                            "cooomptuesd":cooomptuesd,
                            "currentDay":currentDay,
                            "completedMonmmm":completedMonmmm,
                            "completedMonmm":completedMonmm,
                            "completedMonm":completedMonm,
                            "furahiday":furahiday,
                            "tagg":taggMonWEDO,
                            "furahia":furahia,
                            "friesday":friesday,
                            "thurahia":thurahia,
                            "thurahiday":thurahiday,
                            "thriesday":thriesday,
                            "completedWEBO":completedWEBO,
                            "completedWEBBO":completedWEBBO,
                            "completedWEBBBO":completedWEBBBO,
                            "completedWEBDO":completedWEBDO,
                            "completedWEBBDO":completedWEBBDO,
                            "completedWEBBBDO":completedWEBBBDO,
                            "cWEBDO":cWEBDO,
                            "cWEBBDO":cWEBBDO,
                            "cWEBBBDO":cWEBBBDO,
                            "completedWebDo":completedWebDo,
                            "completedWebbDo":completedWebbDo,
                            "completedWebbbDo":completedWebbbDo,
                            "completedWebo":completedWebo,
                            "completedWebbo":completedWebbo,
                            "completedWebbbo":completedWebbbo,
                            "completedWedo":completedWedo,
                            "completedWeddo":completedWeddo,
                            "completedWedddo":completedWedddo,
                            "completedThors":completedThors,
                            "completedThorrs":completedThorrs,
                            "completedThorrrs":completedThorrrs,
                            "comptuee":comptuee,
                            "comptuess":comptuess,
                            "comptuesdd":comptuesdd,
                            "comptue":comptue,
                            "comptues":comptues,
                            "comptuesd":comptuesd,
                            "completedWed":completedWed,
                            "completedWedd":completedWedd,
                            "completedWeddd":completedWeddd,
                            "penetrationRate":penetrationRate,
                            "ndiini":ndiini,
                            "totalStudee":totalStudee,
                            "rejection":tcf,
                            "duplication":tdf,
                            "completedCorrects":completedCorrects,
                            "completedCorrectss":completedCorrectss,
                            "completedCorrectsss":completedCorrectsss,
                            "completedCorrect":trf,
                            "page1":page1,
                            "activee":activee,
                            "projectss":missesWED1,
                            "nextmealProjection":nextmealProjection1230,
                            "mealtaps":aa,
                            "money":mpesa,
                        }
                        return render(request, "home.html",  data235678)
                    if dayEntered == 'Tuesday':
                        DayMT = "Tuesday" #thursday
                        DateMT = tuesdaysi.strftime("%d") #25
                        MonthMT = tuesdaysi.strftime("%B") #'JANUARY'
                        YearMTT = tuesdaysi.strftime("%Y") #2021
                        idate = str(tuesdaysi.date())
                        timeFormatDayTUE = '?startDate='+ idate + '_00:00&endDate=' + idate + '_23:59'
                        requestMondayFormatT = requests.get(summary + timeFormatDayTUE, headers={'Authorization': f'Bearer {token}'})
                        #print("TESTING:", requestMondayFormat)
                        rawResponseMondayTU = requestMondayFormatT.json()
                        cleanedMondayTUE = rawResponseMondayTU['content']
                        seldad =  cleanedMondayTUE.get('mealTaps', None)
                        for monTUE in seldad:
                            mfddduf = monTUE.get('status', None)
                            if mfddduf == 'complete':
                                trfd = monTUE['count']
                                #print("COMPLETED MONDAY", m)
                            if mfddduf == 'rejected':
                                tcfd = monTUE['count']
                                #print("Rejected MONDAY", mm)
                            if mfddduf == 'duplicate':
                                tdfd = monTUE['count']
                                #print("Duplicated MONDAY", mmm)
                        #missed meals
                        missedMealsMonTUE = cleanedMondayTUE.get('endOfDay', None)
                        ##print()
                        datamissedmealsTUE = {
                            "mealTapssfd1d": missedMealsMonTUE,
                        }
                        missTUE1 = datamissedmealsTUE['mealTapssfd1d']
                        ##print(aaa)
                        missesTUE1 = missTUE1['mealsShortfall']
                        #next meal projections
                        nextmeal12307 = cleanedMondayTUE.get('nextDayProjection', None)
                        nextmealProjection12307 = int(nextmeal12307 or 0)
                        #tag new issues
                        #todoss = data5['content']
                        tagNewIssuesTUE = cleanedMondayTUE.get('devices', None)
                        ##print(usera)
                        dataRawg199 = {
                            "devicescg99": tagNewIssuesTUE,
                            }
                        nfccq219 = dataRawg199['devicescg99']#['nfc_tag']
                        activeeTaggw199 = (nfccq219.get('nfc_tag', None)) #
                        taggMonTUE = (activeeTaggw199)
                         ##Money Collected
                        getMoney8 = cleanedMondayTUE.get('transactions')
                        for getit8 in getMoney8:
                            if getit8['transactionType'] == 'acc_credit':
                                moneyT8 = int(getit8['totalAmount'])
                        data2356789 = {
                            "moneyCollected":moneyT8,
                            'current_user':current_user,
                            "theDate":DateMT,
                            "theMonth":MonthMT,
                            "theYear":YearMTT,
                            "theDay":DayMT,
                            "cmmmm":cmmmm,
                            "cm":cm,
                            "cmmm":cmmm,
                            "coomptue":coomptue,
                            "cooomptues":cooomptues,
                            "cooomptuesd":cooomptuesd,
                            "currentDay":currentDay,
                            "completedMonmmm":completedMonmmm,
                            "completedMonmm":completedMonmm,
                            "completedMonm":completedMonm,
                            "furahiday":furahiday,
                            "tagg":taggMonTUE,
                            "furahia":furahia,
                            "friesday":friesday,
                            "thurahia":thurahia,
                            "thurahiday":thurahiday,
                            "thriesday":thriesday,
                            "completedWEBO":completedWEBO,
                            "completedWEBBO":completedWEBBO,
                            "completedWEBBBO":completedWEBBBO,
                            "completedWEBDO":completedWEBDO,
                            "completedWEBBDO":completedWEBBDO,
                            "completedWEBBBDO":completedWEBBBDO,
                            "cWEBDO":cWEBDO,
                            "cWEBBDO":cWEBBDO,
                            "cWEBBBDO":cWEBBBDO,
                            "completedWebDo":completedWebDo,
                            "completedWebbDo":completedWebbDo,
                            "completedWebbbDo":completedWebbbDo,
                            "completedWebo":completedWebo,
                            "completedWebbo":completedWebbo,
                            "completedWebbbo":completedWebbbo,
                            "completedWedo":completedWedo,
                            "completedWeddo":completedWeddo,
                            "completedWedddo":completedWedddo,
                            "completedThors":completedThors,
                            "completedThorrs":completedThorrs,
                            "completedThorrrs":completedThorrrs,
                            "comptuee":comptuee,
                            "comptuess":comptuess,
                            "comptuesdd":comptuesdd,
                            "comptue":comptue,
                            "comptues":comptues,
                            "comptuesd":comptuesd,
                            "completedWed":completedWed,
                            "completedWedd":completedWedd,
                            "completedWeddd":completedWeddd,
                            "penetrationRate":penetrationRate,
                            "ndiini":ndiini,
                            "totalStudee":totalStudee,
                            "rejection":tcfd,
                            "duplication":tdfd,
                            "completedCorrects":completedCorrects,
                            "completedCorrectss":completedCorrectss,
                            "completedCorrectsss":completedCorrectsss,
                            "completedCorrect":trfd,
                            "page1":page1,
                            "activee":activee,
                            "projectss":missesTUE1,
                            "nextmealProjection":nextmealProjection12307,
                            "mealtaps":aa,
                            "money":mpesa,
                        }
                        return render(request, "home.html",  data2356789)
                if todaytoday == 'Tuesday':
                    #getDayEnteredOnForm = dayEntered
                    mondaysis = day - timedelta(1)
                    if dayEntered == 'Monday':
                        tDayMTF = "Monday" #thursday
                        tDateMTF = mondaysis.strftime("%d") #25
                        tMonthMTF = mondaysis.strftime("%B") #'JANUARY'
                        tYearMTTF = mondaysis.strftime("%Y") #2021
                        tidateFFF = str(mondaysis.date())
                        timeFormatDayMM = '?startDate='+ tidateFFF + '_00:00&endDate=' + tidateFFF + '_23:59'
                        requestMondayFormatTT = requests.get(summary + timeFormatDayMM, headers={'Authorization': f'Bearer {token}'})
                        #print("TESTING:", requestMondayFormat)
                        rawResponseMondayMM = requestMondayFormatTT.json()
                        cleanedMondayMON = rawResponseMondayMM['content']
                        seldom =  cleanedMondayMON.get('mealTaps', None)
                        for monwe in seldom:
                            mfdddus = monwe.get('status', None)
                            if mfdddus == 'complete':
                                trf2 = monwe['count']
                                #print("COMPLETED MONDAY", m)
                            if mfdddus == 'rejected':
                                tcf2 = monwe['count']
                                #print("Rejected MONDAY", mm)
                            if mfdddus == 'duplicate':
                                tdf2 = monwe['count']
                                #print("Duplicated MONDAY", mmm)
                        #missed meals
                        missedMealsMonWE = cleanedMondayMON.get('endOfDay', None)
                        ##print()
                        datamissedmealsWEDOP = {
                            "mealTapssfd1P": missedMealsMonWE,
                        }
                        missMON1 = datamissedmealsWEDOP['mealTapssfd1P']
                        ##print(aaa)
                        missesWED1P = missMON1['mealsShortfall']
                        #next meal projections
                        nextmeal1230P = cleanedMondayMON.get('nextDayProjection', None)
                        nextmealProjection1230P = int(nextmeal1230P or 0)
                        tagNewIssuesWEDOP = cleanedMondayMON.get('devices', None)
                        ##print(usera)
                        dataRawg19P = {
                            "devicescg9P": tagNewIssuesWEDOP,
                            }
                        nfccq21P = dataRawg19P['devicescg9P']#['nfc_tag']
                        activeeTaggw19P = (nfccq21P.get('nfc_tag', None)) #
                        taggMonWEDOP = (activeeTaggw19P)
                         ##Money Collected
                        getMoney9 = cleanedMondayMON.get('transactions')
                        for getit9 in getMoney9:
                            if getit9['transactionType'] == 'acc_credit':
                                moneyT9 = int(getit9['totalAmount'])
                        data2356789P = {
                            "moneyCollected":moneyT9,
                            'current_user':current_user,
                            "theDate":tDateMTF,
                            "theMonth":tMonthMTF,
                            "theYear":tYearMTTF,
                            "theDay":tDayMTF,
                            "cmmmm":cmmmm,
                            "cm":cm,
                            "cmmm":cmmm,
                            "coomptue":coomptue,
                            "cooomptues":cooomptues,
                            "cooomptuesd":cooomptuesd,
                            "currentDay":currentDay,
                            "completedMonmmm":completedMonmmm,
                            "completedMonmm":completedMonmm,
                            "completedMonm":completedMonm,
                            "furahiday":furahiday,
                            "tagg":taggMonWEDOP,
                            "furahia":furahia,
                            "friesday":friesday,
                            "thurahia":thurahia,
                            "thurahiday":thurahiday,
                            "thriesday":thriesday,
                            "completedWEBO":completedWEBO,
                            "completedWEBBO":completedWEBBO,
                            "completedWEBBBO":completedWEBBBO,
                            "completedWEBDO":completedWEBDO,
                            "completedWEBBDO":completedWEBBDO,
                            "completedWEBBBDO":completedWEBBBDO,
                            "cWEBDO":cWEBDO,
                            "cWEBBDO":cWEBBDO,
                            "cWEBBBDO":cWEBBBDO,
                            "completedWebDo":completedWebDo,
                            "completedWebbDo":completedWebbDo,
                            "completedWebbbDo":completedWebbbDo,
                            "completedWebo":completedWebo,
                            "completedWebbo":completedWebbo,
                            "completedWebbbo":completedWebbbo,
                            "completedWedo":completedWedo,
                            "completedWeddo":completedWeddo,
                            "completedWedddo":completedWedddo,
                            "completedThors":completedThors,
                            "completedThorrs":completedThorrs,
                            "completedThorrrs":completedThorrrs,
                            "comptuee":comptuee,
                            "comptuess":comptuess,
                            "comptuesdd":comptuesdd,
                            "comptue":comptue,
                            "comptues":comptues,
                            "comptuesd":comptuesd,
                            "completedWed":completedWed,
                            "completedWedd":completedWedd,
                            "completedWeddd":completedWeddd,
                            "penetrationRate":penetrationRate,
                            "ndiini":ndiini,
                            "totalStudee":totalStudee,
                            "rejection":tcf2,
                            "duplication":tdf2,
                            "completedCorrects":completedCorrects,
                            "completedCorrectss":completedCorrectss,
                            "completedCorrectsss":completedCorrectsss,
                            "completedCorrect":trf2,
                            "page1":page1,
                            "activee":activee,
                            "projectss":missesWED1P,
                            "nextmealProjection":nextmealProjection1230P,
                            "mealtaps":aa,
                            "money":mpesa,
                        }
                        return render(request, "home.html",  data2356789P)
            if request.method == 'POST' and 'btnform2' in request.POST:
                startdateentered = (request.POST['start'])
                enddateentered = (request.POST['end'])
                dateeee = startdateentered[-2:]
                monthth = startdateentered[-5]
                monththh = startdateentered[-4]
                monthfordate = monthth+monththh
                yearfordate = startdateentered[:4]
                #############################################
                datetimesetting = '?startDate='+ startdateentered + '_00:00&endDate=' + enddateentered + '_23:59'
                datetimesett = requests.get(summary + datetimesetting, headers={'Authorization': f'Bearer {token}'})
                rawdatetime = datetimesett.json()
                cleaneddatetime = rawdatetime['content']
                datetimemealtaps =  cleaneddatetime.get('mealTaps', None)
                for monwe11 in datetimemealtaps:
                    mfdddus11 = monwe11.get('status', None)
                    if mfdddus11 == 'complete':
                        successdate = monwe11['count']
                        #print("COMPLETED MONDAY", m)
                    if mfdddus11 == 'rejected':
                        rejectdate = monwe11['count']
                        #print("Rejected MONDAY", mm)
                    if mfdddus11 == 'duplicate':
                        rejectdup = monwe11['count']
                        #print("Duplicated MONDAY", mmm)
                missedMealsdatetime = cleaneddatetime.get('endOfDay', None)
                ##print()
                datamissedmealsWEDOP1 = {
                    "mealTapssfd1P1": missedMealsdatetime,
                }
                missMON1date = datamissedmealsWEDOP1['mealTapssfd1P1']
                ##print(aaa)
                missesWED1Pdate = missMON1date['mealsShortfall']
                #next meal projections
                nextmeal1230P1 = cleaneddatetime.get('nextDayProjection', None)
                nextmealProjectiondatetime = int(nextmeal1230P1 or 0)
                #tag new issues
                #todoss = data5['content']
                tagNewIssuesWEDOP11 = cleaneddatetime.get('devices', None)
                ##print(usera)
                dataRawg19P111 = {
                    "devicescg9P111": tagNewIssuesWEDOP11,
                }
                nfccq21P12 = dataRawg19P111['devicescg9P111']#['nfc_tag']
                activeeTaggw19P21 = (nfccq21P12.get('nfc_tag', None)) #
                taggMonDate = (activeeTaggw19P21)
                finalMoney = cleaneddatetime.get('transactions')
                for getget in finalMoney:
                    if getget['transactionType'] == 'acc_credit':
                        moneyfinal = int(getget['totalAmount'])
                data2av = {
                    "moneyCollected":moneyfinal,
                    'current_user':current_user,
                    "theDay":theDay,
                    "theDate":dateeee,
                    "theMonth":monthfordate,
                    "theYear":yearfordate,
                    "cmmmm":cmmmm,
                    "cm":cm,
                    "cmmm":cmmm,
                    "coomptue":coomptue,
                    "cooomptues":cooomptues,
                    "cooomptuesd":cooomptuesd,
                    "currentDay":currentDay,
                    "completedMonmmm":completedMonmmm,
                    "completedMonmm":completedMonmm,
                    "completedMonm":completedMonm,
                    "furahiday":furahiday,
                    "tagg":taggMonDate,
                    "furahia":furahia,
                    "friesday":friesday,
                    "thurahia":thurahia,
                    "thurahiday":thurahiday,
                    "thriesday":thriesday,
                    "completedWEBO":completedWEBO,
                    "completedWEBBO":completedWEBBO,
                    "completedWEBBBO":completedWEBBBO,
                    "completedWEBDO":completedWEBDO,
                    "completedWEBBDO":completedWEBBDO,
                    "completedWEBBBDO":completedWEBBBDO,
                    "cWEBDO":cWEBDO,
                    "cWEBBDO":cWEBBDO,
                    "cWEBBBDO":cWEBBBDO,
                    "completedWebDo":completedWebDo,
                    "completedWebbDo":completedWebbDo,
                    "completedWebbbDo":completedWebbbDo,
                    "completedWebo":completedWebo,
                    "completedWebbo":completedWebbo,
                    "completedWebbbo":completedWebbbo,
                    "completedWedo":completedWedo,
                    "completedWeddo":completedWeddo,
                    "completedWedddo":completedWedddo,
                    "completedThors":completedThors,
                    "completedThorrs":completedThorrs,
                    "completedThorrrs":completedThorrrs,
                    "comptuee":comptuee,
                    "comptuess":comptuess,
                    "comptuesdd":comptuesdd,
                    "comptue":comptue,
                    "comptues":comptues,
                    "comptuesd":comptuesd,
                    "completedWed":completedWed,
                    "completedWedd":completedWedd,
                    "completedWeddd":completedWeddd,
                    "penetrationRate":penetrationRate,
                    "ndiini":ndiini,
                    "totalStudee":totalStudee,
                    "rejection":rejectdate,
                    "duplication":rejectdup,
                    "completedCorrects":completedCorrects,
                    "completedCorrectss":completedCorrectss,
                    "completedCorrectsss":completedCorrectsss,
                    "completedCorrect":successdate,
                    "page1":page1,
                    "activee":activee,
                    "projectss":missesWED1Pdate,
                    "nextmealProjection":nextmealProjectiondatetime,
                    "mealtaps":aa,
                    "money":mpesa,
                }
                return render(request, "home.html",  data2av)    
        #####################################################################################
            data2 = {
                "moneyCollected":money,
                'current_user':current_user,
                "theDay":theDay,
                "theDate":theDate,
                "theMonth":theMonth,
                "theYear":theYear,
                "cmmmm":cmmmm,
                "cm":cm,
                "cmmm":cmmm,
                "coomptue":coomptue,
                "cooomptues":cooomptues,
                "cooomptuesd":cooomptuesd,
                "currentDay":currentDay,
                "completedMonmmm":completedMonmmm,
                "completedMonmm":completedMonmm,
                "completedMonm":completedMonm,
                "furahiday":furahiday,
                "tagg":tagg,
                "furahia":furahia,
                "friesday":friesday,
                "thurahia":thurahia,
                "thurahiday":thurahiday,
                "thriesday":thriesday,
                "completedWEBO":completedWEBO,
                "completedWEBBO":completedWEBBO,
                "completedWEBBBO":completedWEBBBO,
                "completedWEBDO":completedWEBDO,
                "completedWEBBDO":completedWEBBDO,
                "completedWEBBBDO":completedWEBBBDO,
                "cWEBDO":cWEBDO,
                "cWEBBDO":cWEBBDO,
                "cWEBBBDO":cWEBBBDO,
                "completedWebDo":completedWebDo,
                "completedWebbDo":completedWebbDo,
                "completedWebbbDo":completedWebbbDo,
                "completedWebo":completedWebo,
                "completedWebbo":completedWebbo,
                "completedWebbbo":completedWebbbo,
                "completedWedo":completedWedo,
                "completedWeddo":completedWeddo,
                "completedWedddo":completedWedddo,
                "completedThors":completedThors,
                "completedThorrs":completedThorrs,
                "completedThorrrs":completedThorrrs,
                "comptuee":comptuee,
                "comptuess":comptuess,
                "comptuesdd":comptuesdd,
                "comptue":comptue,
                "comptues":comptues,
                "comptuesd":comptuesd,
                "completedWed":completedWed,
                "completedWedd":completedWedd,
                "completedWeddd":completedWeddd,
                "penetrationRate":penetrationRate,
                "ndiini":ndiini,
                "totalStudee":totalStudee,
                "rejection":rejection,
                "duplication":duplication,
                "completedCorrects":completedCorrects,
                "completedCorrectss":completedCorrectss,
                "completedCorrectsss":completedCorrectsss,
                "completedCorrect":completedCorrect,
                "page1":page1,
                "activee":activee,
                "projectss":activeer,
                "nextmealProjection":nextmealProjection,
                "mealtaps":aa,
                "money":mpesa,
            }
            return render(request, "home.html",  data2) 
    else:
        return render(request, "home2.html")

def logout(request):
    try:
        token = request.session['access_token']
    except:
        return render(request, "home2.html")
    json={"token": f'{token}', "userId": "1"}
    headers = {'Authorization': f'Bearer {token}'}
    response3 = requests.post('https://tap2eat.co.ke/pilot/api/v1/user/auth/sign-out', json=json, headers=headers)
    print(response3.status_code)
    del request.session['user']
    del request.session['access_token']
    return redirect('/login')

def usertable1(request):
    try:
        token = request.session['access_token']
    except:
        return render(request, "home2.html")
    response2 = requests.get('https://tap2eat.co.ke/pilot/api/v1/user'+'?pgSize=10000000&q=role.idEQ3', headers={'Authorization': f'Bearer {token}'})
    if response2.status_code == 200 and 'user' in request.session:
        current_user = request.session['user']
        data1 = response2.json()
        todoss = response2.json()
        projects = todoss['content']
        todos = projects.get('data', None)
        ##print(todos)
        ########################################################################
        p = Paginator(todos, 20)
        ##print(p.count)#shows all items in page
        pageNum = request.GET.get('page', 1)
        page1 = p.page(pageNum)
        ##print()
        data = {
            "current_user":current_user,
            "page1":page1
        }
        ########################################################################
        return render(request, "userlists.html", data)
    else:
        return render(request, "home2.html")

def test(request):
    return render(request, "home2.html")

def test2(request):
    return render(request, "base.html")

def usertable2(request):
    try:
        token = request.session['access_token']
    except:
        return render(request, "home2.html")
    response2 = requests.get('https://tap2eat.co.ke/pilot/api/v1/user'+'?pgSize=1000000&q=role.idEQ4', headers={'Authorization': f'Bearer {token}'})
    if response2.status_code == 200 and 'user' in request.session:
        current_user = request.session['user']
        data1 = response2.json()
        ##print(data1)
        #todos = response2.json()
        todoss = data1['content']
        todos = todoss.get('data', 0)
        ##print(todos)
        ###############################PAGINATE###############################
        ########################################################################
        p = Paginator(todos, 20)
        ##print(p.count)#shows all items in page
        pageNum = request.GET.get('page', 1)
        page1 = p.page(pageNum)
        ##print()
        data = {
            "current_user":current_user,
            "page1":page1
        }
        if request.method == 'POST':
            toSearch = (request.POST['search2'])
            #print(toSearch)
            #filterType1 = 'customerReferenceEQ'
            #filterType2 = 'mpesaReceiptNumberEQ'
            searchRequest = requests.get('https://tap2eat.co.ke/pilot/api/v1/user'+'?pgSize=10000000&q=role.idEQ4,firstNameEQ'+toSearch, headers={'Authorization': f'Bearer {token}'})
            found = searchRequest.json()
            found1 = found['content']
            found2 = found1.get('data', None)
            ##print(found2)
            paginatedSearch = Paginator(found2, 5)
            pageSearch = request.GET.get('page', 1)
            pgSearch = paginatedSearch.page(pageSearch)
            dataSearch = {
                "current_user":current_user,
                "page1":pgSearch,
            }
            return render(request, "userlists2.html", dataSearch)
        ########################################################################
        ###############################ENDPAGINATION##########################
        return render(request, "userlists2.html", data)
    else:
        return render(request, "home2.html")

def usertable3(request):
    try:
        token = request.session['access_token']
    except:
        return render(request, "home2.html")
    response2 = requests.get('https://tap2eat.co.ke/pilot/api/v1/user'+'?pgSize=10000000&q=role.idEQ5', headers={'Authorization': f'Bearer {token}'})
    #data1 = response2.json()
    #data1['content']['data']
    #print("Token: " +access_token)
    #print(response2.status_code)
    if response2.status_code == 200 and 'user' in request.session:
        current_user = request.session['user']
        data1 = response2.json()
        #todos = response2.json()
        projects = data1['content']
        todos = projects.get('data', 0)
        #print(todos)
        ###############################PAGINATE###############################
        ###############################PAGINATE###############################
        ########################################################################
        p = Paginator(todos, 20)
        ##print(p.count)#shows all items in page
        pageNum = request.GET.get('page', 1)
        page1 = p.page(pageNum)
        ##print()
        data = {
            "current_user":current_user,
            "page1":page1
        }
        ##filter start
        if request.method == 'POST':
            toSearch = (request.POST['search2'])
            #print(toSearch)
            #filterType1 = 'customerReferenceEQ'
            #filterType2 = 'mpesaReceiptNumberEQ'
            searchRequest = requests.get('https://tap2eat.co.ke/pilot/api/v1/user'+'?pgSize=10000000&q=role.idEQ5,firstNameEQ'+toSearch, headers={'Authorization': f'Bearer {token}'})
            found = searchRequest.json()
            found1 = found['content']
            found2 = found1.get('data', None)
            paginatedSearch = Paginator(found2, 5)
            pageSearch = request.GET.get('page', 1)
            pgSearch = paginatedSearch.page(pageSearch)
            dataSearch = {
                "current_user":current_user,
                "page1":pgSearch,
            }
            return render(request, "userlists3.html", dataSearch)
        ########################################################################
        ###############################ENDPAGINATION##########################
        ###############################ENDPAGINATION##########################
        return render(request, "userlists3.html", data)
    else:
        return render(request, "home2.html")        


def dailyreports(request):
    try:
        token = request.session['access_token']
    except:
        return render(request, "home2.html")
    response2 = requests.get('https://tap2eat.co.ke/pilot/api/v1/user'+'?pgSize=100000&q=role.idEQ5', headers={'Authorization': f'Bearer {token}'})
    #data1 = response2.json()
    #data1['content']['data']
    #print("Token: " +access_token)
    #print(response2.status_code)
    if response2.status_code == 200 and 'user' in request.session:
        current_user = request.session['user']
        data1 = response2.json()
        ##print(data1)
        #todos = response2.json()
        todoss = data1['content']
        todos = todoss.get('data')
    ###############################
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RegisteredStudents.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'FIRSTNAME', 'LASTNAME', 'STATUS'])
    for todo in todos:
        writer.writerow([todo.get('userId'), todo.get('firstName'), todo.get('lastName'), todo['status']])
    return response       

def createuser(request):
    try:
        token = request.session['access_token']
    except:
        return render(request, "home2.html")
    username = request.session['user']
    if username == 'system.admin@tap2eat.co.ke':
        #do something
        context = {
            "current_user":username,
        }
        try:
            token = request.session['access_token']
        except:
            return render(request, "home2.html")
        if request.method == 'POST' and 'user' in request.session:
            current_user = request.session['user']
            firstname = (request.POST['first_name'])
            lastname = (request.POST['last_name'])
            username = (request.POST['phonenumber'])
            password = (request.POST['psw'])
            email = (request.POST['email'])
            roleid = (request.POST['role'])
            roleidd = int(roleid)
            data = {
                'firstName':firstname,
                'lastName':lastname,
                'roleId':roleidd,
                'profile':{'passcode':password},
                'contacts':[{'typeId':1, 'value':username},{'typeId':2, 'value':email}],
            }
            #print(data)
            response2 = requests.post("https://tap2eat.co.ke/pilot/api/v1/user", json=data ,headers={'Authorization': f'Bearer {token}'})
            #print(response2.status_code)
            if response2.status_code == 200:
                return redirect('/home')
            else:
                return HttpResponse("User Created")
    else:
        return HttpResponse("Not Allowed")

    return render(request, 'createuser.html', context)

#MPESA Payments View
def mpesa(request):
    try:
        token = request.session['access_token']
    except:
        return render(request, "home2.html")
    response2 = requests.get('https://tap2eat.co.ke/pilot/api/v1/payments'+'?pgSize=1000000000', headers={'Authorization': f'Bearer {token}'})
    if response2.status_code == 200 and 'user' in request.session:
        current_user = request.session['user']
        data1 = response2.json()
        projects = data1['content']
        todos = projects.get('data', 0)
        ###############################PAGINATE###############################
        p = Paginator(todos, 20)
        ##print(p.count)#shows number of items in page
        pageNum = request.GET.get('page', 1)
        page1 = p.page(pageNum)
        data = {
            "current_user":current_user,
            "page1":page1
        }
        if request.method == 'POST' and 'user' in request.session:
            current_user = request.session['user']
            toSearch = (request.POST['search2'])
            tofilter = (request.POST['search_param'])
            ##print(tofilter)
            #filterType1 = 'customerReferenceEQ'
            #filterType2 = 'mpesaReceiptNumberEQ'
            if tofilter == 'Receipt':
                filterType = 'mpesaReceiptNumberEQ'
            elif tofilter == 'Mobile':
                filterType = 'customerReferenceEQ'
            else:
                filterType = 'customerReferenceEQ'         
            searchRequest = requests.get('https://tap2eat.co.ke/pilot/api/v1/payments'+'?pgSize=1000000000&q='+ filterType + toSearch, headers={'Authorization': f'Bearer {token}'})
            found = searchRequest.json()
            found1 = found['content']
            found2 = found1.get('data', None)
            paginatedSearch = Paginator(found2, 5)
            pageSearch = request.GET.get('page', 1)
            pgSearch = paginatedSearch.page(pageSearch)
            dataSearch = {
                "current_user":current_user,
                "page1":pgSearch,
            }
            return render(request, "mpesa.html", dataSearch)
        ###############################ENDPAGINATION##########################
        return render(request, "mpesa.html", data)
    else:
        return render(request, "home2.html")

def sms(request):
    try:
        token = request.session['access_token']
    except:
        return render(request, "home2.html")
    response2 = requests.get('https://tap2eat.co.ke/pilot/api/v1/user'+'?pgSize=1000000&q=role.idEQ4', headers={'Authorization': f'Bearer {token}'})
    if response2.status_code == 200 and 'user' in request.session:
        current_user = request.session['user']
        data1 = response2.json()
        todoss = data1['content']
        todos = todoss.get('data', None)
    ###############################
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Parents.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'FIRSTNAME', 'LASTNAME', 'CONTACT', 'BALANCE', 'STATUS'])
    for todo in todos:
        for items in todo['contacts']:
            writer.writerow([todo['userId'], todo['firstName'], todo['lastName'], items['value'], todo['balance'], todo['status']])
    return response

################################################# Meal Taps EndPoint
def taptap(request):
    try:
        token = request.session['access_token']
    except:
        return render("home2.html")
    response2 = requests.get('https://tap2eat.co.ke/pilot/api/v1/meal/tap?pgSize=10000000', headers={'Authorization': f'Bearer {token}'})
    if response2.status_code == 200 and 'user' in request.session:
        current_user = request.session['user']
        data1 = response2.json()
        #todos = response2.json()
        projects = data1['content']
        todos = projects.get('data', 0)
        p = Paginator(todos, 20)
        pageNum = request.GET.get('page', 1)
        page1 = p.page(pageNum)
        data = {
            "current_user":current_user,
            "page1":page1
        }
        ##filter start
        if request.method == 'POST' and 'user' in request.session:
            current_user = request.session['user']
            toSearch = (request.POST['search2'])
            ##print(toSearch)
            #filterType1 = 'customerReferenceEQ'
            #filterType2 = 'mpesaReceiptNumberEQ'
            searchRequest = requests.get('https://tap2eat.co.ke/pilot/api/v1/meal/tap'+'?pgSize=10000000&q=role.idEQ5,firstNameEQ'+toSearch, headers={'Authorization': f'Bearer {token}'})
            found = searchRequest.json()
            found1 = found['content']
            found2 = found1.get('data', None)
            paginatedSearch = Paginator(found2, 10)
            pageSearch = request.GET.get('page', 1)
            pgSearch = paginatedSearch.page(pageSearch)
            dataSearch = {
                "current_user":current_user,
                "page1":pgSearch,
            }
            return render(request, "mealtaps.html", dataSearch)
        return render(request, "mealtaps.html", data)
    else:
        return render(request, "home2.html")        
