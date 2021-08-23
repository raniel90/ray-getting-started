import time
import ray
import datetime

ray.init()

time_before = datetime.datetime.now()


@ray.remote
def get_products():
    print("Getting products on database...")

    time.sleep(10)
    return ["maçã", "banana"]


@ray.remote
def get_target_public():
    print("Getting target_public on database...")

    time.sleep(20)
    return ["Público 1", "Público 2", "Público 3"]


products_remote = get_products.remote()
target_public_remote = get_target_public.remote()

products_response = ray.get(products_remote)
target_public_response = ray.get(target_public_remote)

print(f"products_response: {products_response}")
print(f"target_public_response: {target_public_response}")

time_after = datetime.datetime.now()
diff_time = time_after - time_before


print(f"Execution Time: {diff_time.seconds} seconds")
