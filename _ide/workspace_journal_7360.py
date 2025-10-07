# 2025-10-07T15:41:45.643941200
import vitis

client = vitis.create_client()
client.set_workspace(path="02_Vitis_workspace")

platform = client.get_component(name="01_freertos_platform")
status = platform.build()

comp = client.get_component(name="freertos_hello_world")
comp.build()

status = comp.clean()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

vitis.dispose()

