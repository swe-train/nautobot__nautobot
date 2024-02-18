import dramatiq


# nautobot_task is used in a few places for non-job based background tasks
# we offer it in this way for backwards compatability
nautobot_task = dramatiq.actor
