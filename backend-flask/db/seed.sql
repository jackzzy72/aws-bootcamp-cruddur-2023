-- this file was manually created

INSERT INTO public.users (display_name, email,handle, cognito_user_id)
VALUES
  ('PCS Jack', 'pcs_jack@outlook.com','pcs' ,'MOCK'),
  ('Jack zou', 'jackzzy2018@gmail.com','jackzzy2018' ,'MOCK'),
  ('Andrew Brown', 'andrew@exampro.co','andrewbrown' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'jackzzy2018' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  ),
  (
    (SELECT uuid from public.users WHERE users.handle = 'pcs' LIMIT 1),
    'I am the other seed data!',
    current_timestamp + interval '10 day'
  );
