from __future__ import unicode_literals

from django.db import models

class TrainTrafficRequest(models.Model):
	MESSAGE = 'msg'
	STATION = 'st'
	ANNOUNCEMENT = 'ann'
	REQUEST_TYPES = (
		(MESSAGE, 'Message'),
		(STATION, 'Station'),
		(ANNOUNCEMENT, 'Announcement'),
	)
	created = models.DateTimeField(auto_now_add=True)
	requestType = models.CharField(choices=REQUEST_TYPES, default=STATION, max_length=100)
	station = models.CharField(max_length=100, blank=True, default='')
	owner = models.ForeignKey('auth.User', related_name='trainTrafficRequests')

	class Meta:
		ordering = ('created',)

