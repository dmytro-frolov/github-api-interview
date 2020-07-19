import logging
from json.decoder import JSONDecodeError

from django.http import JsonResponse

log = logging.getLogger(__name__)


def logged(func):
    """
    To determine which method of connection used to github
    """

    def with_logging(*args, **kwargs):
        log.info(f'Using {func.__name__} method')
        return func(*args, **kwargs)

    return with_logging


def to_json_resp(req_call):
    """
    This function checks result from github endpoint end returns result as jsonresp
    """
    def wrap(*args, **kwargs):
        try:
            result = req_call(*args, **kwargs)
            result_json = result.json()

            return JsonResponse(result_json, status=result.status_code, safe=False)

        except (JSONDecodeError, KeyError):
            log.error(f'error {result.text}')
            return JsonResponse({'error': result.text}, status=400, safe=False)

    return wrap
