import requests
import idom

from idom import component, event, html, hooks, use_state, run, web


mui = web.module_from_template(
    "react@^17.0.0",
    "@material-ui/core@4.12.4",
)
# Getting framer motion
motion = web.module_from_template(
    "react@^17.0.0",
    "www.unpkg.com/framer-motion@^6.5.1",
)

Motion = web.export(motion, "Motion")
Button = web.export(mui, "Button")
Card = web.export(mui, "Card")
Slider = web.export(mui, "Slider")
Box = web.export(mui, "Box")

@component
def AstronautComponent():
    
    url = 'http://api.open-notify.org/astros.json'
    url_request = requests.get(url)
    data = url_request.json()
    total_astronauts = data['number']
    return html.div(
        {
            'className': 'main-container',
            'style': {
                # 'background-color': '#f5f5f5',
                'background-image': 'url("https://cdn.pixabay.com/photo/2016/09/08/12/00/stars-1654074_960_720.jpg")',
                'min-height': '100vh',
                'display': 'flex',
                'flex-direction': 'column',
                'align-items': 'center',
                'justify-content': 'center',
                'padding': '20px',
                'box-sizing': 'border-box',
                'border': '1px solid #ccc',
                'border-radius': '5px',
                'box-shadow': '0px 0px 10px #ccc',
                'margin': '0 auto',
                'margin-top': '20px',
                'margin-bottom': '20px',
                'text-align': 'center',
                'font-family': 'Roboto, sans-serif',
                'font-size': '1.5em',
                'color': '#fff',
                'text-shadow': '0px 0px 10px #ccc',
            }
        },
        html.img(
            {
                "src": "https://snipstock.com/assets/cdn/png/36334c8b466fe29a3f0e9c0a8c91aecb.png",
                "style": {
                  "width": "250px",
                  "height": "250px",
                  "position": "absolute",
                  "top": "calc(18% - 125px)",
                  "left": "calc(15% - 125px)",
                },
            }
        ),
        html.img(
            {
                "src": "https://snipstock.com/assets/cdn/png/36334c8b466fe29a3f0e9c0a8c91aecb.png",
                "style": {
                  "width": "250px",
                  "height": "250px",
                  "position": "absolute",
                  "top": "calc(18% - 125px)",
                  "left": "calc(85% - 125px)",
                },
            }
        ),
        html.h1("Astronauts Tracker"),
        html.p(
            'Total number of astronauts: ' + str(total_astronauts)
        ),
        html.div(
            {
                "className": "card-container",
                "style": {
                    "display": "grid",
                    "grid-template-columns": "repeat(3, 1fr)",
                    "grid-template-rows": "repeat(1fr 1fr)",
                    "grid-gap": "calc(10px + 1vw)",
                }    
            },
            [
            html.div(
            {
                'className': 'astronaut-card',
                'style': {
                    'justify-content': 'center',
                    'align-items': 'center',
                    'width': '100%',
                    'margin': '0 auto',
                    'margin-top': '20px',
                    'margin-bottom': '20px',
                    'text-align': 'center',
                    'font-family': 'Roboto, sans-serif',
                    'color': '#fff',
                    'text-shadow': '0px 0px 10px #ccc',
                    'padding': '20px',
                    'box-sizing': 'border-box',
                    'border': '1px solid #ccc',
                    'border-radius': '5px',
                    'box-shadow': '0px 0px 10px #ccc',
                },
            },
                html.p(
                    [
                        html.span(
                            data['people'][i]['name'] + ' is on the ' + data['people'][i]['craft'] + '.'
                        ),
                    ]
                ),
            )
            for i in range(total_astronauts)
        ]
        ),
        Button({"color": "primary", "variant": "contained"}, "SpaceX"),
    )