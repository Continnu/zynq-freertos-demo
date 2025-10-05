# 2025-10-04T15:18:48.980494300
import vitis

client = vitis.create_client()
client.set_workspace(path="02_Vitis_workspace")

advanced_options = client.create_advanced_options_dict(dt_overlay="0")

platform = client.create_platform_component(name = "01_freertos_platform",hw_design = "$COMPONENT_LOCATION/../../01_Vivado/01_zynq_test/vitis/system_wrapper.xsa",os = "freertos",cpu = "ps7_cortexa9_0",domain_name = "freertos_ps7_cortexa9_0",generate_dtb = False,advanced_options = advanced_options)

comp = client.create_app_component(name="freertos_app_test",platform = "$COMPONENT_LOCATION/../01_freertos_platform/export/01_freertos_platform/01_freertos_platform.xpfm",domain = "freertos_ps7_cortexa9_0")

comp = client.get_component(name="freertos_app_test")
status = comp.clean()

platform = client.get_component(name="01_freertos_platform")
status = platform.build()

comp.build()

client.delete_component(name="freertos_app_test")

client.delete_component(name="componentName")

comp = client.create_app_component(name="01_hello_world",platform = "$COMPONENT_LOCATION/../01_freertos_platform/export/01_freertos_platform/01_freertos_platform.xpfm",domain = "freertos_ps7_cortexa9_0")

comp = client.get_component(name="01_hello_world")
status = comp.clean()

status = comp.clean()

client.delete_component(name="01_hello_world")

comp = client.create_app_component(name="freertos_hello_world",platform = "$COMPONENT_LOCATION/../01_freertos_platform/export/01_freertos_platform/01_freertos_platform.xpfm",domain = "freertos_ps7_cortexa9_0",template = "freertos_hello_world")

comp = client.get_component(name="freertos_hello_world")
status = comp.clean()

status = platform.build()

comp.build()

