import os
import sys
import json
from datetime import datetime,timedelta
from bson import json_util 
from pymongo import MongoClient
import boto3
import botocore

bucket = 'tmp-test-kinesis'
def check_exists(bucket):
	s3 = boto3.resource('s3')
	exists = False
	try:
		# check bucket availabel
		s3.meta.client.head_bucket(Bucket=bucket)
	except botocore.exceptions.ClientError as e:
		exists = False
	else:
		exists = True

def create_bucket(bucket):
	# create bucket
	s3.create_bucket(Bucket=bucket)

def upload_s3(bucket, key, path_file):
	s3.Object(bucket, key).put(Body=open(path_file, 'rb'))

client = MongoClient('mongodb://localhost:27017')
db = client.fossil_q_stg

now = datetime.now()
# convert date string to datetime object
time = now - timedelta(days=57)
start = datetime(time.year, time.month, time.day, 0, 0, 0)
end = datetime(time.year, time.month, time.day, 23, 59, 59)

# # export data activity
# activites = db.Activity.find({'updatedAt': {'$lte': end, '$gte': start}})
# if activites.count > 0:
# 	with open(time.day + "_activity.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	steps	distance	calories	type	sourceType	sourceId	"\
# 			"ACL	uri	timeZone	date	intensity	startDate	endDate	createdAt	updatedAt")
# 		for activity in activites:
# 			record_file.write(activity['objectId'] +"	"+ activity['owner'] +"	"+ activity['steps']\
# 				+"	"+ activity['distance'] +"	"+ activity['calories'] +"	"+ activity['type']\
# 				+"	"+ activity['sourceType'] +"	"+ activity['sourceId'] +"	"+ activity['ACL']\
# 				+"	"+ activity['uri'] +"	"+ activity['timeZone'] +"	"+ activity['date']\
# 				+"	"+ activity['intensity'] +"	"+ activity['startDate'] +"	"+ activity['endDate']\
# 				+"	"+ activity['createdAt'] +"	"+ activity['updatedAt'] + "\n")

# # export data activity day summary
# act_day_summaries = db.ActivityDaySummary.find({'updatedAt': {'$lte': end, '$gte': start}})
# if act_day_summaries.count > 0:
# 	with open(time.day + "_activity_day_summary.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	date	goalSteps	totalSteps	totalDistance	totalCalories	totalActivities	"\
# 			"totalIntensityDistInStep	reachGoal	createdAt	updatedAt")
# 		for act_day_summary in act_day_summaries:
# 			record_file.write(act_day_summary['objectId'] +"	"+ act_day_summary['owner'] +"	"+ act_day_summary['date']\
# 				+"	"+ act_day_summary['goalSteps'] +"	"+ act_day_summary['totalSteps'] +"	"+ act_day_summary['totalDistance']\
# 				+"	"+ act_day_summary['totalCalories'] +"	"+ act_day_summary['totalActivities'] +"	"+ act_day_summary['totalIntensityDistInStep']\
# 				+"	"+ act_day_summary['reachGoal'] +"	"+ act_day_summary['createdAt'] +"	"+ act_day_summary['updatedAt'] + "\n")

# # export data activity setting
# act_settings = db.ActivitySetting.find({'updatedAt': {'$lte': end, '$gte': start}})
# if act_settings.count > 0:
# 	with open(time.day + "_activity_setting.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	currentGoalSteps	createdAt	updatedAt")
# 		for act_setting in act_settings:
# 			record_file.write(act_setting['objectId'] +"	"+ act_setting['owner'] +"	"+ act_setting['currentGoalSteps']\
# 				+"	"+ act_setting['createdAt'] +"	"+ act_setting['updatedAt'] + "\n")

# # export data activity statistic
# act_statistics = db.ActivityStatistic.find({'updatedAt': {'$lte': end, '$gte': start}})
# if act_statistics.count > 0:
# 	with open(time.day + "_activity_statistic.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	totalDistance	totalCalories	totalSteps"\
# 			"	totalActivities	totalDays	totalWeeks	totalIntensityDistInStep	bestDay"\
# 			"	createdAt	updatedAt")
# 		for act_statistic in act_statistics:
# 			record_file.write(act_statistic['objectId'] +"	"+ act_statistic['owner'] +"	"+ act_statistic['totalDistance']\
# 				+"	"+ act_statistic['totalCalories'] +"	"+ act_statistic['totalSteps'] +"	"+ act_statistic['totalActivities']\
# 				+"	"+ act_statistic['totalDays'] +"	"+ act_statistic['totalWeeks'] +"	"+ act_statistic['totalIntensityDistInStep']\
# 				+"	"+ act_statistic['bestDay'] +"	"+ act_statistic['createdAt'] +"	"+ act_statistic['updatedAt'] + "\n")

# # export data alarm
# alarms = db.Alarm.find({'updatedAt': {'$lte': end, '$gte': start}})
# if alarms.count > 0:
# 	with open(time.day + "_alarm.tsv", "w") as record_file:
# 		record_file.write("objectId	hour	minute	days	owner"\
# 			"	title	isRepeated	isActive	createdAt	updatedAt")
# 		for alarm in alarms:
# 			record_file.write(alarm['objectId'] +"	"+ alarm['hour'] +"	"+ alarm['minute']\
# 				+"	"+ alarm['days'] +"	"+ alarm['owner'] +"	"+ alarm['title']\
# 				+"	"+ alarm['isRepeated'] +"	"+ alarm['isActive']\
# 				+"	"+ alarm['createdAt'] +"	"+ alarm['updatedAt'] + "\n")

# # export data alarm setting
# alarm_settings = db.AlarmSetting.find({'updatedAt': {'$lte': end, '$gte': start}})
# if alarm_settings.count > 0:
# 	with open(time.day + "_alarm_setting.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	isEnabled	createdAt	updatedAt")
# 		for alarm_setting in alarm_settings:
# 			record_file.write(alarm_setting['objectId'] +"	"+ alarm_setting['owner'] +"	"+ alarm_setting['isEnabled']\
# 				+"	"+ alarm_setting['createdAt'] +"	"+ alarm_setting['updatedAt'] + "\n")

# # export data api del logs
# api_del_logs = db.APIDeleteLog.find({'updatedAt': {'$lte': end, '$gte': start}})
# if api_del_logs.count > 0:
# 	with open(time.day + "_api_del_log.tsv", "w") as record_file:
# 		record_file.write("objectId	operationObjectId	operationClass	operationType	"\
# 			"status	createdAt	updatedAt")
# 		for api_del_log in api_del_logs:
# 			record_file.write(api_del_log['objectId'] +"	"+ api_del_log['operationObjectId'] +"	"+ api_del_log['operationClass']\
# 				+"	"+ api_del_log['operationType'] +"	"+ api_del_log['status']\
# 				+"	"+ api_del_log['createdAt'] +"	"+ api_del_log['updatedAt'] + "\n")

# # export data curiosity challenge
# curiosity_challenges = db.CuriosityChallenge.find({'updatedAt': {'$lte': end, '$gte': start}})
# if curiosity_challenges.count > 0:
# 	with open(time.day + "_curiosity_challenge.tsv", "w") as record_file:
# 		record_file.write("objectId	challengeId	completedMask	startDay	"\
# 			"user	createdAt	updatedAt")
# 		for curiosity_challenge in curiosity_challenges:
# 			record_file.write(curiosity_challenge['objectId'] +"	"+ curiosity_challenge['challengeId'] +"	"+ curiosity_challenge['completedMask']\
# 				+"	"+ curiosity_challenge['startDay'] +"	"+ curiosity_challenge['user']\
# 				+"	"+ curiosity_challenge['createdAt'] +"	"+ curiosity_challenge['updatedAt'] + "\n")

# # export data curiosity photo
# curiosity_photos = db.CuriosityPhoto.find({'updatedAt': {'$lte': end, '$gte': start}})
# if curiosity_photos.count > 0:
# 	with open(time.day + "_curiosity_photo.tsv", "w") as record_file:
# 		record_file.write("objectId	caption	imageFile	challenge	day	"\
# 			"weekday	user	createdAt	updatedAt")
# 		for curiosity_photo in curiosity_photos:
# 			record_file.write(curiosity_photo['objectId'] +"	"+ curiosity_photo['caption'] +"	"+ curiosity_photo['imageFile']\
# 				+"	"+ curiosity_photo['challenge'] +"	"+ curiosity_photo['day'] +"	"+ curiosity_photo['weekday']\
# 				+"	"+ curiosity_photo['user'] +"	"+ curiosity_photo['createdAt'] +"	"+ curiosity_photo['updatedAt'] + "\n")

# # export data delete log
# del_logs = db.DeleteLog.find({'updatedAt': {'$lte': end, '$gte': start}})
# if del_logs.count > 0:
# 	with open(time.day + "_delete_log.tsv", "w") as record_file:
# 		record_file.write("objectId	caption	imageFile	challenge	day	"\
# 			"weekday	user	createdAt	updatedAt")
# 		for del_log in del_logs:
# 			record_file.write(del_logs['objectId'] +"	"+ del_logs['caption'] +"	"+ del_logs['imageFile']\
# 				+"	"+ del_log['challenge'] +"	"+ del_log['day'] +"	"+  del_log['weekday']\
# 				+"	"+ del_log['user'] +"	"+ del_log['createdAt'] +"	"+ del_log['updatedAt'] + "\n")

# # export data device
# devices = db.Device.find({'updatedAt': {'$lte': end, '$gte': start}})
# if devices.count > 0:
# 	with open(time.day + "_device.tsv", "w") as record_file:
# 		record_file.write("objectId	deviceId	hostOS	manufacturer	mac_address	firmwareRevision	hostSystemLocale	"\
# 			"hostMaker	productDisplayName	lastConnection	hardwareRevision	softwareRevision	hostOSVersion	"\
# 			"hostSystemLanguage	hostModel	sku	lastDisconnection	lastRecoveryModeStart	lastFirmwareUpdate	"\
# 			"lastRecoveryModeEnd	appRevision	hostOSName	wrist	deviceType	owner	createdAt	updatedAt")
# 		for device in devices:
# 			record_file.write(device['objectId'] +"	"+ device['deviceId'] +"	"+ device['hostOS'] +"	"+ device['manufacturer']\
# 				+"	"+ device['mac_address'] +"	"+ device['firmwareRevision'] +"	"+ device['hostSystemLocale']\
# 				+"	"+ device['hostMaker'] +"	"+ device['productDisplayName'] +"	"+ device['lastConnection']\
# 				+"	"+ device['hardwareRevision'] +"	"+ device['softwareRevision'] +"	"+ device['hostOSVersion']\
# 				+"	"+ device['hostSystemLanguage'] +"	"+ device['hostModel'] +"	"+ device['sku']\
# 				+"	"+ device['lastDisconnection'] +"	"+ device['lastRecoveryModeStart'] +"	"+ device['lastFirmwareUpdate']\
# 				+"	"+ device['lastRecoveryModeEnd'] +"	"+ device['appRevision'] +"	"+ device['hostOSName']\
# 				+"	"+ device['wrist'] +"	"+ device['deviceType'] +"	"+ device['owner'] +"	"+ device['createdAt']\
# 				+"	"+ device['updatedAt'] + "\n")

# # export data facebook auth
# facebook_auths = db.FacebookAuth.find({'updatedAt': {'$lte': end, '$gte': start}})
# if facebook_auths.count > 0:
# 	with open(time.day + "_facebook_auth.tsv", "w") as record_file:
# 		record_file.write("objectId	accessToken	uid	expirationDate	email	firstName	lastName	"\
# 			"middleName	name	gender	birthday	locale	createdAt	updatedAt")
# 		for fb_auth in facebook_auths:
# 			record_file.write(fb_auth['objectId'] +"	"+ fb_auth['accessToken'] +"	"+ fb_auth['uid']\
# 				+"	"+ fb_auth['expirationDate'] +"	"+ fb_auth['email'] +"	"+ fb_auth['firstName']\
# 				+"	"+ fb_auth['lastName'] +"	"+ fb_auth['middleName'] +"	"+ fb_auth['name'] +"	"+ fb_auth['gender']\
# 				+"	"+ fb_auth['birthday'] +"	"+ fb_auth['locale'] +"	"+ fb_auth['createdAt']\
# 				+"	"+ fb_auth['updatedAt'] + "\n")

# # export data firmware
# firmwares = db.Firmware.find({'updatedAt': {'$lte': end, '$gte': start}})
# if firmwares.count > 0:
# 	with open(time.day + "_firmware.tsv", "w") as record_file:
# 		record_file.write("objectId	deviceModel	versionNumber	downloadUrl	checksum	isLatest	minIOSVersion	"\
# 			"maxIOSVersion	minAndroidVersion	maxAndroidVersion	createdAt	updatedAt")
# 		for fw in firmwares:
# 			record_file.write(fw['objectId'] +"	"+ fw['deviceModel'] +"	"+ fw['versionNumber']\
# 				+"	"+ fw['downloadUrl'] +"	"+ fw['checksum'] +"	"+ fw['isLatest']\
# 				+"	"+ fw['minIOSVersion'] +"	"+ fw['maxIOSVersion'] +"	"+ fw['minAndroidVersion']\
# 				+"	"+ fw['maxAndroidVersion'] +"	"+ fw['createdAt'] +"	"+ fw['updatedAt'] + "\n")

# # export data ForgotPasswordRequest
# forgot_pw_requestes = db.ForgotPasswordRequest.find({'updatedAt': {'$lte': end, '$gte': start}})
# if forgot_pw_requestes.count > 0:
# 	with open(time.day + "_forgot_pw_request.tsv", "w") as record_file:
# 		record_file.write("objectId	email	expiration	createdAt	updatedAt")
# 		for forgot_pw_req in forgot_pw_requestes:
# 			record_file.write(forgot_pw_req['objectId'] +"	"+ forgot_pw_req['email'] +"	"+ forgot_pw_req['expiration']\
# 				+"	"+ forgot_pw_req['createdAt'] +"	"+ forgot_pw_req['updatedAt'] + "\n")

# # export data Goal
# goals = db.Goal.find({'updatedAt': {'$lte': end, '$gte': start}})
# if goals.count > 0:
# 	with open(time.day + "_goal.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	name	frequencyUnit	target	periodType	periodValue	startedAt	"\
# 			"endedAt	goalPhases	isActive	isDeleted	createdAt	updatedAt")
# 		for goal in goals:
# 			record_file.write(goal['objectId'] +"	"+ goal['owner'] +"	"+ goal['frequencyUnit'] +"	"+ goal['target']\
# 				+"	"+ goal['periodType'] +"	"+ goal['periodValue'] +"	"+ goal['startedAt'] +"	"+ goal['endedAt']\
# 				+"	"+ goal['goalPhases'] +"	"+ goal['isActive'] +"	"+ goal['isDeleted']\
# 				+"	"+ goal['createdAt'] +"	"+ goal['updatedAt'] + "\n")

# # export data GoalSummary
# goal_summaries = db.GoalSummary.find({'updatedAt': {'$lte': end, '$gte': start}})
# if goal_summaries.count > 0:
# 	with open(time.day + "_goal_summary.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	goalId	day	goalsMet	totalDuration	average	bestStreak	"\
# 			"createdAt	updatedAt")
# 		for goal_summary in goal_summaries:
# 			record_file.write(goal_summary['objectId'] +"	"+ goal_summary['owner'] +"	"+ goal_summary['goalId']\
# 				+"	"+ goal_summary['day'] +"	"+ goal_summary['goalsMet'] +"	"+ goal_summary['totalDuration']\
# 				+"	"+ goal_summary['average'] +"	"+ goal_summary['bestStreak']\
# 				+"	"+ goal_summary['createdAt'] +"	"+ goal_summary['updatedAt'] + "\n")

# # export data GoalTrackingEvent
# goal_tracking_events = db.GoalTrackingEvent.find({'updatedAt': {'$lte': end, '$gte': start}})
# if goal_tracking_events.count > 0:
# 	with open(time.day + "_goal_tracking_event.tsv", "w") as record_file:
# 		record_file.write("objectId	goalId	owner	day	trackedAt	targetCount	autoDetected	"\
# 			"createdAt	updatedAt")
# 		for goal_tracking_event in goal_tracking_events:
# 			record_file.write(goal_tracking_event['objectId'] +"	"+ goal_tracking_event['goalId'] +"	"+ goal_tracking_event['owner']\
# 				+"	"+ goal_tracking_event['day'] +"	"+ goal_tracking_event['trackedAt'] +"	"+ goal_tracking_event['targetCount']\
# 				+"	"+ goal_tracking_event['autoDetected']+"	"+ goal_tracking_event['createdAt'] +"	"+ goal_tracking_event['updatedAt'] + "\n")

# # export data GoogleAuth
# google_auths = db.GoogleAuth.find({'updatedAt': {'$lte': end, '$gte': start}})
# if google_auths.count > 0:
# 	with open(time.day + "_google_auth.tsv", "w") as record_file:
# 		record_file.write("objectId	exp	aud	email	iss	sub	iat	azp	name	picture	locale	emailVerified	"\
# 			"user	givenName	atHash	familyName	createdAt	updatedAt")
# 		for google_auth in google_auths:
# 			record_file.write(google_auth['objectId'] +"	"+ google_auth['exp'] +"	"+ google_auth['aud']\
# 				+"	"+ google_auth['email'] +"	"+ google_auth['iss'] +"	"+ google_auth['sub']\
# 				+"	"+ google_auth['iat']+"	"+ google_auth['azp'] +"	"+ google_auth['name']\
# 				+"	"+ google_auth['picture']+"	"+ google_auth['locale'] +"	"+ google_auth['emailVerified']\
# 				+"	"+ google_auth['user']+"	"+ google_auth['givenName'] +"	"+ google_auth['atHash']\
# 				+"	"+ google_auth['familyName']+"	"+ google_auth['createdAt'] +"	"+ google_auth['updatedAt'] + "\n")

# # export data Graph
# graphs = db.Graph.find({'updatedAt': {'$lte': end, '$gte': start}})
# if graphs.count > 0:
# 	with open(time.day + "_graph.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	steps	date	startDate	endDate	distance	calories	timeZone	"\
# 			"createdAt	updatedAt")
# 		for graph in graphs:
# 			record_file.write(graph['objectId'] +"	"+ graph['owner'] +"	"+ graph['steps']\
# 				+"	"+ graph['date'] +"	"+ graph['startDate'] +"	"+ graph['endDate']\
# 				+"	"+ graph['distance']+"	"+ graph['calories'] +"	"+ graph['timeZone']\
# 				+"	"+ graph['createdAt'] +"	"+ graph['updatedAt'] + "\n")

# # export data Installation
# installations = db.Installation.find({'updatedAt': {'$lte': end, '$gte': start}})
# if installations.count > 0:
# 	with open(time.day + "_installation.tsv", "w") as record_file:
# 		record_file.write("objectId	appVersion	installationId	badge	appMarketingVersion	appName	timeZone	model	"\
# 			"appIdentifier	deviceType	parseVersion	appBuildNumber	osVersion	localeIdentifier	"\
# 			"user	createdAt	updatedAt")
# 		for installation in installations:
# 			record_file.write(installation['objectId'] +"	"+ installation['appVersion'] +"	"+ installation['installationId']\
# 				+"	"+ installation['badge'] +"	"+ installation['appMarketingVersion'] +"	"+ installation['appName']\
# 				+"	"+ installation['timeZone']+"	"+ installation['model'] +"	"+ installation['appIdentifier']\
# 				+"	"+ installation['deviceType'] +"	"+ installation['parseVersion'] +"	"+ installation['appBuildNumber']\
# 				+"	"+ installation['osVersion'] +"	"+ installation['localeIdentifier'] +"	"+ installation['user']\
# 				+"	"+ installation['createdAt'] +"	"+ installation['updatedAt'] + "\n")

# # export data Mapping
# mappings = db.Mapping.find({'updatedAt': {'$lte': end, '$gte': start}})
# if mappings.count > 0:
# 	with open(time.day + "_mapping.tsv", "w") as record_file:
# 		record_file.write("objectId	deviceId	mode	gesture	action	extraInfo	createdAt	updatedAt")
# 		for mapping in mappings:
# 			record_file.write(mapping['objectId'] +"	"+ mapping['deviceId'] +"	"+ mapping['mode']\
# 				+"	"+ mapping['gesture'] +"	"+ mapping['action'] +"	"+ mapping['extraInfo']\
# 				+"	"+ mapping['createdAt'] +"	"+ mapping['updatedAt'] + "\n")

# # export data OperationLog
# operation_logs = db.OperationLog.find({'updatedAt': {'$lte': end, '$gte': start}})
# if operation_logs.count > 0:
# 	with open(time.day + "_operation_log.tsv", "w") as record_file:
# 		record_file.write("objectId	error	operationName	operationObjectId	createdAt	updatedAt")
# 		for operation_log in operation_logs:
# 			record_file.write(operation_log['objectId'] +"	"+ operation_log['error'] +"	"+ operation_log['operationName']\
# 				+"	"+ operation_log['operationObjectId'] +"	"+ operation_log['createdAt'] +"	"+ operation_log['updatedAt'] + "\n")

# # export data OTASession
# ota_sessions = db.OTASession.find({'updatedAt': {'$lte': end, '$gte': start}})
# if operation_logs.count > 0:
# 	with open(time.day + "_ota_session.tsv", "w") as record_file:
# 		record_file.write("objectId	uid	os	serialNumber	osVersion	deviceModel	sdkVersion	appVersion	startTime	"\
# 			"endTime	oldFirmware	newFirmware	otaPercent	retries	debugLog	isSuccess	serverTime	battery")
# 		for ota_session in ota_sessions:
# 			record_file.write(ota_session['objectId'] +"	"+ ota_session['uid'] +"	"+ ota_session['os']\
# 				+"	"+ ota_session['serialNumber'] +"	"+ ota_session['osVersion'] +"	"+ ota_session['deviceModel']\
# 				+"	"+ ota_session['sdkVersion'] +"	"+ ota_session['appVersion'] +"	"+ ota_session['startTime']\
# 				+"	"+ ota_session['endTime'] +"	"+ ota_session['oldFirmware'] +"	"+ ota_session['newFirmware']\
# 				+"	"+ ota_session['otaPercent'] +"	"+ ota_session['retries'] +"	"+ ota_session['debugLog']\
# 				+"	"+ ota_session['isSuccess'] +"	"+ ota_session['serverTime'] +"	"+ ota_session['battery'] + "\n")

# # export data PasswordResetToken
# pw_reset_tokens = db.PasswordResetToken.find({'updatedAt': {'$lte': end, '$gte': start}})
# if pw_reset_tokens.count > 0:
# 	with open(time.day + "_pw_reset_token.tsv", "w") as record_file:
# 		record_file.write("objectId	email	expiration	createdAt	updatedAt")
# 		for pw_reset_token in pw_reset_tokens:
# 			record_file.write(pw_reset_token['objectId'] +"	"+ pw_reset_token['email'] +"	"+ pw_reset_token['expiration']\
# 				+"	"+ pw_reset_token['createdAt'] +"	"+ pw_reset_token['updatedAt'] + "\n")

# # export data SecondTimeZone
# second_time_zones = db.SecondTimeZone.find({'updatedAt': {'$lte': end, '$gte': start}})
# if second_time_zones.count > 0:
# 	with open(time.day + "_second_time_zone.tsv", "w") as record_file:
# 		record_file.write("objectId	timeZoneId	timeZoneName	cityName	owner	rawOffset	isActive	createdAt	updatedAt")
# 		for second_time_zone in second_time_zones:
# 			record_file.write(second_time_zone['objectId'] +"	"+ second_time_zone['timeZoneId']\
# 				+"	"+ second_time_zone['timeZoneName'] +"	"+ second_time_zone['cityName']\
# 				+"	"+ second_time_zone['owner'] +"	"+ second_time_zone['rawOffset'] +"	"+ second_time_zone['isActive']\
# 				+"	"+ second_time_zone['createdAt'] +"	"+ second_time_zone['updatedAt'] + "\n")

# # export data SecondTimeZoneSetting
# second_time_zone_settings = db.SecondTimeZoneSetting.find({'updatedAt': {'$lte': end, '$gte': start}})
# if second_time_zone_settings.count > 0:
# 	with open(time.day + "_second_time_zone_setting.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	isEnabled	createdAt	updatedAt")
# 		for second_time_zone_setting in second_time_zone_settings:
# 			record_file.write(second_time_zone_setting['objectId'] +"	"+ second_time_zone_setting['owner']\
# 				+"	"+ second_time_zone_setting['isEnabled'] +"	"+ second_time_zone_setting['createdAt']\
# 				+"	"+ second_time_zone_setting['updatedAt'] + "\n")

# # export data SessionToken
# session_tokens = db.SessionToken.find({'updatedAt': {'$lte': end, '$gte': start}})
# if session_tokens.count > 0:
# 	with open(time.day + "_session_token.tsv", "w") as record_file:
# 		record_file.write("objectId	createdWith	restricted	installationId	expiresAt	user	createdAt	updatedAt")
# 		for session_token in session_tokens:
# 			record_file.write(session_token['objectId'] +"	"+ session_token['createdWith']\
# 				+"	"+ session_token['restricted'] +"	"+ session_token['installationId']\
# 				+"	"+ session_token['expiresAt'] +"	"+ session_token['user']\
# 				+"	"+ session_token['createdAt'] +"	"+ session_token['updatedAt'] + "\n")

# # export data SetupDeviceSession
# setup_device_sessions = db.SetupDeviceSession.find({'updatedAt': {'$lte': end, '$gte': start}})
# if setup_device_sessions.count > 0:
# 	with open(time.day + "_setup_device_session.tsv", "w") as record_file:
# 		record_file.write("objectId	uid	os	osVersion	deviceModel	sdkVersion	appVersion	devicesCount	setupResult	"\
# 			"serialNumber	firmware	startTime	endTime	debugLog	serverTime")
# 		for setup_device_session in setup_device_sessions:
# 			record_file.write(setup_device_session['objectId'] +"	"+ setup_device_session['uid']\
# 				+"	"+ setup_device_session['osVersion'] +"	"+ setup_device_session['deviceModel']\
# 				+"	"+ setup_device_session['sdkVersion'] +"	"+ setup_device_session['appVersion']\
# 				+"	"+ setup_device_session['devicesCount'] +"	"+ setup_device_session['setupResult']\
# 				+"	"+ setup_device_session['serialNumber'] +"	"+ setup_device_session['firmware']\
# 				+"	"+ setup_device_session['startTime'] +"	"+ setup_device_session['endTime']\
# 				+"	"+ setup_device_session['debugLog'] +"	"+ setup_device_session['serverTime'] + "\n")

# # export data SleepDaySummary
# sleep_day_summaries = db.SleepDaySummary.find({'updatedAt': {'$lte': end, '$gte': start}})
# if sleep_day_summaries.count > 0:
# 	with open(time.day + "_sleep_day_summary.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	date	goalMinutes	totalSleepMinutes	totalSleeps	totalSleepStateDistInMinute	"\
# 			"reachGoal	createdAt	updatedAt")
# 		for sleep_day_summary in sleep_day_summaries:
# 			record_file.write(sleep_day_summary['objectId'] +"	"+ sleep_day_summary['owner']\
# 				+"	"+ sleep_day_summary['date'] +"	"+ sleep_day_summary['goalMinutes']\
# 				+"	"+ sleep_day_summary['totalSleepMinutes'] +"	"+ sleep_day_summary['totalSleeps']\
# 				+"	"+ sleep_day_summary['totalSleepStateDistInMinute'] +"	"+ sleep_day_summary['reachGoal']\
# 				+"	"+ sleep_day_summary['createdAt'] +"	"+ sleep_day_summary['updatedAt'] + "\n")

# # export data SleepSession
# sleep_sessions = db.SleepSession.find({'updatedAt': {'$lte': end, '$gte': start}})
# if sleep_sessions.count > 0:
# 	with open(time.day + "_sleep_session.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	date	timezoneOffset	source	deviceSerialNumber	syncTime	bookmarkTime	"\
# 			"realStartTime	realEndTime	realSleepMinutes	realSleepStateDistInMinute	editedStartTime	editedEndTime	"\
# 			"editedSleepMinutes	editedSleepStateDistInMinute	normalizeSleepQuality	sleepStates	createdAt	updatedAt")
# 		for sleep_session in sleep_sessions:
# 			record_file.write(sleep_session['objectId'] +"	"+ sleep_session['owner']\
# 				+"	"+ sleep_session['date'] +"	"+ sleep_session['timezoneOffset']\
# 				+"	"+ sleep_session['source'] +"	"+ sleep_session['deviceSerialNumber']\
# 				+"	"+ sleep_session['syncTime'] +"	"+ sleep_session['bookmarkTime']\
# 				+"	"+ sleep_session['realStartTime'] +"	"+ sleep_session['realEndTime']\
# 				+"	"+ sleep_session['realSleepMinutes'] +"	"+ sleep_session['realSleepStateDistInMinute']\
# 				+"	"+ sleep_session['editedStartTime'] +"	"+ sleep_session['editedEndTime']\
# 				+"	"+ sleep_session['editedSleepMinutes'] +"	"+ sleep_session['editedSleepStateDistInMinute']\
# 				+"	"+ sleep_session['normalizeSleepQuality'] +"	"+ sleep_session['sleepStates']\
# 				+"	"+ sleep_session['createdAt'] +"	"+ sleep_session['updatedAt'] + "\n")

# # export data SleepSetting
# sleep_settings = db.SleepSetting.find({'updatedAt': {'$lte': end, '$gte': start}})
# if sleep_settings.count > 0:
# 	with open(time.day + "_sleep_setting.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	currentGoalMinutes	createdAt	updatedAt")
# 		for sleep_setting in sleep_settings:
# 			record_file.write(sleep_setting['objectId'] +"	"+ sleep_setting['owner']\
# 				+"	"+ sleep_setting['currentGoalMinutes'] +"	"+ sleep_setting['createdAt']\
# 				+"	"+ sleep_setting['updatedAt'] + "\n")

# # export data SleepStatistic
# sleep_statistics = db.SleepStatistic.find({'updatedAt': {'$lte': end, '$gte': start}})
# if sleep_statistics.count > 0:
# 	with open(time.day + "_sleep_statistic.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	totalDays	totalSleeps	totalSleepMinutes	totalSleepStateDistInMinute	"\
# 			"currentGoal	createdAt	updatedAt")
# 		for sleep_statistic in sleep_statistics:
# 			record_file.write(sleep_statistic['objectId'] +"	"+ sleep_statistic['owner']\
# 				+"	"+ sleep_statistic['totalDays'] +"	"+ sleep_statistic['totalSleeps']\
# 				+"	"+ sleep_statistic['totalSleepMinutes'] +"	"+ sleep_statistic['totalSleepStateDistInMinute']\
# 				+"	"+ sleep_statistic['currentGoal'] +"	"+ sleep_statistic['createdAt']\
# 				+"	"+ sleep_statistic['updatedAt'] + "\n")

# # export data SleepSummary
# sleep_summaries = db.SleepSummary.find({'updatedAt': {'$lte': end, '$gte': start}})
# if sleep_summaries.count > 0:
# 	with open(time.day + "_sleep_summary.tsv", "w") as record_file:
# 		record_file.write("objectId	owner	date	timezoneOffset	goalMinutes	sleepMinutes	sleepStateDistInMinute	"\
# 			"createdAt	updatedAt")
# 		for sleep_summary in sleep_summaries:
# 			record_file.write(sleep_summary['objectId'] +"	"+ sleep_summary['owner']\
# 				+"	"+ sleep_summary['date'] +"	"+ sleep_summary['timezoneOffset']\
# 				+"	"+ sleep_summary['goalMinutes'] +"	"+ sleep_summary['sleepMinutes']\
# 				+"	"+ sleep_summary['sleepStateDistInMinute'] +"	"+ sleep_summary['createdAt']\
# 				+"	"+ sleep_summary['updatedAt'] + "\n")

# # export data Subscription
# subscriptions = db.Subscription.find({'updatedAt': {'$lte': end, '$gte': start}})
# if subscriptions.count > 0:
# 	with open(time.day + "_subscriptions.tsv", "w") as record_file:
# 		record_file.write("objectId	subscriptionType	optIn	user	createdAt	updatedAt")
# 		for subscription in subscriptions:
# 			record_file.write(subscription['objectId'] +"	"+ subscription['subscriptionType']\
# 				+"	"+ subscription['optIn'] +"	"+ subscription['user']\
# 				+"	"+ subscription['createdAt'] +"	"+ subscription['updatedAt'] + "\n")

# # export data Summary
# summaries = db.Summary.find({'updatedAt': {'$lte': end, '$gte': start}})
# if summaries.count > 0:
# 	with open(time.day + "_summary.tsv", "w") as record_file:
# 		record_file.write("objectId	timeZoneName	calories	steps	distance	uri	stepGoal	day	month	year	"\
# 			"owner	createdAt	updatedAt")
# 		for summary in summaries:
# 			record_file.write(summary['objectId'] +"	"+ summary['timeZoneName']\
# 				+"	"+ summary['calories'] +"	"+ summary['steps']\
# 				+"	"+ summary['distance'] +"	"+ summary['uri']\
# 				+"	"+ summary['stepGoal'] +"	"+ summary['day']\
# 				+"	"+ summary['month'] +"	"+ summary['year']\
# 				+"	"+ summary['owner'] +"	"+ summary['createdAt']\
# 				+"	"+ summary['updatedAt'] + "\n")

# # export data SyncSession
# sync_sessions = db.SyncSession.find({'updatedAt': {'$lte': end, '$gte': start}})
# if summaries.count > 0:
# 	with open(time.day + "_sync_session.tsv", "w") as record_file:
# 		record_file.write("objectId	uid	serialNumber	firmware	os	osVersion	deviceModel	sdkVersion	appVersion	"\
# 			"calculationLibVersion	syncMode	activityPoint	postSyncActivityPoint	timezone	postSyncTimezone	"\
# 			"goal	postSyncGoal	clockState	postClockState	retries	failureReason	deviceIdentifier	battery	"\
# 			"activityTaggingState	alarm	inactiveNotificationState	callNotificationState	userInfo	isDataLoss	"\
# 			"isSuccess	clientIp	serverTime	clientType	sid	startTime	endTime	debugLog	preSyncStep	postSyncStep	"\
# 			"preSyncGoalInStep	postSyncGoalInStep	createdAt	updatedAt")
# 		for sync_session in sync_sessions:
# 			record_file.write(sync_session['objectId'] +"	"+ sync_session['uid'] +"	"+ sync_session['serialNumber']\
# 				+"	"+ sync_session['firmware'] +"	"+ sync_session['os'] +"	"+ sync_session['osVersion']\
# 				+"	"+ sync_session['deviceModel'] +"	"+ sync_session['sdkVersion'] +"	"+ sync_session['appVersion']\
# 				+"	"+ sync_session['calculationLibVersion'] +"	"+ sync_session['syncMode'] +"	"+ sync_session['activityPoint']\
# 				+"	"+ sync_session['postSyncActivityPoint'] +"	"+ sync_session['timezone'] +"	"+ sync_session['postSyncTimezone']\
# 				+"	"+ sync_session['goal'] +"	"+ sync_session['postSyncGoal'] +"	"+ sync_session['clockState']\
# 				+"	"+ sync_session['postClockState'] +"	"+ sync_session['retries'] +"	"+ sync_session['failureReason']\
# 				+"	"+ sync_session['deviceIdentifier'] +"	"+ sync_session['battery'] +"	"+ sync_session['activityTaggingState']\
# 				+"	"+ sync_session['alarm'] +"	"+ sync_session['inactiveNotificationState'] +"	"+ sync_session['callNotificationState']\
# 				+"	"+ sync_session['userInfo'] +"	"+ sync_session['isDataLoss'] +"	"+ sync_session['isSuccess']\
# 				+"	"+ sync_session['clientIp'] +"	"+ sync_session['serverTime'] +"	"+ sync_session['clientType']\
# 				+"	"+ sync_session['sid'] +"	"+ sync_session['startTime'] +"	"+ sync_session['endTime']\
# 				+"	"+ sync_session['debugLog'] +"	"+ sync_session['preSyncStep'] +"	"+ sync_session['postSyncStep']\
# 				+"	"+ sync_session['preSyncGoalInStep'] +"	"+ sync_session['postSyncGoalInStep'] +"	"+ sync_session['createdAt']\
# 				+"	"+ sync_session['updatedAt'] + "\n")

# export data User
users = db.User.find({'updatedAt': {'$lte': end, '$gte': start}})
if users.count > 0:
	with open(time.day + "_user.tsv", "w") as record_file:
		record_file.write("objectId	email	username	weightInGrams	heightInCentimeters	externalId	brand	authType	"\
			"unit	isCuriosityOnboardingComplete	isNotificationsOnboardingComplete	isActivityOnboardingComplete	"\
			"integrations	firstName	lastName	gender	birthday	registrationComplete	isOnboardingComplete	"\
			"activeDeviceId	sessionToken	perishableToken	diagnosticEnabled	emailProgress	profilePicture	"\
			"integrations	createdAt	updatedAt")
		for user in users:
			record_file.write(user['objectId'] +"	"+ user['email'] +"	"+ user['username']\
				+"	"+ user['weightInGrams'] +"	"+ user['heightInCentimeters'] +"	"+ user['externalId']\
				+"	"+ user['brand'] +"	"+ user['authType'] +"	"+ user['unit']\
				+"	"+ user['isCuriosityOnboardingComplete'] +"	"+ user['isNotificationsOnboardingComplete'] +"	"+ user['isActivityOnboardingComplete']\
				+"	"+ user['integrations'] +"	"+ user['firstName'] +"	"+ user['lastName']\
				+"	"+ user['gender'] +"	"+ user['birthday'] +"	"+ user['registrationComplete']\
				+"	"+ user['isOnboardingComplete'] +"	"+ user['activeDeviceId'] +"	"+ user['sessionToken']\
				+"	"+ user['perishableToken'] +"	"+ user['diagnosticEnabled'] +"	"+ user['emailProgress']\
				+"	"+ user['profilePicture'] +"	"+ user['integrations'] +"	"+ user['createdAt']\
				+"	"+ user['updatedAt'] + "\n")
