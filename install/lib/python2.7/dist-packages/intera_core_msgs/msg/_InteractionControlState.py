# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from intera_core_msgs/InteractionControlState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class InteractionControlState(genpy.Message):
  _md5sum = "f3fbd4a2356cb48da2df759db65614d8"
  _type = "intera_core_msgs/InteractionControlState"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """## InteractionControlState.msg ##
# Internal state of the interaction controller including
# whether the controller is active, current impedence parameters,
# and the commanded endpoint forces by the interaction controller

Header header

bool      interaction_control_active

## Impedance Control Parameters
float64[] K_impedance
float64[] D_impedance

## Force Control Parameters
# Vector of forces (wrench) (N and Nm) commanded by the interaction controller
# for the endpoint.
float64[] endpoint_force_command

string endpoint_name
bool in_endpoint_frame
bool disable_damping_in_force_control
bool disable_reference_resetting

## Parameters for Constrained Zero-G Behaviors
# Please refer to InteractionControlCommand.msg for more details
bool rotations_for_constrained_zeroG
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  __slots__ = ['header','interaction_control_active','K_impedance','D_impedance','endpoint_force_command','endpoint_name','in_endpoint_frame','disable_damping_in_force_control','disable_reference_resetting','rotations_for_constrained_zeroG']
  _slot_types = ['std_msgs/Header','bool','float64[]','float64[]','float64[]','string','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,interaction_control_active,K_impedance,D_impedance,endpoint_force_command,endpoint_name,in_endpoint_frame,disable_damping_in_force_control,disable_reference_resetting,rotations_for_constrained_zeroG

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(InteractionControlState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.interaction_control_active is None:
        self.interaction_control_active = False
      if self.K_impedance is None:
        self.K_impedance = []
      if self.D_impedance is None:
        self.D_impedance = []
      if self.endpoint_force_command is None:
        self.endpoint_force_command = []
      if self.endpoint_name is None:
        self.endpoint_name = ''
      if self.in_endpoint_frame is None:
        self.in_endpoint_frame = False
      if self.disable_damping_in_force_control is None:
        self.disable_damping_in_force_control = False
      if self.disable_reference_resetting is None:
        self.disable_reference_resetting = False
      if self.rotations_for_constrained_zeroG is None:
        self.rotations_for_constrained_zeroG = False
    else:
      self.header = std_msgs.msg.Header()
      self.interaction_control_active = False
      self.K_impedance = []
      self.D_impedance = []
      self.endpoint_force_command = []
      self.endpoint_name = ''
      self.in_endpoint_frame = False
      self.disable_damping_in_force_control = False
      self.disable_reference_resetting = False
      self.rotations_for_constrained_zeroG = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_B().pack(self.interaction_control_active))
      length = len(self.K_impedance)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.K_impedance))
      length = len(self.D_impedance)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.D_impedance))
      length = len(self.endpoint_force_command)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.endpoint_force_command))
      _x = self.endpoint_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_4B().pack(_x.in_endpoint_frame, _x.disable_damping_in_force_control, _x.disable_reference_resetting, _x.rotations_for_constrained_zeroG))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 1
      (self.interaction_control_active,) = _get_struct_B().unpack(str[start:end])
      self.interaction_control_active = bool(self.interaction_control_active)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.K_impedance = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.D_impedance = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.endpoint_force_command = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.endpoint_name = str[start:end].decode('utf-8')
      else:
        self.endpoint_name = str[start:end]
      _x = self
      start = end
      end += 4
      (_x.in_endpoint_frame, _x.disable_damping_in_force_control, _x.disable_reference_resetting, _x.rotations_for_constrained_zeroG,) = _get_struct_4B().unpack(str[start:end])
      self.in_endpoint_frame = bool(self.in_endpoint_frame)
      self.disable_damping_in_force_control = bool(self.disable_damping_in_force_control)
      self.disable_reference_resetting = bool(self.disable_reference_resetting)
      self.rotations_for_constrained_zeroG = bool(self.rotations_for_constrained_zeroG)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_B().pack(self.interaction_control_active))
      length = len(self.K_impedance)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.K_impedance.tostring())
      length = len(self.D_impedance)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.D_impedance.tostring())
      length = len(self.endpoint_force_command)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.endpoint_force_command.tostring())
      _x = self.endpoint_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_4B().pack(_x.in_endpoint_frame, _x.disable_damping_in_force_control, _x.disable_reference_resetting, _x.rotations_for_constrained_zeroG))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 1
      (self.interaction_control_active,) = _get_struct_B().unpack(str[start:end])
      self.interaction_control_active = bool(self.interaction_control_active)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.K_impedance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.D_impedance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.endpoint_force_command = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.endpoint_name = str[start:end].decode('utf-8')
      else:
        self.endpoint_name = str[start:end]
      _x = self
      start = end
      end += 4
      (_x.in_endpoint_frame, _x.disable_damping_in_force_control, _x.disable_reference_resetting, _x.rotations_for_constrained_zeroG,) = _get_struct_4B().unpack(str[start:end])
      self.in_endpoint_frame = bool(self.in_endpoint_frame)
      self.disable_damping_in_force_control = bool(self.disable_damping_in_force_control)
      self.disable_reference_resetting = bool(self.disable_reference_resetting)
      self.rotations_for_constrained_zeroG = bool(self.rotations_for_constrained_zeroG)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_4B = None
def _get_struct_4B():
    global _struct_4B
    if _struct_4B is None:
        _struct_4B = struct.Struct("<4B")
    return _struct_4B