1. Edit the file `original_code.py` to add a status field to the Article model with these exact specifications:
   - Add STATUS_CHOICES list at the start of the class with three choices: ('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')
   - Add a CharField named 'status' with max_length=10, choices=STATUS_CHOICES, and default='draft'