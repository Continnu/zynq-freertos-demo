# 2025-10-04T14:39:23.105437300
import vitis

client = vitis.create_client()
client.set_workspace(path="02_Vitis_workspace")

advanced_options = client.create_advanced_options_dict(dt_overlay="0")

platform = client.create_platform_component(name = "01_freertos",hw_design = "$COMPONENT_LOCATION/../../01_Vivado/01_zynq_test/vitis/system_wrapper.xsa",os = "freertos",cpu = "ps7_cortexa9_0",domain_name = "freertos_ps7_cortexa9_0",generate_dtb = False,advanced_options = advanced_options)

vitis.dispose()

vitis.dispose()

