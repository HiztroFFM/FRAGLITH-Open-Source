import json
import unittest

from tools.log_triage import classify, summarize


class TriageTests(unittest.TestCase):
    def test_priority(self):
        self.assertEqual(classify('ERROR Failed to preallocate (Not enough disk space)'), 'disk_space')
        self.assertEqual(classify('Could not load plugin foo.dll'), 'plugin_dependencies')
        self.assertEqual(classify('m_vecOrigin cellZ outside of cell bounds'), 'world_position')
        self.assertEqual(classify('Missing animation on model'), 'animation_assets')
        self.assertEqual(classify('Failed to load model.vmdl'), 'asset_loading')

    def test_no_log_contents_retained(self):
        private = 'PASSWORD=secret123 user@example.com 192.0.2.1 /private/location'
        output = json.dumps(summarize([private, 'ERROR Failed to preallocate ' + private]))
        for secret in ('secret123', 'example.com', '192.0.2.1', '/private/location'):
            self.assertNotIn(secret, output)
        self.assertEqual(summarize(['normal', 'Failed to preallocate'])['categorized_lines'], 1)

    def test_empty(self):
        self.assertEqual(summarize([])['total_lines'], 0)
        self.assertEqual(summarize([])['categories'], {})


if __name__ == '__main__':
    unittest.main()
