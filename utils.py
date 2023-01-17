def user_request(request : str):
    request_list = request.split(" ")
    return request_list

def request_analyses(request):
    request_list = user_request(request)
    from_ = ''
    to_ = ''
    title = ''
    quantity = 0
    for ind in range(len(request_list)):
        if request_list[ind] == "склад":
            if request_list[ind-1] in ['в', 'на']:
                to_ = "store"
            elif request_list[ind-1] in ['с', 'из', 'со']:
                from_ = "store"
        elif request_list[ind] == "магазин":
            if request_list[ind-1] in ['в', 'на']:
                to_ = "shop"
            elif request_list[ind-1] in ['с', 'из', 'со']:
                from_ = "shop"
        elif request_list[ind].isdigit():
            title = request_list[ind+1]
            quantity = request_list[ind]

    return from_, to_, title, quantity