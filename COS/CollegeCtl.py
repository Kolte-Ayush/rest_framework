from django.shortcuts import render

# from .Baseservice import BaseCtl
# from .models import College
#
#
# class CollegeCtl(BaseCtl):
#
#     def submit(self, request, params={}):
#         pass
#
#     def display(self, request, **kwargs):
#         if request.GET:
#             query = request.GET['collegeName']
#             context = str(query)
#             if context:
#                 data = College.objects.filter(collegeName="collegeName")
#                 return render(request, "list.html", {"pageList": data})
#             else:
#                 data = College.objects.all()
#                 return render(request, "list.html", {"pageList": data})
#         else:
#             data = College.objects.all()
#             return render(request, "list.html", {"pageList": data})
