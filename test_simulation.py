import unittest
from catcher.simulation import SimulationConfig, run_trial


class SimulationTests(unittest.TestCase):
    def test_trial_returns_expected_fields(self):
        result = run_trial(SimulationConfig(max_time=0.1))
        self.assertIn("captured", result)
        self.assertIn("capture_time", result)
        self.assertIn("distance", result)
        self.assertIn("catcher", result)
        self.assertIn("runner", result)

    def test_initial_overlap_is_capture_at_zero(self):
        cfg = SimulationConfig(catcher_start=(2, 2), runner_start=(2, 2))
        result = run_trial(cfg)
        self.assertTrue(result["captured"])
        self.assertEqual(result["capture_time"], 0.0)


if __name__ == "__main__":
    unittest.main()
