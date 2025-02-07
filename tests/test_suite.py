# -*- coding: utf-8 -*-
import os
import sys
import logging

from dotenv import load_dotenv

from msteamsapi import (
    ContainerStyle, FactSet, Container, AdaptiveCard, TeamsWebhook, 
    TextSize, TextWeight, CompoundButton, Table, TableCell, TextBlock,
    TextBlockStyle, TextColor
)

load_dotenv()

log = logging.getLogger(__name__)

PYTHON_VERSION = sys.version.split(" ")[0]
MSTEAMS_TEST_HOOK = os.getenv("MSTEAMS_TEST_HOOK")
MSTEAMS_TEST_EMAIL = os.getenv("MSTEAMS_TEST_EMAIL")
MSTEAMS_TEST_NAME = os.getenv("MSTEAMS_TEST_NAME")


def test_table():
    assert MSTEAMS_TEST_HOOK
    webhook = TeamsWebhook(MSTEAMS_TEST_HOOK)
    card = AdaptiveCard()
    background_image_url = "https://github.com/d1ng3s/msteamsapi/raw/add-my-features/tests/background_red.png"
    card.add_compound_button(CompoundButton("Info Title in CompoundButton", "badge", True, "descriptive message"))
    card.mention(MSTEAMS_TEST_EMAIL, MSTEAMS_TEST_NAME, add_text_block=True)
    table = Table([1])
    table.add_row([TableCell(TextBlock("statement on what is happening",color=TextColor.LIGHT),rounded_corners=True, background_image_url=background_image_url)])
    table.add_row([TableCell(TextBlock("and another statement on something else",color=TextColor.LIGHT),rounded_corners=True, background_image_url=background_image_url)])
    table.add_row([TableCell(TextBlock("and a third one would you believe it, but this time it's a bit longer this one",color=TextColor.LIGHT),rounded_corners=True, background_image_url=background_image_url)])
    card.add_table(table)
    table = Table([1],show_grid_lines=False)
    table.add_row([TableCell(TextBlock("Detailed Nested Info",weight=TextWeight.BOLDER,style=TextBlockStyle.HEADING),show_border=False)])
    nested_table = Table([1,1])
    nested_table.add_row([TableCell(TextBlock("Property Name 1")),TableCell(TextBlock("Property Value 1"))],style=ContainerStyle.EMPHASIS)
    nested_table.add_row([TableCell(TextBlock("Property Name 2")),TableCell(TextBlock("Property Value 2"))],style=ContainerStyle.EMPHASIS)
    nested_table.add_row([TableCell(TextBlock("Property Name 3")),TableCell(TextBlock("Property Value 3"))],style=ContainerStyle.EMPHASIS)    
    table.add_row([TableCell(nested_table)])
    card.add_table(table)
    card.add_url_button("Check it out", "http://www.google.com")
    card.add_url_button("Check this out too", "http://www.google.be")
    webhook.add_cards(card)
    webhook.send(Channel="Test")


# def test_happy_pass():
#     assert MSTEAMS_TEST_HOOK
#     webhook = TeamsWebhook(MSTEAMS_TEST_HOOK)
#     title = "Python %s" % PYTHON_VERSION
#     log.info("You should now receive an AdaptiveCard with title: %s" % title)

#     card = AdaptiveCard(title=title, title_style=ContainerStyle.DEFAULT)

#     card.add_background(url="https://github.com/ALERTua/msteamsapi/raw/main/tests/background.png")

#     container = Container(style=ContainerStyle.DEFAULT)

#     card.mention(MSTEAMS_TEST_EMAIL, MSTEAMS_TEST_NAME, add_text_block=True)
#     mention_tag = card.mention(MSTEAMS_TEST_EMAIL, "this dude")

#     image_url = "https://github.com/ALERTua/msteamsapi/raw/main/tests/test_image.png"
#     container.add_image(image_url, "image alt text")
#     container.add_text_block(
#         "multiline\n\ntext\n\nmention 1: %s" % mention_tag,
#         size=TextSize.DEFAULT,
#         weight=TextWeight.DEFAULT,
#         color="default",
#     )
#     container.add_text_block(
#         """Blabla

# - item 1
# - item 2
# - item 3


# [url](https://github.com/ALERTua/msteamsapi)
#         """,
#         size=TextSize.DEFAULT,
#         weight=TextWeight.DEFAULT,
#         color="default",
#     )

#     factset = FactSet(("fact 1", "fact 1 value"))
#     factset.add_facts(("fact 2", "fact 2 value"), ("fact 3", "fact 3 value"))
#     container.add_fact_set(factset)

#     card.add_container(container)

#     for i, url in enumerate(["https://google.com/", "https://goo.gle"]):
#         card.add_url_button("url %s" % i, url)

#     webhook.add_cards(card)
#     webhook.send()
#     log.info("Card Sent")
