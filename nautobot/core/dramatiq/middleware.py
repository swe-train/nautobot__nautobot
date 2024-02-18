from dramatiq.middleware import Middleware


class NautobotJobsMiddleware(Middleware):

    @property
    def actor_options(self):
        """The set of options that may be configured on each actor.
        """
        return set([
            "name",
            "has_sensitive_variables",
            "soft_time_limit",
            "time_limit",
        ])

