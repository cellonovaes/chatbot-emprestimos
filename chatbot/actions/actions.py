from rasa_sdk.events import UserUtteranceReverted
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker

from rasa_sdk.executor import CollectingDispatcher


class BD_RECUPERA_DADOS_EMPRESTIMO_EXISTENTE(Action):
    def name(self) -> Text:
        return "bd_recupera_dados_emprestimo_existente"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = tracker.get_slot("slot_id_emprestimo")
        parcelas = 7
        valor_parcela = 380
        msg = "Empréstimo {}: {} parcelas pendentes de {} reais."\
            .format(id, parcelas, valor_parcela)
        dispatcher.utter_message(text=msg)
        return []

class PREENCHE_SLOT_TRANSBORDO_NEGOCIACOES(Action):
    def name(self) -> Text:
        return "preenche_slot_transbordo_negociacoes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tracker.set_slot("slot_setor", "negociacoes")
        return []

class PREENCHE_SLOT_TRANSBORDO_INFORMACOES(Action):
    def name(self) -> Text:
        return "preenche_slot_transbordo_informacoes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tracker.set_slot("slot_setor", "informacoes")
        return []

class PREENCHE_SLOT_TRANSBORDO_NEGOCIACOES(Action):
    def name(self) -> Text:
        return "preenche_slot_transbordo_negociacoes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tracker.set_slot("slot_setor", "negociacoes")
        return []

class PREENCHE_SLOT_TRANSBORDO_VENDAS(Action):
    def name(self) -> Text:
        return "preenche_slot_transbordo_vendas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tracker.set_slot("slot_setor", "vendas")
        return []

class WS_CONSULTA_CREDITO_SCORE(Action):
    def name(self) -> Text:
        return "ws_consulta_credito_score"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        score = "800"
        tracker.set_slot("slot_score", score)
        dispatcher.utter_message(text=score)
        return []

class BD_BUSCA_TAXA_JUROS(Action):
    def name(self) -> Text:
        return "bd_busca_taxa_juros"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        taxa = "3.7"
        dispatcher.utter_message(text=taxa)
        return []

class GERA_SIMULACAO(Action):
    def name(self) -> Text:
        return "gera_simulacao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        parcela = "1500"
        dispatcher.utter_message(text=parcela)
        return []


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


class ActionGreetingName(Action):

    def name(self) -> Text:
        return "cumprimenta_pelo_nome"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot("slot_nome")
        msg = "Prazer {}!".format(nome)
        dispatcher.utter_message(text=msg)
        return []
