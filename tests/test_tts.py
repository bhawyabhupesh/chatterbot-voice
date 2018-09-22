from unittest import TestCase
from unittest.mock import patch
from chatterbot.conversation import Statement
from chatterbot_voice import VoiceOutput


def fake_get_espeak_call_result(cls, text):
    return text


class TextToSpeechTests(TestCase):

    def setUp(self):
        self.adapter = VoiceOutput()

    @patch.object(
        VoiceOutput,
        'get_espeak_call_result',
        fake_get_espeak_call_result
    )
    def test_response_returned(self):
        """
        Test that a response statement is returned from the adapter.
        """
        statement = Statement("Testing speech synthesis.")

        self.assertEqual(
            self.adapter.process_response(statement),
            statement.text
        )
