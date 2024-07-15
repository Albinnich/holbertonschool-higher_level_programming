import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error.Template is not a string")
        return

    if not isinstance(attendees, list):
        print("Error. Not a list")
        return

    if template.strip() = "":
        print("Error. Template is empty, no output files generated.")
        return

    if not attendees:
        print("Error. No data provided, no output files generated.")
        return
