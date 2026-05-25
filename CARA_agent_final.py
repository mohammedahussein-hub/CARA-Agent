# CARA: Cloud Requirements Analyzer Agent
import re
import json

class CARA:
    def __init__(self):
        self.name = "Cloud Requirements Analyzer Agent"
        self.ar_keywords = ["يجب أن", "من الضروري", "يلزم", "من المطلوب"]
        self.en_keywords = ["must", "shall", "required", "necessary"]
        self.non_functional_keywords = [
            "performance", "time", "response", "speed",
            "security", "encryption", "authentication",
            "cost", "price", "budget", "availability", "uptime"
        ]
    
    def classify(self, text):
        if not isinstance(text, str):
            return "FR"
        text_lower = text.lower()
        for kw in self.non_functional_keywords:
            if kw in text_lower:
                return "NFR"
        return "FR"

if __name__ == "__main__":
    agent = CARA()
    test = "The system must respond within 2 seconds"
    print(f"Classification: {agent.classify(test)}")
