"""Context policy of src/agent.run_agent with scripted (fake) controller/retriever: no API calls."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.agent import AgentConfig, GeminiController, run_agent  # noqa: E402


def chunk(cid):
    return {"id": cid, "text": "x" * 900, "source_id": "doc", "source": "doc.pdf", "page": 1,
            "metadata": {"page_end": 1, "article": 1}, "score": 0.5}


class FakeRetriever:
    def __init__(self):
        self.batches = [[chunk("a1"), chunk("a2"), chunk("a3")], [chunk("b1"), chunk("b2"), chunk("b3")]]

    def search(self, query, *, filters=None, top_k=3):
        return self.batches.pop(0)


class FakeController:
    """Search twice, then answer citing b1 (the best chunk of the second search)."""
    render = staticmethod(GeminiController.render)

    def __init__(self):
        self.turn = 0

    def decide(self, prompt):
        self.turn += 1
        usage = {"input_tokens": 0, "output_tokens": 0, "thinking_tokens": 0, "seconds": 0, "retries": 0}
        if self.turn <= 2:
            return {"tool": "search", "args": {"query": f"q{self.turn}"}, "usage": usage}
        return {"tool": "answer", "args": {"answer": "ok [b1]", "citations": ["b1"]}, "usage": usage}


class ContextPolicyTest(unittest.TestCase):
    def run_policy(self, policy):
        cfg = AgentConfig(model="fake", budget=2900, context_policy=policy)  # fits 3 chunks of ~950 chars
        return run_agent("question?", FakeController(), FakeRetriever(), cfg)

    def test_first_keeps_oldest_search(self):
        out = self.run_policy("first")
        self.assertEqual(out["final_context_ids"], ["a1", "a2", "a3"])
        self.assertEqual(out["status"], "abstain")  # b1 never reached the context -> citation invalid

    def test_recent_prefers_newest_search(self):
        out = self.run_policy("recent")
        self.assertEqual(out["final_context_ids"], ["b1", "b2", "b3"])
        self.assertEqual(out["status"], "answered")


if __name__ == "__main__":
    unittest.main()
