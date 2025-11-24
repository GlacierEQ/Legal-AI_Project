import os
import sys
import builtins
import types
import importlib
from io import StringIO

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # noqa: E402

sys.modules["paraphrase"] = types.ModuleType("paraphrase")
sys.modules["paraphrase"].paraphrase = lambda *args, **kwargs: []
sys.modules["predict"] = types.ModuleType("predict")
sys.modules["predict"].run_prediction = lambda *args, **kwargs: {"0": ""}


class DummyBlob:
    def __init__(self, text):
        self.sentiment = types.SimpleNamespace(
            polarity=1 if "love" in text else -1 if "terrible" in text else 0
        )


sys.modules["textblob"] = types.ModuleType("textblob")
sys.modules["textblob"].TextBlob = DummyBlob

sys.modules["flask"] = types.ModuleType("flask")


class DummyFlask:
    def __init__(self, *args, **kwargs):
        pass

    def route(self, *args, **kwargs):
        def decorator(func):
            return func

        return decorator


sys.modules["flask"].Flask = DummyFlask
sys.modules["flask"].request = types.SimpleNamespace(files={}, form={})
sys.modules["flask_cors"] = types.ModuleType("flask_cors")
sys.modules["flask_cors"].CORS = lambda *args, **kwargs: None


def import_app(monkeypatch, data="Q1\nQ2\n"):
    monkeypatch.setattr(builtins, "open", lambda *args, **kwargs: StringIO(data))
    if "flask_server.app" in sys.modules:
        importlib.reload(sys.modules["flask_server.app"])
    else:
        importlib.import_module("flask_server.app")
    return sys.modules["flask_server.app"]


def test_get_contract_analysis_positive(monkeypatch):
    app = import_app(monkeypatch)
    assert app.getContractAnalysis("I love this contract.") == "Positive"


def test_get_contract_analysis_negative(monkeypatch):
    app = import_app(monkeypatch)
    assert app.getContractAnalysis("This contract is terrible.") == "Negative"


def test_load_questions_short(monkeypatch):
    app = import_app(monkeypatch, "Question 1\nQuestion 2\n")
    assert app.load_questions_short() == ["Question 1\n", "Question 2\n"]
