freeze ("$(PORT_DIR)/modules")
freeze("$(MPY_DIR)/drivers/onewire")
freeze("$(MPY_DIR)/drivers/dht", "dht.py")
include("$(MPY_DIR)/extmod/uasyncio/manifest.py")
include("$(MPY_DIR)/drivers/neopixel/manifest.py")
freeze ("$(MPY_LIB_DIR)/", "lsm6dsox.py")
freeze ("$(MPY_LIB_DIR)/", "ble_advertising.py")
