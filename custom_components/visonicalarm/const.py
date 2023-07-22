DOMAIN = "visonicalarm"
CONF_PANEL_ID = "panel_id"
CONF_PIN_REQUIRED_ARM = "pin_required_arm"
CONF_PIN_REQUIRED_DISARM = "pin_required_disarm"

PROCESS_TIMEOUT = 60
DEFAUL_SCAN_INTERVAL = 30

DATA = "data"
UPDATE_LISTENER = "update_listener"
VISONIC_PLATFORMS = ["alarm_control_panel", "sensor", "switch"]

PANELS = ["VISONIC_PANEL"]
CONTACT_SENSORS = ["CONTACT", "MC303_VANISH"]
MOTION_SENSORS = [
    "FLAT_PIR_SMART",
    "MOTION",
    "MOTION_DUAL",
    "MOTION_V_ANTIMASK",
    "MOTION_CAMERA",
    "CURTAIN",
]
OTHER_SENSORS = ["KEYFOB_ARM_LED", "OUTDOOR"]
SUPPORTED_SENSORS = [*PANELS, *CONTACT_SENSORS, *MOTION_SENSORS, *OTHER_SENSORS]

SENSOR_TYPE_FRIENDLY_NAME = {
    "CONTACT": "Contact Sensor",
    "MC303_VANISH": "Contact Sensor",
    "CURTAIN": "Curtain Motion Sensor",
    "FLAT_PIR_SMART": "Smart PIR Sensor",
    "MOTION": "Motion Sensor",
    "MOTION_DUAL": "Motion Dual Sensor",
    "MOTION_V_ANTIMASK": "Motion Sensor",
    "MOTION_CAMERA": "Motion Camera",
    "KEYFOB_ARM_LED": "Keyfob",
    "OUTDOOR": "Outdoor",
    "VISONIC_PANEL": "Alarm Panel",
}
