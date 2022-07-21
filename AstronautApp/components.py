import json
import asyncio
import idom
from pathlib import Path
from idom import component, event, html, hooks, use_state


@component
def hello_world(recipient: str):
    return html.h1(f"Hello, {recipient}!")


@component
def todo_list():
    return html.div(
                html.h1("My Todo List"),
                html.ul(
                    html.li("Design a cool new app"),
                    html.li("Build it"),
                    html.li("Share it with the world!"),
                )
            )


@component
def dog_image():
    return html.img(
        {
            "src": "https://picsum.photos/id/237/500/300",
            "style": {"width": "50%", "marginLeft": "25%"},
            "alt": "Billie Holiday",
        }
    )


@component
def Photo(alt_text, image_id):
    return html.img(
        {
            "src": f"https://picsum.photos/id/{image_id}/500/200",
            "style": {"width": "50%"},
            "alt": alt_text,
        }
    )


@component
def Gallery():
    return html.section(
        html.h1("Photo Gallery"),
        Photo("Landscape", image_id=830),
        Photo("City", image_id=274),
        Photo("Puppy", image_id=237),
    )


@component
def MyTodoList():
    return html.div(
        html.h1("My Todo List"),
        html.img({"src": "https://picsum.photos/id/0/500/300"}),
        html.ul(
            html.li("The first thing I need to do is ....")
        ),
    )


@component
def Item(name, done):
    return html.li(name, " ✔" if done else "")


@component
def TodoList():
    return html.section(
        html.h1("My Todo List"),
        html.ul(
            Item("Find a cool problem to solve", done=True),
            Item("Build an app to solve it", done=True),
            Item("Share that app with the world!", done=False),
        ),
    )


@component
def DataList(items, filter_by_priority=None, sort_by_priority=False):
    if filter_by_priority is not None:
        items = [i for i in items if i["priority"] <= filter_by_priority]
    if sort_by_priority:
        items = list(sorted(items, key=lambda i: i["priority"]))
    list_item_elements = [html.li(i["text"], key=i["id"]) for i in items]
    return html.ul(list_item_elements)


@component
def TodoList2():
    tasks = [
        {"id": 0, "text": "Make breakfast (important)", "priority": 0},
        {"id": 1, "text": "Feed the dog (important)", "priority": 0},
        {"id": 2, "text": "Do laundry", "priority": 2},
        {"id": 3, "text": "Go on a run (important)", "priority": 1},
        {"id": 4, "text": "Clean the house", "priority": 2},
        {"id": 5, "text": "Go to the grocery store", "priority": 2},
        {"id": 6, "text": "Do some coding", "priority": 1},
        {"id": 7, "text": "Read a book (important)", "priority": 1},
    ]
    return html.section(
        html.h1("My Todo List"),
        DataList(tasks, filter_by_priority=1, sort_by_priority=True),
    )


tasks = [
        {"id": 0, "text": "Make breakfast"},
        {"id": 1, "text": "Feed the dog"},
        {"id": 2, "text": "Do laundry"},
        {"id": 3, "text": "Go on a run"},
        {"id": 4, "text": "Clean the house"},
        {"id": 5, "text": "Go to the grocery store"},
        {"id": 6, "text": "Do some coding"},
        {"id": 7, "text": "Read a book"},
    ]


@component
def ListItem(text):
    return html.li(text)


@component
def ListElement():
    return [ListItem(t["text"], key=t["id"]) for t in tasks]


@component
def PrintButton(display_text, message_text):
    def handle_event(event):
        print(message_text)

    return html.button({"onClick": handle_event, }, display_text)


@component
def App():
    return html.div(
        PrintButton("Play", "Playing"),
        PrintButton("Pause", "Paused"),
    )


HERE = Path(__file__)
DATA_PATH = HERE.parent / "data2.json"
sculpture_data = json.loads(DATA_PATH.read_text())
food_data = json.loads(DATA_PATH.read_text())


@component
def Gallery2():
    index, set_index = hooks.use_state(0)

    def handle_click(event):
        set_index(index + 1)

    bounded_index = index % len(sculpture_data)
    sculpture = sculpture_data[bounded_index]
    alt = sculpture["alt"]
    artist = sculpture["artist"]
    description = sculpture["description"]
    name = sculpture["name"]
    url = sculpture["url"]

    return html.div(
        html.button({"onClick": handle_click}, "Next"),
        html.h2(name, " by ", artist),
        html.p(f"{bounded_index + 1} of {len(sculpture_data)}"),
        html.img({"src": url, "alt": alt, "style": {"height": "200px"}}),
        html.p(description),
    )


@component
def App2():
    recipient, set_recipient = use_state("Alice")
    message, set_message = use_state("")

    @event(prevent_default=True)
    async def handle_submit(event):
        set_message("")
        print("About to send message...")
        await asyncio.sleep(5)
        print(f"Sent '{message}' to {recipient}")

    return html.form(
        {"onSubmit": handle_submit, "style": {"display": "inline-grid"}},
        html.label(
            "To: ",
            html.select(
                {
                    "value": recipient,
                    "onChange":
                        lambda event:
                            set_recipient(event["target"]["value"]),
                },
                html.option({"value": "Alice"}, "Alice"),
                html.option({"value": "Bob"}, "Bob"),
            ),
        ),
        html.input(
            {
                "type": "text",
                "placeholder": "Your message...",
                "value": message,
                "onChange":
                    lambda event:
                        set_message(event["target"]["value"]),
            }
        ),
        html.button({"type": "submit"}, "Send"),
    )


@component
def ColorButton():
    color, set_color = use_state("gray")

    def handle_click(event):
        set_color("orange")
        set_color("pink")
        set_color("blue")

    def handle_reset(event):
        set_color("gray")

    return html.div(
        html.button(
            {"onClick":
                handle_click, "style":
                    {"backgroundColor": color}}, "Set Color"
        ),
        html.button(
            {"onClick":
                handle_reset, "style":
                    {"backgroundColor": color}}, "Reset"
        ),
    )


def increment(old_number):
    new_number = old_number + 1
    return new_number


@component
def Counter2():
    number, set_number = use_state(0)

    def handle_click(event):
        set_number(increment)
        set_number(increment)
        set_number(increment)

    return html.div(
        html.h1(number),
        html.button({"onClick": handle_click}, "Increment"),
    )


@component
def Form():
    person, set_person = use_state(
        {
            "first_name": "Barbara",
            "last_name": "Hepworth",
            "email": "bhepworth@sculpture.com"
        }
    )

    def handle_first_name_change(event):
        set_person({**person, "first_name": event["target"]["value"]})

    def handle_last_name_change(event):
        set_person({**person, "last_name": event["target"]["value"]})

    def handle_email_change(event):
        set_person({**person, "email": event["target"]["value"]})

    return html.div(
        html.label(
            "First Name: ",
            html.input(
                {
                    "value": person["first_name"],
                    "onChange": handle_first_name_change
                },
            ),
        ),
        html.label(
            "Last Name: ",
            html.input(
                {
                    "value": person["last_name"],
                    "onChange": handle_last_name_change
                },
            ),
        ),
        html.label(
            "Email: ",
            html.input(
                {
                    "value": person["email"],
                    "onChange": handle_email_change
                },
            ),
        ),
        html.p(
            f"{person['first_name']} {person['last_name']} ({person['email']})"
            ),
    )


@component
def Button():
    def handle_event(event):
        print(event)

    return html.button({"onClick": handle_event}, "Click me!")


@component
def PrintButton2(display_text, message_text):
    def handle_event(event):
        print(message_text)

    return html.button({"onClick": handle_event}, display_text)


@component
def App3():
    return html.div(
        PrintButton("Play", "Playing"),
        PrintButton("Pause", "Paused"),
    )


@component
def Button2(display_text, on_click):
    return html.button({"onClick": on_click}, display_text)


@component
def PlayButton(movie_name):
    def handle_click(event):
        print(f"Playing {movie_name}")

    return Button(f"Play {movie_name}", on_click=handle_click)


@component
def FastForwardButton():
    def handle_click(event):
        print("Skipping ahead")

    return Button("Fast Forward", on_click=handle_click)


@component
def App4():
    return html.div(
        PlayButton("Buena Vista Social Club"),
        FastForwardButton(),
    )


@component
def ButtonWithDelay(message, delay):
    async def handle_event(event):
        await asyncio.sleep(delay)
        print(message)

    return html.button({"onClick": handle_event}, message)


@component
def App5():
    return html.div(
        ButtonWithDelay("Print 3 seconds later", delay=3),
        ButtonWithDelay("Print immediately", delay=0),
    )


@idom.component
def PlayDinosaurSound():
    event, set_event = idom.hooks.use_state(None)
    return idom.html.div(
        idom.html.audio(
          {
              "controls": True,
              "onTimeUpdate": lambda event: set_event(event),
              "src": "shorturl.at/dflV4",
          }
        ),
        idom.html.pre(json.dumps(event, indent=2)),
    )


@component
def DoNotChangePages():
    return html.div(
        html.p("Normally clicking this link would take you to a new page"),
        html.a(
            {
                "onClick": event(lambda event: None, prevent_default=True),
                "href": "https://www.google.com",
            },
            "https://www.google.com",
        ),
    )


@component
def DivInDiv():
    stop_propagation, set_stop_propagation = hooks.use_state(True)
    inner_count, set_inner_count = hooks.use_state(0)
    outer_count, set_outer_count = hooks.use_state(0)

    div_in_div = html.div(
        {
            "onClick": lambda event: set_outer_count(outer_count + 1),
            "style":
                {
                    "height": "100px",
                    "width": "100px",
                    "backgroundColor": "red"
                },
        },
        html.div(
            {
                "onClick": event(
                    lambda event: set_inner_count(inner_count + 1),
                    stop_propagation=stop_propagation,
                ),
                "style":
                    {
                        "height": "50px",
                        "width": "50px",
                        "backgroundColor": "blue"
                    },
            },
        ),
    )

    return html.div(
        html.button(
            {
                "onClick":
                    lambda event:
                        set_stop_propagation(not stop_propagation)
            },
            "Toggle Propagation",
        ),
        html.pre(f"Will propagate: {not stop_propagation}"),
        html.pre(f"Inner click count: {inner_count}"),
        html.pre(f"Outer click count: {outer_count}"),
        div_in_div,
    )


@component
def Gallery3():
    index, set_index = hooks.use_state(0)
    show_more, set_show_more = hooks.use_state(False)

    def handle_next_click(event):
        set_index(index + 1)

    def handle_more_click(event):
        set_show_more(not show_more)

    bounded_index = index % len(sculpture_data)
    sculpture = sculpture_data[bounded_index]
    alt = sculpture["alt"]
    artist = sculpture["artist"]
    description = sculpture["description"]
    name = sculpture["name"]
    url = sculpture["url"]

    return html.div(
        html.button({"onClick": handle_next_click}, "Next"),
        html.h2(name, " by ", artist),
        html.p(f"{bounded_index + 1} or {len(sculpture_data)}"),
        html.img({"src": url, "alt": alt, "style": {"height": "200px"}}),
        html.div(
          html.button(
              {"onClick": handle_more_click},
              f"{'Hide' if show_more else 'Show'} details",
          ),
          (html.p(description) if show_more else ""),
        ),
    )


@component
def App6():
    return html.div(
        html.section({"style": {"width": "50%", "float": "left"}}, Gallery()),
        html.section({"style": {"width": "50%", "float": "left"}}, Gallery()),
    )


@component
def Counter():
    number, set_number = use_state(0)

    async def handle_click(event):
        await asyncio.sleep(3)
        set_number(lambda old_number: old_number + 1)

    return html.div(
        html.h1(number),
        html.button({"onClick": handle_click}, "Increment"),
    )


@component
def MovingDot():
    position, set_position = use_state({"x": 0, "y": 0})

    async def handle_pointer_move(event):
        outer_div_info = event["currentTarget"]
        outer_div_bounds = outer_div_info["boundingClientRect"]
        set_position(
            {
                "x": event["clientX"] - outer_div_bounds["x"],
                "y": event["clientY"] - outer_div_bounds["y"],
            }
        )

    return html.div(
        {
            "onPointerMove": handle_pointer_move,
            "style": {
                "position": "relative",
                "height": "200px",
                "width": "100%",
                "backgroundColor": "white",
            },
        },
        html.div(
            {
                "style": {
                    "position": "absolute",
                    "backgroundColor": "red",
                    "borderRadius": "50%",
                    "width": "20px",
                    "height": "20px",
                    "left": "-10px",
                    "top": "-10px",
                    "transform":
                        f"translate({position['x']}px, {position['y']}px)",
                },
            }
        ),
    )


@component
def ArtistList():
    artist_to_add, set_artist_to_add = use_state("")
    artists, set_artists = use_state(
        ["Marta Colvin Andrade", "Lamidi Olonade Fakeye", "Louise Nevelson"]
    )

    def handle_change(event):
        set_artist_to_add(event["target"]["value"])

    def handle_add_click(event):
        if artist_to_add not in artists:
            set_artists([*artists, artist_to_add])
            set_artist_to_add("")

    def make_handle_delete_click(index):
        def handle_click(event):
            set_artists(artists[:index] + artists[index + 1])

        return handle_click

    return html.div(
        html.h1("Inspiring scultptors:"),
        html.input({"value": artist_to_add, "onChange": handle_change}),
        html.button({"onClick": handle_add_click}, "Add"),
        html.ul(
            [
                html.li(
                    name,
                    html.button(
                        {
                            "onClick": make_handle_delete_click(index)
                        },
                        "Delete"
                    ),
                    key=name,
                )
                for index, name in enumerate(artists)
            ]
        ),
    )


@component
def CounterList():
    counters, set_counters = use_state([0, 0, 0])

    def make_increment_click_handler(index):
        def handle_click(event):
            new_value = counters[index] + 1
            set_counters(
                counters[:index] + [new_value] + counters[index + 1]
            )

        return handle_click

    return html.ul(
        [
            html.li(
                count,
                html.button(
                    {
                        "onClick": make_increment_click_handler(index)
                    },
                    "+1"
                ),
                key=index,
            )
            for index, count in enumerate(counters)
        ]
    )


@component
def ArtistList2():
    artists, set_artists = use_state(
        ["Marta Colvin Andrade", "Lamidi Olonade Fakeye", "Louise Nevelson"]
    )

    def handle_sort_click(event):
        set_artists(list(sorted(artists)))

    def handle_reverse_click(event):
        set_artists(list(reversed(artists)))

    return html.div(
        html.h1("Inspiring scultptors:"),
        html.button({"onClick": handle_sort_click}, "Sort"),
        html.button({"onClick": handle_reverse_click}, "Reverse"),
        html.ul([html.li(name, key=name) for name in artists]),
    )


@component
def Grid():
    line_size = 5
    selected_indices, set_selected_indices = use_state({1, 2, 4})

    def make_handle_click(index):
        def handle_click(event):
            if index in selected_indices:
                set_selected_indices(selected_indices - {index})
            else:
                set_selected_indices(selected_indices | {index})

        return handle_click

    return html.div(
        {"style": {"display": "flex", "flex-direction": "row"}},
        [
            html.div(
                {
                    "onClick": make_handle_click(index),
                    "style": {
                        "height": "30px",
                        "width": "30px",
                        "backgroundColor": (
                            "black" if index in selected_indices else "white"
                        ),
                        "outline": "1px solid grey",
                        "cursor": "pointer",
                    },
                },
                key=index,
            )
            for index in range(line_size)
        ],
    )


@component
def SyncedInputs():
    value, set_value = hooks.use_state("")
    return html.p(
        Input("First input", value, set_value),
        Input("Second input", value, set_value),
    )


@component
def Input(label, value, set_value):
    def handle_change(event):
        set_value(event["target"]["value"])

    return html.label(
        label + " ", html.input({"value": value, "onChange": handle_change})
    )


@component
def FilterableList():
    value, set_value = hooks.use_state("")
    return html.p(Search(value, set_value), html.hr(), Table(value, set_value))


@component
def Search(value, set_value):
    def handle_change(event):
        set_value(event["target"]["value"])

    return html.label(
        "Search by Food Name: ",
        html.input(
            {
                "value": value, "onChange": handle_change
            }
        )
    )


def Table(value, set_value):
    rows = []
    for row in food_data:
        name = html.td(row["name"])
        descr = html.td(row["description"])
        tr = html.tr(name, descr, value)
        if value == "":
            rows.append(tr)
        else:
            if value.lower() in row["name"].lower():
                rows.append(tr)
        headers = html.tr(
            html.td(html.b("name")),
            html.td(html.b("description"))
        )
    table = html.table(html.thead(headers), html.tbody(rows))
    return table


def increment2(last_count):
    return last_count + 1


def decrement(last_count):
    return last_count - 1


@component
def Counter3():
    initial_count = 0
    count, set_count = hooks.use_state(initial_count)

    return html.div(
        f"Count: {count}",
        html.button(
            {
                "onClick":
                    lambda event:
                        set_count(initial_count)
            },
            "Reset"
        ),
        html.button({"onClick": lambda event: set_count(increment2)}, "+"),
        html.button({"onClick": lambda event: set_count(decrement)}, "-"),
    )
