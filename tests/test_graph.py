import pytest
from package.graph import display
from datetime import datetime
import subprocess
from package.graph import copy_to_clipboard
import os
import sys
import shutil

def test_display_right_password():
    current_time = datetime.now().strftime("%H%M")
    assert display("test",current_time) == None 

def test_display_wrong_password():
    with pytest.raises(ValueError, match="syntax error"):
        display("test",1234)

def test_copy_to_clipboard(monkeypatch):
    def mock_run(*args, **kwargs):
        pass
    monkeypatch.setattr(subprocess, "run", mock_run)
    
    try: 
        copy_to_clipboard("Whatever test")
    except Exception as e:
        pytest.fail("Unexpected error raised: {e}")