from django.urls import path
from . import views
urlpatterns=[ 
    path('',views.main),
    path('main',views.main),
    path('search',views.search),
    path('about',views.about),
    path('contact',views.contact),

    path('login',views.login),
    path('logout',views.logout),
    path('logstatus',views.logstatus),
    path('ahome',views.ahome),
    path('addcat',views.addcat),
    path('delcat',views.delcat),
    path('addcomp',views.addcomp),
    path('delcomp',views.delcomp),
    path('addsub',views.addsub),
    path('delsub',views.delsub),
    path('addstaff',views.addstaff),
    path('viewstaff',views.viewstaff),
    path('viewstaff2',views.viewstaff2),
    path('salary',views.salary),
    path('paidsalary',views.paidsalary),
    path('arequest',views.arequest),
    path('acpt',views.acpt),
    path('shome',views.shome),
    path('addcustomer',views.addcustomer),
   
    path('supdate',views.supdate),
    path('srequest',views.srequest),
    path('addstock',views.addstock),
    path('stock',views.stock),
    path('stockupd',views.stockupd),
    path('viewcustomer',views.viewcustomer),
    path('sprofile',views.sprofile),
    path('svcustomer',views.svcustomer),
    path('scustomer',views.scustomer),


  
    
    path('sale',views.sale),
    path('sale2',views.sale2),
    path('salarylist',views.salarylist),
    path('delete',views.delete),
    path('uprod',views.uprod),
    path('password',views.password),
    path('reset',views.reset),
    path('pasnew',views.pasnew),
    path('sumof',views.sumof),
    path('saledet',views.saledet),
    path('billsum',views.billsum),
    path('singlebill',views.singlebill),
    path('showbill',views.showbill),
    path('tencus',views.tencus),
    path('saledt',views.saledt),
    path('salert',views.salert),
    # path('salert2',views.salert2),
    path('saledtf',views.saledtf),
    path('uhome',views.uhome),
    path('uprod',views.uprod),
    path('feedback',views.feedback),
    path('complaint',views.complaint),
    path('billpurch',views.billpurch),
    path('billpurch2',views.billpurch2),
    path('dailyexp',views.dailyexp),
    path('fbview',views.fbview),
    path('cmview',views.cmview),





]