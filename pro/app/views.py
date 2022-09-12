from re import sub
from this import d
from tkinter import RIDGE
from django.shortcuts import render
from django.http import HttpResponseRedirect
from app import dbconnection
from django.core.files.storage import FileSystemStorage
from datetime import datetime,date
import random
import string
def main(request):
     if request.method=='POST':
        sr=request.POST['sch']
        if sr=='category':
            sql1="select * from category"
            a=dbconnection.allrow(sql1)
            return render(request,'search.html',{'a':a})
        elif sr=='company':
            sql1="select * from company"
            b=dbconnection.allrow(sql1)
            return render(request,'search.html',{'b':b})
        elif sr=='sub-category':
            sql1="select * from subcat"
            c=dbconnection.allrow(sql1)
            return render(request,'search.html',{'c':c})
        else:
            msg="NO RESULT FOUND"
            return render(request,'search.html',{'msg':msg})
     return render(request,'index.html',{})
def logout(request):
    un=request.session['un']
    dt=datetime.now()
    t=dt.strftime("%H:%M:%S")
    sql="update log_status set log_out='"+t+"',status='1' where username='"+un+"' and status='0'"
    dbconnection.addrow(sql)
    return HttpResponseRedirect('http://127.0.0.1:8000/')

def login(request):
    if request.method=='POST':
        un=request.POST['un']
        pas=request.POST['pas']
        sql="select * from data where username='"+un+"' and password='"+pas+"'"
        a=dbconnection.onerow(sql)
        dt=datetime.now()
        t=dt.strftime("%H:%M:%S")
        d=date.today()
        if a:
             request.session['un']=un
             if a[3]=='staff':
                if a[4]==1:
                    sql1="INSERT INTO `log_status`(`username`,`date`,`login_time`,`log_out`,`status`) VALUES ('"+un+"','"+str(d)+"','"+str(t)+"',0,0)"
                    dbconnection.addrow(sql1)
                    return HttpResponseRedirect('http://127.0.0.1:8000/shome')
                else:
                    msg1="YOUR ACCOUNT IS TEMPORARY BLOCKED PLEASE CONTACT ADMIN"
                    return render(request,'login.html',{'msg1':msg1})
            
             elif a[3]=='admin':
                return HttpResponseRedirect('http://127.0.0.1:8000/ahome')
             elif a[3]=='user':
                return HttpResponseRedirect('http://127.0.0.1:8000/uhome')
        else:
            msg='INVALID USERNAME OR PASSWORD'
            return render(request,'login.html',{'msg':msg})
        
    return render(request,'login.html',{})
    
def ahome(request):
    sql="select qty from stock"
    data=dbconnection.allrow(sql)
    k=0
    data2=[]
    ilist=[]
    ilist2=[]
    ilist3=[]
    for i in data:
        for j in i:
            if j<50:
                ilist.append(j)
                k=k+1
    for i in ilist:
        sql1="select id from stock where qty='"+str(i)+"'"
        data1=dbconnection.onerow(sql1)   
        ilist2.append(data1)                
    for d1 in ilist2:
        for jj in d1:                 
            sql2="SELECT stock.id, category.catname, subcat.sub_cat, company.company,stock.qty FROM stock INNER JOIN category ON stock.cid = category.cid INNER JOIN subcat ON stock.sub_id = subcat.sub_id INNER JOIN company ON stock.com_id = company.com_id where id='"+str(jj)+"'"
            data2=dbconnection.allrow(sql2)
            ilist3.append(data2)  
    return render(request,'admin/ahome.html',{'k':k,'d':ilist2,'il':ilist,'ee':data2,'oo':ilist3})

# def ahome(request):
#     sql="select id,qty from stock where qty<50"
#     data=dbconnection.allrow(sql)
#     count=0
#     ilist=[]
#     lowstocks=[]
#     data2=[]
#     
#     for i in data:
#         count=count+1
#         for i2 in str(i[0]):                 
#             ilist.append(i2)                 
#     for i in ilist:               
#         sql2="""SELECT stock.id, category.catname, subcat.sub_cat, company.company,stock.qty 
#         FROM stock INNER JOIN category ON stock.cid = category.cid
#         INNER JOIN subcat ON stock.sub_id = subcat.sub_id
#         INNER JOIN company ON stock.com_id = company.com_id
#         WHERE id='"""+i+"""';"""
#         data2=dbconnection.allrow(sql2)
#         lowstocks.append(data2)              
#     return render(request,'admin/ahome.html',{'count':count,'lowstocks':lowstocks})

def search(request):
    if request.method=='POST':
        sr=request.POST['sch']
        if sr=='category':
            sql1="select * from category"
            a=dbconnection.allrow(sql1)
            return render(request,'search.html',{'a':a})
        elif sr=='subcategory':
            sql1="select * from subcat"
            b=dbconnection.allrow(sql1)
            return render(request,'search.html',{'b':b})
        elif sr=='company':
            sql1="select * from company"
            c=dbconnection.allrow(sql1)
            return render(request,'search.html',{'c':c})
        else:
            msg="no search result"
            return render(request,'search.html',{'msg':msg})
    return render(request,'search.html',{})
        
def contact(request):
    return render(request,'contact.html',{})
def about(request):
    return render(request,'about.html',{})
            
    

def addcat(request):
    sql1="select * from category"
    a=dbconnection.allrow(sql1)
    if request.POST.get('caty'):
        cat=request.POST['cat']
        sql="INSERT INTO `category`(`catname`) VALUES('"+cat+"')"
        dbconnection.addrow(sql)
        return HttpResponseRedirect("addcat")
    if request.GET.get("nid"):
        rid=request.GET['nid']
        sql="select * from category where cid='"+rid+"'"
        b=dbconnection.onerow(sql)
        if request.POST.get("updcat"):
            cat=request.POST['scat']
            sql1="update category set catname='"+cat+"'where cid='"+rid+"'"
            dbconnection.addrow(sql1)
            return HttpResponseRedirect("addcat")
        return render(request,'admin/addcat.html',{'a':a,'b':b})    
    return render(request,'admin/addcat.html',{'a':a})

def delcat(request):   
    rid=request.GET['nid']
    sql1="delete from category where cid='"+rid+"'"
    dbconnection.addrow(sql1)
    return HttpResponseRedirect('http://127.0.0.1:8000/addcat')

def addcomp(request):
    sql1="select * from company"
    a=dbconnection.allrow(sql1)
    if request.POST.get('comp'):
        comp=request.POST['com']
        sql="INSERT INTO `company`(`company`) VALUES('"+comp+"')"
        dbconnection.addrow(sql)
        return HttpResponseRedirect("addcomp")
    if request.GET.get("nid"):
        rid=request.GET['nid']
        sql="select * from company where com_id='"+rid+"'"
        b=dbconnection.onerow(sql)
        if request.POST.get("updcom"):
            com=request.POST['scom']
            sql1="update company set company='"+com+"'where com_id='"+rid+"'"
            dbconnection.addrow(sql1)
            return HttpResponseRedirect("addcomp")
        return render(request,'admin/addcomp.html',{'a':a,'b':b})  
    return render(request,'admin/addcomp.html',{'a':a})

def delcomp(request):
    rid=request.GET['nid']
    sql1="delete from company where com_id='"+rid+"'"
    dbconnection.addrow(sql1)
    return HttpResponseRedirect('addcomp')

def addsub(request):
    sql1="select * from category"
    a=dbconnection.allrow(sql1)
    sql="select subcat.sub_id,category.catname,subcat.sub_cat,subcat.amount from subcat inner join category on subcat.cid=category.cid"
    b=dbconnection.allrow(sql)
    if request.POST.get('ad'):
        cat=request.POST['cat']
        subc=request.POST['sub']
        num=request.POST['num']
        sql3="INSERT INTO `subcat`(`cid`,`sub_cat`,`amount`) VALUES('"+cat+"','"+subc+"','"+num+"')"
        dbconnection.addrow(sql3)
        return HttpResponseRedirect('addsub')
    if request.GET.get('nid'):
        rid=request.GET['nid']
        sql3="select * from subcat where sub_id='"+rid+"'"
        c=dbconnection.onerow(sql3)
        if request.POST.get('uad'):
            subc=request.POST['usub']
            num=request.POST['unum']
            sql="update subcat set sub_cat='"+subc+"',amount='"+num+"' where sub_id='"+rid+"'"
            dbconnection.addrow(sql)
        return render(request,'admin/addsub.html',{'b':b,'a':a,'c':c})
    return render(request,'admin/addsub.html',{'b':b,'a':a})

def delsub(request):
    rid=request.GET['nid']
    sql="delete from subcat where sub_id='"+rid+"'"
    dbconnection.addrow(sql)
    return HttpResponseRedirect('addsub')
    

def logstatus(request):
    if request.method=='POST':
        fd=request.POST['fd']
        td=request.POST['td']
        sql="select * from log_status where date between'"+fd+"' and '"+td+"'"
        a=dbconnection.allrow(sql)
        return render(request,'admin/logstatus.html',{'a':a})
    return render(request,'admin/logstatus.html',{})


def viewstaff(request):
    sql="select * from addstaff"
    a=dbconnection.allrow(sql)
    return render(request,'admin/viewstaff.html',{'a':a})

def viewstaff2(request):
    rid=request.GET['aid']
    sql="select * from addstaff where staff_id='"+rid+"'"
    a=dbconnection.onerow(sql)
    if request.POST.get('b1'):
        sql="update addstaff set status= '1' where username='"+str(a[7])+"'"
        dbconnection.addrow(sql)
        sql="update data set status= 1 where username='"+str(a[7])+"'"
        dbconnection.addrow(sql)
        return HttpResponseRedirect('viewstaff2?aid='+rid)
    elif request.POST.get('b2'):
        sql="update addstaff set status= '0' where username='"+str(a[7])+"'"
        dbconnection.addrow(sql)
        sql="update data set status= '0' where username='"+str(a[7])+"'"
        dbconnection.addrow(sql)
        return HttpResponseRedirect('viewstaff2?aid='+rid)
    elif request.POST.get('b3'):
        sal=request.POST['sal']
        sql="update addstaff set salary='"+sal+"' where staff_id='"+rid+"'"
        dbconnection.addrow(sql)
        return HttpResponseRedirect('viewstaff2?aid='+rid)

    if a[6]==1:
        s="ACTIVE"
    else:
        s="DEACTIVE"
    return render(request,'admin/viewstaff2.html',{'a':a,'s':s})

def addstaff(request):
    if request.method=='POST':
        name=request.POST['nm']
        address=request.POST['ad']
        dob=request.POST['dt']
        phone=request.POST['ph']
        salary=request.POST['sal']
        us=request.POST['un']
        pas=request.POST['pas']
        img=request.FILES['up']
        fs=FileSystemStorage()
        fs.save('app/static/pics/'+img.name,img)
        sql="INSERT INTO `addstaff`(`name`,`address`,`dob`,`phone`,`salary`,`status`,`username`,`password`,`image`) VALUES('"+name+"','"+address+"','"+dob+"','"+phone+"','"+salary+"',1,'"+us+"','"+pas+"','"+img.name+"')"
        dbconnection.addrow(sql)
        sql1="INSERT INTO `data`(`username`, `password`, `type`,`status`) VALUES ('"+us+"','"+pas+"','staff',1)"
        dbconnection.addrow(sql1)
        return HttpResponseRedirect('addstaff')
    return render(request,'admin/addstaff.html',{})

def salarylist(request):
    sql="select * from addstaff"
    a=dbconnection.allrow(sql)
    return render(request,'admin/salarylist.html',{'a':a})

def salary(request):
    rid=request.GET['sid']
    sql1="select * from addstaff where staff_id='"+rid+"'"
    a=dbconnection.onerow(sql1)
    # un=request.session['un']
    # sql="select * from data where username='"+un+"'"
    # a1=dbconnection.onerow(sql)
    if request.method=='POST':
        name=request.POST['nm']
        message=request.POST['msg']
        dat=request.POST['dt']
        amount=request.POST['sal']
        sql2="select * from salary where staff_id='"+rid+"'"
        b=dbconnection.onerow(sql2)
        s="select extract(MONTH from '"+dat+"')"
        h=dbconnection.onerow(s)
        if b:
            if b[6]!=int(amount):
                msg="SALARY LIMIT REACHED"
                return render(request,'admin/salary.html',{'msg':msg})
            elif b[5]==str(h[0]):
                msg1="ALREADY GIVEN" 
                return render(request,'admin/salary.html',{'msg1':msg1})
            else:
                sql3="INSERT INTO `salary`(`staff_id`,`date`,`staff_name`,`message`,`month`,`amount`,`addby`) VALUES('"+rid+"','"+dat+"','"+name+"','"+message+"','"+str(h[0])+"','"+amount+"','"+un+"')"
                dbconnection.addrow(sql3)
        elif int(amount)!=a[5]:
            msg="SALARY LIMIT REACHED"
            return render(request,'admin/salary.html',{'msg':msg,'s':h})
        else:
            sql3="INSERT INTO `salary`(`staff_id`,`date`,`staff_name`,`message`,`month`,`amount`,`addby`) VALUES('"+rid+"','"+dat+"','"+name+"','"+message+"','"+str(h[0])+"','"+amount+"','"+un+"')"
            dbconnection.addrow(sql3)
    return render(request,'admin/salary.html',{'a':a})

def paidsalary(request):
    sql="select * from salary"
    a=dbconnection.allrow(sql)
    return render(request,'admin/paidsalary.html',{'a':a})

def stock(request):
    sql="select category.catname,company.company,subcat.sub_cat,stock.qty,stock.amount from stock inner join category on stock.cid=category.cid inner join company on stock.com_id=company.com_id inner join subcat on stock.sub_id=subcat.sub_id"
    a=dbconnection.allrow(sql)
    return render(request,'admin/stock.html',{'a':a})
def stockupd(request):
    if request.method=='POST':
        fd=request.POST['fd']
        td=request.POST['td']
        sql="select category.catname,subcat.sub_cat,company.company,addstock.qty,addstock.date,addstock.purchase_amount,addstock.addby from addstock inner join category on addstock.cid=category.cid inner join company on addstock.company_id=company.com_id inner join subcat on addstock.sub_id=subcat.sub_id where date between '"+fd+"'and '"+td+"'"
        a=dbconnection.allrow(sql)
        return render(request,'admin/stockupd.html',{'a':a})
    return render(request,'admin/stockupd.html',{})
    

def saledet(request):
    sql="select * from bill"
    a=dbconnection.allrow(sql)
    return render(request,'admin/saledet.html',{'a':a})

def viewcustomer(request):
    sql="select * from addcustomer"
    a=dbconnection.allrow(sql)
    return render(request,'admin/viewcustomer.html',{'a':a})

def actdeac(request):
    sql="select * from addstaff"
    a=dbconnection.allrow(sql)
    return render(request,'admin/actdeac.html',{'a':a})
    
def tencus(request):
    sql="select * from addcustomer order by  purchase_amount desc"
    a=dbconnection.allrow(sql)
    sql="update addcustomer set addcustomer.purchase_amount=(select sum(bill.amount) from bill where addcustomer.id=bill.cus_id)" 
    dbconnection.addrow(sql)
    return render(request,'admin/tencus.html',{'a':a})

def saledt(request):
    if request.method=='POST':
        dt=request.POST['dt']
        sql="select date,sum(amount) from bill where date='"+str(dt)+"'"
        a=dbconnection.onerow(sql)
        return render(request,'admin/saledt.html',{'a':a})
    return render(request,'admin/saledt.html',{})

def saledtf(request):
    cid=request.GET['cid']
    sql="select bill_no,date,amount from bill where date='"+str(cid)+"'"
    b=dbconnection.allrow(sql)
    return render(request,'admin/saledtf.html',{'b':b})

def salert(request):
    sql="select * from addstaff"
    s=dbconnection.allrow(sql)
    if request.method=="POST":
        un=request.POST['sf']
        dt=request.POST['dt']
        sql="select category.catname,subcat.sub_cat,company.company,sale_table.qty,sale_table.amount from sale_table inner join category on sale_table.cat_id=category.cid inner join company on sale_table.com_id=company.com_id inner join subcat on sale_table.sub_id=subcat.sub_id where addby='"+un+"' and date='"+dt+"'"

        # sql="select date,addby,sum(amount) from bill where addby='"+un+"' and date='"+dt+"'"
        a=dbconnection.allrow(sql)
        return render(request,'admin/salert.html',{'a':a,'s':s})
    return render(request,'admin/salert.html',{'s':s})

def salert2(request):
    rid=request.GET['cid']
    sid=request.GET['nid']
    sql="select category.catname,subcat.sub_cat,company.company,sale_table.qty,sale_table.amount from sale_table inner join category on sale_table.cat_id=category.cid inner join company on sale_table.com_id=company.com_id inner join subcat on sale_table.sub_id=subcat.sub_id where date='"+rid+"' and addby='"+sid+"'"
    b=dbconnection.allrow(sql)
    return render(request,'admin/salert.html',{'b':b})

def dailyexp(request):
    if request.method=="POST":
        dt=request.POST['dt']
        sql="select sum(amount) from bill where date='"+dt+"'"
        a=dbconnection.onerow(sql)
        sql1="select amount from salary where date='"+dt+"'"
        b=dbconnection.onerow(sql1)
        sql2="select sum(purchase_amount) from addstock where date='"+dt+"'"
        c=dbconnection.onerow(sql2)
        return render(request,'admin/dailyexp.html',{'a':a,'b':b,'c':c})
    return render(request,'admin/dailyexp.html',{})

def fbview(request):
    sql="select feedback.date,addcustomer.name,addcustomer.image,addcustomer.phone,feedback.feedback from feedback inner join addcustomer on feedback.cus_id=addcustomer.id"
    a=dbconnection.allrow(sql)
    return render(request,'admin/fbview.html',{'a':a})

def cmview(request):
    sql="select complaint.date,addcustomer.name,addcustomer.image,addcustomer.phone,complaint.complaint from complaint inner join addcustomer on complaint.cus_id=addcustomer.id"
    a=dbconnection.allrow(sql)
    return render(request,'admin/cmview.html',{'a':a})









    
def shome(request):
    un=request.session['un']
    sql="select name from addstaff where username='"+un+"'"
    a=dbconnection.onerow(sql)
    return render(request,'staff/shome.html',{'a':a[0]})
def svcustomer(request):
    sql="select * from addcustomer"
    a=dbconnection.allrow(sql)
    return render(request,'staff/svcustomer.html',{'a':a})
def scustomer(request):
    if request.method=='POST':
        cs=request.POST['sc']
        sql="select * from addcustomer where name='"+cs+"'"
        a=dbconnection.allrow(sql)
        return render(request,'staff/scustomer.html',{'a':a})
    return render(request,'staff/scustomer.html',{})
    

def sprofile(request):
    un=request.session['un']
    sql="select * from addstaff where username ='"+un+"'"
    a=dbconnection.onerow(sql)
    if a[6]==1:
        msg="ACTIVE"
    else:
        msg="DEACTIVATED"
    return render(request,'staff/sprofile.html',{'a':a,'b':msg})

def password(request):
    if request.method=='POST':
        un=request.POST['us']
        sql="select * from addstaff where username='"+un+"'"
        a=dbconnection.onerow(sql)
        if a:
            if un in a:
                sql1="INSERT INTO `password`(`cus_id`, `username`, `password`, `status`) VALUES ('"+str(a[0])+"','"+un+"','requested','0')"
                dbconnection.addrow(sql1)
                msg="password request submitted"
                return render(request,'password.html',{'msg':msg})
            else:
                msg="invalid email"
                return render(request,'password.html',{msg:'msg'})
    return render(request,'password.html',{})

def reset(request):
    sql="select * from password where status='0'"
    a=dbconnection.allrow(sql)
    if a:
        return render(request,'admin/reset.html',{'a':a})
    else:
        msg1="NO CURRENT REQUEST"
        return render(request,'admin/reset.html',{'msg':msg1})


def pasnew(request):
    un=request.GET['cid']
    pw=passgen()
    sql1="update addstaff set password='"+pw+"' where username='"+un+"'"
    dbconnection.addrow(sql1)
    sql2="update data set password='"+pw+"' where username='"+un+"'"
    dbconnection.addrow(sql2)
    sql2="update password set status='1',password='"+pw+"'where username='"+un+"' and status='0'"
    dbconnection.addrow(sql2)
    msg="YOUR NEW PASSWORD IS '"+pw+"'"
    return render(request,'admin/reset.html',{'msg':msg})

def passgen():
    characters = list(string.digits)
    random.shuffle(characters)
    password=[]
    for i in range(4):
        password.append(random.choice(characters))
    random.shuffle(password)
    pw="".join(password)
    return pw





def addcustomer(request):
    if request.method=='POST':
        name=request.POST['nm']
        address=request.POST['ad']
        phone=request.POST['ph']
        un=request.POST['un']
        pa=request.POST['pas']
        img=request.FILES['up']
        fs=FileSystemStorage()
        fs.save('app/static/pics/'+img.name,img)
        sql="INSERT INTO `addcustomer`(`name`,`address`,`phone`,`purchase_amount`,`username`,`password`,`image`) VALUES('"+name+"','"+address+"','"+phone+"',0,'"+un+"','"+pa+"','"+img.name+"')"
        dbconnection.addrow(sql)
        sql1="INSERT INTO `data`(`username`, `password`, `type`) VALUES ('"+un+"','"+pa+"','user')"
        dbconnection.addrow(sql1)
    return render(request,'staff/addcustomer.html',{})

def supdate(request):
    un=request.session['un']
    sql="select * from addstaff where username ='"+un+"'"
    a=dbconnection.onerow(sql)
    if request.POST.get('det'):
        name=request.POST['nm']
        address=request.POST['ad']
        phone=request.POST['ph']
        sql="UPDATE `addstaff` SET `name`='"+name+"',`address`='"+address+"',`phone`='"+phone+"' WHERE `username`='"+un+"'"
        dbconnection.addrow(sql)
        return HttpResponseRedirect('http://127.0.0.1:8000/supdate')
    elif request.POST.get('pic'):
        img=request.FILES['up']
        fs=FileSystemStorage()
        fs.save('app/static/pics/'+img.name,img)
        sql="UPDATE `addstaff` SET `image`='"+img.name+"' WHERE `username`='"+un+"'"
        dbconnection.addrow(sql)
        return HttpResponseRedirect('http://127.0.0.1:8000/supdate')
    elif request.POST.get('pas'):
        opas=request.POST['opas']
        npas=request.POST['npas']
        cpas=request.POST['cpas']
        if opas in a[8]:
            if npas==cpas:
                sql="UPDATE `addstaff` SET `password`='"+cpas+"' WHERE `username`='"+un+"'"
                dbconnection.addrow(sql)
            else:
                msg="PASSWORD MISMATCH"
                return render(request,'staff/supdate.html',{'a':a,'msg':msg})
        else:
            msg="OLD PASSWORD IS WRONG"
            return render(request,'staff/supdate.html',{'a':a,'msg':msg})
    return render(request,'staff/supdate.html',{'a':a})

def srequest(request):
    un=request.session['un']
    sql="select * from addstaff where username='"+un+"'"
    c=dbconnection.onerow(sql)
    if request.method=='POST':
        sid=request.POST['std']
        nm=request.POST['nm']
        fd=request.POST['dt1']
        td=request.POST['dt2']
        rs=request.POST['rs']
        a2=str(fd)
        b2=str(td)
        a=a2.split("-")
        b=b2.split("-")
        a1=date(int(a[0]),int(a[1]),int(a[2]))
        b1=date(int(b[0]),int(b[1]),int(b[2]))
        dif=b1-a1
        em=dif.days+1
        sql1="insert into `leave_request`(`staff_id`,`username`,`fromd`,`tod`,`days`,`reason`,`status`)values('"+sid+"','"+nm+"','"+fd+"','"+td+"','"+str(em)+"','"+rs+"','requested')"
        dbconnection.addrow(sql1)
        sql2="select * from leave_request where username='"+un+"'"
        a1=dbconnection.onerow(sql2)
        if a1[6]=='requested':
            msg="REQUESTED WAITING FOR CONFIRMATION"
            return render(request,'srequest.html',{'msg':msg})
    return render(request,'staff/srequest.html',{'b':c})


def arequest(request):
    sql="select * from leave_request where status='requested' "
    a=dbconnection.allrow(sql)
    if a:
        return render(request,'admin/arequest.html',{'a':a})
    else:
        msg='NO CURRENT LEAVE REQUESTS'
        return render(request,'admin/arequest.html',{'msg':msg})    
def acpt(request):
    rid=request.GET['cid']
    sql="select * from leave_request where staff_id='"+rid+"' and status='requested'"
    a=dbconnection.onerow(sql)
    sql1="select * from addstaff where staff_id='"+rid+"'"
    n=dbconnection.onerow(sql1)
    if request.POST.get('b1'):
        sql="update leave_request set status='granted' where staff_id='"+rid+"' and status='requested'"
        dbconnection.addrow(sql)
        return HttpResponseRedirect('arequest')
    elif request.POST.get('b2'):
        sql="update leave_request set status='denied' where staff_id='"+rid+"' and status='requested'"
        dbconnection.addrow(sql)
        return HttpResponseRedirect('arequest')
    return render(request,'admin/acpt.html',{'a':a,'n':n})


def addstock(request):
    un=request.session['un']
    sql1="select * from addstaff where username='"+un+"'"
    s=dbconnection.onerow(sql1)
    sql2='select * from category'
    a=dbconnection.allrow(sql2)
    sql3='select * from company'
    a1=dbconnection.allrow(sql3)
    sql4='select * from subcat'
    a2=dbconnection.allrow(sql4)
    if request.method=='POST':
        cat=request.POST['cat']
        sub=request.POST['sub']
        com=request.POST['com']
        qty=request.POST['qty']
        d=datetime.today()
        sql="select * from subcat where sub_id='"+sub+"' and cid='"+cat+"'"
        n=dbconnection.onerow(sql)
        res=int(qty)*int(n[3])
        sql5="INSERT INTO `addstock`(`cid`, `sub_id`, `company_id`, `qty`,`date`,`purchase_amount`,`addby`) VALUES ('"+cat+"','"+sub+"','"+com+"','"+qty+"','"+str(d)+"','"+str(res)+"','"+un+"')"
        dbconnection.addrow(sql5)
        sql6="select * from stock where cid='"+cat+"' and com_id= '"+com+"' and sub_id='"+sub+"'"
        data=dbconnection.onerow(sql6)
        if data:
            var=data[4]+int(qty)
            sql7="UPDATE `stock` SET `qty`='"+str(var)+"' WHERE cid='"+cat+"' and com_id= '"+com+"' and sub_id='"+sub+"'"
            dbconnection.addrow(sql7)
        else:
            sql8="INSERT INTO `stock`(`cid`, `sub_id`, `com_id`, `qty`, `amount`) VALUES ('"+cat+"','"+sub+"','"+com+"','"+qty+"','"+str(n[3])+"')"
            dbconnection.addrow(sql8)
    return render(request,'staff/addstock.html',{'a':a,'a1':a1,'a2':a2,'s':s})

def sale(request):
    un=request.session['un']
    if request.method=='POST':
        cid=request.POST['cus']
        d=date.today()
        sql="INSERT INTO `bill`( `date`, `cus_id`, `amount`, `status`, `addby`) VALUES ('"+str(d)+"','"+cid+"','0','0','"+un+"')"
        dbconnection.addrow(sql)
        return HttpResponseRedirect('sale2?cid='+cid)
    sql1="select * from addcustomer"
    a=dbconnection.allrow(sql1)
    return render(request,'staff/sale.html',{'a':a})

def sale2(request):
    sql1="SELECT * FROM `category`"
    data1=dbconnection.allrow(sql1)
    sql2="SELECT * FROM `company`"
    data2=dbconnection.allrow(sql2)
    sql3="SELECT * FROM `subcat`"
    data3=dbconnection.allrow(sql3)
    cusid=request.GET['cid']
    dat=date.today()
    sql6="SELECT * FROM `addcustomer` where Id='"+cusid+"'"
    data6=dbconnection.onerow(sql6)
    sql4="SELECT * FROM `bill` WHERE `Cus_id`='"+cusid+"' and `Date`='"+str(dat)+"'and Status='0'"
    data4=dbconnection.onerow(sql4)
    sql7="SELECT * FROM `sale_table` where `Bill_no`='"+str(data4[0])+"'"
    data7=dbconnection.allrow(sql7)
    sid=request.session['un']
    if request.POST.get('addpro'): 
        bill=request.POST['bill']
        catid=request.POST['cat']
        subcat=request.POST['sub']
        com=request.POST['com']
        quan=request.POST['qun']
        amt=request.POST['amt']
        var=int(quan)*int(amt)
        sql8="Select qty from stock where cid= '"+catid+"' and `sub_id`='"+subcat+"' and `com_id`='"+com+"' "
        data8=dbconnection.onerow(sql8)
        sql7="SELECT * FROM `sale_table` where `Bill_no`='"+bill+"'"
        data7=dbconnection.allrow(sql7)
        
        if int(data8[0])<int(quan):
            msg="Out of stock,Available Stock is '"+str(data8[0])+"'"
            return render(request,'staff/sale2.html',{'msg':msg,'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data6':data6,'data7':data7,'cid':cusid})
        else:
            sql5="INSERT INTO `sale_table`(`Bill_no`, `Date`, `Cat_Id`, `Sub_Id`, `com_Id`, `qty`, `amount`, `AddBy`) VALUES('"+bill+"','"+str(dat)+"','"+catid+"','"+subcat+"','"+com+"','"+quan+"','"+str(var)+"','"+sid+"')"
            dbconnection.addrow(sql5)
            ans=int(data8[0])-int(quan)
            sql9="update stock set Qty='"+str(ans)+"'  where Cid= '"+catid+"' and `Sub_id`='"+subcat+"' and `com_Id`= '"+com+"' "
            dbconnection.addrow(sql9)
            sql7="SELECT * FROM `sale_table` where `Bill_No`='"+bill+"'"
            data7=dbconnection.allrow(sql7)
            return HttpResponseRedirect("/sale2?cid="+cusid)
    elif request.POST.get('Total'):
        var="select sum(Amount) from sale_table where Bill_No='"+str(data4[0])+"'"
        var1=dbconnection.onerow(var)
        return render(request,'staff/sale2.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data6':data6,'data7':data7,'cid':cusid,'var':var1})
    elif request.POST.get('Proceed'):
        var="select sum(Amount) from sale_table where Bill_No='"+str(data4[0])+"'"
        var1=dbconnection.onerow(var)
        sql2="UPDATE `bill` SET Status=1 , Amount='"+str(var1[0])+"' where Bill_no='"+str(data4[0])+"' "
        dbconnection.addrow(sql2)
        return render(request,'staff/sale2.html',{'bilid':data4[0]})
    return render(request,'staff/sale2.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data6':data6,'data7':data7,'cid':cusid,'bilid':data4[0]})

def delete(request):
    rid=request.GET['pid']
    bid=request.GET['cid']
    sql="select * from sale_table  where id='"+rid+"'"
    data=dbconnection.onerow(sql)
    catid=str(data[3])
    subcat=str(data[4])
    com=str(data[5])
    sql="select qty FROM stock where Cid= '"+catid+"' and `Sub_id`='"+subcat+"' and `com_id`= '"+com+"' "
    data1=dbconnection.onerow(sql)
    q=int(data[6])+int(data1[0])
    sql="update stock set qty='"+str(q)+"' where cid= '"+catid+"' and `sub_id`='"+subcat+"' and `com_id`= '"+com+"' "
    dbconnection.addrow(sql)
    sql="delete from sale_table where id='"+rid+"'"
    dbconnection.addrow(sql)
    return HttpResponseRedirect('http://127.0.0.1:8000/sale2?cid='+bid)

def sumof(request):
    sid=request.GET['cid']
    sql1="select sum(amount) from sale_table where bill_no='"+sid+"'"
    n=dbconnection.onerow(sql1)
    m=int(n[0])
    sql2="UPDATE `bill` SET `amount`='"+str(m)+"',`status`='1' WHERE bill_no='"+sid+"'"
    dbconnection.addrow(sql2)
    return render(request,'staff/sale2.html',{'n':m})

def billsum(request):
    sql="update addcustomer set addcustomer.purchase_amount=(select sum(bill.amount) from bill where addcustomer.id=bill.cus_id)" 
    dbconnection.addrow(sql)
    sql1="select * from addcustomer"
    a=dbconnection.allrow(sql1)
    return render(request,'admin/billsum.html',{'a':a})

def singlebill(request):
    cid=request.GET['aid']
    sql1="select * from bill where cus_id='"+cid+"'"
    a=dbconnection.allrow(sql1)
    return render(request,'admin/singlebill.html',{'a':a})

def showbill(request):
    nid=request.GET['nid']
    sql="select category.catname,subcat.sub_cat,company.company,sale_table.qty,sale_table.amount from sale_table inner join category on sale_table.cat_id=category.cid inner join subcat on sale_table.sub_id=subcat.sub_id inner join company on sale_table.com_id=company.com_id  where bill_no='"+nid+"'"
    b=dbconnection.allrow(sql)
    return render(request,'admin/showbill.html',{'b':b})



def uhome(request):
    un=request.session['un']
    sql="select name from addcustomer where username='"+un+"'"
    a=dbconnection.onerow(sql)
    return render(request,'customer/uhome.html',{'a':a[0]})
def uprod(request):
    sql="select category.catname,company.company,subcat.sub_cat from stock inner join category on stock.cid=category.cid inner join company on stock.com_id=company.com_id inner join subcat on stock.sub_id=subcat.sub_id"
    a=dbconnection.allrow(sql)
    return render(request,'customer/uprod.html',{'a':a})

def billpurch(request):
    un=request.session['un']
    sql1="select id from addcustomer where username='"+un+"'"
    n=dbconnection.onerow(sql1)
    for i in n:
        m=int(i)
    sql="select bill_no,date,amount from bill where cus_id='"+str(m)+"'"
    a=dbconnection.allrow(sql)
    return render(request,'customer/billpurch.html',{'a':a})

def billpurch2(request):
    rid=request.GET['cid']
    sql="select category.catname,company.company,subcat.sub_cat,sale_table.qty,sale_table.amount from sale_table inner join category on sale_table.cat_id=category.cid inner join company on sale_table.com_id=company.com_id inner join subcat on sale_table.sub_id=subcat.sub_id where bill_no='"+rid+"'"
    a=dbconnection.allrow(sql)
    return render(request,'customer/billpurch2.html',{'a':a})

def feedback(request):
    un=request.session['un']
    sql4="select id from addcustomer where username='"+un+"'"
    i=dbconnection.onerow(sql4)
    d=datetime.now()
    if request.method=='POST':
        cus=request.POST['cus']
        fb=request.POST['fb']
        sql3="insert into `feedback`(`cus_id`,`date`,`feedback`) values('"+cus+"','"+str(d)+"','"+fb+"')"
        dbconnection.addrow(sql3)
        return HttpResponseRedirect('feedback')
    return render(request,'customer/feedback.html',{'i':i})

def complaint(request):
    un=request.session['un']
    sql4="select id from addcustomer where username='"+un+"'"
    i=dbconnection.onerow(sql4)
    d=datetime.now()
    if request.method=='POST':
        cus=request.POST['cus']
        cp=request.POST['cp']
        sql3="insert into `complaint`(`cus_id`,`date`,`complaint`) values('"+cus+"','"+str(d)+"','"+cp+"')"
        dbconnection.addrow(sql3)
        return render(request,'customer/complaint.html',{'i':i})
    return render(request,'customer/complaint.html',{'i':i})






