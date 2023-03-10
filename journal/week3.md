# Week 3 — Decentralized Authentication

## Install AWS Amplify

## Provision Cognito User Group in AWS console
![screenshot](Assets/cognitouserpool.png)

## Config Amplify - modify code in app.js to hook up cognito pool

## Conditionally show components based on Logged in or Logged out
### Log in screenshot

![screenshot](Assets/login.png)

### Log in screenshot

![screenshot](Assets/logout.png)

## Modify code for Signin Page, Signout Page , Confirmation Page and Recovery Page


## Transfer Auth token from frontend to backend
- Add headers in the 'HomeFeedpage.js' 
- add cors code in app.py
- add debug code to check if we recieve the auth headers. 
   ````
    app.logger.debug(
       request.headers.get('Authorization')
    )

## Jwt token code
- add new cogenito_jwt_token.py under lib folder
- modify app.py for the following code
```
@app.route("/api/activities/home", methods=['GET'])
def data_home():
 #app.logger.debug("Auth Header")
 # app.logger.debug(
 #   request.headers.get('Authorization')
 # )
  access_token = extract_access_token(request.headers)
  try:
    claims = cognito_jwt_token.verify(access_token)
    # authenicatied request
    app.logger.debug("authenicated")
    app.logger.debug(claims)
    app.logger.debug(claims['username'])
    cognito_user_id=claims['username']
    app.logger.debug(cognito_user_id)
    data = HomeActivities.run(cognito_user_id)
   
  except TokenVerifyError as e:
    # unauthenicatied request
    app.logger.debug(e)
    app.logger.debug("unauthenicated")
  return data, 200
```
- modify code in home_activites.py to add arguement to Run(cognito_user_id)
- add extra code in home_activites.py to
```
   if cognito_user_id != None:
        extra_crud = {
          'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
          'handle':  'Jack',
          'message': 'My dear brother pcs, it the humans that are the problem',
          'created_at': (now - timedelta(hours=1)).isoformat(),
          'expires_at': (now + timedelta(hours=12)).isoformat(),
          'likes': 1042,
          'replies': []
        }
        results.insert(0,extra_crud)
```
- result
![screenshot](Assets/auth.png)
Signin result
![screenshot](Assets/signin_auth.png)