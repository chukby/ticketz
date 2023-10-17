import uuid
from django.db import models
from users.models import User


class Ticket(models.Model):
    TICKET_STATE = (
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('pending', 'Pending'),
    )
    ticket_number = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User,
                                    on_delete=models.DO_NOTHING,
                                    null=True,
                                    blank=True)
    date_accepted = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    is_resolved = models.BooleanField(default=False)
    date_closed = models.DateTimeField(null=True, blank=True)
    closed_by = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='closed_by')
    ticket_state = models.CharField(max_length=12, choices=TICKET_STATE)

    def __str__(self):
        return self.title
