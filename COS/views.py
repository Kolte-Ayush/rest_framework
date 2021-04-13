from pprint import pprint
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from bsedata.bse import BSE
# from rest_framework.response import Response
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from oauth2_provider.contrib.rest_framework import (
    OAuth2Authentication,
    TokenMatchesOASRequirements,
)
from oauth2_provider.models import AccessToken, Application


def action(request, page, action=""):
    print("------------------> 1")
    ctlName = page + "Ctl()"
    ctlObj = eval(ctlName)
    return ctlObj.execute(request)


def stock(request):
    try:
        b = BSE()
        b = BSE(update_codes=True)
        tl = b.topLosers()
        tg = b.topGainers()
        get_all = b.getScripCodes()
        return render(request, "StockHome.html", {"gainer": tg, "looser": tl, "getAll": get_all})
        # return JsonResponse(get_all)
    except:
        return HttpResponse("Please Check your Internet Connection")
    # b = BSE(update_codes=True)
    # tl = b.topLosers()
    # tg = b.topGainers()
    # stock_list = b.getScripCodes()
    # t = tuple(stock_list.items())
    # page = request.GET.get('page', 1)
    # paginator = Paginator(t, 8)
    # try:
    #     get_all = paginator.page(page)
    # except PageNotAnInteger:
    #     get_all = paginator.page(1)
    # except EmptyPage:
    #     get_all = paginator.page(paginator.num_pages)
    # return render(request, "StockHome.html", {"gainer": tg, "looser": tl, 'getAll': get_all})


# class AuthToken(APIView):
#     authentication_classes = [OAuth2Authentication]
#     permission_classes = [TokenMatchesOASRequirements]
#     @staticmethod
#     def get(self, request):
#         return "dadad"
class TokenAuth(APIView):
    permission_classes = IsAuthenticated,

    def get(self):
        return "Hello"
