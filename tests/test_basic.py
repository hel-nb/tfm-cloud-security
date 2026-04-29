from services.users.app import lambda_handler

def test_users_lambda():
    result = lambda_handler({}, {})
    assert result["statusCode"] == 200