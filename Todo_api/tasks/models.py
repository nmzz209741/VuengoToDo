from django.db import models

class Task(models.Model):
  TODO = 'todo'
  IN_PROGRESS = 'in_progress'
  DONE = 'done'

  STATUS_CHOICES = (
    (TODO, 'Todo'),
    (IN_PROGRESS, 'In Progress'),
    (DONE, 'Done')
  )

  title = models.CharField(max_length=255, blank=False)
  status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=TODO)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)