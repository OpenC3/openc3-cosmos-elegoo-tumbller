set_line_delay(0)

class Tumbller:
  def __init__(self):
    self.motion = False
    self.turning = False
    self.direction = None
    self.keypad_direction = None
    self.left_x = None
    self.left_y = None
    self.right_x = None
    self.right_y = None
    self.triangle = None
    self.circle = None
    self.cross = None
    self.square = None
    self.r3 = None
    self.l3 = None
    self.options = None
    self.share = None
    self.r2 = None
    self.l2 = None
    self.r1 = None
    self.l1 = None
    self.pad = None
    self.home = None

  def update_state(self):
    values = get_tlm_values([
      "DUALSENSE__BTSTATE__DIRECTION__CONVERTED",
      "DUALSENSE__BTSTATE__LEFT_X__CONVERTED",
      "DUALSENSE__BTSTATE__LEFT_Y__CONVERTED",
      "DUALSENSE__BTSTATE__RIGHT_X__CONVERTED",
      "DUALSENSE__BTSTATE__RIGHT_Y__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_TRIANGLE__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_CIRCLE__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_CROSS__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_SQUARE__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_R3__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_L3__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_OPTIONS__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_SHARE__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_R2__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_L2__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_R1__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_L1__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_PAD__CONVERTED",
      "DUALSENSE__BTSTATE__BUTTON_HOME__CONVERTED",
    ])

    self.prev_keypad_direction = self.keypad_direction
    self.prev_left_x = self.left_x
    self.prev_left_y = self.left_y
    self.prev_right_x = self.right_x
    self.prev_right_y = self.right_y
    self.prev_triangle = self.triangle
    self.prev_circle = self.circle
    self.prev_cross = self.cross
    self.prev_square = self.square
    self.prev_r3 = self.r3
    self.prev_l3 = self.l3
    self.prev_options = self.options
    self.prev_share = self.share
    self.prev_r2 = self.r2
    self.prev_l2 = self.l2
    self.prev_r1 = self.r1
    self.prev_l1 = self.l1
    self.prev_pad = self.pad
    self.prev_home = self.home

    self.keypad_direction = values[0][0]
    self.left_x = values[1][0]
    self.left_y = values[2][0]
    self.right_x = values[3][0]
    self.right_y = values[4][0]
    self.triangle = values[5][0]
    self.circle = values[6][0]
    self.cross = values[7][0]
    self.square = values[8][0]
    self.r3 = values[9][0]
    self.l3 = values[10][0]
    self.options = values[11][0]
    self.share = values[12][0]
    self.r2 = values[13][0]
    self.l2 = values[14][0]
    self.r1 = values[15][0]
    self.l1 = values[16][0]
    self.pad = values[17][0]
    self.home = values[18][0]

  def handle_buttons(self):
    if self.triangle == "ON" and self.prev_triangle != "ON":
      cmd("TUMBLLER STAND_UP")

    if self.cross == "ON" and self.prev_cross != "ON":
      cmd("TUMBLLER FALL_DOWN")

    if self.square == "ON" and self.prev_square != "ON":
      cmd("TUMBLLER LED_DOWN")

    if self.circle == "ON" and self.prev_circle != "ON":
      cmd("TUMBLLER LED_UP")

    if self.l3 == "ON" and self.prev_l3 != "ON":
      cmd("TUMBLLER FOLLOW_MODE")

    if self.r3 == "ON" and self.prev_r3 != "ON":
      cmd("TUMBLLER OBSTACLE_MODE")

    if self.l1 == "ON" and self.prev_l1 != "ON":
      cmd("TUMBLLER LED_OFF")

    if self.r1 == "ON" and self.prev_r1 != "ON":
      cmd("TUMBLLER LED_MID")

    if self.pad == "ON" and self.prev_pad != "ON":
      cmd("TUMBLLER LED_NEXT_MODE")

  def joystick_direction(self, left_right, up_down):
    up = False
    down = False
    left = False
    right = False

    if up_down < 100:
      up = True
    elif up_down > 150:
      down = True
    if left_right < 100:
      left = True
    elif left_right > 150:
      right = True

    if up:
      if left:
        return "UP_LEFT"
      elif right:
        return "UP_RIGHT"
      else:
        return "UP"
    elif down:
      if left:
        return "DOWN_LEFT"
      elif right:
        return "DOWN_RIGHT"
      else:
        return "DOWN"
    elif left:
      return "LEFT"
    elif right:
      return "RIGHT"

    return "NONE"

  def move_direction(self, direction):
    match direction:
      case "NONE":
        if self.direction != "NONE":
          cmd("TUMBLLER STOP")
        self.motion = False
        self.turning = False
      case "UP":
        if self.direction != "UP":
          if self.turning:
            cmd("TUMBLLER STOP")
          cmd("TUMBLLER FORWARD")
        self.motion = True
        self.turning = False
      case "UP_LEFT":
        if self.direction != "UP_LEFT":
          cmd("TUMBLLER FORWARD")
          cmd("TUMBLLER LEFT")
        self.motion = True
        self.turning = True
      case "UP_RIGHT":
        if self.direction != "UP_RIGHT":
          cmd("TUMBLLER FORWARD")
          cmd("TUMBLLER RIGHT")
        self.motion = True
        self.turning = True
      case "DOWN":
        if self.direction != "DOWN":
          if self.turning:
            cmd("TUMBLLER STOP")
          cmd("TUMBLLER BACKWARD")
        self.motion = True
        self.turning = False
      case "DOWN_LEFT":
        if self.direction != "DOWN_LEFT":
          cmd("TUMBLLER BACKWARD")
          cmd("TUMBLLER LEFT")
        self.motion = True
        self.turning = True
      case "DOWN_RIGHT":
        if self.direction != "DOWN_RIGHT":
          cmd("TUMBLLER BACKWARD")
          cmd("TUMBLLER RIGHT")
        self.motion = True
        self.turning = True
      case "LEFT":
        if self.direction != "LEFT":
          if self.motion:
            cmd("TUMBLLER STOP")
          cmd("TUMBLLER LEFT")
        self.motion = False
        self.turning = True
      case "RIGHT":
        if self.direction != "RIGHT":
          if self.motion:
            cmd("TUMBLLER STOP")
          cmd("TUMBLLER RIGHT")
        self.motion = False
        self.turning = True

    self.direction = direction

  def run(self):
    while True:
      wait(0.05)
      self.update_state()

      # Handle Direction Keypad
      direction = self.keypad_direction
      if direction == "NONE":
        direction = self.joystick_direction(self.left_x, self.left_y)
      if direction == "NONE":
        direction = self.joystick_direction(self.right_x, self.right_y)

      self.move_direction(direction)
      self.handle_buttons()

Tumbller().run()