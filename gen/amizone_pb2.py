# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: amizone.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.type import date_pb2 as google_dot_type_dot_date__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ramizone.proto\x12\x1ago_amizone.server.proto.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/date.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\x0e\n\x0c\x45mptyMessage\"=\n\x14\x43lassScheduleRequest\x12%\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\x04\x64\x61te\"3\n\tCourseRef\x12\x12\n\x04\x63ode\x18\x01 \x01(\tR\x04\x63ode\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"0\n\x0bSemesterRef\x12!\n\x0csemester_ref\x18\x01 \x01(\tR\x0bsemesterRef\"<\n\nAttendance\x12\x1a\n\x08\x61ttended\x18\x01 \x01(\x05R\x08\x61ttended\x12\x12\n\x04held\x18\x02 \x01(\x05R\x04held\"-\n\x05Marks\x12\x12\n\x04have\x18\x01 \x01(\x02R\x04have\x12\x10\n\x03max\x18\x02 \x01(\x02R\x03max\"\x8a\x02\n\x06\x43ourse\x12\x37\n\x03ref\x18\x01 \x01(\x0b\x32%.go_amizone.server.proto.v1.CourseRefR\x03ref\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x46\n\nattendance\x18\x03 \x01(\x0b\x32&.go_amizone.server.proto.v1.AttendanceR\nattendance\x12H\n\x0einternal_marks\x18\x04 \x01(\x0b\x32!.go_amizone.server.proto.v1.MarksR\rinternalMarks\x12!\n\x0csyllabus_doc\x18\x05 \x01(\tR\x0bsyllabusDoc\"G\n\x07\x43ourses\x12<\n\x07\x63ourses\x18\x01 \x03(\x0b\x32\".go_amizone.server.proto.v1.CourseR\x07\x63ourses\"\x99\x01\n\x10\x41ttendanceRecord\x12\x46\n\nattendance\x18\x01 \x01(\x0b\x32&.go_amizone.server.proto.v1.AttendanceR\nattendance\x12=\n\x06\x63ourse\x18\x02 \x01(\x0b\x32%.go_amizone.server.proto.v1.CourseRefR\x06\x63ourse\"[\n\x11\x41ttendanceRecords\x12\x46\n\x07records\x18\x01 \x03(\x0b\x32,.go_amizone.server.proto.v1.AttendanceRecordR\x07records\"\xbc\x02\n\x0eScheduledClass\x12=\n\x06\x63ourse\x18\x01 \x01(\x0b\x32%.go_amizone.server.proto.v1.CourseRefR\x06\x63ourse\x12\x39\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x18\n\x07\x66\x61\x63ulty\x18\x04 \x01(\tR\x07\x66\x61\x63ulty\x12\x12\n\x04room\x18\x05 \x01(\tR\x04room\x12K\n\nattendance\x18\x08 \x01(\x0e\x32+.go_amizone.server.proto.v1.AttendanceStateR\nattendance\"X\n\x10ScheduledClasses\x12\x44\n\x07\x63lasses\x18\x01 \x03(\x0b\x32*.go_amizone.server.proto.v1.ScheduledClassR\x07\x63lasses\"\xbf\x01\n\x11\x41mizoneDiaryEvent\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x1f\n\x0b\x63ourse_code\x18\x02 \x01(\tR\ncourseCode\x12\x1f\n\x0b\x63ourse_name\x18\x03 \x01(\tR\ncourseName\x12\x18\n\x07\x66\x61\x63ulty\x18\x04 \x01(\tR\x07\x66\x61\x63ulty\x12\x12\n\x04room\x18\x05 \x01(\tR\x04room\x12\x14\n\x05start\x18\x06 \x01(\tR\x05start\x12\x10\n\x03\x65nd\x18\x07 \x01(\tR\x03\x65nd\"\x92\x01\n\rScheduledExam\x12=\n\x06\x63ourse\x18\x01 \x01(\x0b\x32%.go_amizone.server.proto.v1.CourseRefR\x06\x63ourse\x12.\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x04time\x12\x12\n\x04mode\x18\x03 \x01(\tR\x04mode\"l\n\x13\x45xaminationSchedule\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12?\n\x05\x65xams\x18\x02 \x03(\x0b\x32).go_amizone.server.proto.v1.ScheduledExamR\x05\x65xams\"\xe2\x02\n\x07Profile\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12+\n\x11\x65nrollment_number\x18\x02 \x01(\tR\x10\x65nrollmentNumber\x12K\n\x13\x65nrollment_validity\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x12\x65nrollmentValidity\x12\x14\n\x05\x62\x61tch\x18\x04 \x01(\tR\x05\x62\x61tch\x12\x18\n\x07program\x18\x05 \x01(\tR\x07program\x12>\n\rdate_of_birth\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teOfBirth\x12\x1f\n\x0b\x62lood_group\x18\x07 \x01(\tR\nbloodGroup\x12$\n\x0eid_card_number\x18\x08 \x01(\tR\x0cidCardNumber\x12\x12\n\x04uuid\x18\t \x01(\tR\x04uuid\"0\n\x08Semester\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03ref\x18\x02 \x01(\tR\x03ref\"R\n\x0cSemesterList\x12\x42\n\tsemesters\x18\x01 \x03(\x0b\x32$.go_amizone.server.proto.v1.SemesterR\tsemesters\"`\n\x0bWifiMacInfo\x12\x1c\n\taddresses\x18\x01 \x03(\tR\taddresses\x12\x14\n\x05slots\x18\x02 \x01(\x05R\x05slots\x12\x1d\n\nfree_slots\x18\x03 \x01(\x05R\tfreeSlots\"4\n\x18\x44\x65registerWifiMacRequest\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\"Y\n\x16RegisterWifiMacRequest\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12%\n\x0eoverride_limit\x18\x02 \x01(\x08R\roverrideLimit\"q\n\x1a\x46illFacultyFeedbackRequest\x12\x16\n\x06rating\x18\x01 \x01(\x05R\x06rating\x12!\n\x0cquery_rating\x18\x02 \x01(\x05R\x0bqueryRating\x12\x18\n\x07\x63omment\x18\x03 \x01(\tR\x07\x63omment\"<\n\x1b\x46illFacultyFeedbackResponse\x12\x1d\n\nfilled_for\x18\x01 \x01(\x05R\tfilledFor*L\n\x0f\x41ttendanceState\x12\x0b\n\x07PENDING\x10\x00\x12\x0b\n\x07PRESENT\x10\x01\x12\n\n\x06\x41\x42SENT\x10\x02\x12\x06\n\x02NA\x10\x03\x12\x0b\n\x07INVALID\x10\x04\x32\xbb\x0c\n\x0e\x41mizoneService\x12\x84\x01\n\rGetAttendance\x12(.go_amizone.server.proto.v1.EmptyMessage\x1a-.go_amizone.server.proto.v1.AttendanceRecords\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/api/v1/attendance\x12\xb6\x01\n\x10GetClassSchedule\x12\x30.go_amizone.server.proto.v1.ClassScheduleRequest\x1a,.go_amizone.server.proto.v1.ScheduledClasses\"B\x82\xd3\xe4\x93\x02<\x12:/api/v1/class_schedule/{date.year}/{date.month}/{date.day}\x12\x8b\x01\n\x0fGetExamSchedule\x12(.go_amizone.server.proto.v1.EmptyMessage\x1a/.go_amizone.server.proto.v1.ExaminationSchedule\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/api/v1/exam_schedule\x12}\n\x0cGetSemesters\x12(.go_amizone.server.proto.v1.EmptyMessage\x1a(.go_amizone.server.proto.v1.SemesterList\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/api/v1/semesters\x12\x82\x01\n\nGetCourses\x12\'.go_amizone.server.proto.v1.SemesterRef\x1a#.go_amizone.server.proto.v1.Courses\"&\x82\xd3\xe4\x93\x02 \x12\x1e/api/v1/courses/{semester_ref}\x12{\n\x11GetCurrentCourses\x12(.go_amizone.server.proto.v1.EmptyMessage\x1a#.go_amizone.server.proto.v1.Courses\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/api/v1/courses\x12}\n\x0eGetUserProfile\x12(.go_amizone.server.proto.v1.EmptyMessage\x1a#.go_amizone.server.proto.v1.Profile\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/api/v1/user_profile\x12}\n\x0eGetWifiMacInfo\x12(.go_amizone.server.proto.v1.EmptyMessage\x1a\'.go_amizone.server.proto.v1.WifiMacInfo\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/api/v1/wifi_mac\x12\x8c\x01\n\x0fRegisterWifiMac\x12\x32.go_amizone.server.proto.v1.RegisterWifiMacRequest\x1a(.go_amizone.server.proto.v1.EmptyMessage\"\x1b\x82\xd3\xe4\x93\x02\x15:\x01*\"\x10/api/v1/wifi_mac\x12\x97\x01\n\x11\x44\x65registerWifiMac\x12\x34.go_amizone.server.proto.v1.DeregisterWifiMacRequest\x1a(.go_amizone.server.proto.v1.EmptyMessage\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/api/v1/wifi_mac/{address}\x12\xb2\x01\n\x13\x46illFacultyFeedback\x12\x36.go_amizone.server.proto.v1.FillFacultyFeedbackRequest\x1a\x37.go_amizone.server.proto.v1.FillFacultyFeedbackResponse\"*\x82\xd3\xe4\x93\x02$:\x01*\"\x1f/api/v1/faculty/feedback/submitB\xe2\x03Z2github.com/ditsuke/go-amizone/server/gen/go/api_v1\x92\x41\xaa\x03\x12\x8b\x01\n\x0b\x41mizone API\"1\n\x07\x64itsuke\x12\x13https://ditsuke.com\x1a\x11hello@ditsuke.com*B\n\x07GPL-2.0\x12\x37https://github.com/ditsuke/go-amizone/blob/main/LICENSE2\x05\x30.6.0\x1a\x0f\x61mizone.fly.dev*\x02\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonRP\n\x03\x34\x30\x33\x12I\nGReturned when the user does not have permission to access the resource.Z;\n9\n\tBasicAuth\x12,\x08\x01\x12(Valid auth credentials for s.amizone.edub\x12\n\x10\n\tBasicAuth\x12\x03\n\x01*r>\n\x15More about go-amizone\x12%https://github.com/ditsuke/go-amizoneb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'amizone_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/ditsuke/go-amizone/server/gen/go/api_v1\222A\252\003\022\213\001\n\013Amizone API\"1\n\007ditsuke\022\023https://ditsuke.com\032\021hello@ditsuke.com*B\n\007GPL-2.0\0227https://github.com/ditsuke/go-amizone/blob/main/LICENSE2\0050.6.0\032\017amizone.fly.dev*\002\001\0022\020application/json:\020application/jsonRP\n\003403\022I\nGReturned when the user does not have permission to access the resource.Z;\n9\n\tBasicAuth\022,\010\001\022(Valid auth credentials for s.amizone.edub\022\n\020\n\tBasicAuth\022\003\n\001*r>\n\025More about go-amizone\022%https://github.com/ditsuke/go-amizone'
  _AMIZONESERVICE.methods_by_name['GetAttendance']._options = None
  _AMIZONESERVICE.methods_by_name['GetAttendance']._serialized_options = b'\202\323\344\223\002\024\022\022/api/v1/attendance'
  _AMIZONESERVICE.methods_by_name['GetClassSchedule']._options = None
  _AMIZONESERVICE.methods_by_name['GetClassSchedule']._serialized_options = b'\202\323\344\223\002<\022:/api/v1/class_schedule/{date.year}/{date.month}/{date.day}'
  _AMIZONESERVICE.methods_by_name['GetExamSchedule']._options = None
  _AMIZONESERVICE.methods_by_name['GetExamSchedule']._serialized_options = b'\202\323\344\223\002\027\022\025/api/v1/exam_schedule'
  _AMIZONESERVICE.methods_by_name['GetSemesters']._options = None
  _AMIZONESERVICE.methods_by_name['GetSemesters']._serialized_options = b'\202\323\344\223\002\023\022\021/api/v1/semesters'
  _AMIZONESERVICE.methods_by_name['GetCourses']._options = None
  _AMIZONESERVICE.methods_by_name['GetCourses']._serialized_options = b'\202\323\344\223\002 \022\036/api/v1/courses/{semester_ref}'
  _AMIZONESERVICE.methods_by_name['GetCurrentCourses']._options = None
  _AMIZONESERVICE.methods_by_name['GetCurrentCourses']._serialized_options = b'\202\323\344\223\002\021\022\017/api/v1/courses'
  _AMIZONESERVICE.methods_by_name['GetUserProfile']._options = None
  _AMIZONESERVICE.methods_by_name['GetUserProfile']._serialized_options = b'\202\323\344\223\002\026\022\024/api/v1/user_profile'
  _AMIZONESERVICE.methods_by_name['GetWifiMacInfo']._options = None
  _AMIZONESERVICE.methods_by_name['GetWifiMacInfo']._serialized_options = b'\202\323\344\223\002\022\022\020/api/v1/wifi_mac'
  _AMIZONESERVICE.methods_by_name['RegisterWifiMac']._options = None
  _AMIZONESERVICE.methods_by_name['RegisterWifiMac']._serialized_options = b'\202\323\344\223\002\025:\001*\"\020/api/v1/wifi_mac'
  _AMIZONESERVICE.methods_by_name['DeregisterWifiMac']._options = None
  _AMIZONESERVICE.methods_by_name['DeregisterWifiMac']._serialized_options = b'\202\323\344\223\002\034*\032/api/v1/wifi_mac/{address}'
  _AMIZONESERVICE.methods_by_name['FillFacultyFeedback']._options = None
  _AMIZONESERVICE.methods_by_name['FillFacultyFeedback']._serialized_options = b'\202\323\344\223\002$:\001*\"\037/api/v1/faculty/feedback/submit'
  _globals['_ATTENDANCESTATE']._serialized_start=2835
  _globals['_ATTENDANCESTATE']._serialized_end=2911
  _globals['_EMPTYMESSAGE']._serialized_start=180
  _globals['_EMPTYMESSAGE']._serialized_end=194
  _globals['_CLASSSCHEDULEREQUEST']._serialized_start=196
  _globals['_CLASSSCHEDULEREQUEST']._serialized_end=257
  _globals['_COURSEREF']._serialized_start=259
  _globals['_COURSEREF']._serialized_end=310
  _globals['_SEMESTERREF']._serialized_start=312
  _globals['_SEMESTERREF']._serialized_end=360
  _globals['_ATTENDANCE']._serialized_start=362
  _globals['_ATTENDANCE']._serialized_end=422
  _globals['_MARKS']._serialized_start=424
  _globals['_MARKS']._serialized_end=469
  _globals['_COURSE']._serialized_start=472
  _globals['_COURSE']._serialized_end=738
  _globals['_COURSES']._serialized_start=740
  _globals['_COURSES']._serialized_end=811
  _globals['_ATTENDANCERECORD']._serialized_start=814
  _globals['_ATTENDANCERECORD']._serialized_end=967
  _globals['_ATTENDANCERECORDS']._serialized_start=969
  _globals['_ATTENDANCERECORDS']._serialized_end=1060
  _globals['_SCHEDULEDCLASS']._serialized_start=1063
  _globals['_SCHEDULEDCLASS']._serialized_end=1379
  _globals['_SCHEDULEDCLASSES']._serialized_start=1381
  _globals['_SCHEDULEDCLASSES']._serialized_end=1469
  _globals['_AMIZONEDIARYEVENT']._serialized_start=1472
  _globals['_AMIZONEDIARYEVENT']._serialized_end=1663
  _globals['_SCHEDULEDEXAM']._serialized_start=1666
  _globals['_SCHEDULEDEXAM']._serialized_end=1812
  _globals['_EXAMINATIONSCHEDULE']._serialized_start=1814
  _globals['_EXAMINATIONSCHEDULE']._serialized_end=1922
  _globals['_PROFILE']._serialized_start=1925
  _globals['_PROFILE']._serialized_end=2279
  _globals['_SEMESTER']._serialized_start=2281
  _globals['_SEMESTER']._serialized_end=2329
  _globals['_SEMESTERLIST']._serialized_start=2331
  _globals['_SEMESTERLIST']._serialized_end=2413
  _globals['_WIFIMACINFO']._serialized_start=2415
  _globals['_WIFIMACINFO']._serialized_end=2511
  _globals['_DEREGISTERWIFIMACREQUEST']._serialized_start=2513
  _globals['_DEREGISTERWIFIMACREQUEST']._serialized_end=2565
  _globals['_REGISTERWIFIMACREQUEST']._serialized_start=2567
  _globals['_REGISTERWIFIMACREQUEST']._serialized_end=2656
  _globals['_FILLFACULTYFEEDBACKREQUEST']._serialized_start=2658
  _globals['_FILLFACULTYFEEDBACKREQUEST']._serialized_end=2771
  _globals['_FILLFACULTYFEEDBACKRESPONSE']._serialized_start=2773
  _globals['_FILLFACULTYFEEDBACKRESPONSE']._serialized_end=2833
  _globals['_AMIZONESERVICE']._serialized_start=2914
  _globals['_AMIZONESERVICE']._serialized_end=4509
# @@protoc_insertion_point(module_scope)
