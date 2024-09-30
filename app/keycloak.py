from keycloak.keycloak_openid import KeycloakOpenID
import os

# Configure Keycloak client
keycloak_openid = KeycloakOpenID(
    server_url=os.getenv("KEYCLOAK_URL"),
    client_id=os.getenv("KEYCLOAK_CLIENT_ID"),
    realm_name=os.getenv("KEYCLOAK_REALM"),
    client_secret_key=os.getenv("KEYCLOAK_SECRET")
)

def create_keycloak_user(username, email, password):
    keycloak_openid.admin.create_user({
        "username": username,
        "email": email,
        "enabled": True,
        "credentials": [{
            "type": "password",
            "value": password,
            "temporary": False
        }]
    })

def get_token(username, password):
    token = keycloak_openid.token(username, password)
    return token

def introspect_token(token):
    return keycloak_openid.introspect(token)

def validate_token(token):
    user_info = keycloak_openid.userinfo(token)
    return user_info
