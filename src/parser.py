def parse_script(script_path):
    """
    Parses a script file into a list of scenes with descriptions and dialogues.

    Args:
        script_path (str): Path to the script file.

    Returns:
        list of dict: List of scenes, each containing a description and dialogue.
    """
    scenes = []
    with open(script_path, "r") as file:
        lines = file.readlines()

    current_scene = {}
    for line in lines:
        line = line.strip()
        if line.startswith("# Scene"):
            if current_scene:
                scenes.append(current_scene)
            current_scene = {"description": "", "dialogue": ""}
        elif line.startswith("Description:"):
            current_scene["description"] = line.replace("Description:", "").strip()
        elif line.startswith("Dialogue:"):
            current_scene["dialogue"] = line.replace("Dialogue:", "").strip()

    if current_scene:
        scenes.append(current_scene)

    return scenes
