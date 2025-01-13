# app_hardening.py

def harden_application(app_name):
    """
    Harden the specified application by applying security best practices.
    
    Args:
        app_name (str): The name of the application to harden.
    
    Returns:
        dict: A summary of the hardening actions taken.
    """
    actions_taken = []
    
    # Example hardening actions
    if app_name == "example_app":
        actions_taken.append("Disabled unnecessary features.")
        actions_taken.append("Configured secure settings.")
        actions_taken.append("Updated to the latest version.")
    
    return {
        "application": app_name,
        "actions": actions_taken
    }

def apply_custom_policy(policy):
    """
    Apply a custom hardening policy defined in YAML format.
    
    Args:
        policy (dict): The custom policy to apply.
    
    Returns:
        dict: A summary of the policy application results.
    """
    results = []
    
    for app, settings in policy.items():
        result = harden_application(app)
        results.append(result)
    
    return {
        "applied_policies": results
    }