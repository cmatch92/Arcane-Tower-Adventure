import unittest
from io import StringIO
from unittest.mock import patch

import TextBasedGame


class TestTextBasedGame(unittest.TestCase):
    def setUp(self):
        self.rooms = {
            'Entrance': {'North': 'Library', 'South': 'Dungeon'},
            'Dungeon': {'North': 'Entrance', 'East': 'Throne Room'},
            'Throne Room': {'West': 'Dungeon'}
        }
        self.room_items = {
            'Entrance': None,
            'Dungeon': 'Silver Key',
            'Throne Room': None
        }
        self.room_descriptions = {
            'Entrance': 'Entrance desc',
            'Dungeon': 'Dungeon desc',
            'Throne Room': 'Throne Room desc'
        }
        self.required_artifacts = ['Silver Key', 'Other Item']

    def run_game(self, commands):
        with patch('builtins.input', side_effect=commands):
            with patch('sys.stdout', new=StringIO()) as output:
                TextBasedGame.main()
                return output.getvalue()

    def test_case_insensitive_commands(self):
        output = self.run_game([
            'HELP',
            'STATUS',
            'GO NORTH',
            'GET ANCIENT SPELLBOOK',
            'STATUS',
            'EXIT'
        ])

        self.assertIn('Commands:', output)
        self.assertIn('You are in the Library', output)
        self.assertIn('You picked up the Ancient Spellbook!', output)
        self.assertIn('Inventory: Ancient Spellbook', output)

    def test_inventory_display_empty(self):
        with patch('sys.stdout', new=StringIO()) as output:
            TextBasedGame.show_status(
                'Entrance',
                [],
                self.room_items,
                self.room_descriptions,
                self.required_artifacts
            )

        self.assertIn('Your pack is empty.', output.getvalue())
        self.assertIn('Artifacts collected: 0 / 2', output.getvalue())

    def test_inventory_display_items(self):
        with patch('sys.stdout', new=StringIO()) as output:
            TextBasedGame.show_status(
                'Entrance',
                ['Silver Key'],
                self.room_items,
                self.room_descriptions,
                self.required_artifacts
            )

        self.assertIn('Inventory: Silver Key', output.getvalue())
        self.assertIn('Artifacts collected: 1 / 2', output.getvalue())

    def test_item_collection(self):
        inventory = TextBasedGame.get_item(
            'Dungeon', 'silver key', [], self.room_items
        )

        self.assertEqual(inventory, ['Silver Key'])
        self.assertIsNone(self.room_items['Dungeon'])

    def test_throne_room_stays_locked_without_key(self):
        output = self.run_game(['GO SOUTH', 'GO EAST', 'STATUS', 'EXIT'])

        self.assertIn('The heavy iron door to the Throne Room is locked!', output)
        self.assertIn('You need a Silver Key to unlock it.', output)
        self.assertIn('You are in the Dungeon', output)
        self.assertNotIn('You are in the Throne Room', output)

    def test_game_wins_after_collecting_all_artifacts(self):
        output = self.run_game([
            'GO NORTH',
            'GET ANCIENT SPELLBOOK',
            'GO EAST',
            'GET MAGIC POTION',
            'GO WEST',
            'GO WEST',
            'GET STAR CHART',
            'GO SOUTH',
            'GET ENCHANTED FLOWER',
            'GO EAST',
            'GO EAST',
            'GET CRYSTAL SWORD',
            'GO NORTH',
            'GET MYSTIC AMULET',
            'GO SOUTH',
            'GO WEST',
            'GO SOUTH',
            'GET SILVER KEY',
            'GO EAST'
        ])

        self.assertIn('Artifacts collected: 7 / 7', output)
        self.assertIn('CONGRATULATIONS! YOU WIN!', output)
        self.assertNotIn('GAME OVER. You have been defeated.', output)

    def test_game_ends_in_defeat_without_all_artifacts(self):
        output = self.run_game(['GO SOUTH', 'GET SILVER KEY', 'GO EAST'])

        self.assertIn('You are missing 6 artifact(s)!', output)
        self.assertIn('GAME OVER. You have been defeated.', output)
        self.assertNotIn('CONGRATULATIONS! YOU WIN!', output)


if __name__ == '__main__':
    unittest.main()
