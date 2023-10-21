from deps.binding.Python.maa.library import Library
from deps.binding.Python.maa.resource import Resource
from deps.binding.Python.maa.common import Status
import sys

if __name__ == "__main__":
    Library.open("./deps/bin")

    resource = Resource()
    res_id = resource.post_path("./assets/resource/")
    result = resource.wait(res_id)

    if result == Status.success:
        print("success")
    elif result == Status.failure:
        print("failure")
        sys.exit(1)
    
    print("pipeline is ok")
