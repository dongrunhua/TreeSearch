def load_intention(params):
    result = []

    if not isinstance(params, dict):
        return "数据错误"

    child_list = []

    for i in order_list[-1]:
        for k, v in i.items():
            child = v.get("child")

            if child:
                child_list.extend(child)

    for k, v in params.items():
        if k in child_list:
            num = 0
            parent = v.get("parent")

            for i in parent:
                if i not in save_list:
                    num += 1
                    break
            if num == 0:
                result.append({k: v})

    if result:
        for i in result:
            for k, v in i.items():
                save_list.append(k)
        order_list.append(result)

    if child_list:
        load_intention(params)


order_list = []
result = []
save_list = []


def main(params):

    global order_list,result,save_list
    order_list = []
    result = []
    save_list = []

    for k, v in params.items():
        if not v.get("parent"):
            result.append({k: v})
            save_list.append(k)

    order_list.append(result)
    load_intention(params)


    return order_list

