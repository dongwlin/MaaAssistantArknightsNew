from deps.binding.Python.maa.library import Library
from deps.binding.Python.maa.resource import Resource
from deps.binding.Python.maa.controller import AdbController
from deps.binding.Python.maa.maa import Maa

if __name__ == "__main__":
    Library.open("./deps/bin")

    resource = Resource()
    res_id = resource.post_path("./assets/resource/")
    resource.wait(res_id)

    controller = AdbController("adb", "127.0.0.1:16384", agent_path="./deps/share/MaaAgentBinary/")
    ctrl_id = controller.post_connection()
    controller.wait(ctrl_id)

    maa_inst = Maa()
    maa_inst.bind(resource, controller)

    if not maa_inst.inited():
        print("Failed to init MAA")
        exit(1)

    task_id = maa_inst.post_task("StartUp", {})
    maa_inst.wait(task_id)