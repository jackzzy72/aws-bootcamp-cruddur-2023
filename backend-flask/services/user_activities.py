import os
from datetime import datetime, timedelta, timezone
# import XRay SDK libraries
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from lib.db import db

class UserActivities:
  # def __init__(self, request):
  #       #self.xray_recorder = xray_recorder
  #       self.request = request
  
  def run(user_handle):
    # try:
    #   # Start a segment
    #   parent_subsegment = xray_recorder.begin_subsegment('user_activities_start')
    #   parent_subsegment.put_annotation('url', self.request.url)  
    #   model = {
    #     'errors': None,
    #     'data': None
    #   }

    #   now = datetime.now(timezone.utc).astimezone()

    #   if user_handle == None or len(user_handle) < 1:
    #     model['errors'] = ['blank_user_handle']
    #   else:
    #     try:
    #       # Start a subsegment
    #       subsegment = xray_recorder.begin_subsegment('user_activities_nested_subsegment')
    #       now = datetime.now() 
    #       results = [{
    #         'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
    #         'handle':  'Andrew Brown',
    #         'message': 'Cloud is fun!',
    #         'created_at': (now - timedelta(days=1)).isoformat(),
    #         'expires_at': (now + timedelta(days=31)).isoformat()
    #       }]
    #       model['data'] = results
    #       xray_dict['results'] = len(model['data'])
    #       subsegment.put_metadata('results', xray_dict, 'user_activities')
    #     except Exception as e:
    #       # Raise the error in the segment
    #       raise e
    #     finally:  
    #       xray_recorder.end_subsegment()
    # except Exception as e:
    #   # Raise the error in the segment
    #   raise e
    # finally:  
    #   # Close the segment
    #   xray_recorder.end_subsegment()
        model = {
            'errors': None,
            'data': None
        }
        if user_handle == None or len(user_handle) < 1:
            model['errors'] = ['blank_user_handle']
        else:
            print("else:")
            sql = db.template('users', 'show')
            results = db.query_object_json(sql, {'handle': user_handle})
            model['data'] = results

        return model