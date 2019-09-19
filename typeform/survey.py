from typeform import Typeform


typeform = Typeform('<typeform-api-token>')
forms = typeform.forms

fields = []


# Sample: multiple chpoice question
multiple_choice = {
      "ref": "<Reference_to_this_question>",
    "title": "<question itself>",
    "type": "multiple_choice",
    "properties": {
        "randomize": False,
        "allow_multiple_selection": False,
        "allow_other_choice": True,
        "vertical_alignment": True,
        "choices": [
          {
            "label": "<multiple choice option_1>",
            "ref": "<reference_to_option_1>"
          },
          {
            "label": "<multiple choice option_2>",
            "ref": "<reference_to_option_2>"
          },
          {
            "label": "<multiple choice option_n>",
            "ref": "<reference_to_option_n>"
          }
        ]
      },
    "validations": {
        "required": True
      }
    }
fields.append(multiple_choice)


# Sample: open ended # QUESTION:
open_ended = {
      "ref": "open_ended_reference",
      "title": "<Can we help you?>",
      "type": "long_text",
      "validations": {
        "required": False,
        "max_length": 200
      }
    }
fields.append(open_ended)

# Createing the form itself
forms.create({'title': "<title of the form>", "fields": fields})

## P.S. to get the form id and the link
form_id = [x["id"] for x in typeform.forms.list()["items"] if x["title"]=="<title of the form>"][0]
form_link = "https://<account_name>.typeform.com/to/"+form_id
