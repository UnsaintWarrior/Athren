from discord.utils import get 
from config import ROLES_TO_CHECK, CATEGORIES_TO_CREATE

async def handle_initchecks(client):
    print("Initializing checks\n")
    # Run the checks for each guild the bot is in
    for guild in client.guilds:
        print (f'Checking {guild.name}')
        all_checks_passed = await checks(guild,ROLES_TO_CHECK)
        if all_checks_passed:
            print(f"Initialization complete, no errors found for {guild.name}\n")
        else:
            print(f"Initialization checks failed for {guild.name}\n")
            # print(f'End of checks for {guild.name}\n')

from discord.utils import get 
from config import ROLES_TO_CHECK, CATEGORIES_TO_CREATE

async def handle_initchecks(client):
    print("Initializing checks\n")
    # Run the checks for each guild the bot is in
    for guild in client.guilds:
        print (f'Checking {guild.name}')
        all_checks_passed = await checks(guild,ROLES_TO_CHECK)
        if all_checks_passed:
            print(f"Initialization complete, no errors found for {guild.name}\n")
        else:
            print(f"Initialization checks failed for {guild.name}\n")
            # print(f'End of checks for {guild.name}\n')

async def checks(guild, ROLES_TO_CHECK):
    # Flags for each check
    role_exists = True
    category_exists = True

    # Check for role existence
    for role_name in ROLES_TO_CHECK:
        existing_role = get(guild.roles, name=role_name)
    if not existing_role:
        print(f"Missing {role_name} role.")
        role_exists = False  # Set flag to False if the role doesn't exist

    for category_name in CATEGORIES_TO_CREATE:
    # Check for category existence
        existing_categories = get(guild.categories, name=category_name)
        if not existing_categories:
            print(f"Missing {category_name} category, probably missing channels too")
            category_exists = False  # Set flag to False if the category doesn't exist

        # Return True if all checks passed
        return role_exists and category_exists
