def simple_middleware(get_response):
    print("Setup")

    def middleware(request):
        key = 'viewed_pages_' + request.path
        request.session[key] = request.session.get(key, 0) + 1
        request.view_count = request.session[key]

        response = get_response(request)

        return response
    
    return middleware