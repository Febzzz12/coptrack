from django.shortcuts import render,HttpResponseRedirect
import MySQLdb
import datetime
from django.core.files.storage import FileSystemStorage
import qrcode as ad

db=MySQLdb.connect("localhost","root","","guestlabour")
c=db.cursor()

def index(request):
    return render(request,"index.html")

def adminhome(request):
    return render(request,"adminhome.html")

def labourhome(request):
    return render(request,"labourhome.html")

def policehome(request):
    return render(request,"policehome.html")

def userhome(request):
    return render(request,"userhome.html")

def login(request):
    msg=""
    request.session['name']=""
    if(request.POST):      
        name=request.POST.get("name")
        password=request.POST.get("password")
        z="select usertype,status from login where username='"+str(name)+"' and password='"+str(password)+"'"
        print(z)
        c.execute(z)
        data=c.fetchone()
        # print(data[0])
    
        request.session['name']=name
     
        if data:
            if(data[0]=="user" and data[1]=="approved"):
                z="select * from user where email='"+str(name)+"' and password='"+str(password)+"'"
                print("qryyyy",z)
                c.execute(z)
                data12=c.fetchone()
                uid=data12[0]
                uname=data12[1]
                email=data12[5]
                request.session["uid"]=uid
                request.session["uname"]=uname
                request.session["email"]=email
                return HttpResponseRedirect("/userhome")
            elif(data[0]=="labour" and data[1]=="approved"):
                z="select * from labour where name='"+str(name)+"' and password='"+str(password)+"'"
                print("qryyyy",z)
                c.execute(z)
                data12=c.fetchone()
                uid=data12[0]
                uname=data12[1]
                email=data12[5]
                request.session["uid"]=uid
                request.session["uname"]=name
                request.session["email"]=email
                return HttpResponseRedirect("/labourhome")
            elif(data[0]=="police" and data[1]=="approved"):
                z="select * from police where email='"+str(name)+"' and password='"+str(password)+"'"
                c.execute(z)
                data12=c.fetchone()
                uid=data12[0]
                uname=data12[1]
                email=data12[5]
                request.session["uid"]=uid
                request.session["uname"]=uname
                request.session["email"]=email
                return HttpResponseRedirect("/policehome")
            elif(data[0]=="admin"):
                return HttpResponseRedirect("/adminhome")
            else:
                msg="You Are Not Approved Yet"
        else:
            msg="INVALID USER NAME OR PASSWORD"     
    return render (request,"login.html",{"msg":msg})

def userregister(request):
    msg=""
    if request.POST:
        name=request.POST.get("name")
        address=request.POST.get("address")
        place=request.POST.get("place")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        password=request.POST.get("password")  
        pincode=request.POST.get("pincode")     
        c.execute("insert into user(`name`,`address`,`place`,`phone`,`email`,`password`,`pincode`,`status`) values('"+name+"','"+address+"','"+place+"','"+phone+"','"+email+"','"+password+"','"+pincode+"','approved')")
        db.commit()
        c.execute("insert into login(username,password,usertype,status) values('"+email+"','"+password+"','user','approved')")
        db.commit()
        msg="SUCCESSFULLY ADDED"
    return render(request,"userregister.html",{"msg":msg})

def labourregister(request):
    msg=""
    c.execute("select * from police")
    data1=c.fetchall()
    if request.POST:
        name=request.POST.get("name")
        age=request.POST.get("age")
        aadhar=request.POST.get("aadhar")
        voterid=request.POST.get("voterid")
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        place=request.POST.get("place")
        pincode=request.POST.get("pincode")     
        password=request.POST.get("password")  
        desig=request.POST.get("desig")
        police=request.POST.get("police")
        c.execute("insert into labour(`name`,`age`,`aadhar`,`voterid`,`address`,`phone`,`place`,`pincode`,`password`,`job`,`police`,`status`) values('"+name+"','"+age+"','"+aadhar+"','"+voterid+"','"+address+"','"+phone+"','"+place+"','"+pincode+"','"+password+"','"+desig+"','"+police+"','pending')")
        db.commit()
        c.execute("insert into login(username,password,usertype,status) values('"+name+"','"+password+"','labour','pending')")
        db.commit()
        msg="SUCCESSFULLY ADDED"
        c.execute("select max(lid) from labour")
        max=c.fetchall()
        idd=max[0][0]
        c.execute("select * from labour where lid='"+str(idd)+"'")
        data=c.fetchall()
        img=ad.make(data)
        
        # fs=FileSystemStorage()
        # filename=fs.save(img.name,img)
        # path=fs.url(filename)
        db.commit()
    return render(request,"labourregister.html",{"msg":msg,"data1":data1})

def policeregister(request):
    msg=""
    if request.POST:
        name=request.POST.get("name")
        address=request.POST.get("address")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        place=request.POST.get("place")
        pincode=request.POST.get("pincode")     
        password=request.POST.get("password")  
        c.execute("insert into police(`name`,`address`,`email`,`phone`,`place`,`pincode`,`password`,`status`) values('"+name+"','"+address+"','"+email+"','"+phone+"','"+place+"','"+pincode+"','"+password+"','approved')")
        db.commit()
        c.execute("insert into login(username,password,usertype,status) values('"+email+"','"+password+"','police','approved')")
        db.commit()
        msg="SUCCESSFULLY ADDED"
    return render(request,"policeregister.html",{"msg":msg})

################################################################################################################

def adminviewcomplaint(request):
    c.execute("select f.cid,f.description,f.date,u.name from complaint f join user u on f.userid=u.uid")
    data=c.fetchall() 
    return render(request,"adminviewcomplaint.html",{"data":data})

def adminviewlabour(request):
    data=""
    c.execute("select lid,name,age,aadhar,voterid,address,phone,place,pincode,job,police from labour where status='approved'")
    data=c.fetchall() 
    return render(request,"adminviewlabour.html",{"data":data})

def adminviewpolice(request):
    data=""
    c.execute("select pid,name,address,email,phone,place,pincode from police where status='approved'")
    data=c.fetchall() 
    return render(request,"adminviewpolice.html",{"data":data})

def adminviewuser(request):
    data=""
    c.execute("select uid,name,address,place,phone,email,pincode from user where status='approved'")
    data=c.fetchall() 
    return render(request,"adminviewuser.html",{"data":data})

def adminviewbooking(request):
    data=""
    c.execute("select b.bid,u.name,l.name,b.bdate,b.date,b.status,b.days,b.amt from booking b join user u on u.uid=b.uid join labour l on l.lid=b.lid")
    data=c.fetchall()
    return render(request,"adminviewbooking.html",{"data":data})

def adminupdatestatus(request):
    if request.GET:
        bid=request.GET.get("id")
        c.execute("update booking set status='approved' where bid='"+bid+"'")
        db.commit()
        return HttpResponseRedirect('/adminviewbooking')
    return render(request,"adminviewbooking.html")

###########################################################################################################

def policeapprovelabour(request):
    data=""
    uid=request.session['uid']
    uname=request.session["uname"]
    c.execute("select lid,name,age,aadhar,voterid,address,phone,place,pincode,job,police,status from labour where police='"+str(uname)+"' and status='pending'")
    data=c.fetchall() 
    print("*****************")
    print(data)
    adata="select lid,name,age,aadhar,voterid,address,phone,place,pincode,job,police,status from labour where police='"+str(uname)+"' and status='approved'"
    c.execute(adata)
    data2=c.fetchall()
    print(data2)
    return render(request,"policeapprovelabour.html",{"data":data,"data2":data2})

def policeapproved(request):
    if request.GET:
        uid=request.GET.get("id")
        email=request.GET.get("em")
        c.execute("update labour set status='approved' where lid='"+uid+"'")
        db.commit()
        c.execute("update login set status='approved' where username='"+str(email)+"'")
        db.commit()
        return HttpResponseRedirect('/policeapprovelabour')
        ####card generation venam with qrcode
    return render(request,"policeapprovelabour.html")

def policereject(request):
    if request.GET:
        uid=request.GET.get("id")
        email=request.GET.get("em")
        c.execute("delete from labour where lid='"+uid+"'")
        db.commit()
        c.execute("delete from login where username='"+str(email)+"'")
        db.commit()
        return HttpResponseRedirect('/policeapprovelabour')
    return render (request,"policeapprovelabour.html")

def policereplycomplaints(request):
    if request.GET:
        id=request.GET.get("id")
        if request.POST:
            reply=request.POST.get("reply")
            c.execute("update complaint set actions='"+str(reply)+"' where cid='"+str(id)+"'")
            db.commit()
            return HttpResponseRedirect('/policeviewcomplaints/')
    return render(request,"policereplycomplaints.html")

def policeviewcomplaints(request):
    uid=request.session['uid']
    uname=request.session["uname"]
    c.execute("select f.cid,f.description,f.date,u.name,f.actions from complaint f join user u on f.userid=u.uid")
    data=c.fetchall() 
    return render(request,"policeviewcomplaints.html",{"data":data})

#################################################################################################################

def useraddcomplaint(request):
    msg=""
    if request.session['uid']:
        uid=request.session['uid']
        c.execute("select cid,description,date,actions from complaint where userid='"+str(uid)+"'")
        data=c.fetchall()
        if(request.POST):
            complaint=request.POST.get("complaint")
            date=datetime.datetime.now()
            c.execute("insert into complaint(description,date,userid)values('"+str(complaint)+"','"+str(date)+"','"+str(uid)+"')")
            db.commit()
            msg="SEND SUCCESSFULLY"
            return HttpResponseRedirect('/useraddcomplaint')
    return render (request,"useraddcomplaint.html",{"msg":msg,"data":data})

def userviewlabour(request):
    data=""
    c.execute("select lid,name,age,aadhar,voterid,address,phone,place,pincode,job,police,img from labour where status='approved'")
    data=c.fetchall() 
    return render(request,"userviewlabour.html",{"data":data})

def userbooklabour(request):
    msg=""
    uid=request.session['uid']
    print(uid)
    if request.GET:
        lid=request.GET.get("id")
        date=datetime.datetime.now()
        if request.POST:
            ondate=request.POST.get("ondate")
            day=request.POST.get("day")
            amt=request.POST.get("amt")
            c.execute("insert into booking(`uid`,`lid`,`bdate`,`date`,`status`,`days`,`amt`)values('"+str(uid)+"','"+str(lid)+"','"+str(date)+"','"+str(ondate)+"','applied','"+str(day)+"','"+str(amt)+"')")
            db.commit()
            msg="SEND SUCCESSFULLY"
            return HttpResponseRedirect('/userviewlabour')
    return render(request,"userbooklabour.html",{"msg":msg})

def userviewbooking(request):
    data=""
    uid=request.session['uid']
    c.execute("select b.bid,u.name,l.name,b.bdate,b.date,b.status,b.days,b.amt from booking b join user u on u.uid=b.uid join labour l on l.lid=b.lid where b.uid='"+str(uid)+"'")
    data=c.fetchall()
    return render(request,"userviewbooking.html",{"data":data})

def payment1(request):
    if request.GET:
        id=request.GET.get("id")
        day=int(request.GET.get("day"))
        amt=int(request.GET.get("amt"))
        total=day*amt
        request.session["price"]=total
        c.execute("update booking set status='payed' where bid='"+str(id)+"'")
        db.commit()
        if request.POST:
            card=request.POST.get("test")
            request.session["card"]=card
            cardno=request.POST.get("cardno")
            request.session["card_no"]=cardno
            pinno=request.POST.get("pinno")
            request.session["pinno"]=pinno
            return HttpResponseRedirect("/payment2")
    return render(request,"payment1.html")

def payment2(request):
    cno=request.session["card_no"]
    amount=request.session["price"]
    if request.POST:
        return HttpResponseRedirect("/payment3")
    return render(request,"payment2.html",{"cno":cno,"amount":amount})

def payment3(request):
    return render(request,"payment3.html")

def payment4(request):
    return render(request,"payment4.html")

def payment5(request):
    cno=request.session["card_no"]
    today = datetime.datetime.now()
    name =  request.session['uname'] 
    amount = request.session["price"]
    return render(request,"payment5.html",{"cno":cno,"today":today,"name":name,"amount":amount})



########################################################################################################

def labourviewapprovedbooking(request):
    data=""
    uid=request.session['uid']
    c.execute("select b.bid,u.name,l.name,b.bdate,b.date,b.status,b.days,b.amt from booking b join user u on u.uid=b.uid join labour l on l.lid=b.lid where b.lid='"+str(uid)+"' and (b.status='approved' or b.status='payed')")
    data=c.fetchall()
    return render(request,"labourviewapprovedbooking.html",{"data":data})

def labourviewcertificate(request):
    data=""
    uid=request.session['uid']
    qry="select * from labour where lid='"+str(uid)+"'"
    print("hiiii",qry)
    c.execute(qry)
    data=c.fetchall()
    print(data)
    return render(request,"labourviewcertificate.html",{"data":data})