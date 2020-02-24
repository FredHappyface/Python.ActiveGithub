#!/usr/bin/env python3

import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR) + "/lib")

from githubREST import getRepoTraffic
import githubGraph
import json
from os.path import exists
import utils

def mergeDataWithJson(repoName, trafficType):
	if exists("userReposTraffic.json"):
		userReposTraffic = json.loads(open("userReposTraffic.json", "r").read())
	else:
		utils.logPrint("userReposTraffic.json does not exist - creating", "warning")
		userReposTraffic = {}
	if repoName not in userReposTraffic:
		utils.logPrint("{} does not exist - creating" .format(repoName), "warning")
		userReposTraffic[repoName] = {}
	if trafficType not in userReposTraffic[repoName]:
		utils.logPrint("{} does not exist - creating" .format(trafficType), "warning")
		userRepoTrafficType = [{'timestamp': '2000-01-01T00:00:00Z', 'uniques': 0}]
	else:
		userRepoTrafficType = userReposTraffic[repoName][trafficType]

	days = getRepoTraffic(repoName, trafficType)[trafficType]
	for day in days:
		if utils.getDatetime(
			userRepoTrafficType[-1]["timestamp"]) < utils.getDatetime(day["timestamp"]):
			userRepoTrafficType.append({'timestamp': day["timestamp"], 'uniques': day["uniques"]})

	userReposTraffic[repoName][trafficType] = userRepoTrafficType
	with open("userReposTraffic.json", "w") as f:
		json.dump(userReposTraffic, f)


def getJsonData(repoName, trafficType):
	userRepoTraffic = json.loads(open("userReposTraffic.json", "r").read())[repoName][trafficType]
	returnData = 0
	for trafficEntity in userRepoTraffic:
		returnData += trafficEntity["uniques"]
	return returnData



username, lifespan = utils.getUsernameAndLifespan()
sourceRepos = githubGraph.getListOfUserRepos(username, "repositories")
sortRepos = []
for repoData in sourceRepos:
	repositoryShortName = repoData["name"]
	repositoryName = username+"/"+repositoryShortName
	"""Forks
	"""
	aliveForks, _ = githubGraph.getListOfAliveForks(repoData, lifespan, enableNewer=False)
	"""Stars
	"""
	stars = githubGraph.getStargazerCount(username, repositoryShortName)
	"""Clones
	"""
	mergeDataWithJson(repositoryName, "clones")
	clones = getJsonData(repositoryName, "clones")
	"""Views
	"""
	mergeDataWithJson(repositoryName, "views")
	views = getJsonData(repositoryName, "views")
	score = len(aliveForks) * 8 + stars * 4 + clones * 2 + views
	sortRepos.append((score,
	("[\033[91mArchived\033[00m] " if repoData["isArchived"] else "") + repositoryName,
	len(aliveForks), stars, clones, views))


def getKey(item):
	return item[0]

sortedRepos = sorted(sortRepos, key=getKey, reverse=True)

for repoData in sortedRepos:
	utils.logPrint("{}: score={} ({}:{}:{}:{})"
	.format(repoData[1], repoData[0], repoData[2], repoData[3],
	repoData[4], repoData[5]), "info")
