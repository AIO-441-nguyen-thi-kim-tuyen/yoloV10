from streamlit.testing.v1 import AppTest


def test_smoke_page_input():
    at = AppTest.from_file('../../safety_helmet_detection_app.py')
    at.run(timeout=30)
    assert not at.exception

    # Run example image
    at.button[0].run()
    assert not at.exception



