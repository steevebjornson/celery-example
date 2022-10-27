from tasks import add, tsum

def on_message(body):
    if "SUCCESS" not in body["status"]:
        print("task failed")
        return
    print(body["result"])

if __name__ == "__main__":
    print("running 'add' function as celery task")
    r = add.delay(1, 2)
    r.get(on_message=on_message)

    print("running 'tsum' function as celery task")
    r = tsum.delay(list(range(10)))
    r.get(on_message=on_message)
