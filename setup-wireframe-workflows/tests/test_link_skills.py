"""Run with python3 -m unittest discover -s setup-wireframe-workflows/tests."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'link-skills.py'


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.dest = Path(self.temp.name).resolve() / 'skills'

    def run_link(self, *extra):
        return subprocess.run([sys.executable, str(SCRIPT), '--client', 'codex', '--skills-dir', str(self.dest), '--all', *extra], capture_output=True, text=True)

    def test_preview_and_idempotent_install(self):
        result = self.run_link()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.dest.exists())
        result = self.run_link('--execute')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(json.loads(result.stdout)['completed']), 12)
        result = self.run_link('--execute')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(all(x['action'] == 'unchanged' for x in json.loads(result.stdout)['links']))

    def test_conflict_prevents_all_writes(self):
        self.dest.mkdir()
        (self.dest / 'build-wireframes').mkdir()
        result = self.run_link('--execute')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(list(self.dest.iterdir()), [self.dest / 'build-wireframes'])

    def test_broken_link_is_preserved(self):
        self.dest.mkdir()
        target = self.dest / 'missing'
        (self.dest / 'build-wireframes').symlink_to(target)
        self.assertEqual(self.run_link('--execute').returncode, 1)
        self.assertTrue((self.dest / 'build-wireframes').is_symlink())
        self.assertEqual(list(self.dest.iterdir()), [self.dest / 'build-wireframes'])

    def test_directory_symlink_is_refused(self):
        real = self.dest.parent / 'real'
        real.mkdir()
        self.dest.symlink_to(real, target_is_directory=True)
        self.assertEqual(self.run_link('--execute').returncode, 1)
        self.assertEqual(list(real.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
