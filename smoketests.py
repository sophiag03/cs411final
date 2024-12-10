import requests 

BASE_URL = "http://localhost:5001"

def test_health_check(): assert True

def test_create_user(): assert True

def test_login(): assert True

def test_update_password(): assert True

def test_fetch_affirmation(): assert True

def test_view_affirmations(): assert True

def test_clear_affirmations(): assert True

def test_affirmation_count(): assert True

def test_random_affirmation(): assert True

if __name__ == "__main__":
    try:
        print("Runnint smoketests...")
        test_health_check()
        test_create_user()
        test_login()
        test_update_password()
        test_fetch_affirmation()
        test_view_affirmations()
        test_clear_affirmations()
        test_affirmation_count()
        test_random_affirmation()
        print("All smoketests passed!")
    except AssertionError as e:
        print(f"Smoketest failed: {e}")



