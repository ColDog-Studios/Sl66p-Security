from pathlib import Path
import yaml

class PolicySupport:
    def __init__(self, policy_file: str):
        self.policy_file = Path(policy_file)
        self.policies = self.load_policies()

    def load_policies(self):
        if not self.policy_file.exists():
            raise FileNotFoundError(f"Policy file {self.policy_file} not found.")
        with open(self.policy_file, 'r') as file:
            return yaml.safe_load(file)

    def get_policy(self, policy_name: str):
        return self.policies.get(policy_name, None)

    def validate_policy(self, policy_name: str, config: dict):
        policy = self.get_policy(policy_name)
        if not policy:
            raise ValueError(f"Policy {policy_name} not found.")
        # Implement validation logic based on policy
        return True  # Placeholder for actual validation result

    def list_policies(self):
        return list(self.policies.keys())