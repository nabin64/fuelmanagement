
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, Hod_Views, Local_Views, Patrol_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),
    path('Hod/Home', Hod_Views.HOME, name='hod_home'),



    path('Hod/Add/Employee', Hod_Views.ADD_EMPLOYEE, name='add_employee'),
    path('Hod/View/Employee', Hod_Views.VIEW_EMPLOYEE, name='view_employee'),
    path('Hod/Employee/Edit/<str:id>',
         Hod_Views.EDIT_EMPLOYEE, name='edit_employee'),
    path('Hod/Employee/Update', Hod_Views.UPDATE_EMPLOYEE, name='update_employee'),


    path('Hod/Add/Department', Hod_Views.ADD_DEPARTMENT, name='add_department'),
    path('Hod/View/Department', Hod_Views.VIEW_DEPARTMENT, name='view_department'),


    path('Hod/Add/Petrolpump', Hod_Views.ADD_PETROLPUMP, name='add_petrolpump'),
    path('Hod/View/Patrolpump', Hod_Views.VIEW_PETROLPUMP, name='view_petrolpump'),



    path('Local/Add/Coupon/<str:id>', Local_Views.ADD_COUPON, name='add_coupon'),
    path('Hod/Issue/Coupon/', Hod_Views.ISSUE_COUPON, name='issue_coupon'),
    path('Hod/View/Coupon/', Hod_Views.VIEW_COUPON, name='view_coupon'),
    path('Hod/Print/Coupon/<str:id>', Hod_Views.PRINT_COUPON, name='print_coupon'),
    path('Hod/Print/Coupon/Home/Go', Hod_Views.PRINT_COUPON_HOME,
         name='print_coupon_home'),


    path('Hod/Report/Coupon/Employee/<str:id>',
         Hod_Views.REPORT_COUPON_EMPLOYEE, name='report_coupon'),
    path('Hod/Report/Coupon/Petrolpump/<str:id>',
         Hod_Views.REPORT_COUPON_PETROLPUMP, name='report_coupon_petrolpump'),

    path('Hod/Search/Coupon', Hod_Views.SEARCH_COUPON, name='search_coupon'),
    path('Hod/View/Request/Coupon/', Hod_Views.VIEW_REQUESTED_COUPON,
         name='view_request_coupon'),

    path('Hod/Search/Datewise/Coupon', Hod_Views.SEARCH_COUPON_DATEWISE,
         name='search_coupon_datewise'),






    # url for local level staff
    path('Local/Home', Local_Views.HOME, name='local_home'),
    path('Local/View/Coupon/', Local_Views.VIEW_COUPON, name='view_staff_coupon'),
    path('Local/Add/Coupon', Local_Views.STAFF_ADD_COUPON,
         name='local_staff_add_coupon'),
    path('Local/Issue/Coupon/', Local_Views.ISSUE_COUPON,
         name='issue_staff_coupon'),







    path('Patrol/Home', Patrol_Views.HOME, name='patrol_home'),





    path('base/', views.HOME, name="base"),




    # Local Level Url




    # ajax url

    path('ajax/load-district/', views.LOAD_DISTRICT,
         name='ajax_load_district'),
    path('ajax/load-local/', views.LOAD_LOCAL_LEVEL,
         name='ajax_load_local_level'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
