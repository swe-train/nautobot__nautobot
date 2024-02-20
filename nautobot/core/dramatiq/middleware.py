import logging
import sys
import traceback

from dramatiq.middleware import Middleware


LOGGER = logging.getLogger(__name__)


class NautobotJobsMiddleware(Middleware):

    @property
    def actor_options(self):
        """The set of options that may be configured on each actor.
        """
        return set([
            "approval_required",
            "description",
            "has_sensitive_variables",
            "hidden",
            "name",
            "soft_time_limit",
            "task_queues",  # TODO(john): figure this one out
            "time_limit",
        ])


class JobResultStateMiddleware(Middleware):
    """This middleware keeps track of task executions.
    """

    @staticmethod
    def get_jobresult_id(message):
        return message.options.get("nautobot_job_result_id", False)

    def before_process_message(self, broker, message):
        from nautobot.extras.models.jobs import JobResult, JobResultStatusChoices

        jobresult_id = self.get_jobresult_id(message)
        if jobresult_id:
            LOGGER.debug("Updating JobResult from message %r.", jobresult_id)
            jobresult = JobResult.objects.get(pk=jobresult_id)
            jobresult.set_status(JobResultStatusChoices.STATUS_RUNNING)
            jobresult.validated_save()

    def after_process_message(self, broker, message, *, result=None, exception=None, status=None):
        from nautobot.extras.models.jobs import JobResult, JobResultStatusChoices

        jobresult_id = self.get_jobresult_id(message)
        if jobresult_id:
            jobresult = JobResult.objects.get(pk=jobresult_id)
            if exception is not None:
                status = JobResultStatusChoices.STATUS_FAILED
                exc_type, exc_value, exc_traceback = sys.exc_info()
                formatted_exception = traceback.format_exception(
                    exception,
                    exc_value,
                    exc_traceback,
                    limit=30,
                )
                message.options["traceback"] = "".join(formatted_exception)
                jobresult.traceback = message.options["traceback"]

            elif status is None:
                status = JobResultStatusChoices.STATUS_COMPLETED

            LOGGER.debug("Updating JobResult from message %r.", jobresult_id)
            jobresult = JobResult.objects.get(pk=jobresult_id)
            jobresult.set_status(status)
            jobresult.validated_save()
