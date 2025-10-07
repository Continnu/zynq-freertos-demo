# 2025-10-07T18:21:36.227956100
import vitis

client = vitis.create_client()
client.set_workspace(path="02_Vitis_workspace")

platform = client.get_component(name="01_freertos_platform")
status = platform.update_hw(hw_design = "$COMPONENT_LOCATION/../../01_Vivado/01_zynq_test/vitis/system_wrapper.xsa")

status = platform.build()

comp = client.get_component(name="freertos_hello_world")
status = comp.clean()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.update_hw(hw_design = "$COMPONENT_LOCATION/../../01_Vivado/01_zynq_test/vitis/system_wrapper.xsa")

status = platform.update_hw(hw_design = "$COMPONENT_LOCATION/../../01_Vivado/01_zynq_test/vitis/system_wrapper.xsa")

status = platform.update_hw(hw_design = "$COMPONENT_LOCATION/../../01_Vivado/01_zynq_test/vitis/system_wrapper.xsa")

status = platform.update_hw(hw_design = "$COMPONENT_LOCATION/../../01_Vivado/01_zynq_test/vitis/system_wrapper.xsa")

status = platform.build()

status = platform.build()

status = comp.clean()

status = platform.build()

comp.build()

status = comp.clean()

status = platform.build()

comp.build()

client.delete_component(name="01_freertos_platform")

client.delete_component(name="01_freertos_platform")

client.delete_component(name="freertos_hello_world")

client.delete_component(name="componentName")

advanced_options = client.create_advanced_options_dict(dt_overlay="0")

platform = client.create_platform_component(name = "01_freertos_platform",hw_design = "$COMPONENT_LOCATION/../../01_Vivado/01_zynq_test/vitis/system_wrapper.xsa",os = "freertos",cpu = "ps7_cortexa9_0",domain_name = "freertos_ps7_cortexa9_0",generate_dtb = False,advanced_options = advanced_options)

status = platform.build()

comp = client.create_app_component(name="01_freertos_helloworld",platform = "$COMPONENT_LOCATION/../01_freertos_platform/export/01_freertos_platform/01_freertos_platform.xpfm",domain = "freertos_ps7_cortexa9_0")

comp = client.create_app_component(name="01_freertos_hello_world",platform = "$COMPONENT_LOCATION/../01_freertos_platform/export/01_freertos_platform/01_freertos_platform.xpfm",domain = "freertos_ps7_cortexa9_0",template = "freertos_hello_world")

client.delete_component(name="01_freertos_helloworld")

comp = client.get_component(name="01_freertos_hello_world")
status = comp.clean()

status = platform.build()

comp.build()

status = platform.update_hw(hw_design = "$COMPONENT_LOCATION/../../01_Vivado/01_zynq_test/vitis/system_wrapper.xsa")

status = platform.build()

status = comp.clean()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

