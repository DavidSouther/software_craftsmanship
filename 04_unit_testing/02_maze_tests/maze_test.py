import unittest
import unittest.mock
import maze


class LockTestCase(unittest.TestCase):
    def test_add_fitting_key(self):
        lock = maze.Lock()

        lock.add_fitting_key("blue")

        self.assertEqual(lock.fitting_keys, ["blue"])

    def test_add_duplicate_fitting_key(self):
        lock = maze.Lock()

        lock.add_fitting_key("blue")
        lock.add_fitting_key("blue")

        self.assertEqual(lock.fitting_keys, ["blue"])

    def test_accepts_fitting_key(self):
        lock = maze.Lock()
        lock.add_fitting_key("blue")

        accepts = lock.accepts("blue")

        self.assertTrue(accepts)

    def test_does_not_accept_missing_key(self):
        lock = maze.Lock()
        lock.add_fitting_key("blue")

        accepts = lock.accepts("red")

        self.assertFalse(accepts)


class KeyringTestCase(unittest.TestCase):
    def test_add_key(self):
        keyring = maze.Keyring()

        keyring.add_key("blue")

        self.assertEqual(keyring.keys, ["blue"])

    def test_add_duplicate_key(self):
        keyring = maze.Keyring()

        keyring.add_key("blue")
        keyring.add_key("blue")

        self.assertEqual(keyring.keys, ["blue"])

    def test_can_unlock_door_no_lock(self):
        keyring = maze.Keyring()
        door = maze.Door(maze.Room(), maze.Room())

        can_unlock = keyring.can_unlock(door)

        self.assertTrue(can_unlock)

    def test_can_unlock_door_having_key(self):
        key = "blue"
        keyring = maze.Keyring()
        lock = maze.Lock()
        keyring.add_key(key)
        lock.add_fitting_key(key)
        door = maze.Door(maze.Room(), maze.Room(), lock)

        can_unlock = keyring.can_unlock(door)

        self.assertTrue(can_unlock)

    def test_cannot_unlock_door_missing_key(self):
        keyring = maze.Keyring()
        lock = maze.Lock()
        keyring.add_key("blue")
        lock.add_fitting_key("red")
        door = maze.Door(maze.Room(), maze.Room(), lock)

        can_unlock = keyring.can_unlock(door)

        self.assertFalse(can_unlock)


class DoorTestCase(unittest.TestCase):
    def test_tracks_other_side(self):
        room_a = maze.Room("A")
        room_b = maze.Room("B")
        door = maze.Door(room_a, room_b)

        other_size_a = door.other_side(room_a)
        other_size_b = door.other_side(room_b)

        self.assertEqual(other_size_a, room_b)
        self.assertEqual(other_size_b, room_a)


class RoomTestCase(unittest.TestCase):
    def test_add_north_door(self):
        room = maze.Room("A")
        north_room = maze.Room("B")

        room.add_north_door(north_room)

        self.assertEqual(room.north_door.other_side(room), north_room)
        self.assertEqual(
            north_room.south_door.other_side(north_room), room)
        self.assertIsNone(north_room.north_door)

    def test_add_south_door(self):
        pass

    def test_add_east_door(self):
        pass

    def test_add_west_door(self):
        pass

    def test_on_enter_adds_key(self):
        room = maze.Room("A", "blue")
        player = maze.Player()

        room.on_enter(player)

        self.assertIn("blue", player.keyring.keys)


class PlayerTestCase(unittest.TestCase):
    def test_can_move_through_unlocked_door(self):
        room_a = maze.Room("A")
        room_b = maze.Room("B")
        room_a.add_north_door(room_b)
        player = maze.Player(room_a)

        player.move_through(room_a.north_door)

        self.assertEqual(player.current_room, room_b)

    def test_can_move_through_locked_door_with_key(self):
        key = "blue"
        room_a = maze.Room("A")
        room_b = maze.Room("B")
        lock = maze.Lock()
        lock.add_fitting_key(key)
        room_a.add_north_door(room_b, lock)
        player = maze.Player(room_a)
        player.keyring.add_key(key)

        player.move_through(room_a.north_door)

        self.assertEqual(player.current_room, room_b)

    def test_cannot_move_through_locked_door_without_key(self):
        room_a = maze.Room("A")
        room_b = maze.Room("B")
        lock = maze.Lock()
        lock.add_fitting_key("blue")
        room_a.add_north_door(room_b, lock)
        player = maze.Player(room_a)

        player.move_through(room_a.north_door)

        self.assertEqual(player.current_room, room_a)

    def test_cannot_move_through_None_door(self):
        room_a = maze.Room("A")
        player = maze.Player(room_a)

        player.move_through(room_a.north_door)

        self.assertEqual(player.current_room, room_a)


class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = maze.basic_maze()

    @unittest.mock.patch("builtins.print")
    def test_print_room(self, mock_print):
        self.game.print_room()

        mock_print.assert_any_call("You are in the entry way.")
        mock_print.assert_any_call("There is a door to the (n)orth.")
        mock_print.assert_any_call("There is a door to the (e)ast.")

    def test_move_player(self):
        kitchen = self.game.end_room
        dining_room = kitchen.south_door.other_side(kitchen)

        self.game.move_player("n")

        self.assertEqual(self.game.player.current_room, dining_room)

    @unittest.mock.patch("builtins.print")
    def test_move_player_no_room(self, mock_print):
        self.game.move_player("s")

        self.assertEqual(
            self.game.player.current_room, self.game.start_room)

    @unittest.mock.patch("builtins.print")
    @unittest.mock.patch("builtins.input")
    def skip_test_play_stuck(self, mock_print, mock_input):
        mock_input.side_effects = ["n", "n", "q"]

        self.game.play()

        mock_print.assert_any_call("You are in the entry way.")
        mock_print.assert_any_call("You are in the library.")
        mock_print.assert_any_call("Cannot move through that door.")

    @unittest.mock.patch("builtins.print")
    @unittest.mock.patch("builtins.input")
    def skip_test_play_win(self, mock_print, mock_input):
        mock_input.side_effects = ["e", "w", "n", "n"]

        self.game.play()

        mock_print.assert_any_call("Picked up blue key")
        mock_print.assert_any_call("You are in the library.")
        mock_print.assert_any_call("You are in the dining room.")
        mock_print.assert_any_call("You won the treasure")


if __name__ == "__main__":
    unittest.main()