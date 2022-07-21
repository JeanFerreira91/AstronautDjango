import idom

from idom import web, html, use_state

mui = web.module_from_template(
    "react@^17.0.0",
    "@material-ui/core@4.12.4",
)

Box = web.export(mui, "Box")
Slider = web.export(mui, "Slider")

@idom.component
def SliderComponentMui():
    value, set_value = use_state([20, 70])
    
    def handle_change(event, newValue):
        set_value(newValue)
    
    return html.div(
        {
            "className": "slider-container",
            "style": {
                "width": "30%",
                "margin": "0 auto",
                "margin-top": "10%",
            },
        },
        Slider(
            {
                "defaultValue": 50,
                "step": 1,
                "min": 0,
                "max": 100,
                "aria-labelledby": "label",
                "aria-label": "Default",
                "valueLabelDisplay": "on",
            },
        ),
        Slider(
            {
                "getAriaLabel": lambda value: "Temperature range {}".format(value),
                "value": value,
                "onChange": handle_change,
                "valueLabelDisplay": "auto",
            },
        ),
    )


@idom.component
def SliderInBox():
    return html.div(
        Box(
            {
                "sx": 
                {
                    "width": "300",
                },
            },
            Slider(
                {
                    "defaultValue": 50,
                    "step": 1,
                    "min": 0,
                    "max": 100,
                    "aria-labelledby": "label",
                    "aria-label": "Default",
                    "valueLabelDisplay": "on",
                },
            ),
        ),
    )