from unittest import TestCase
from event_handler import EventListener, EventThrower


class SomeListener(EventListener):
    def listen_something(self):
        self.foo = 'bar'


class EventedTest(TestCase):
    def test_event_model(self):
        listener = SomeListener()
        listener.on('something', listener.listen_something)

        thrower = EventThrower()
        thrower.add_listener(listener)

        self.assertTrue(getattr(listener, 'foo', None) is None)

        thrower.emit('something')

        self.assertEqual(listener.foo, 'bar')

    def test_a_listener_can_be_killed(self):
        listener = SomeListener()
        listener.on('something', listener.listen_something)

        thrower = EventThrower()
        thrower.add_listener(listener)

        thrower.emit('something')

        self.assertEqual(listener.foo, 'bar')

        del listener
        """ Garbage collector is required to simulate time passing """
        import gc; gc.collect()

        thrower.emit('something')
        self.assertEqual(0, len(thrower.__LISTENERS__))
