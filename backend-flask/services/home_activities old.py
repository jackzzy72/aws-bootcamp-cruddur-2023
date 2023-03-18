from datetime import datetime, timedelta, timezone
from opentelemetry import trace
from lib.db import pool, query_wrap_array

tracer = trace.get_tracer("HomeActivities")

class HomeActivities:
  #def run(logger):
  def run(cognito_user_id):
   # span.set_attribute("app.result_lengh", len(results))
   
    sql = query_wrap_array("""
      SELECT
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
      FROM public.activities
      LEFT JOIN public.users ON users.uuid = activities.user_uuid
      ORDER BY activities.created_at DESC
      """)
    print("SQL-START================")
    print(sql)
    print("SQL-STOP================")
    with pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql)
          # this will return a tuple
          # the first field being the data
        json = cur.fetchone()
        print("DEBUG-START================")
        print(json[0])
        print("DEBUG-END==================")
    return json[0]
    return results
