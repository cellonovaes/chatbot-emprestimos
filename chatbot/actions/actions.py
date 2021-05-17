
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "fallback_action"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_fallback")
        return [UserUtteranceReverted()]


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker

from rasa_sdk.executor import CollectingDispatcher


class ActionGreetingName(Action):

 def name(self) -> Text:
     return "action_greeting_name"

 def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
     name= tracker.get_slot("slot_nome")
     msg="Prazer {}!".format(name)
     dispatcher.utter_message(text=msg)

     return []
