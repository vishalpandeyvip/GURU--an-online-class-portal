from django.urls import path,include
from .views import *
from django_email_verification import urls as mail_urls

urlpatterns = [
    path('',home,name="home"),
    path('homepage/',homepage,name="homepage"),
    path('email/', include(mail_urls)),
    path('<unique_id>/',subjects,name="subjects"),

    path('<unique_id>/<int:subject_id>/',subject_page,name="subject_page"),
    path('<unique_id>/<int:subject_id>/delete/',delete_subject,name="delete_subject"),

    path('<unique_id>/<subject_id>/resource/',resource,name="resources"),
    path('<unique_id>/<subject_id>/<id>/read/',read_note,name="read_note"),
    path('<unique_id>/<subject_id>/<id>/resource/update/',resource_update,name="update_resource"),
    path('<unique_id>/<subject_id>/<id>/resource/delete/',resource_delete,name="delete_resource"),
    
    path('<unique_id>/<subject_id>/announcement/',announcement,name="announcement"),
    path('<unique_id>/<subject_id>/<id>/announcement/',announcement_page,name="announcement_page"),
    path('<unique_id>/<subject_id>/<id>/announcement/update/',announcement_update,name="update_announcement"),
    path('<unique_id>/<subject_id>/<id>/announcement/delete/',announcement_delete,name="delete_announcement"),

    path('<unique_id>/<subject_id>/assignments/',assignment,name="assignments"),
    path('<unique_id>/<subject_id>/<id>/assignment/',assignment_page,name="assignment_page"),
    path('<unique_id>/<subject_id>/<id>/assignment/update/',assignment_update,name="update_assignment"),
    path('<unique_id>/<subject_id>/<id>/assignment/delete/',assignment_delete,name="delete_assignment"),

    path('<unique_id>/<subject_id>/this_subject/',this_subject,name="this_subject")
]