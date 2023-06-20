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
    
print("async manage lots of messages")
task_queue = []
for i in range(10):
    task_queue.append(add.delay(i, i))

results = []
while task_queue:
    task = task_queue.pop()
    if task.ready():
        print(f"task: {task.id} ready")
        results.append(task.get())
        continue
    print(f"task: {task.id} not ready--returning to queue")
    task_queue.append(task)

[print(result) for result in results]

