# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "")
  file(REMOVE_RECURSE
  "E:\\02_Projects\\02_Vitis_workspace\\01_freertos_platform\\zynq_fsbl\\zynq_fsbl_bsp\\include\\diskio.h"
  "E:\\02_Projects\\02_Vitis_workspace\\01_freertos_platform\\zynq_fsbl\\zynq_fsbl_bsp\\include\\ff.h"
  "E:\\02_Projects\\02_Vitis_workspace\\01_freertos_platform\\zynq_fsbl\\zynq_fsbl_bsp\\include\\ffconf.h"
  "E:\\02_Projects\\02_Vitis_workspace\\01_freertos_platform\\zynq_fsbl\\zynq_fsbl_bsp\\include\\sleep.h"
  "E:\\02_Projects\\02_Vitis_workspace\\01_freertos_platform\\zynq_fsbl\\zynq_fsbl_bsp\\include\\xilffs.h"
  "E:\\02_Projects\\02_Vitis_workspace\\01_freertos_platform\\zynq_fsbl\\zynq_fsbl_bsp\\include\\xilffs_config.h"
  "E:\\02_Projects\\02_Vitis_workspace\\01_freertos_platform\\zynq_fsbl\\zynq_fsbl_bsp\\include\\xilrsa.h"
  "E:\\02_Projects\\02_Vitis_workspace\\01_freertos_platform\\zynq_fsbl\\zynq_fsbl_bsp\\include\\xiltimer.h"
  "E:\\02_Projects\\02_Vitis_workspace\\01_freertos_platform\\zynq_fsbl\\zynq_fsbl_bsp\\include\\xtimer_config.h"
  "E:\\02_Projects\\02_Vitis_workspace\\01_freertos_platform\\zynq_fsbl\\zynq_fsbl_bsp\\lib\\libxilffs.a"
  "E:\\02_Projects\\02_Vitis_workspace\\01_freertos_platform\\zynq_fsbl\\zynq_fsbl_bsp\\lib\\libxilrsa.a"
  "E:\\02_Projects\\02_Vitis_workspace\\01_freertos_platform\\zynq_fsbl\\zynq_fsbl_bsp\\lib\\libxiltimer.a"
  )
endif()
