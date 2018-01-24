# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
import json
from igdb_api_python.igdb import igdb
igdb = igdb("KEY")

def index(request):
	return render(request, 'index.html')

def searchgames(request):
	key = request.GET.get('term', None)
	games = {}
	if key!=None:
		key = key.strip()
		#print key
		result = igdb.games({
		    'search': [key],
	    	'fields':['name'],
		    'limit': 10,
		})
		games = result.body
		# for game in games:
		# 	game['text'] = game.pop('name')
	
	return HttpResponse(json.dumps({'status': "success", "games": games}), content_type="application/json")

def searchplatforms(request):
	result = igdb.platforms({
	    'filters' :{
	        "[name][eq]": "PC (Microsoft Windows)",
	    },
	    'order':["name:asc"],
	    'fields':['name'],
	})

	platforms = result.body

	result = igdb.platforms({
	    'filters': {
	        "[generation][eq]": 7,
	    },
	    'order':["name:asc"],
	    'fields':['name'],
	})

	platforms += result.body

	result = igdb.platforms({
	    'filters': {
	        "[generation][eq]": 8,
	    },
	    'order':["name:asc"],
	    'fields':['name'],
	})

	platforms += result.body
	return HttpResponse(json.dumps({'status': "success", 'platforms': platforms}), content_type="application/json")