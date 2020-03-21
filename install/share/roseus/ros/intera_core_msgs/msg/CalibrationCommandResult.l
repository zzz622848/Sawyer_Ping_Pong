;; Auto-generated. Do not edit!


(when (boundp 'intera_core_msgs::CalibrationCommandResult)
  (if (not (find-package "INTERA_CORE_MSGS"))
    (make-package "INTERA_CORE_MSGS"))
  (shadow 'CalibrationCommandResult (find-package "INTERA_CORE_MSGS")))
(unless (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT")
  (make-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))

(in-package "ROS")
;;//! \htmlinclude CalibrationCommandResult.msg.html


(intern "*SUCCESS*" (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(shadow '*SUCCESS* (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(defconstant intera_core_msgs::CalibrationCommandResult::*SUCCESS* "Success")
(intern "*STOPPED*" (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(shadow '*STOPPED* (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(defconstant intera_core_msgs::CalibrationCommandResult::*STOPPED* "Stopped")
(intern "*GENERIC_FAILURE*" (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(shadow '*GENERIC_FAILURE* (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(defconstant intera_core_msgs::CalibrationCommandResult::*GENERIC_FAILURE* "calibrationFailure")
(intern "*INCOMPLETE*" (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(shadow '*INCOMPLETE* (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(defconstant intera_core_msgs::CalibrationCommandResult::*INCOMPLETE* "incomplete")
(intern "*GRIPPER_ON*" (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(shadow '*GRIPPER_ON* (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(defconstant intera_core_msgs::CalibrationCommandResult::*GRIPPER_ON* "cannotCalibrateWithGripper")
(intern "*TORQUES_EXCEEDED_THRESHOLD*" (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(shadow '*TORQUES_EXCEEDED_THRESHOLD* (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(defconstant intera_core_msgs::CalibrationCommandResult::*TORQUES_EXCEEDED_THRESHOLD* "torquesExceededThreshold")
(intern "*PLANNER_FAILURE*" (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(shadow '*PLANNER_FAILURE* (find-package "INTERA_CORE_MSGS::CALIBRATIONCOMMANDRESULT"))
(defconstant intera_core_msgs::CalibrationCommandResult::*PLANNER_FAILURE* "plannerFailure")
(defclass intera_core_msgs::CalibrationCommandResult
  :super ros::object
  :slots (_result _statusId ))

(defmethod intera_core_msgs::CalibrationCommandResult
  (:init
   (&key
    ((:result __result) nil)
    ((:statusId __statusId) "")
    )
   (send-super :init)
   (setq _result __result)
   (setq _statusId (string __statusId))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:statusId
   (&optional __statusId)
   (if __statusId (setq _statusId __statusId)) _statusId)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ;; string _statusId
    4 (length _statusId)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;; string _statusId
       (write-long (length _statusId) s) (princ _statusId s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _statusId
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _statusId (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get intera_core_msgs::CalibrationCommandResult :md5sum-) "42762277c2f2777e046b77cebb5b2b55")
(setf (get intera_core_msgs::CalibrationCommandResult :datatype-) "intera_core_msgs/CalibrationCommandResult")
(setf (get intera_core_msgs::CalibrationCommandResult :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# result
bool result
string statusId
# possible values for statusId are:
string SUCCESS=Success
string STOPPED=Stopped
string GENERIC_FAILURE=calibrationFailure
string INCOMPLETE=incomplete
string GRIPPER_ON=cannotCalibrateWithGripper
string TORQUES_EXCEEDED_THRESHOLD=torquesExceededThreshold
string PLANNER_FAILURE=plannerFailure



")



(provide :intera_core_msgs/CalibrationCommandResult "42762277c2f2777e046b77cebb5b2b55")

