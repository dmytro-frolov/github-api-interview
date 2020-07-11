from django.http import JsonResponse


def logged(func):
    """
    To determine which method of connection used to github
    """

    def with_logging(*args, **kwargs):
        # todo: logging here
        print(f'Using {func.__name__} method')
        return func(*args, **kwargs)

    return with_logging


def to_json_resp(req_call):
    """
    This function checks result from github endpoint end returns result as jsonresp
    """
    def wrap(*args, **kwargs):
        #todo: logging and exception handler for json
        try:
            result = req_call(*args, **kwargs)
            js = result.json()
            status_code = result.status_code

            return JsonResponse(js, status=status_code, safe=False)

        except KeyError:
            print()
    return wrap