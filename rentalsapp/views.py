from django.shortcuts import render
from django.http import Http404
from rentalsapp.models import *

def index(request):
    items = Item.objects.exclude(amount=0)
    return render(request, 'rentalsapp/index.html',  {
        'items': items,
    })

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'rentalsapp/item_detail.html', {
        'item': item,
    })

def contracts(request):
    contracts = Contract.objects.exclude(erc_lastName='')
    return render(request, 'rentalsapp/contracts.html',  {
        'contracts': contracts,
    })

def contract_detail(request, id):
    try:
        contract = Contract.objects.get(id=id)
    except Contract.DoesNotExist:
        raise Http404('This contract item does not exist')
    return render(request, 'rentalsapp/contract_detail.html', {
        'contract': contract,
    })
